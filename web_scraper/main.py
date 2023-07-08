from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from web_scraper.spiders.reddit_spider import RedditSpider

def main():
    url = input("Enter the URL to scrape: ")
    process = CrawlerProcess(get_project_settings())
    process.crawl(RedditSpider, start_urls=[url])
    process.start()

if __name__ == "__main__":
    main()
