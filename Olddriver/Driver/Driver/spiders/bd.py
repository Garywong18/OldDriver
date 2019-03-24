# -*- coding: utf-8 -*-
import scrapy
import json


class BdSpider(scrapy.Spider):
    name = 'bd'
    allowed_domains = ['jiakaobaodian.com']
    start_urls = ['https://api2.jiakaobaodian.com/api/open/exercise/sequence.htm?_r=14588837051401314078&carType=car&cityCode=110000&course=kemu1&_=0.6534614660872664']

    def parse(self, response):
        json_data = response.text
        dict_data = json.loads(json_data)
        question_id = dict_data['data']
        for i in question_id:
            headers = {
                'referer':'http://www.jiakaobaodian.com/mnks/exercise/0-car-kemu1.html?id={}'.format(i)
            }
            url = 'https://api2.jiakaobaodian.com/api/open/question/view.htm?_r=13537871457392893100&questionId={}'.format(i)
            yield scrapy.Request(
                url,
                headers=headers,
                callback=self.parse_json
            )

    def parse_json(self,response):
        item = {}
        json_data = response.text
        dict_data = json.loads(json_data)
        item['answer'] = dict_data['data']['answer']
        item['question'] = dict_data['data']['question']
        option_dict = {
            '1':dict_data['data']['optionA'],
            '2': dict_data['data']['optionB'],
            '3': dict_data['data']['optionC'],
            '4': dict_data['data']['optionD'],
            '5': dict_data['data']['optionE'],
            '6': dict_data['data']['optionF'],
            '7': dict_data['data']['optionG'],
            '8': dict_data['data']['optionH']

        }
        for key in list(option_dict.keys()):
            if option_dict[key] is '':
                del option_dict[key]

        item['option'] = option_dict
        if dict_data['data']['mediaType'] == 1:
            item['page_url'] = dict_data['data']['mediaContent']
        else:
            item['page_url'] = ''
        yield item

