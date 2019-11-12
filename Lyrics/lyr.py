#encoding: utf-8
import dbus
import requests
import json
import time
from show import match_time,refresh_console
last_token = " "
start_time = time.time()
global_lyrics = ""


def refresh():
    session = dbus.SessionBus()
    spotifydbus = session.get_object("org.mpris.MediaPlayer2.spotify","/org/mpris/MediaPlayer2")
    spotifyinterface = dbus.Interface(spotifydbus, "org.freedesktop.DBus.Properties")
    metadata = spotifyinterface.Get("org.mpris.MediaPlayer2.Player", "Metadata")
    title = metadata['xesam:title']
    artist = metadata['xesam:artist'][0]
    imageUrl = metadata['mpris:artUrl']
    global start_time
    #获取一个秒级别的时间戳
    global global_lyrics
    '''
    if global_lyrics != "":
        # 传递一个时间差
        match_time(global_lyrics, time.time()-start_time)
    '''
    global last_token
    if last_token == title+artist+imageUrl:
        if global_lyrics != "":
            refresh_console(time.time()-start_time)
        return
    NEmusic_url = 'http://localhost:3000/search?keywords='+artist+" "+title
    res = requests.get(NEmusic_url)
    text = res.text
    jr = json.loads(text)
    last_token = title+artist+imageUrl
    try:
        song_id = jr['result']['songs'][0]['id']
        print("song id=", song_id)
        NElyrics = 'http://localhost:3000/lyric?id='+str(song_id)
        lyricsRes = requests.get(NElyrics)
        lyricsJson = json.loads(lyricsRes.text)
        # global global_lyrics
        global_lyrics = lyricsJson['lrc']['lyric']
        match_time(global_lyrics, 0)
        # last_token = title+artist+imageUrl
        start_time = time.time()
        print(artist, "-", title)
        # print(artist)
    except Exception as e:
        print("网易云获取song失败", title, e)
        global_lyrics = ""


while True:
    refresh()
