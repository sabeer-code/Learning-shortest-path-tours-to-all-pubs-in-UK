import scrapy


class PubsSpider(scrapy.Spider):
    
    name = "pubs"
    
    start_urls = ['https://www.pubsgalore.co.uk/counties/bedfordshire/',
                  'https://www.pubsgalore.co.uk/counties/berkshire/',
                  'https://www.pubsgalore.co.uk/counties/bristol/',
                  'https://www.pubsgalore.co.uk/counties/buckinghamshire/',
                  'https://www.pubsgalore.co.uk/counties/cambridgeshire/',
                  'https://www.pubsgalore.co.uk/counties/cheshire/',
                  'https://www.pubsgalore.co.uk/counties/cornwall/',
                  'https://www.pubsgalore.co.uk/counties/county-durham/',
                  'https://www.pubsgalore.co.uk/counties/cumbria/',
                  'https://www.pubsgalore.co.uk/counties/derbyshire/',
                  'https://www.pubsgalore.co.uk/counties/devon/',
                  'https://www.pubsgalore.co.uk/counties/dorset/',
                  'https://www.pubsgalore.co.uk/counties/east-riding-of-yorkshire/',
                  'https://www.pubsgalore.co.uk/counties/east-sussex/',
                  'https://www.pubsgalore.co.uk/counties/essex/',
                  'https://www.pubsgalore.co.uk/counties/gloucestershire/',
                  'https://www.pubsgalore.co.uk/counties/hampshire/',
                  'https://www.pubsgalore.co.uk/counties/herefordshire/',
                  'https://www.pubsgalore.co.uk/counties/hertfordshire/',
                  'https://www.pubsgalore.co.uk/counties/isle-of-wight/',
                  'https://www.pubsgalore.co.uk/counties/kent/',
                  'https://www.pubsgalore.co.uk/counties/lancashire/',
                  'https://www.pubsgalore.co.uk/counties/leicestershire/',
                  'https://www.pubsgalore.co.uk/counties/lincolnshire/',
                  'https://www.pubsgalore.co.uk/counties/central-london/',
                  'https://www.pubsgalore.co.uk/counties/greater-london/',
                  'https://www.pubsgalore.co.uk/counties/greater-manchester/',
                  'https://www.pubsgalore.co.uk/counties/merseyside/',
                  'https://www.pubsgalore.co.uk/counties/norfolk/',
                  'https://www.pubsgalore.co.uk/counties/north-yorkshire/',
                  'https://www.pubsgalore.co.uk/counties/northamptonshire/',
                  'https://www.pubsgalore.co.uk/counties/northumberland/',
                  'https://www.pubsgalore.co.uk/counties/nottinghamshire/',
                  'https://www.pubsgalore.co.uk/counties/oxfordshire/',
                  'https://www.pubsgalore.co.uk/counties/rutland/',
                  'https://www.pubsgalore.co.uk/counties/shropshire/',
                  'https://www.pubsgalore.co.uk/counties/somerset/',
                  'https://www.pubsgalore.co.uk/counties/south-yorkshire/',
                  'https://www.pubsgalore.co.uk/counties/staffordshire/',
                  'https://www.pubsgalore.co.uk/counties/suffolk/',
                  'https://www.pubsgalore.co.uk/counties/surrey/',
                  'https://www.pubsgalore.co.uk/counties/tyne-wear/',
                  'https://www.pubsgalore.co.uk/counties/warwickshire/',
                  'https://www.pubsgalore.co.uk/counties/west-midlands/',
                  'https://www.pubsgalore.co.uk/counties/west-sussex/',
                  'https://www.pubsgalore.co.uk/counties/west-yorkshire/',
                  'https://www.pubsgalore.co.uk/counties/wiltshire/',
                  'https://www.pubsgalore.co.uk/counties/worcestershire/',
                  'https://www.pubsgalore.co.uk/counties/county-antrim/',
                  'https://www.pubsgalore.co.uk/counties/county-armagh/',
                  'https://www.pubsgalore.co.uk/counties/county-down/',
                  'https://www.pubsgalore.co.uk/counties/county-fermanagh/',
                  'https://www.pubsgalore.co.uk/counties/county-londonderry/',
                  'https://www.pubsgalore.co.uk/counties/county-tyrone/',
                  'https://www.pubsgalore.co.uk/counties/borders/',
                  'https://www.pubsgalore.co.uk/counties/central/',
                  'https://www.pubsgalore.co.uk/counties/dumfries-galloway/',
                  'https://www.pubsgalore.co.uk/counties/fife/',
                  'https://www.pubsgalore.co.uk/counties/grampian/',
                  'https://www.pubsgalore.co.uk/counties/highland/',
                  'https://www.pubsgalore.co.uk/counties/lothian/',
                  'https://www.pubsgalore.co.uk/counties/orkney/',
                  'https://www.pubsgalore.co.uk/counties/shetland/',
                  'https://www.pubsgalore.co.uk/counties/strathclyde/',
                  'https://www.pubsgalore.co.uk/counties/tayside/',
                  'https://www.pubsgalore.co.uk/counties/western-isles/',
                  'https://www.pubsgalore.co.uk/counties/clwyd/',
                  'https://www.pubsgalore.co.uk/counties/dyfed/',
                  'https://www.pubsgalore.co.uk/counties/gwent/',
                  'https://www.pubsgalore.co.uk/counties/gwynedd/',
                  'https://www.pubsgalore.co.uk/counties/mid-glamorgan/',
                  'https://www.pubsgalore.co.uk/counties/powys/',
                  'https://www.pubsgalore.co.uk/counties/south-glamorgan/',
                  'https://www.pubsgalore.co.uk/counties/west-glamorgan/'
                  ]
    
    
    def parsePub(self, response):
        
        yield{
            'pub_name': response.xpath("//meta[@property='og:title']").css("meta::attr(content)").get(),
            'region': response.xpath("//meta[@property='og:region']").css("meta::attr(content)").get(),
            'locality': response.xpath("//meta[@property='og:locality']").css("meta::attr(content)").get(),
            'url': response.xpath("//meta[@property='og:url']").css("meta::attr(content)").get(),
            'longitude': response.xpath("//meta[@property='og:longitude']").css("meta::attr(content)").get(),
            'latitude': response.xpath("//meta[@property='og:latitude']").css("meta::attr(content)").get(),
            'postcode': response.xpath("//meta[@property='og:postal-code']").css("meta::attr(content)").get(),
            'country': response.xpath("//meta[@property='og:country-name']").css("meta::attr(content)").get()
        }
    
    
    
    def parseTown(self, response):
        pubs = response.css('div.pubopen a::attr(href)').getall()
                
#         To include closed pubs
#          pubs += response.css('div.pubclosed a::attr(href)').getall()
                
          if pubs is not None:
              for pub in pubs:
                  pub = response.urljoin(pub)
                  yield scrapy.Request(pub, callback=self.parsePub)

    
    def parse(self, response):
        
        towns = response.css('a.townlink::attr(href)').getall()
        
        if towns is not None:
            for town in towns:
                town = response.urljoin(town)
                yield scrapy.Request(town, callback=self.parseTown)