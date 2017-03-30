# -*- coding:utf-8 -*-
'''
file name: auto_upload.py
function : be used to upload the pic to qiniu.com
            then the pic will be delete
'''


from sevencow import Cow
from sevencow import CowException
import os


class AutoUploadPic(object):

    def __init__(self):

        self.cow = Cow("t6UadOn0bPkZE_qSFCmqvP1aVGyRGa6fyehGBAq6",
                       "tvOqQBsf6yZEAom95GVSncn1AUoZedQ2PEmRDrdi")
        # print(cow.list_buckets())
        self.current_bucket = None

    def upload_picture(self, bucket_name, file_name, keep_name=True):
        '''
        upload picture to qiniu
        '''

        self.current_bucket = self.cow.get_bucket(bucket_name)
        try:
            ret = self.current_bucket.put(file_name, keep_name=keep_name)
            return ret
        except CowException as e:
            print e.url          # 出错的url
            print e.status_code  # 返回码
            print e.content      # api 错误的原因
            return None


def get_change_files(path):
    '''
    get the change files list
    '''
    ret = os.popen("git status -s %s" % path)
    return [(line.split()[1]) for line in ret]


if __name__ == "__main__":
    al = AutoUploadPic()
    pictures = get_change_files("../picture/")

    for pic in pictures:
        ret = al.upload_picture("hexo-picture", pic)
        if ret is not None:
            print ("上传成功：%s " % ret)

