## 豆瓣电影爬虫
import requests
url_init="https://movie.douban.com/top250?start={0}&filter="
urls=[url_init.format(x*25) for x in range(10)]
print(urls)
#r=requests.get(url)
#print(r.text)