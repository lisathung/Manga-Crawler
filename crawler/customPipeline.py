import scrapy
from scrapy.pipelines.images import ImagesPipeline

class CustomImageNamePipeline(ImagesPipeline):
    '''
    overwrites the base ImagesPipeline to save the images into chapter wise folders
    '''
    def get_media_requests(self, item, info):
        '''
        set the metadata for your file
        '''
        return [scrapy.Request(item['image_urls'][0], meta={'image_name':item['manga_page'] , 'image_folder':item['manga_chapter'] })]

    def file_path(self, request, response=None, info=None):
        '''
        define the folder and file name
        '''
        return '{}/{}.jpg'.format(request.meta['image_folder'] , request.meta['image_name'])