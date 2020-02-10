# -*- coding: UTF-8 -*-
import os
import sys
import barcode
import utils
from PIL import Image, ImageDraw, ImageFont
from barcode.writer import ImageWriter
from barcode.codex import Code128
from PyQt4 import QtGui, QtCore

IMG_DEFAULT_LEN = "60"
IMG_DEFAULT_WIDTH = "40"
PRINT_DEFAULT_DIP = "200"

class makeEan(object):
    # 创建图像,设置图像大小及颜色
    def __init__(self):
        self.__obj_utils = utils.Utils()
        self.__offset_height = 5
        # self.__ean_default_size = ()

    def createEan(self, title_txt, info_txt, ean_code, num, path, size, dip):
        imgCopySize = [0, 0]
        try:
            imgCopySize[0] = float(size[0])
            imgCopySize[1] = float(size[1])
        except ValueError:
            pass
        try:
            imgCopySize[0] = int(size[0])
            imgCopySize[1] = int(size[1])
        except ValueError:
            pass
        self.scale = (imgCopySize[0]*float(dip)/(float(IMG_DEFAULT_LEN)*float(PRINT_DEFAULT_DIP)), imgCopySize[1]*float(dip)/(float(IMG_DEFAULT_WIDTH)*float(PRINT_DEFAULT_DIP)))
        self.minScale = self.scale[0] < self.scale[1] and self.scale[0] or self.scale[1]
        imgCopySize = (
            int(dip * imgCopySize[0]*0.03937), int(dip*imgCopySize[1]*0.03937))
        titleTxt = title_txt + "*" + num
        infoTxt = info_txt
        eanCode = ean_code
        self.imgCopyNum = int(num) or 0
        imTitle = Image.new(
            'RGBA', (imgCopySize[0], imgCopySize[1]), (255, 255, 255, 255))
        #Image.open("resources/ean/imgTitleBg.png")
        imCopy = Image.new(
            'RGBA', (imgCopySize[0], imgCopySize[1]), (255, 255, 255, 255))
        #Image.open("resources/ean/imgCopyBg.png")
        draw1 = ImageDraw.Draw(imTitle)
        draw1.line([(1, 1), (imgCopySize[0] - 1, 1), (imgCopySize[0] - 1, imgCopySize[1]-1),
                    (1, imgCopySize[1]-1), (1, 1)], fill=(217, 50, 50, 255), width=5)

        draw2 = ImageDraw.Draw(imCopy)
        draw2.line([(1, 1), (imgCopySize[0] - 1, 1), (imgCopySize[0] - 1, imgCopySize[1]-1),
                    (1, imgCopySize[1]-1), (1, 1)], fill=(217, 50, 50, 255), width=5)

        # 设置本次使用的字体
        #fontsFolder = 'C:\Windows\Fonts'
        # font1 = ImageFont.truetype(os.path.join(fontsFolder, 'Arial.TTF'), 420)
        font1 = ImageFont.truetype("C:/windows/fonts/simsun.ttc", int(40*self.minScale))
        font2 = ImageFont.truetype("C:/windows/fonts/simsun.ttc", int(25*self.minScale))
        font3 = ImageFont.truetype("C:/windows/fonts/simsun.ttc", int(28*self.minScale))

        ean = Code128(eanCode, writer=ImageWriter())
        ean.save("tempEan")
        imgEan = Image.open("tempEan.png")
        size = (int(imgEan.size[0]*self.scale[0]), int(imgEan.size[1]*self.scale[1]))
        print size
        imgEan = imgEan.resize(size)
        imgEan.crop((0, 0, imgEan.size[0], imgEan.size[1]))
        imCopy.paste(imgEan, ((imCopy.size[0]-imgEan.size[0])/2, 15))

        length = len(titleTxt)
        utf8_length = len(titleTxt.encode('utf-8'))  # 获取放入的文字编码后的长度
        length = (utf8_length - length) / 2 + length  # 汉字是2个字节 英文和数字是单字节
        draw1.text(((imTitle.size[0] - length * 11)/2, (imTitle.size[1]-22)/2),
                   unicode(titleTxt, 'UTF-8'), fill=(0, 0, 0, 255), font=font1)
        tempTextSize = draw2.textsize(infoTxt, font2)
        draw2.text((imCopy.size[0]/2-tempTextSize[0]/2, imCopy.size[1] - 70),
                   unicode(infoTxt, 'UTF-8'), fill=(0, 0, 0, 255), font=font2)
        tempTextSize = draw2.textsize("Make In China", font3)
        draw2.text(10, imCopy.size[1] - 40),
                   unicode("New", 'UTF-8'), fill=(0, 0, 0, 255), font=font3)
        draw2.text((imCopy.size[0]- (10 + tempTextSize[0]), imCopy.size[1] - 40),
                   unicode("Make In China", 'UTF-8'), fill=(0, 0, 0, 255), font=font3)

        # 绘制线框
        #draw.line([(1, 1), (980, 1), (980, 1780), (1, 1780), (1, 1)], fill=(217, 217, 217, 255), width=5)
        showNum = self.imgCopyNum + 1
        resultImg = Image.new(
            'RGBA', (imCopy.size[0], showNum*imCopy.size[1]+self.imgCopyNum*self.__offset_height), (0, 0, 0, 255))
        imTitleOrigin = imTitle.crop((0, 0, imCopy.size[0], imCopy.size[1]))
        resultImg.paste(imTitleOrigin)

        for i in range(showNum):
            region = imCopy.crop((0, 0, imCopy.size[0], imCopy.size[1]))
            resultImg.paste(region, (0, (i+1)*(imCopy.size[1]+self.__offset_height)))
        resultImg.show()

        if(os.path.exists("tempEan.png")):
            os.remove("tempEan.png")
       # self.__obj_utils.create_dir_not_exist(self.__obj_utils.transform_path(path))
       # resultImg.save(path+"\\"+title_txt+".png", 'png')

        return True
        # 保存图像
        #filename = 'day.png'#+ str(i) +
        #imCopy.save(filename)
