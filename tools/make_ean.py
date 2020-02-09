# -*- coding: UTF-8 -*-
import os
import sys
import barcode
from PIL import Image, ImageDraw, ImageFont
from barcode.writer import ImageWriter
from barcode.codex import Code128
from PyQt4 import QtGui, QtCore

class makeEan(object):
    # 创建图像,设置图像大小及颜色
    def __init__(self):
        self.imgCopyNum = 0

    def createEan(self, title_txt, info_txt, ean_code, num):
        titleTxt = title_txt + "*"+ num
        infoTxt = info_txt
        eanCode = ean_code
        self.imgCopyNum = int(num) or self.imgCopyNum
        imTitle = Image.open("resources/ean/imgTitleBg.png")
        imCopy = Image.open("resources/ean/imgCopyBg.png")
        draw1 = ImageDraw.Draw(imTitle)
        draw2 = ImageDraw.Draw(imCopy)

        # 设置本次使用的字体
        #fontsFolder = 'C:\Windows\Fonts'
        # font1 = ImageFont.truetype(os.path.join(fontsFolder, 'Arial.TTF'), 420)
        font1 = ImageFont.truetype("C:/windows/fonts/simsun.ttc", 22)
        font2 = ImageFont.truetype("C:/windows/fonts/simsun.ttc", 15)

        # "simsun.ttc", 40)
        # 计算各文本的放置位置
        #txtSize1 = draw1.textsize(titleTxt, font1)
        txtSize2 = draw2.textsize(infoTxt, font2)

        length = len(titleTxt)    
        utf8_length = len(titleTxt.encode('utf-8')) #获取放入的文字编码后的长度    
        length = (utf8_length - length) / 2 + length  #汉字是2个字节 英文和数字是单字节    
        draw1.text(((imTitle.size[0]- length * 11)/2, (imTitle.size[1]-22)/2),  unicode(titleTxt,'UTF-8'), fill=(0,0,0, 255), font=font1)
        draw2.text((imCopy.size[0]/2-txtSize2[0]/2, imCopy.size[1] - 50),  unicode(infoTxt,'UTF-8'), fill=(0,0,0, 255), font=font2)

        ean = Code128(eanCode, writer=ImageWriter())
        ean.save("tempEan")
        imgEan = Image.open("tempEan.png")
        imgEan.crop((0,0,imgEan.size[0],imgEan.size[1]))
        imgEan = imgEan.resize((imCopy.size[0]-26, 110)) 
        imCopy.paste(imgEan,((imCopy.size[0]-imgEan.size[0])/2,15))
        
        # 绘制线框
        #draw.line([(20, 20), (980, 20), (980, 1780), (20, 1780), (20, 20)], fill=(217, 217, 217, 255), width=5)
        showNum = self.imgCopyNum + 1
        resultImg = Image.new('RGB', (imCopy.size[0], showNum*imCopy.size[1]), (0, 0, 0))

        imTitleOrigin = imTitle.crop((0,0,imCopy.size[0],imCopy.size[1]))
        resultImg.paste(imTitleOrigin)
        
        for i in range(showNum):
          region = imCopy.crop((0,0,imCopy.size[0],imCopy.size[1]))
          resultImg.paste(region,(0,(i+1)*imCopy.size[1]))
        resultImg.show()
        
        if(os.path.exists("tempEan.png")):
            os.remove("tempEan.png")
        # 保存图像
        #filename = 'day.png'#+ str(i) +
        #imCopy.save(filename)
