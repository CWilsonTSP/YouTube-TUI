import requests
import urllib.parse
from result import Result

def load_config():
    # eventually, these should reference the user's XDG variables
    # try loading from these locations first
    # XXX Perhaps, we simply launch the "main" script from a bash script,
    # as that would allow us to to directly interface with the shell
    # that we are loading variables from
    locations = ["$HOME/.config/yttui/yttuirc", "$HOME/.yttuirc"]
    for loc in locations:
        ...
        # if file exists, open it and load it. Then break.
        # else, create the file with defaults

def main():
    # ask the user for input
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

# if this file is the one that is run,
if __name__ == "__main__":
    main()
