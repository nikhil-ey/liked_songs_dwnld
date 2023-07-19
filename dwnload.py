import youtube_dl
#read songs.csv and search youtube for the song
#convert to MP3 using youtube_dl module
import os
import pandas as pd
from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
from pathlib import Path
import yt_dlp


def Download_list(los):
	print(los)
	#ids = []
	BASE="https://www.youtube.com/watch?v="
	for index, item in enumerate(los):
		vid_id = yt_search(item)
		vid_id=(BASE+vid_id)
		print(vid_id)
		Download_song(vid_id)
		#ids += [vid_id]
	print("Downloading complete")
	


def Download_song(lov):
	SAVE_PATH = str(os.path.join(Path.home(), "Downloads/songs"))
	try:
		os.mkdir(SAVE_PATH)
	except:
		print("download folder exists")
	ydl_opts = {
    	'format': 'bestaudio/best',
		'outtmpl': SAVE_PATH + '/%(title)s.%(ext)s',
	}
	with yt_dlp.YoutubeDL(ydl_opts) as ydl:
	    ydl.download(lov)
	    #yt-dlp used since its faster than youtube dl

#fn to search titles
def yt_search(title):
    BASIC="http://www.youtube.com/results?search_query="
    URL = (BASIC + title)
    print(URL)
    URL.replace(" ", "+")
    print(URL)
    page = requests.get(URL)
    session = HTMLSession()
    response = session.get(URL)
    response.html.render(sleep=1)
    soup = BeautifulSoup(response.html.html, "html.parser")
    results = soup.find('a', id="video-title")
    print(results)
    print(results['href'].split('/watch?v=')[1])
    return results['href'].split('/watch?v=')[1]



#read the pandas file
def __main__():
    df= pd.read_csv('songs.csv')
    df=df['song names'].tolist() #convert to list
    #yt_search(df[1])
    Download_list(df)


    print(df)

__main__()