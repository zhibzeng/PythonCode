# -*- coding: utf-8 -*-
__author__ = 'Administrator'

import MySQLdb


def ConnectTest(host='localhost', user='root', password='', db=''):
    try:
        conn = MySQLdb.connect(host=host, user=user, passwd=password, db=db, port=3306)
        cur = conn.cursor()
        cur.execute('select * from wp_users')
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
        print"Mysql Error %d: %s" % (e.args[0], e.args[1])


def CreateTable():
    try:
        conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='7165092054',port=3306)
        cur=conn.cursor()
        cur.execute('create database if not exists python')
        conn.select_db('python')
        cur.execute('create table test(id int,info varchar(20))')
        value=[1,'hi rollen']
        cur.execute('insert into test values(%s,%s)',value)
        values=[]
        for i in range(20):
            values.append((i,'hi rollen'+str(i)))
        cur.executemany('insert into test values(%s,%s)',values)
        cur.execute('update test set info="I am rollen" where id=3')
        conn.commit()
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def ShowData():
    try:
        conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='7165092054',port=3306)
        cur=conn.cursor()
        conn.select_db('python')
        count=cur.execute('select * from test')
        print 'there has %s rows record' % count
        result=cur.fetchone()
        print result
        print 'ID: %s info %s' % result
        results=cur.fetchmany(5)
        for r in results:
            print r
        print '=='*10
        cur.scroll(0,mode='absolute')
        results=cur.fetchall()
        for r in results:
            print r[1]
        conn.commit()
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])


def GetTransportationData():
    try:
        conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='7165092054',port=3306,charset='UTF8')
        cur=conn.cursor()
        sql = "set names 'UTF8'"
        cur.execute(sql)
        conn.select_db('transportation')
        count=cur.execute('select * from image')
        print('there has %s rows record' % count)
        print('*'*10)
        cur.scroll(0,mode='absolute')
        results=cur.fetchall()
        for r in results:
            line = []
            for i in r:
                line.insert(len(line),i)
            print(line)
            print(line[2])
        conn.commit()
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])


if __name__ == '__main__':
    #ConnectTest('127.0.0.1', 'root', '7165092054', 'youth')
    #CreateTable()
    #ShowData()
    GetTransportationData()