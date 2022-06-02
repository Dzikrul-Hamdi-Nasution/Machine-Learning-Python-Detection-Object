
from icrawler.builtin import BingImageCrawler                  
classes=['nature','mountain','car','person','park','bicycle']
number=1000
for c in classes:
    google_crawler=BingImageCrawler         (storage={'root_dir':'n'}) 
    google_crawler.crawl(keyword=c,filters=None,max_num=number,offset=0)          