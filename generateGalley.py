import glob

imagePath = './Photos'
mimeType = '*.jpg'

searchFiles = imagePath+"/"+mimeType

htmlTemplate = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        <style>
            :root {
                --card_width: 250px;
                --row_increment: 10px;
                --card_border_radius: 16px;
                --card_small: 26;
                --card_medium: 33;
                --card_large: 45;
            }

            body {
                margin: 0;
                padding: 0;
                padding-top: 5px;
                background-color: grey;
            }

            .pin_container {
                margin: 0;
                padding: 0;
                width: 80vw;
                position: absolute;
                left: 50%;
                transform: translateX(-50%);

                display: grid;
                grid-template-columns: repeat(auto-fill, var(--card_width));
                grid-auto-rows: var(--row_increment);
                justify-content: center;

                background-color: black;
            }

            .card {
                padding: 0;
                margin: 15px 10px;
                border-radius: var(--card_border_radius);
                background-color: red;
            }

            .card_small {
                grid-row-end: span var(--card_small);
            }

            .card_medium {
                grid-row-end: span var(--card_medium);
            }

            .card_large {
                grid-row-end: span var(--card_large);
            }
        </style>
    </head>

    <body>
        <div class="pin_container">
    """
    
print(htmlTemplate)

dir_path = r''+searchFiles+''

count = 0
for file in glob.glob(dir_path, recursive=True):
  
    imageFilename = file
    i = imageFilename.split('/')[2]
    count = count+1
    
    if count%2:
      htmlClass = "card_medium"
    else:
      htmlClass = "card_large"
    
    htmlTemplateImages = """
     <div class="card """+htmlClass+"""">
              <img src=" """+file+""" " width="250">
            </div>
    """
    
    print(htmlTemplateImages)
    print(count)
    
    # image.thumbnail((imageResizeWidthTo, imageResizeHeightTo))
    # image.save(imageResizedDir+"/"+i)

htmlTemplateEnd = """
     </div>
    </body>
    </html>
"""

print (htmlTemplateEnd)