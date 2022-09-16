import cv2, random
vidcap = cv2.VideoCapture('/Users/rithwikgupta/Downloads/test.mov')
success,image = vidcap.read()
count = 10
cv2.imwrite("frame%d.png" % count, image)
while success:
  success,image2 = vidcap.read()
  
  
  if (random.randint(1, 100) == 100):
  	cv2.imwrite("frame%d.png" % (count + 1), image2)
  	count += 1

  image = image2