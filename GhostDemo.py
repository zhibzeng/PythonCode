# -*- coding:utf8 -*-
import urllib2,re,os,time
import chardet
import cookielib,httplib,urllib
from BeautifulSoup import BeautifulSoup
from ghost import Ghost
if __name__=='__main__':
    print 'hello'
    webURL = 'http://www.imanhua.com/'
    cartoonNum = raw_input("请输入漫画编号:")
    basicURL = webURL + u'comic/' + cartoonNum

    #通过Ghost模拟js获取动态网页生成的图片src
    class FetcherCartoon:
        def getCartoonUrl(self,url):

            if url is None:
                return false
            #todo many decide about url

            try:
                ghost = Ghost()
                #open webkit
                ghost.open(url)
                #exceute javascript and get what you want
                page, resources = ghost.wait_for_page_loaded()
                result, resources = ghost.evaluate("document.getElementById('comic').getAttribute('src');", expect_loading=True)
                del resources
            except Exception,e:
                print e
                return None
            return result

    #解决乱码问题
    html_1 = urllib2.urlopen(basicURL,timeout=120).read()
    mychar = chardet.detect(html_1)
    bianma = mychar['encoding']
    if bianma == 'utf-8' or bianma == 'UTF-8':
        html = html_1
    else :
        html = html_1.decode('gb2312','ignore').encode('utf-8')

    #获取漫画名称
    soup = BeautifulSoup(html)
    cartoonName = soup.find('div',class_='share').find_next_sibling('h1').get_text()
    print u'正在下载漫画： ' + cartoonName


    #传入url模拟Get请求，获取图片内容
    def GetImageContent(wholeurl,imgurl):
        #time.sleep(0.1)
        req = urllib2.Request(imgurl)
        req.add_header('Referer', wholeurl)
        content = urllib2.urlopen(req).read()

        rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/\:*?"<>|'
        new_title = re.sub(rstr, "", str(imgurl)[-20:])

        with open(cartoonName+'/'+new_title,'wb') as code:
            code.write(content)

    #创建文件夹
    path = os.getcwd()               # 获取此脚本所在目录
    new_path = os.path.join(path,cartoonName)
    if not os.path.isdir(new_path):
      os.mkdir(new_path)

    #解析所有章节的URL
    chapterURLList = []
    chapterLI_all = soup.find('ul',id = 'subBookList').find_all('a')
    for chapterLI in chapterLI_all:
        chapterURLList.append(chapterLI.get('href'))
        #print chapterLI.get('href')

    #遍历章节的URL
    for chapterURL in chapterURLList:
        chapter_soup = BeautifulSoup(urllib2.urlopen(webURL+str(chapterURL),timeout=120).read())
        chapterName = chapter_soup.find('div',id = 'title').find('h2').get_text()
        print u'正在下载章节： ' + chapterName

        #根据最下行的最大页数获取总页数
        allChapterPage = chapter_soup.find('strong',id = 'pageCurrent').find_next_sibling('strong').get_text()
        print allChapterPage
        #然后遍历所有页，组合成url，保存图片
        currentPage = 1
        fetcher = FetcherCartoon()
        uurrll = str(webURL+str(chapterURL))
        imgurl = fetcher.getCartoonUrl(uurrll)
        if imgurl is not None:
            while currentPage <= int(allChapterPage):
                wholeurl = str(webURL+str(chapterURL)+u'?p='+str(currentPage))
                page = "%03d"%(currentPage)
                url = str(imgurl[:-7] + str(page) + imgurl[-4:])
                print wholeurl
                print url
                GetImageContent(wholeurl,url)

                currentPage += 1


    print "~~~~~~~~~~~~~~~~~~~~~~~~~~END~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    #为了避免双击的时候直接一闪退出，在最后面加了这么一句
    raw_input("Press <Enter> To Quit!")
