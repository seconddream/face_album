import os
import cv2
import uuid
import numpy as np

from model.crop import FaceCrop

file_list = [os.path.join('input/ne', f) for f in os.listdir('input/ne') if f != '.DS_Store']
image_list = [cv2.imread(f) for f in file_list]


faceCropper = FaceCrop()
for index, image in enumerate(image_list):
    print(file_list[index])
    face_positions = faceCropper.crop(image)
    for x, y, w, h in face_positions:
        face_image = cv2.resize(image[y:(y + h), x:(x + w)], (150,150))
        face_image = cv2.blur(face_image, (5,5))
        face_image = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)
        face_image = cv2.equalizeHist(face_image)
        cv2.imwrite(os.path.join('test', str(uuid.uuid4())+'.jpg'), face_image)