from PIL import Image

#이미지오픈

im = Image.open("./cat.jpg")
#RGB->Gray
gray_im=im.convert('L')

gray_im.show()
#이미지 저장

gray_im.save("./gray_cat.jpg")