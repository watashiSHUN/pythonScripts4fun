#! /usr/bin/env python3
"""
    you can download H manga from www.sis001
    or search for threads that contains a certain keyword
"""
from lxml import html
import requests
import sys

# TODO login while reading user input
loginUrl = 'http://www.sis001.com/forum/logging.php?action=login'
chromeString = 'formhash=afdb9562&referer=&cookietime=2592000&loginfield=username&62838ebfea47071969cead9d87a2f1f7=mike53669&c95b1308bda0a3589f68f75d23b15938=5678&questionid=0&answer=&loginsubmit=true'
keyValue = chromeString.split('&')
data = dict([tuple(x.split('=')) for x in keyValue if len(x.split('='))>1])
response = requests.post(loginUrl,data=data)
setCookies = response.cookies
# TODO write cookies to file, load if exist
# TODO get cookies should be in azure function
# do not expose your credentials... they can use your cookies to load chrome
def downloads(hentaiUrl, count):
    print("start downloading: " + hentaiUrl)
    page = requests.get(hentaiUrl,cookies=setCookies)
    tree = html.fromstring(page.text)
    images = tree.xpath('//img')
    for x in images:
        link = x.get('src')
        if(link.endswith('.jpg')):
            imageContent = requests.get(link)
            fname = str(count)+'.jpg'
            print(fname, end=" ", flush=True) # won't flush until it sees a newline
            with open(fname,'wb') as f:
                #TODO bad request
                f.write(imageContent.content)
            count += 1 # only jpg increase the count
    print() # newline
    return count

def search(begin,length,string):
    # start with page 1
    for i in range(begin,begin+length):
        # FIXME for testing, count+10
        hentaiUrl = "http://www.sis001.com/forum/forum-60-%d.html"%i
        page = requests.get(hentaiUrl,cookies=setCookies)
        # TODO educated guess instead of hard coding
        page.encoding = 'gbk'
        tree = html.fromstring(page.text)
        threadTitle = tree.xpath('//tbody[starts-with(@id,"normalthread")]/tr/th')
        for row in threadTitle:
            anchorELement = row.xpath('./span[@id]/a')[0]
            text = anchorELement.text
            if string in text:
                print(row.xpath('./em/a')[0].text+" "+text + " page %d"%i, flush=True)
                # searchUrl = 'http://www.sis001.com/forum/'+anchorELement.get('href')
                # threadPages = row.xpath('./span[@class]')
                # if threadPages:
                #     print(',', len(threadPages[0]), end ="")

if __name__ == "__main__":
    if(len(sys.argv) > 1):
        lastRequestEnd = 0
        for arg in sys.argv[1:]:
            lastRequestEnd = downloads(arg,lastRequestEnd)
    else:
        # stdin user interface
        print("menu: 1. search title keyword")
        option = int(input())
        if option == 1:
            pages = int(input("how many pages?"))
            string = input("type string token that you are looking for:")
            for _ in range(pages):
                search(_+1,1,string)
