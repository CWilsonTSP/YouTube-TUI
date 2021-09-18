import requests
import json
import urllib.parse

class Result:
    def __init__(self,title,channel,date,ID,thumbnail):
        self.title = title
        self.channel = channel
        self.date = date
        self.ID = ID
        self.thumbnail = thumbnail

def main():
    inp = input("Enter a search Query: ")
    # print(inp)
    query = """https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q=""" + urllib.parse.quote(inp) + """&key=AIzaSyDXxvLRGt4V3p6yzi-34rCz9W0cLcoTVds"""
    # r = requests.get("https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q=c%2B%2B%20tutorial&key=AIzaSyDXxvLRGt4V3p6yzi-34rCz9W0cLcoTVds")
    r = requests.get(query)
    r_dict = r.json()

    results = []
    for item in r_dict["items"]:
        #print(item["snippet"]["title"], item["id"])
        if item["id"]["kind"] == "youtube#video":
            results.append(Result(item["snippet"]["title"],item["snippet"]["channelTitle"],item["snippet"]["publishTime"],item["id"]["videoId"],item["snippet"]["thumbnails"]["high"]["url"]))

    for v in results:
        print(v.title,v.channel,v.date,v.ID,v.thumbnail)

if __name__ == "__main__":
    main()
