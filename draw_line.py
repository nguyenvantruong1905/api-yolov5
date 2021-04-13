# importing cv2 
import cv2 
   
# path
   
# Reading an image in default mode
image = cv2.imread("download.jpeg")
   
# Window name in which image is displayed
window_name = 'Image'
  
# Start coordinate, here (0, 0)
# represents the top left corner of image
start_point = (0, 250)
  
# End coordinate, here (250, 250)
# represents the bottom right corner of image
end_point = (800, 250)
  
# Green color in BGR
color = (0, 300, 0)
  
# Line thickness of 9 px
thickness = 2
  
# Using cv2.line() method
# Draw a diagonal green line with thickness of 9 px
new_width = 800
new_height = 500
img_resized = cv2.resize(src=image, dsize=(new_width, new_height))

im = cv2.line(img_resized, start_point, end_point, color, thickness)
  
# Displaying the image 
cv2.imshow(window_name, im) 
cv2.waitKey()
cv2.destroyAllWindows()