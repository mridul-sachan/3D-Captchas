#!/usr/bin/python27

'''
This code generates a 3d captcha image which is un-breakable by bots.
@Author : Mridul  
@Date : April 2, 2017
'''

import string 
import random 
import cv2 
import numpy, pylab
from PIL import Image, ImageDraw, ImageFont
#import matplotlib.axes3d as axes3d
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
from PIL import Image 

def id_generator():
    print 'Generating plain captcha using letters and digits.'
    captcha_list = []
    size = 4                   #here we have taken captcha length as 4, we can change it to desired length.
    chars = string.ascii_uppercase + string.digits # generating characters by combining letters and strings.
    for _ in range(size):
        captcha_val = ''.join(random.choice(chars))
        captcha_list.append(captcha_val)
	
    captcha_str = ""	
    for item in captcha_list:
        captcha_str = captcha_str + str(item)
    captcha_val = captcha_str
    return captcha_val	
	
def threed_gen():

    captcha = id_generator()
    print 'Converting plain captcha into a 3D image based captcha.'

    image_size = (70,30)

    img = Image.new('L', image_size, 255)
    drw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 20)

    drw.text((5,5), captcha, font=font)
    img.save('plain_captcha.png')

    X , Y = numpy.meshgrid(range(image_size[0]),range(image_size[1]))
    Z = 1-numpy.asarray(img)/255

    fig = pylab.figure()
    ax = Axes3D(fig)
    ax.plot_wireframe(X, -Y, Z, rstride=1, cstride=1)
    ax.set_zlim((0,50))
    fig.savefig('3d_captcha.png')


def show_captcha():
    img = cv2.imread('3d_captcha.png',0)
    cv2.imshow('Captcha Window',img)
    k = cv2.waitKey(0)
    if k == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()
    elif k == ord('s'):
        cv2.imwrite('001.png',img)
        cv2.destroyAllWindows()
	
def main():


    print '1. Normal Captcha :'
    print '2. 3D based Captcha :'
    inp = raw_input('Enter your choice from above :')
    if inp == '1':
        threed_gen()
        show_original()
    elif inp == '2':
        threed_gen()
        show_captcha()
    else :
        print 'Try Again...Wrong Input chosen.'
        exit()

    print 'Captcha generated successfully.'

		
def show_original():
    img = cv2.imread('plain_captcha.png',0)
    cv2.imshow('Plain Image',img)
    k = cv2.waitKey(0)
    if k == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()
    elif k == ord('s'): 
        cv2.imwrite('002.png',img)
        cv2.destroyAllWindows()
   

	
if __name__ == "__main__":
    main()


    

'''
import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('messi5.jpg',0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
'''