import sys
import pygame

# 使用pygame之前必须初始化
pygame.init()
pygame.font.init()

# 设置主屏窗口
screen = pygame.display.set_mode((900, 400))
# 绘制一条宽度为 3 的红色对角线
pygame.draw.line(screen, (0, 255, 0), [0, 0], (500, 450), 3)
# 绘制多条蓝色的直线（连续直线，非抗锯齿），False 表示首尾不相连
pygame.draw.lines(screen, (0, 0, 255), False, [[0, 80], [50, 90], [200, 80], [220, 30]], 1)
# 绘制一个灰色的矩形区域，以灰色填充区域
pygame.draw.rect(screen, (155, 155, 155), (75, 10, 50, 20), 0)
# 绘制一个线框宽度为2的矩形区域
pygame.draw.rect(screen, (0, 0, 0), [150, 10, 50, 20], 2)
# 绘制一个椭圆形,其线宽为2
pygame.draw.ellipse(screen, (255, 0, 0), (225, 10, 50, 20), 2)
# 绘制一个实心的红色椭圆形
pygame.draw.ellipse(screen, (255, 0, 0), (300, 10, 50, 20))
# 绘制一个绿色边框(宽度为2)三角形
pygame.draw.polygon(screen, (100, 200, 45), [[100, 100], [0, 200], [200, 200]], 2)
# 绘制一个蓝色实心的圆形，其中[60,250]表示圆心的位置，40为半径，width默认为0
pygame.draw.circle(screen, (0, 0, 255), [60, 250], 40)
# 绘制一个圆弧,其中0表示弧线的开始位置，pi/2表示弧线的结束位置，2表示线宽
pygame.draw.arc(screen, (255, 10, 0), (210, 75, 150, 125), 0, pi / 2, 2)
