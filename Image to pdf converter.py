#import the image libry from pillow
from PIL import Image

#select the image file
image = "Image_file.jpg"

#Now open the file
image  = Image.open(image)

#convert this file
final_image=image.convert("RGB")

#Now save the file into pdf
final_image.save("final_img.pdf","PDF",resolution=80)