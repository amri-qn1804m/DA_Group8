import  requests
url = 'http://172.18.58.238/snow'
r = requests.get(url)
print(r.text)
print("Status code:")
print("\t*",r.status_code)

if r.status_code == 200:
    print("Ok!")
if r.status_code == 404:
    print("Not Found.")

h = requests.head(url)
print("Header.")
print("**********")

for x in h.headers:
    print("\t",x,".",h.headers[x])
print("**********")

headers = {
    'User-Agent':'Mobile'
}

url2 ='http://httpbin.org/headers'
rh=requests.get(url2,headers=headers)
print(rh.text)

import scrapy
class NewSpider(scrapy.Spider):
        name = "new_spider"
        start_urls = ['http://172.18.58.238/snow.php']
        def parse(self, response):
            xpath_selector = '//img'
            for x in response.xpath(xpath_selector):
                newsel = '@src'
                yield {
                        'Image Link': x.xpath(newsel).extract_first(),
                }




