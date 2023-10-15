import cv2
#configer the image

source="krishna.jpeg"
destination="newkrishna.jpeg"
scale_percentage=30

#reading the image
image=cv2.imread(source)
#cv2.imshow("krishna",image)


# change configer the image

new_width=int(image.shape[1]*scale_percentage/100)
new_hight=int(image.shape[0]*scale_percentage/100)


#resize the image and store the image an another file

ouput=cv2.resize(image,(new_width,new_hight))
cv2.imwrite("newkrishna.jpeg",ouput)

#resize image output

new_image=cv2.imread(destination)
cv2.imshow("newkrishna",new_image)
cv2.waitKey(0)