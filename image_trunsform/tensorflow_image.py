#!/usr/bin/python3
# -*-coding:UTF-8-*-
import matplotlib.pyplot as plt
import tensorflow as tf

image_bytes = tf.gfile.FastGFile("1.png", 'rb').read()  # 字节
with tf.Session() as session:
    img = tf.image.decode_jpeg(image_bytes)
    # 翻转图片
    img_flipped = tf.image.flip_up_down(img)  # 上下反转
    img_flipped = tf.image.flip_left_right(img_flipped)  # 左右反转
    img_flipped = tf.image.transpose_image(img_flipped)  # 对角线反转
    img_flipped = tf.image.random_flip_up_down(img_flipped)  # 随机上下反转
    img_flipped = tf.image.random_flip_left_right(img_flipped)  # 随机左右反转
    # 亮度设置
    img_adjust = tf.image.adjust_brightness(img_flipped, -0.5)  # 增加亮度
    img_adjust = tf.image.adjust_brightness(img_adjust, +0.5)  # 降低亮度
    img_adjust = tf.image.random_brightness(img_adjust, max_delta=0.3)  # 随机调整亮度，亮度在[-max_delta, +max_delta]]
    img_saturation = tf.image.adjust_saturation(img_adjust, 1.5)  # 支持random#饱和度
    img_hue = tf.image.adjust_hue(img_saturation, delta=0.2)  # 色度
    # 对比度
    img_contrast = tf.image.adjust_contrast(img_hue, 0.5)
    # 图片标准化
    img_standard = tf.image.per_image_standardization(img_adjust)
    img_standard = tf.clip_by_value(img_standard, 0.0, 10)
    # 转成数组
    img_array = img_standard.eval()
    plt.imshow(img_array)
    plt.show()
