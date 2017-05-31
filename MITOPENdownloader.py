#! /usr/bin/env python3

import requests,bs4
from os import path
from threading import Thread

class Video:
    chunkSize = 500000
    def __init__(self, url, title):
        self.url = url
        self.title = title

    def download(self, outputDir):
        self.videoStream = requests.get(self.url,stream=True)
        # 'Content-Length': '121291539'
        self.length = int(self.videoStream.headers['Content-Length'])
        # 'Content-Type': 'video/mp4'
        self.suffix = "." + self.videoStream.headers['Content-Type'].split('/')[1]

        with open(path.join(outputDir,self.title+self.suffix),'wb') as f:
            print("start downloading",'"', self.title,'"', flush=True)
            written = 0
            for chunk in self.videoStream.iter_content(self.chunkSize):
                written += f.write(chunk)
                print("progress", written*100//self.length,"%\r",flush=True,end="")
            print("finished downloading",'"', self.title,'"', flush=True)

if __name__ == "__main__":
    # testUrl = "http://www.archive.org/download/MIT6.006F11/MIT6_006F11_lec01_300k.mp4"
    # v = Video(testUrl,"Lecture 1: Algorithmic Thinking, Peak Finding")
    # v1 = Video("http://www.archive.org/download/MIT6.006F11/MIT6_006F11_lec02_300k.mp4","Lecture 2: Models of Computation, Document Distance")
    # t = Thread(target=v.download,args=("/home/watashishun/Downloads",))
    # t1 = Thread(target=v1.download,args=("/home/watashishun/Downloads",))
    # t.start()
    # t1.start()

    # for testing
    destination = "/home/watashishun/Downloads"
    host = "https://ocw.mit.edu"
    url = "https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/"


    res = requests.get(url)
    res.raise_for_status()
    mainPage = bs4.BeautifulSoup(res.text)

    videoLs = mainPage.select('div[class="medialisting"] > a')
    for v in videoLs:
        videoTitle = v.get('title')
        videoPlayUrl = host +  v.get('href')
        videoRes = requests.get(videoPlayUrl)
        videoPlayPage = bs4.BeautifulSoup(videoRes.text)
        url = videoPlayPage.select('#vid_transcript li a')[1].get("href")
        video = Video(url,videoTitle)
        video.download(destination)
