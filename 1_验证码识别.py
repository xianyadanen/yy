import pytesseract
from PIL import Image

# 读取图片
img = Image.open("./code/mbb5.png")
# 将图片转成灰度图片
img = img.convert("L")
# img.show()
s = pytesseract.image_to_string(img)
print(s)


