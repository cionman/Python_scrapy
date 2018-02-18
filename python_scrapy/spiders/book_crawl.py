# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BookCrawlSpider(CrawlSpider):
    name = 'book_crawl'
    allowed_domains = ['hanbit.co.kr']
    start_urls = [
                  'http://WWW.hanbit.co.kr/store/books/category_list.html?cate_Cd=001',
                  'http://WWW.hanbit.co.kr/store/books/category_list.html?cate_Cd=002',
                  'http://WWW.hanbit.co.kr/store/books/category_list.html?cate_Cd=003',
                  'http://WWW.hanbit.co.kr/store/books/category_list.html?cate_Cd=004',
                  'http://WWW.hanbit.co.kr/store/books/category_list.html?cate_Cd=005',
                  'http://WWW.hanbit.co.kr/store/books/category_list.html?cate_Cd=006',
                  'http://WWW.hanbit.co.kr/store/books/category_list.html?cate_Cd=007',
                  'http://WWW.hanbit.co.kr/store/books/category_list.html?cate_Cd=008',
                  ]

    rules = (
        Rule(
            # 크롤링할 링크를 정규 표현식을 이용하여 표현
            LinkExtractor(allow=r'store/books/look.php\?p_code=.*')
            # 해당 링크에 요청을 보내고 응답이 오면 실행할 콜백 메소드 지정
            , callback='parse_item'
            # True 인 경우 재귀적 실행
            , follow=True),
        Rule(LinkExtractor(allow=
                           r'store/books/category_list\.html\?page=\d+&cate_cd=00\d+&srt=p_pub_date'))
    )

    def parse_item(self, response):
        i = {}
        i['book_title'] = response.xpath(
            '//*[@id="container"]/div[2]/div[1]/div[1]/div[2]/h3/text()'
        ).extract()

        i['book_author'] = response.xpath(
            '//*[@id="container"]/div[2]/div[1]/div[1]/div[2]/ul/li[1]/span/text()'
        ).extract()

        i['book_translator'] = response.xpath(
            '//*[@id="container"]/div[2]/div[1]/div[1]/div[2]/ul/li[2]/span/text()'
        ).extract()

        i['book_pub_date'] = response.xpath(
            '//*[@id="container"]/div[2]/div[1]/div[1]/div[2]/ul/li[3]/span/text()'
        ).extract()

        i['book_isbn'] = response.xpath(
            '//*[@id="container"]/div[2]/div[1]/div[1]/div[2]/ul/li[5]/span/text()'
        ).extract()
        print("i : ", i)
        return i
