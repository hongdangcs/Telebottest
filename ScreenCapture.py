from PIL import ImageGrab

# Define the coordinates and size of the region to capture
left = 0
top = 800
width = 200
height = 200

# Capture the region and save it to a file

def screenShot(image_name):
    image = ImageGrab.grab(bbox=(left, top, left+width, top+height))
    image.save("photo/"+ image_name +".png")