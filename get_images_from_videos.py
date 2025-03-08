pip install opencv-python
import cv2
import os

# 视频文件路径
video_path = 'D:\学习\AI\video'

# 图像保存目录
image_dir = 'D:\学习\AI'

# 保存图像的时间间隔（单位为秒）
interval = 1

# 创建保存图像的目录
if not os.path.exists(image_dir):
    os.makedirs(image_dir)

# 打开视频文件
cap = cv2.VideoCapture(video_path)

# 获取视频帧速率
fps = cap.get(cv2.CAP_PROP_FPS)

# 计算每隔多少帧保存一张图像
frame_interval = int(interval * fps)

# 初始化计数器
count = 0

# 遍历视频帧
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        # 如果计数器能被frame_interval整除，就保存当前帧
        if count % frame_interval == 0:
            # 生成图像文件名，格式为“image_序号.jpg”
            image_name = 'image_{:04d}.jpg'.format(count)
            # 保存图像文件
            cv2.imwrite(os.path.join(image_dir, image_name), frame)
        count += 1
    else:
        break

# 释放视频文件句柄
cap.release()
