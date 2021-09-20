"""This is an example of how we can use  the subprocess module to open
videos. The below example uses mpv, but you could also yous vlc or 
any other video player that can take a url as an argument. Of course,
you can use one that takes a file as an argument, but you might not want
to download the video to your computer everytime, Its preferable to
stream it.
"""

import subprocess

subprocess.Popen(['mpv', 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'])
