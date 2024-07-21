import os.path
from PIL import Image, UnidentifiedImageError

print( """
 ___  _  __       __  ___  __ 
 )_  / ` ) ) \\_) (_ `  )  (_ `
(__ (_. /_/   / .__) _(_ .__) \n
""")

while True:
    input_path = input("Enter path to original image: ")
    if os.path.isfile(input_path):
        try:
            original_image = Image.open(input_path)
            break
        except UnidentifiedImageError:
            print("Unable to open the image.")
            continue
    else:
        print("Invalid path entered.")

while True:
    new_name = input("Enter name for resized image, excluding extension: ")
    if new_name.strip() != "":
        new_name += ".png"
        break
    else:
        print("Filename cannot be blank.")

while True:
    new_width = input("Enter new width in pixels: ")
    if new_width.isnumeric():
        new_width = int(new_width)
        break
    else:
        print("You must enter a number.") 

while True:
    new_height = input("Enter new height in pixels: ")
    if new_height.isnumeric():
        new_height = int(new_height)
        break
    else:
        print("You must enter a number.") 

# compute new size and resize image
scale_factor = min(new_width / original_image.width, new_height / original_image.height)
new_size = (int(original_image.width * scale_factor), int(original_image.height * scale_factor))
resized_image = original_image.resize(new_size, Image.Resampling.LANCZOS)

# save image and show what it looks like
resized_image.save(new_name)
resized_image.show()
print("Done!")
