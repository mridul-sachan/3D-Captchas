import string 
import random 
import numpy, pylab
from PIL import Image, ImageDraw, ImageFont
#import matplotlib.axes3d as axes3d
from mpl_toolkits.mplot3d import Axes3D

def id_generator(size=4, chars=string.ascii_uppercase + string.digits):
    captcha_val = ''.join(random.choice(chars) for _ in range(size))
	return captcha_val
	
def 3D_Captcha(text):

	sz = (50,30)

	img = Image.new('L', sz, 255)
	drw = ImageDraw.Draw(img)
	font = ImageFont.truetype("arial.ttf", 20)

	drw.text((5,3), 'text', font=font)
	img.save('test.png')

	X , Y = numpy.meshgrid(range(sz[0]),range(sz[1]))
	Z = 1-numpy.asarray(img)/255

	fig = pylab.figure()
	ax = Axes3D(fig)
	ax.plot_wireframe(X, -Y, Z, rstride=1, cstride=1)
	ax.set_zlim((0,50))
	fig.savefig('test2.png')

'''
import string
import random

def id_generator(size=4, chars=string.ascii_uppercase + string.digits):
    print ''.join(random.choice(chars) for _ in range(size))
	
#if __name__ == "__main__":
#    main()
id_generator()
'''