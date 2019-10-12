import scrapy


class QuotesSpider(scrapy.Spider):
    name = "pubs"

    def start_requests(self):
        urls = [
            'https://www.pubsgalore.co.uk/countries/england/',
            'https://www.pubsgalore.co.uk/countries/northern-ireland/',
			'https://www.pubsgalore.co.uk/countries/scotland/',
			'https://www.pubsgalore.co.uk/countries/wales/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        
        county_pages = response.css('a.countyname::attr(href)').getall()
        
        for page in county_pages:
            yield response.follow(page, callback=self.parse)
            
        for town in response.css('a.townlink::attr(href)').getall():
            town_page = response.urljoin(town)
            yield response.follow(town_page, callback=self.parse)
            
        page = response.url.split("/")[-3] + "_" + response.url.split("/")[-2]
        filename = 'pubs-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        #self.log(response.follow(page))
        self.log('Saved file %s' % filename)
		
        addresses = [x.lstrip('(') for x in response.css('span.pubaddress::text').getall() if x != ')'] 
        for i in range(len(response.css('div.publist a::text').getall())):
            yield {
                    'pubname' : response.css('div.publist a::text').getall()[i],
                    'pubaddress' : addresses[i],
                    'pubpostcode' : response.css('span.pubpostcode b::text').getall()[i]
                    }