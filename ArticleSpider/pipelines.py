# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline

#this pipeline it process the item
class ArticlespiderPipeline(object):
    def process_item(self, item, spider):
        return item

#this pipeline it process the font images
#image.py can help us download the images
#and convert images, filter them
class ArticleImagePipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        #if "front_image_url" in item:
        for ok, value in results:
            image_file_path = value["path"]
        item["front_image_path"] = image_file_path
        #we must return item
        #since we need to deal with the next one pipeline
        return item