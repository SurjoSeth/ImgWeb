import sys
import cv2
import numpy as np
image_fullpath=sys.argv[1]
image_name=sys.argv[2]
filter=sys.argv[3]
if filter=="Sketch Style":#sketch
    img = cv2.imread(str(image_fullpath))
    grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    invert=cv2.bitwise_not(grey_img)
    blur=cv2.GaussianBlur(invert,(21,21),0)
    invertedblur=cv2.bitwise_not(blur)
    image=cv2.divide(grey_img,invertedblur,scale=256.0)
    cv2.imwrite("media\\image.jpg",image)
    print('image.jpg',end="")
elif filter=="Increase Brightness":#increase brightness
    img = cv2.imread(str(image_fullpath))
    Intensity_Matrix=np.ones(img.shape,dtype="uint8")*60
    image=cv2.add(img,Intensity_Matrix)
    cv2.imwrite("media\\image.jpg",image)
    print('image.jpg',end="")
elif filter=="Decrease Brightness":#decrease brightness
    img = cv2.imread(str(image_fullpath))
    Intensity_Matrix=np.ones(img.shape,dtype="uint8")*60
    dark=cv2.subtract(img,Intensity_Matrix)
    cv2.imwrite("media\\image.jpg",dark)
    print('image.jpg',end="")
elif filter=="Blur":#blur
    img = cv2.imread(str(image_fullpath))
    image = cv2.blur(img,(50,50)) 
    cv2.imwrite("media\\image.jpg",image)
    print('image.jpg',end="")
elif filter=="Black & White":#grayscale
    img = cv2.imread(str(image_fullpath))
    image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("media\\image.jpg",image)
    print('image.jpg',end="")
elif filter=="Size Downscale":#downsize
    img = cv2.imread(str(image_fullpath))
    down_width = 300
    down_height = 200
    down_points = (down_width, down_height)
    image = cv2.resize(img, down_points, interpolation= cv2.INTER_LINEAR)
    cv2.imwrite("media\\image.jpg",image)
    print('image.jpg',end="")
elif filter=="Size Upscale":#upsize
    img = cv2.imread(str(image_fullpath))
    up_width = 600
    up_height = 400
    up_points = (up_width, up_height)
    image = cv2.resize(img, up_points, interpolation= cv2.INTER_LINEAR)
    cv2.imwrite("media\\image.jpg",image)
    print('image.jpg',end="")
elif filter=="Horizontal Flip":#horizontal flip
    img = cv2.imread(str(image_fullpath))
    image = cv2.flip(img, 1)
    cv2.imwrite("media\\image.jpg",image)
    print('image.jpg',end="")
elif filter=="Vertical Flip":#vertical flip
    img = cv2.imread(str(image_fullpath))
    image = cv2.flip(img, 0)
    cv2.imwrite("media\\image.jpg",image)
    print('image.jpg',end="")
elif filter=="Rotate":#rotate
    img = cv2.imread(str(image_fullpath))
    image = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)
    cv2.imwrite("media\\image.jpg",image)
    print('image.jpg',end="")
elif filter=="Inverted Colour":#invert
    img = cv2.imread(str(image_fullpath))
    grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    invert=cv2.bitwise_not(grey_img)
    cv2.imwrite("media\\image.jpg",invert)
    print('image.jpg',end="")