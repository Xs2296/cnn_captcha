import os, random
import numpy as  np
from PIL import Image

# 字符集
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']

# 配置
CAPTCHA_LIST = number + alphabet + ALPHABET
CAPTCHA_IMAGE_PATH = 'images/'
CAPTCHA_WIDTH = 480
CAPTCHA_HEIGHT = 125
CAPTCHA_LEN = 6


# 图片、验证码
def gen_captcha_text_and_image(imgPath=CAPTCHA_IMAGE_PATH):
    texts = []
    images = []
    for filePath in os.listdir(imgPath):
        captcha_text = filePath.split('.')[0]
        captcha_image = Image.open('images/' + filePath)
        captcha_image = np.array(captcha_image)
        texts.append(captcha_text)
        images.append(captcha_image)
    xx = random.randint(1, 100)
    return texts[xx - 1], images[xx - 1]


if __name__ == '__main__':
    res = gen_captcha_text_and_image()
    print(res)
