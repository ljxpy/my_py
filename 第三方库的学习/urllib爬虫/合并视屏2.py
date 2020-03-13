#合并
print("*********开始合并***********")
from moviepy.editor import *
import os
import time
for i in range(0, 8):
    L = []
    root = r'D:\新建文件夹\编程资源库\爬虫\mov\速度与激情2\%d--%d\\'%(i*200+1,i*200+200)
    for file in range(i*200+1, i*200+201):
            file =str(file)
            # 拼接成完整路径
            filePath = root+file+".ts"
            # 载入视频
            video = VideoFileClip(filePath)
            # 添加到数组
            L.append(video)
            print(file, "完成")
    # 拼接视频
    final_clip = concatenate_videoclips(L)
    del L
    # 生成目标视频文件
    final_clip.to_videofile("D:\新建文件夹\编程资源库\爬虫\mov\速度与激情2\速度与激情%d--%d.mp4"%(i*200+1,i*200+200), fps=24, remove_temp=False)
    time.sleep(10)