import urllib.parse
import urllib.request
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'

def search(search_term, user_agent = user_agent):
    search_url  = "https://www.youtube.com/results?search_query=%s" % urllib.parse.quote_plus(search_term)
    headers = {'User-Agent': user_agent}
    req = urllib.request.Request(search_url, None, headers)
    with urllib.request.urlopen(req) as response:
        search_results = response.read()
    soup = BeautifulSoup(search_results, "lxml")
    result_set = soup.find_all('div','yt-lockup yt-lockup-tile yt-lockup-video vve-check clearfix')
    results = []
    for r in result_set:
        if r.find('h3'):
            result = {}
            result['title'] = r.find('h3').text
            result['video_id'] = r.find_all('button')[1]['data-video-ids']
            if r.find('div', 'yt-lockup-description'):
                result['description'] = r.find('div', 'yt-lockup-description').text
            else:
                result['description'] = ''
            result['img'] = "https://i.ytimg.com/vi/%s/hqdefault.jpg?custom=true&w=246&h=138" % result['video_id']
            result['link'] = "https://www.youtube.com/watch?v=%s" % result['video_id']
            result['fullscreen'] = "https://www.youtube.com/embed/%s" % result['video_id']
            result['fullscreen_auto'] = "https://www.youtube.com/embed/%s?rel=0&autoplay=1" % result['video_id']
            results.append(result)
    return results
