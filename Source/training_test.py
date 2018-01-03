import os
import cv2
import numpy as np

from model.crop import FaceCrop


training_faces = []
training_labels = []

label_list = [f for f in os.listdir('training/') if f != '.DS_Store']
for label in label_list:
    file_list = [f for f in os.listdir('training/'+label) if f != '.DS_Store']
    for file in file_list:
        image = cv2.imread(os.path.join('training', label, file), 0)
        training_faces.append(image)
        training_labels.append(int(label))


model = cv2.face.LBPHFaceRecognizer_create()
model.write('testing.xml')
model.train(training_faces, np.array(training_labels))

n_all = 0
n_right = 0

testing_label_list = [f for f in os.listdir('test/') if f != '.DS_Store']
for testing_label in testing_label_list:
    file_list = [f for f in os.listdir('test/' + testing_label) if f != '.DS_Store']
    for file in file_list:
        image = cv2.imread(os.path.join('test', testing_label, file), 0)
        [predict_label, confident] = model.predict(image)
        print(f'{predict_label, confident}')
        n_all = n_all +1
        match = (predict_label==int(testing_label))
        if match:
            n_right = n_right + 1
        print(f'Testing subject label: {testing_label}  Predicted Label:{predict_label} {match}')
        print('')

print(f'Rate: {n_right/n_all}')














