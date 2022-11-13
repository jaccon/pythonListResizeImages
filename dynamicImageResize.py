import glob
from PIL import Image

imagePath = './Photos'
imageResizedDir = './Resized'
mimeType = '*.jpg'
imageResizeWidthTo = 400
imageResizeHeightTo = 400

searchFiles = imagePath+"/"+mimeType

dir_path = r''+searchFiles+''
for file in glob.glob(dir_path, recursive=True):
  
    imageFilename = file
    i = imageFilename.split('/')[2]
    
    image = Image.open(file)
    originaImageSize = (f"{image.size}")
    print(imageFilename + "; " + originaImageSize)
    
    image.thumbnail((imageResizeWidthTo, imageResizeHeightTo))
    image.save(imageResizedDir+"/"+i)
