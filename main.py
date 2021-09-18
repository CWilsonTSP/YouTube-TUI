import requests
import json
import urllib.parse

def main():
    inp = input("Enter a search Query: ")
    # print(inp)
    query = """https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q=""" + urllib.parse.quote(inp) + """&key=AIzaSyDXxvLRGt4V3p6yzi-34rCz9W0cLcoTVds"""
    # r = requests.get("https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q=c%2B%2B%20tutorial&key=AIzaSyDXxvLRGt4V3p6yzi-34rCz9W0cLcoTVds")
    r = requests.get(query)
    r_dict = r.json()

    for item in r_dict["items"]:
        print(item["snippet"]["title"], item["id"])

if __name__ == "__main__":
    main()
