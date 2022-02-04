# -*- coding: utf-8 -*-
# 导入所需的模块
import sys
import pygame

# 使用pygame之前必须初始化
pygame.init()
pygame.font.init()

# 设置主屏窗口
screen = pygame.display.set_mode((900, 400))
# screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)

# 设置窗口的标题，即游戏名称
pygame.display.set_caption('hello world')
# 填充主窗口的背景颜色，参数值RGB（颜色元组）
screen.fill((156, 156, 156))

# 引入字体类型
f = pygame.font.SysFont("comicsans", 50)
# 生成文本信息，第一个参数文本内容；第二个参数，字体是否平滑；
# 第三个参数，RGB模式的字体颜色；第四个参数，RGB模式字体背景颜色；
text = f.render("Helloworld", True, (255, 0, 0), (0, 0, 255))
# 获得显示对象的rect区域坐标
textRect = text.get_rect()
# 设置显示对象居中
textRect.center = (200, 200)
# 将准备好的文本信息，绘制到主屏幕 Screen 上。
screen.blit(text, textRect)

#创建一个 50*50 的图像,并优化显示
face = pygame.Surface((50,50),flags=pygame.HWSURFACE)
#填充颜色
face.fill(color='pink')

# convert 加载图片的像素格式，是为了提升 Pygame 对图片的处理速度
pygame.image.load("图片路径").convert()

"""
pygame.transform
允许您对加载、创建后的图像进行一系列操作，比如调整图像大小、旋转图片等操作
* scale 缩放至指定的大小
* rotate 旋转
* rotozoom 旋转并缩小或放大

Rect区域位置  创建一个指定位置，大小的矩形区域
rect =pygame.Rect(left,top,width,height) 

draw 绘画 矩形、多边形、圆形、直线、弧线等

mask  处理图形遮罩的模块



"""


# 固定代码段，实现点击"X"号退出界面的功能，几乎所有的pygame都会使用该段代码
while True:
    # 循环获取事件，监听事件状态
    for event in pygame.event.get():
        # 判断用户是否点了"X"关闭按钮,并执行if代码段
        if event.type == pygame.QUIT:
            # 卸载所有模块
            pygame.quit()
            # 终止程序，确保退出程序
            sys.exit()
    screen.blit(face, (100, 100))
    pygame.display.flip()  # 更新屏幕内容
