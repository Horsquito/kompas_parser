import scrapy
from ..items import KompasParserItem
from datetime import datetime



class QuotesSpider(scrapy.Spider):
    name = "kompas_parser"

    def start_requests(self):
        url = 'https://ru.kompass.com/en/searchCompanies?acClassif=&localizationCode=&localizationLabel=&localizationType=&text=caustic+soda&searchType=SUPPLIER'
        yield scrapy.Request(url, self.parse, meta={'download_timeout': 10})

    def parse(self, response):
        links = response.xpath('//h2/a/@href').getall()
        for link in links[3:]:
            url = 'https://ru.kompass.com' + link
            yield scrapy.Request(url, self.parse_company_info, meta={'download_timeout': 10})

    def parse_company_info(self, response):
        item = KompasParserItem()
        name = response.xpath('//h1/text()').get()
        last_update = response.xpath('//*[@id="lastUpdate"]/span/text()').get()
        import_zones = response.xpath('//*[@id="import"]/div[@id="importZones"]/text()').get()
        import_countries = response.xpath('//*[@id="import"]/div[@id="importCountries"]/text()').get()
        export_zones = response.xpath('//*[@id="export"]/div[@id="exportZones"]/text()').get()
        phone = response.xpath('//*[@id="productDetailUpdateable"]/div[2]/div[2]/div[1]/div/div/div[1]/div[3]/span[@class="faxNumber"]/text()').get()
        website = response.xpath('//div[@class="companyWeb"]/div[@class="listWww"]/p/a/text()').get()
        country = response.xpath('//*[@id="productDetailUpdateable"]/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/p[2]/span[2]/text()').get()
        description = response.xpath('//*[@id="mainActivitiesTree"]/ul/li[1]/ul/li/a/text()').getall()
        date_and_time = datetime.now().strftime('%y-%d-%m')
        if import_zones:
            import_zones = import_zones.strip()
        if import_countries:
            import_countries = import_countries.strip()
        if export_zones:
            export_zones = export_zones.strip()
        if phone:
            phone = phone.strip()
        name = name.strip()
        item['name'] = name
        item['last_update'] = last_update
        item['import_zones'] = import_zones
        item['import_countries'] = import_countries
        item['export_zones'] = export_zones
        item['phone'] =  phone
        item['website'] =  website
        item['country'] = country
        item['product'] = 'caustic+soda'
        item['hs_code'] = 281511
        item['source'] = 'https://www.kompass.com/'
        item['date_and_time'] = date_and_time
        item['description'] = description
        yield item
