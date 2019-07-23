import scrapy
from scrapy.pipelines.images import ImagesPipeline

class CustomImageNamePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
            return [scrapy.Request(item, meta={'image_name': item["manga_page"]})]

    def file_path(self, request, response=None, info=None):
        return '%s.jpg' % request.meta['image_name']