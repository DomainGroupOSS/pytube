from __future__ import print_function
from pytube import YouTube

# not necessary, just for demo purposes
from pprint import pprint

#url = "http://www.youtube.com/watch?v=Ik-RsDGPI5Y"
url = 'http://www.youtube.com/embed/GYpvcXNW8AI'
url = url.replace("embed/", "watch?v=")
#url = "http://www.youtube.com/watch?v=GYpvcXNW8AI"
assert 'youtube' in url or 'youtu.be' in url


# Set the video URL.
#try:
yt = YouTube()
yt.url = url
print(yt.filename)
pprint(yt.filter('mp4')[0])
#except:
#    pass


print('Done')
