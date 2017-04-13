# -*- coding:utf-8 -*-
'''
file name: auto_upload.py
function : be used to upload the pic to qiniu.com
            then the pic will be delete
'''


from sevencow import Cow
from sevencow import CowException
import os
import sys
import fire
import shutil


class AutoUploadPic(object):

    def __init__(self):

        self.cow = Cow("t6UadOn0bPkZE_qSFCmqvP1aVGyRGa6fyehGBAq6",
                       "tvOqQBsf6yZEAom95GVSncn1AUoZedQ2PEmRDrdi")
        # print(cow.list_buckets())
        self.current_bucket = None
        self.abs_path = None
        self.parent_path = None

    def upload(self, path, bucket_name="hexo-picture", keep_name=True):
        '''
        upload picture to qiniu
        '''
        files = []

        self.abs_path = os.path.abspath(path)
        if os.path.isfile(self.abs_path):
            self.parent_path = os.path.dirname(self.abs_path)
            file_name = os.path.basename(self.abs_path)
            files.append(file_name)
        elif os.path.isdir(self.abs_path):
            self.parent_path = self.abs_path
            for file_path in os.listdir(self.abs_path):
                if os.path.isfile(file_path):
                    file_name = os.path.basename(file_path)
                    files.append(file_name)

        # change to picture's parent_path
        os.chdir(self.parent_path)

        print("files:%s" % files)

        self.current_bucket = self.cow.get_bucket(bucket_name)
        for file in files:
            try:
                ret = self.current_bucket.put(file, keep_name=keep_name)
                print("上传成功: %s" % ret)

                self.backup_file(file)
            except CowException as e:
                print ("上传失败: file[%s] url[%s] status code[%s] content[%s]" % (
                    file, e.url, e.status_code, e.content))
                continue

    def backup_file(self, file):
        self.bak_path = os.path.join(self.parent_path, ".bak")
        if os.path.isdir(self.bak_path) is False:
            os.mkdir(self.bak_path)
        abs_path = os.path.abspath(file)
        if os.path.isfile(abs_path):
            shutil.move(abs_path, self.bak_path)
        else:
            print("file[%s] is not file" % abs_path)


if __name__ == "__main__":
    al = AutoUploadPic()
    fire.Fire(al)
    # if len(sys.argv) != 2:
    #     print ("输入错误，输入样例：auto_upload.py sample.jpg")
    # print sys.argv
    # # pictures = al.get_change_files("../picture")

    # # print os.getcwd()
    # # for pic in pictures:
    # #     ret = al.upload_picture("hexo-picture", pic)
    # #     if ret is not None:
    # #         print ("上传成功：%s " % ret)
