import tensorflow as tf
from train import cnn_graph
from captcha import gen_captcha_text_and_image
from process import vec2text, convert2gray
from process import CAPTCHA_WIDTH, CAPTCHA_HEIGHT, CAPTCHA_LEN, CAPTCHA_LIST
from PIL import Image
import numpy as np


# 验证码图片转化为文本
def captcha2text(image_list, height=CAPTCHA_HEIGHT, width=CAPTCHA_WIDTH):
    x = tf.placeholder(tf.float32, [None, height * width])
    keep_prob = tf.placeholder(tf.float32)
    y_conv = cnn_graph(x, keep_prob, (height, width))
    saver = tf.train.Saver()
    with tf.Session() as sess:
        saver.restore(sess, tf.train.latest_checkpoint('.'))
        predict = tf.argmax(tf.reshape(y_conv, [-1, CAPTCHA_LEN, len(CAPTCHA_LIST)]), 2)
        vector_list = sess.run(predict, feed_dict={x: image_list, keep_prob: 1})
        vector_list = vector_list.tolist()
        text_list = [vec2text(vector) for vector in vector_list]
        print(text_list)
        print('#' * 30)
        return text_list


if __name__ == '__main__':
    captcha_image = Image.open('2.jpg')
    captcha_image = np.array(captcha_image)
    # text, image = gen_captcha_text_and_image()
    image = convert2gray(captcha_image)
    image = image.flatten() / 255
    pre_text = captcha2text([image])
    print('Label:', 'zNbQ9R', ' Predict:', pre_text)
