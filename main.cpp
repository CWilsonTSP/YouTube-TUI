#include <iostream>
#include <string>

#include "curl.cpp"

// curl \
//   'https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q=c%2B%2B%20tutorial&key=AIzaSyDXxvLRGt4V3p6yzi-34rCz9W0cLcoTVds' \
//   --header 'Accept: application/json' \
//   --compressed


int main(){
    CURLplusplus client;
    std::string x = client.Get("https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q=c%2B%2B%20tutorial&key=AIzaSyDXxvLRGt4V3p6yzi-34rCz9W0cLcoTVds");

    std::cout << x << std::endl;

    return 0;
}
