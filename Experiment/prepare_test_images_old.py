import cv2
import os, shutil

source_folder = 'source_images/'
source_test_folder = 'source_images/test/'
output_folder = 'tf_files/trainingimages/'
test_folder = 'tf_files/testimages/'

corp_out = 0

if not os.path.exists(output_folder):
    os.makedirs(output_folder)
else:
    shutil.rmtree(output_folder)

if not os.path.exists(test_folder):
    os.makedirs(test_folder)
else:
    shutil.rmtree(test_folder)
    os.makedirs(test_folder)

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

emotions = [folder for folder in os.listdir(source_folder) if folder not in ['.DS_Store', 'disgust', 'fear', 'anger', 'test']];

for emotion in emotions:
    if not os.path.exists(output_folder+emotion):
        os.makedirs(output_folder+emotion)
    picture_list = [picture for picture in os.listdir(source_folder + emotion) if picture != '.DS_Store']
    for picture in picture_list:
        image = cv2.imread(source_folder+ emotion + '/' + picture, 0)
        if corp_out == 0:
            cv2.imwrite(output_folder + emotion + '/' + picture[0:-4] + '.jpg', image)
            continue
        faces = faceCascade.detectMultiScale(
            image,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(30, 30),
        )
        print('found {} face in {}, save to training_image/{}...'.format(len(faces), picture, emotion))
        for (x, y, w, h) in faces:
            face_picture = image[y:(y+h), x:(x+w)]
            cv2.imwrite(output_folder + emotion + '/' + picture[0:-4] + '.jpg', face_picture)

test_file_list = [f for f in os.listdir(source_test_folder) if f != '.DS_Store']
for test_file in test_file_list:
    test_image = cv2.imread(source_test_folder+test_file, 0)
    if corp_out == 0:
        cv2.imwrite(test_folder + test_file[0:-4] + '.jpg', test_image)
        continue
    faces = faceCascade.detectMultiScale(
        test_image,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(30, 30),
    )
    print('found {} face in test file {}, save to {} ...'.format(len(faces), test_file, test_folder))
    for (x, y, w, h) in faces:
        face_picture = test_image[y:(y + h), x:(x + w)]
        cv2.imwrite(test_folder + test_file[0:-4] + '.jpg', face_picture)

#if os.path.exists('tf_files/retrained_graph.pb'):
#    os.remove('tf_files/retrained_graph.pb')
#    os.remove('tf_files/retrained_labels.txt')

