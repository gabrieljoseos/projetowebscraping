import scrapy

class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    allowed_domains = ["mercadolivre.com.br"]
    start_urls = ["https://www.mercadolivre.com.br/ofertas?container_id=MLB779535-1"] #Site de oferta do dia (01/08)
    page_count = 1
    max_pages = 6 #Máximo de página encontrado no site 

    def parse(self, response):
        products = response.css('div.promotion-item__description')

        for product in products:
            name = product.css('p.promotion-item__title::text').get()
            old_price_reais = product.css('span.andes-money-amount__fraction::text').getall()[1] if len(product.css('span.andes-money-amount__fraction::text').getall()) > 1 else None
            old_price_cents = product.css('span.andes-money-amount__cents::text').getall()[1] if len(product.css('span.andes-money-amount__cents::text').getall()) > 1 else None
            new_price_reais = product.css('span.andes-money-amount__fraction::text').get()
            new_price_cents = product.css('span.andes-money-amount__cents::text').get()
            discount = product.css('span.promotion-item__discount-text::text').get()
            seller = product.css('span.promotion-item__seller::text').get()

            yield {
                'name': name,
                'old_price_reais': old_price_reais,
                'old_price_cents': old_price_cents,
                'new_price_reais': new_price_reais,
                'new_price_cents': new_price_cents,
                'discount': discount,
                'seller': seller,
            }
# Puxar a informação de todas a páginas
        if self.page_count < self.max_pages:
            next_page = response.css('li.andes-pagination__button.andes-pagination__button--next a::attr(href)').get()
            if next_page:
                self.page_count += 1
                yield response.follow(next_page, self.parse)