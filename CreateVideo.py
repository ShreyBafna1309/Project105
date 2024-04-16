import os
import cv2

path = "C:/Users/91967/OneDrive/Desktop/Project105/PRO-C105-Project-Images-main/Images"

Images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file
        Images.append(file_name)
    
count = len(Images)

frame = cv2.imread(Images[0])
width,height,channels = frame.shape
size = (width,height)
print(size)

out = cv2.VideoWriter("Project.avi",cv2.VideoWriter_fourcc(*"DIVX"),0.8,size)

for i in range(0,count-1):
    frame = cv2.imread(Images[i])
    cv2.imshow("WEB CAM", frame)
    out.write(frame)
    if cv2.waitKey(1000) == 32:
        break

out.release()