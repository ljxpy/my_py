#合并
print("*********开始合并***********")
from moviepy.editor import *
import os
L = []
for root, dirs, files in os.walk(r'D:\新建文件夹\编程资源库\爬虫\mov\速度与激情2\000'):
    files.sort()
    for file in files:
        # 拼接成完整路径
        filePath = os.path.join(root, file)
        # 载入视频
        video = VideoFileClip(filePath)
        # 添加到数组
        L.append(video)
        print(file, "完成")
# 拼接视频
final_clip = concatenate_videoclips(L)
# 生成目标视频文件
final_clip.to_videofile("D:\新建文件夹\编程资源库\爬虫\mov\速度与激情2\速度与激情(完整版).mp4", fps=24, remove_temp=False)
