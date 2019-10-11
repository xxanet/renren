import scrapy
import re

class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/972427324/profile']

    def start_requests(self):
        cookies = '_ga=GA1.2.1863450434.1570508313; _gid=GA1.2.602938173.1570508313; t=8384fe323d03b2f70e974d37ee58ba814; _uij="JTdCJTIydXNlcklkJTIyJTNBOTcyNDI3MzI0JTJDJTIydXNlck5hbWUlMjIlM0ElMjJYWEFuZXQlMjIlMkMlMjJoZWFkRnVsbFVybCUyMiUzQSUyMmh0dHAlM0ElMkYlMkZoZWFkLnhpYW9uZWkuY29tJTJGcGhvdG9zJTJGMCUyRjAlMkZtZW5faGVhZC5naWYlMjIlMkMlMjJnZW5kZXIlMjIlM0ElMjIlMjIlMkMlMjJsb2dDb3VudCUyMiUzQTAlMkMlMjJjb2RlJTIyJTNBMCU3RA=="; id=972427324; renrenuid=972427324; anonymid=k1hcjei1-wynci4; JSESSIONID=abckkQ5ti3plo_GaLOP2w; depovince=GW; ver=7.0; loginfrom=null; springskin=set; jebe_key=6126dea9-74f2-4a4a-a55b-87214c2aa32d%7C82756a37b30d11a980157be65bdda697%7C1570509061021%7C1%7C1570509061152; jebe_key=6126dea9-74f2-4a4a-a55b-87214c2aa32d%7C82756a37b30d11a980157be65bdda697%7C1570509061021%7C1%7C1570509061154; vip=1; wp_fold=0; jebecookies=658c71d2-29b4-4340-8f55-5fccc2a18f47|||||'
        cookies = {i.split("=")[0]:i.split("=")[1] for i in cookies.split(";")}
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies = cookies
        )

    def parse(self, response):
        print(re.findall("XXAnet",response.body.decode()))
        yield scrapy.Request(
            "http://zhibo.renren.com/",
            callback=self.parse_detial
        )

    def parse_detial(self,response):
        print(re.findall("XXAnet", response.body.decode()))






