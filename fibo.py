from ghost import Ghost

def test():
    g = Ghost(wait_timeout=10)
    g = Ghost(display=True)
    g.open("http://www.google.com")


def test1():
    url = "http://www.ebay.com/"
    gh = Ghost()
    # We create a new page
    page, page_name = gh.create_page()
    # We load the main page of ebay
    page_resource = page.open(url, wait_onload_event=True)
    # Full the main bar and click on the search button
    page.set_field_value("#gh-ac", "plane")
    page.click("#gh-btn")
    # Wait for the next page
    page.wait_for_selector("#e1-15")
    # Save the image of the screen
    page.capture_to("plane.png")


def test2():
    ghost = Ghost()
    page, resources = ghost.open('http://www.baidu.com')




if __name__=='__main__':
   test()
