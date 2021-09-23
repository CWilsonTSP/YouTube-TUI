"""Imports"""
import os
import urllib.parse
import requests
from result import Result

def load_config():
    """Load the config file for yttui"""
    dir_config = ""
    try:
        dir_config = os.environ["XDG_CONFIG_HOME"] + "/yttui/"
    except KeyError:
        dir_config = os.environ["HOME"] + "/.config/yttui/"

    print("config file is at ", dir_config)

    try:
        with open(dir_config+"yttui.conf", "r"):
            print("Loading Config")
            # XXX load config file
    except FileNotFoundError:
        print("Config not found, creating")
        try:
            os.mkdir(dir_config)
        except FileExistsError:
            pass

        with open(dir_config+"yttui.conf", "w"):
            # print to this file the config
            ...

def current():
    """I just seperated what was in main into its own function for now"""
    inp = input("Enter a search Query: ")
    # print(inp)
    # create a query string based on the youtube apu and the search input
    query = """https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q=""" + urllib.parse.quote(inp) + """&key=AIzaSyDXxvLRGt4V3p6yzi-34rCz9W0cLcoTVds"""
    r = requests.get(query) # make the request
    r_dict = r.json() # create a dictionary from the request

    # grab all the items from the dict that are videos
    results = []
    for item in r_dict["items"]:
        #print(item["snippet"]["title"], item["id"])
        if item["id"]["kind"] == "youtube#video":
            results.append(Result(item["snippet"]["title"],item["snippet"]["channelTitle"],item["snippet"]["publishTime"],item["id"]["videoId"],item["snippet"]["thumbnails"]["high"]["url"]))

    # print out the results
    for v in results:
        print(v.title,v.channel,v.date,v.ID,v.thumbnail)


def main():
    """main"""
    # ask the user for input
    load_config()
    current()

# if this file is the one that is run,
if __name__ == "__main__":
    main()
