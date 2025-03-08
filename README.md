#  视频片段转图片

1. 简介

因采集数据需要，做一个简单的界面。

1. 最上方的是进度条，可以拖动；
2. 点击暂停，将自动记录当前帧作为起始帧（start frame）
3. 结束帧为起始帧+50帧；
4. save path 是将保存的图片保存地址
5. 点击保存，会将起始帧到结束帧之间的图片每隔5帧进行保存

![](C:\Users\wht\AppData\Roaming\Typora\typora-user-images\image-20230428135040433.png)

2. 环境要求
   1. pyqt
   2. opencv
3. 使用方法
   1. 运行代码，在进度条滑动到指定动作画面前，点击pause，进度条会自动继续，但是会将pause 点击的帧记录在start Frame 
   2. 修改Save Path 地址
   3. 点击保存
4. 程序参数介绍
   1. VideoPlayer的入参是视频源

```python
if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = VideoPlayer('./video/1.mp4')
    player.show()
    sys.exit(app.exec_())
```

 2. ```python
            for frame_num in range(start_frame, start_frame+50):## 50为end Frame 与start Frame 的间隔
                self.cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
                ret, frame = self.cap.read()
                if ret:
                    if self.cap.get(cv2.CAP_PROP_POS_FRAMES)%5 == 0:   # 这里是每隔多少帧保存一张图片
                        path_s = '{}w{:04}.jpg'.format(save_path, frame_num)
                        print(self.cap.get(cv2.CAP_PROP_POS_FRAMES),path_s)
                        cv2.imwrite('{}w{:04}.jpg'.format(save_path, frame_num), frame)
    ```

    