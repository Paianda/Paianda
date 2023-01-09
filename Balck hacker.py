import os,sys,time,datetime,random,hashlib,re,threading,js>
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor>
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Oper>


def keluar():
        print "\x1b[1;91mExit"
        os.sys.
