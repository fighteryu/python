from PIL import Image
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('file')
parser.add_argument('-o','--output')
parser.add_argument('--width',type = int ,default = 100)

parser.add_argument('--height',type = int, default = 50)

args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

ascii_char = list("&@B%8*WM#$oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!;:,\"^`' ")
def get_char(r,b,g,alpha = 256):
  if alpha == 0:
		return ' '
	length = len(ascii_char)
	gray = int(0.2126*r+0.7152*g+0.0722*b)

	unit = (256.0+1)/length
	return ascii_char[int(gray/unit)]

if __name__ == '__main__':
	im = Image.open(IMG)
	im = im.resize((WIDTH,HEIGHT),Image.NEAREST)

	txt = ""

	for i in range(HEIGHT):
		for j in range(WIDTH):
			txt += get_char(*im.getpixel((j,i)))
		txt += '\n'

	print(txt)

	if OUTPUT:
		with open(OUTPUT,'w') as f:
			f.writh(txt)
	else:
		with open("output.txt",'w') as f:
			f.write(txt)
'''python Pillow_PIL_ASCII.py /filename
'''

'''another
'''
import argparse
from PIL import Image

def handle_command():
    '命令行参数处理'
    parser = argparse.ArgumentParser()
    parser.add_argument('filename',help = '图片的路径')
    parser.add_argument('-o','--output',help = '是否输出文件')
    parser.add_argument('--width',type = int,default = 80)
    parser.add_argument('--heigth',type = int,default = 80)

    #获取命令行参数
    return parser.parse_args()

args = handle_command()

class Ptrancefrom(object):
    '实现将图片转化为字符'
    def __init__(self,img,width,heigth):
        self.img = img
        self.width = width
        self.heigth = heigth
        self.ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

    def get_char(self,r,b,g,alpha = 256):
        '将256范围的灰度值映射到70个字符上'
        #灰度值为0时对应字符为空格
        if alpha == 0:
            return ' '

        length = len(self.ascii_char)
        #灰度值的计算公式
        gray = int(0.2126 *r + 0.7152*g + 0.0722*b)

        unit = (256.0 + 1)/length
        return self.ascii_char[int(gray/unit)]

    def print_picture(self):
        '打印图形'
        #打开图片
        im = Image.open(self.img)
        #设置图片像素的大小
        im = im.resize((self.width,self.heigth),Image.NEAREST)

        txt = ""

        for i in range(self.heigth):
            for j in range(self.width):
                txt += self.get_char(*im.getpixel((j,i)))

            txt += '\n'

        print(txt)
'''
    def write_to_file(self):
        '将生成的字符图片写入到文件'
        if args.output:
            with open(args.output,'w') as f:
                f.write(txt)
        else:
            with open('output.txt','w') as f:
                f.write(txt)

pic = Ptrancefrom(args.filename,args.width,args.heigth)

pic.print_picture()
'''
      
