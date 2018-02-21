# -*- coding: utf-8 -*-
import scrapy
import json


class NewSpider(scrapy.Spider):
    name = 'new'
    header={
        "Host": "www.zhihu.com",
        "Referer":"https://www.zhihu.com/question/22212644",
        "X-UDID": "AAAtgc1lLA2PTpSFekS8I-WLyw6fVnJDIZw=",
        "accept":"application/json, text/plain, */*",
"authorization": "Bearer Mi4xbVlYNUFBQUFBQUFBMEd4dkpJNGlEUmNBQUFCaEFsVk5ydEZ1V3dESlVoY3RRMUczVnJKbUtmb1lLQUhfZlgyaUh3|1518437294|599da5070c62457bb7a69f82e45e129fb803cc78",
                                                                                                   "Connection":"keep-alive",
    }

    urls =['http://www.zhihu.com/api/v4/questions/22212644/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cupvoted_followees%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics&limit=20&offset=0&sort_by=default']



    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url, method='GET', callback=self.parse, headers=self.header, cookies=self.cookies)

    def parse(self, response):
        ee = json.loads(response.body_as_unicode())
        a = ee["paging"]
        b = a["next"]
        for stra in response.css('img').xpath("@src").extract():
            if stra.startswith('\\"http'):
                with open('yes.txt','a') as f:
                    f.write(stra[2:-2]+'\n')



            yield scrapy.Request(url=b, method='GET', callback=self.parse, headers=self.header,cookies=self.cookies,)
