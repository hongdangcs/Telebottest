from PIL import ImageGrab

# Define the coordinates and size of the region to capture
left = 100
top = 100
width = 1000
height = 500

# Capture the region and save it to a file
image = ImageGrab.grab(bbox=(left, top, left+width, top+height))
image.save("C://Users//PHAMHONGDANG//Downloads//ScreenShot//screenCapture.png")