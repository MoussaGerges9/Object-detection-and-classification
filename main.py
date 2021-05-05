import cv2

cap = cv2.VideoCapture(0)
classesFile = 'ClassesNames'
classNames = []
with open(classesFile,'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

print(classNames)
print(len(classNames))


while True:
    success, img = cap.read()

    cv2.imshow('Image', img)
    cv2.waitKey(1)
