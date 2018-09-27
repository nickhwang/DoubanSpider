import requests
from lxml import etree

#1.Request a web page and crawl the web page data
url = 'https://movie.douban.com/cinema/nowplaying/guangzhou/'

headers = {
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
    'Referer' : 'https://movie.douban.com/'
}

response = requests.get(url,headers=headers)
text = response.text

#2.Make rules to crawl the data you want
html = etree.HTML(text)
uls = html.xpath('//ul[@class="lists"]')[0]
lis = uls.xpath('./li')
movies = []
for li in lis:
    title = li.xpath('./@data-title')[0]
    score = li.xpath('./@data-score')[0]
    release = li.xpath('./@data-release')[0]
    duration = li.xpath('./@data-duration')[0]
    region = li.xpath('./@data-region')[0]
    actors = li.xpath('./@data-actors')[0]
    imgs = li.xpath('.//img/@src')[0]
    movie = {
        'title' : title,
        'score' : score,
        'release' : release,
        'duration' : duration,
        'region' : region,
        'actors' : actors,
        'actors' : actors,
        'imgs' : imgs,
    }
    movies.append(movie)
    
#Print Date
print(movies)



#print(etree.tostring(lis,encoding='utf-8').decode('utf-8'))
