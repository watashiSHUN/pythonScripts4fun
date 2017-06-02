#! /usr/bin/env python3

import requests,bs4,re,click
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


class VideoStreamSite():
    hostReg = re.compile(r'.*://[^/]*')
    def __init__(self, url):
        self.url = url
        hostReg = self.hostReg.search(url)
        if hostReg:
            self.host = hostReg.group()
        else:
            raise ValueError("can not get host from URL")

    def singleThreadDownload(self, destination):
        res = requests.get(self.url)
        res.raise_for_status()
        mainPage = bs4.BeautifulSoup(res.text)

        videoList = mainPage.select('div[class="medialisting"] > a')
        for v in videoList:
            videoTitle = v.get('title')
            videoPlayUrl = self.host +  v.get('href')
            videoRes = requests.get(videoPlayUrl)
            videoPlayPage = bs4.BeautifulSoup(videoRes.text)
            url = videoPlayPage.select('#vid_transcript li a')[1].get("href")
            video = Video(url,videoTitle)
            video.download(destination)

@click.command()
@click.option("--url", prompt="stream website url")
@click.option("--output", prompt="output directory")
def commandLine(url,output):
    videoStream = VideoStreamSite(url)
    videoStream.singleThreadDownload(output)

if __name__ == "__main__":
    commandLine()
