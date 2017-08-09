# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class JobBoleArticleItem(scrapy.Item):
    #field mean any transition
    title = scrapy.Field()
    #date
    create_date = scrapy.Field()
    #url
    url = scrapy.Field()
    #url length control
    ur_object_id = scrapy.Field()
    #get the image title
    front_image_url = scrapy.Field()
    #front_iamge_path
    front_iamge_path = scrapy.Field()
    #comment numbers
    comment_nums = scrapy.Field()
    #get the praise nums
    praise_nums = scrapy.Field()
    #get fav numbers
    fav_nums = scrapy.Field()
    #get the tags
    tags = scrapy.Field()
    #get content
    content = scrapy.Field()