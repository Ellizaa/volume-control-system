import cv2

img = cv2.imread('catt.jpg', -1)

print (img)

cv2.imshow('catimage', img)
cv2.waitKey(0)
cv2.destroyAllWindows()