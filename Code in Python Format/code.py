import sys
print("Installing Libraries and dependencies. Please wait")
import pip
def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

install('cvlib')
install('opencv-python')
install('tensorflow')
install('matplotlib')
install('keras')

print("Finished installing. Running the code")

# coding: utf-8
global output_images
global output_labels

output_images = []
output_labels = []
import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
def init(im,j):
    global output_images
    global output_labels
    cv2.imshow('Original Image '+str(j),im)
    cv2.waitKey()
    bbox, label, conf = cv.detect_common_objects(im)
    m = len(label)
    i = 0
    while i<m:
        if label[i]!='truck' and label[i]!='bus' and label[i]!='car' and label[i]!='bicycle' and label[i]!='motorcycle' and label[i]!='train' and label[i]!='airplane'and label[i]!='boat':
            label.pop(i)
            bbox.pop(i)
            conf.pop(i)
            i = i-1
            m = m-1
        i = i+1
    output_image = draw_bbox(im, bbox, label, conf)
    output_images.append(output_image)
    output_labels.append(label)
    print("For the image "+str(j)+" we have ")
    print('Number of cars in the image is ' + str(label.count('car')))
    print('Number of bus in the image is ' + str(label.count('bus')))
    print('Number of truck in the image is ' + str(label.count('truck')))
    print('Number of bicycle in the image is ' + str(label.count('bicycle')))
    print('Number of motorcycle in the image is ' + str(label.count('motorcycle')))
    print('Number of trains in the image is ' + str(label.count('train')))
    print('Number of boats in the image is ' + str(label.count('boat')))
    print('Number of airplane in the image is ' + str(label.count('airplane')))
    if j<9:
        cv2.imshow('Output Image '+str(j),output_image)
    else:
        cv2.imshow('Incorrect Detection '+str(j),output_image)
    cv2.waitKey()
    cv2.destroyAllWindows()
def application(k):
    print("For image "+str(k+1))
    label_for_k = output_labels[k]
    car_revenue = label_for_k.count('car')*80
    bus_revenue=label_for_k.count('bus')*100
    truck_revenue = label_for_k.count('truck')*150
    bicycle_revenue = label_for_k.count('bicycle')*0
    motorcycle_revenue = label_for_k.count('motorcycle')*0
    print("The revenue generated from cars in dollars is ")
    print(car_revenue)
    print("The revenue generated from buses in dollars is ")
    print(bus_revenue)
    print("The revenue generated from trucks in dollars is ")
    print(truck_revenue)
    print("The revenue generated from bicycles in dollars is ")
    print(bicycle_revenue)
    print("The revenue generated from motorcycles in dollars is ")
    print(motorcycle_revenue)
    print("The total revenue generated is $"+str(car_revenue+bus_revenue+truck_revenue+bicycle_revenue+motorcycle_revenue))
print("Vehicle Detection in Road Vehicles")
for i in range(1,6):
    x = "./dataset/"+str(i)+".jpg"
    x = cv2.imread(x)
    init(x,i)
print("Vehicle Detection in Rail-Road Vehicles")
i = 6
x = "./dataset/"+str(i)+".jpg"
x = cv2.imread(x)
init(x,i)
print("Vehicle Detection in WaterWays Vehicles")
i = 7
x = "./dataset/"+str(i)+".jpg"
x = cv2.imread(x)
init(x,i)
print("Vehicle Detection in Airways Vehicles")
i = 8
x = "./dataset/"+str(i)+".jpg"
x = cv2.imread(x)
init(x,i)
print("*****************demo of application******************************")
print("One of the applications of vehicle identification is\ncalculation of toll revenue")
print("Suppose we need to calculate total toll revenue\n for different classes of vehicles")
print("Let's say the toll for\ncar is $80\nbus is $100\ntruck is $150\nfor bicycle and motorcyle is $0")
for i in range(0,5):
    application(i)
cv2.destroyAllWindows()
print("*****************demo of limitation of closeness of objects******************************")
print("There is a limit on the closeness of the objects in YOLO\nFollowing Images have objects too close to each other that YOLO detects only a few number of objects")
for i in range(9,11):
    x = "./dataset/"+str(i)+".jpg"
    x = cv2.imread(x)
    init(x,i)
cv2.destroyAllWindows()
print("***************demo of limitation of detecting special vehicles\nAmbulances and fire brigades are detected as trucks\njeeps are detected as cars or trucks\ntrams are detected as trains or bus or truck")
for i in range(11,14):
    x = "./dataset/"+str(i)+".jpg"
    x = cv2.imread(x)
    init(x,i)
print("If there is any image window open, press any key to close that window")
cv2.waitKey()
cv2.destroyAllWindows()
sys.exit()
