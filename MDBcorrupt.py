# -*- coding=utf-8 -*-
import os
import stat

class MDBcorrupt:

    def __init__(self,filename):
        self.filename = filename

    def corrupt(self):
        os.chmod(self.filename, stat.S_IWRITE)
        f = open(self.filename,"r+b")
        f.seek(3586)
        f.write("\x96\x04\x01\x00\x0c\x01\x01")
        f.close()

    def repair(self):
        os.chmod(self.filename, stat.S_IWRITE)
        f = open(self.filename,"r+b")
        f.seek(3586)
        f.write("\xFF\xFF\xFF\xFF\xFF\xFF\xFF")
        f.close()
