# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
from urllib import request
from scrapy.pipelines.images import ImagesPipeline

from doutuwang import settings


class DoutuwangPipeline(object):
    def __init__(self):
        self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images')
        if not os.path.exists(self.path):
            os.makedirs(self.path)

    def process_item(self, item, spider):
        category = item['category']
        img_list = item['image_urls']
        category = [x.strip() for x in category if x.strip() != '']
        print(category)
        for cate in category:
            if cate:
                category_path = os.path.join(self.path, cate)
                if not os.path.exists(category_path):
                    os.mkdir(category_path)
                for i in range(0, 4):
                    img = img_list[0]
                    img_name = img[-8:]
                    request.urlretrieve(img, os.path.join(category_path, img_name))
                    img_list.remove(img_list[0])
        return item

# class DoutuwangImagesPipeline(ImagesPipeline):
#     def get_media_requests(self, item, info):
#         # 下载之前请求调用
#         # 这个方法本身就是发送请求的
#         request_objs = super(DoutuwangImagesPipeline, self).get_media_requests(item, info)
#         for request_obj in request_objs:
#             request_obj.item = item
#         return request_objs
#
#     def file_path(self, request, response=None, info=None):
#         path = super(DoutuwangImagesPipeline, self).file_path(request, response, info)
#         category = request.item.get('category')
#         images_store = settings.IMAGES_STORE
#         category_path = os.path.join(images_store, category)
#         if os.path.exists(category_path):
#             os.makedirs(category_path)
#         images_store = path.replace("full", "")
#         images_path = os.path.join(category_path, images_store)
#         return images_path
