from pytchat import LiveChat
import datetime as dt
import requests
from bs4 import BeautifulSoup

def get_stream_url():
    # query Yong-Nien Lee (in Chinese) on YouTube to get the video ID of the latest stran
    url_yt = "https://www.youtube.com"
    user = "Chifar899"
    query = "%E6%9D%8E%E6%B0%B8%E5%B9%B4"
    url_query = "{}/user/{}/search?query={}".format(url_yt, user, query)
    req = requests.get(url_query)
    soup = BeautifulSoup(req.content, "html.parser")
    str_target = "window[\"ytInitialData\"] = "
    video_id = None
    for scc in soup.select("script"):
        str_soup = str(scc.string).strip()
        if bool(str_soup) and str_soup[:len(str_target)]==str_target:
            str_soup = str_soup[len(str_target):]
            # find videoId
            str_target = "\"videoId\":\""
            id_target = str_soup.find(str_target)
            id_end = str_soup.find('\",', id_target)
            video_id = str_soup[id_target+len(str_target):id_end]
            break
    return "{}/watch?v={}".format(url_yt, video_id)

def main():
    yt_url = get_stream_url()
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