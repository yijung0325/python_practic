from pytchat import LiveChat
import datetime as dt
import requests
from bs4 import BeautifulSoup
import json

def get_stream_url():

#    user = "Chifar899"
#    url_videos = "https://www.youtube.com/user/{}/videos?view=2".format(user)

    url_videos = "https://www.youtube.com/c/hsuantien/videos"
    req = requests.get(url_videos)
    soup = BeautifulSoup(req.text, "lxml")

    with open("xml.txt", mode='w', encoding="utf-8") as fw:
        fw.write(req.text)
    
    
    

#    print(video_titles)

    return

def main():
    yt_url = get_stream_url()
    yt_url = "https://www.youtube.com/watch?v=X2MuyEyZz-0"
    livechat = LiveChat(yt_url)
    hour_start = 19
    min_start = 30
    time_start = None
    time_chat = None
    count = 0
    limit = 100
    while livechat.is_alive():
        chatdata = livechat.get()
        for c in chatdata.items:
            if not bool(time_start):
                len_time = len(" 19:30:00")
                time_start = dt.datetime.strptime(c.datetime[:-len_time], "%Y-%m-%d")
                time_start = time_start.replace(hour=hour_start, minute=min_start)
            time_chat = dt.datetime.strptime(c.datetime, "%Y-%m-%d %H:%M:%S")
            if time_chat >= time_start:
                print("{} [{}]- {}".format(c.datetime, c.author.name, c.message))
                count += 1
                print("count = {}".format(count))
            chatdata.tick()
            if count > limit:
                break
        if count > limit:
            break

if __name__ == '__main__':
    main()