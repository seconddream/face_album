import os, shutil, cv2


emotion_root_dir = 'Emotion/'
image_root_dir = 'cohn-kanade-images/'
emotion_data_1 = []
emotion_data = []
test_data = []
emotion_dict = ['anger', 'contempt', 'disgust', 'fear', 'happy', 'sadness', 'suprise']
testing_target = ['happy', 'sadness', 'suprise']
emotion_cout = [0,0,0,0,0,0,0]
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
crop = 1


# prepare training and testing image folder

print('preparing training images...')

training_image_dir = 'tf_files/trainingimages/'
testing_image_dir = 'tf_files/testingimages/'

if os.path.exists(training_image_dir):
    shutil.rmtree(training_image_dir)
    os.makedirs(training_image_dir)
else:
    os.makedirs(training_image_dir)

if os.path.exists(testing_image_dir):
    shutil.rmtree(testing_image_dir)
    os.makedirs(testing_image_dir)
else:
    os.makedirs(testing_image_dir)

for t in testing_target:
    os.makedirs(training_image_dir + t)

# find out all the pic with a emotion label

person_dir_list = [f for f in os.listdir(emotion_root_dir) if f != '.DS_Store']
person_dir_list.sort()



for person_dir in person_dir_list:
    person_dir += '/'
    emotion_dir_list = [f for f in os.listdir(emotion_root_dir + person_dir) if f != '.DS_Store']
    for emotion_dir in emotion_dir_list:
        emotion_dir += '/'
        emotion_file = [f for f in os.listdir(emotion_root_dir + person_dir + emotion_dir)]
        if len(emotion_file)!= 0:
            emotion_fid = open(emotion_root_dir + person_dir + emotion_dir + emotion_file[0])
            emotion_index = int(emotion_fid.readline(4))
            emotion_param = emotion_dict[emotion_index-1]
            image_dir = image_root_dir + person_dir + emotion_dir
            image_file_list = [f for f in os.listdir(image_dir) if f != '.DS_Store']
            image_file_list.sort(reverse=1)
            emotion_data_1.append((emotion_param, image_dir, image_file_list[0]))
            emotion_cout[emotion_index-1] += 1

for emotion_type in emotion_dict:
    emotion_type_list = [(first,second,third) for (first,second,third) in emotion_data_1 if first == emotion_type]
    test_data.append(emotion_type_list[0:3])
    emotion_data.append(emotion_type_list[3:])

def write_image(place, crop, emotion_type, source_path, source_name, appending = ''):
    image = cv2.imread(source_path+source_name, 0)
    if crop:
        faces = faceCascade.detectMultiScale(
            image,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(30, 30),
        )
        for (x, y, w, h) in faces:
            image = image[y:(y + h), x:(x + w)]
            cv2.imwrite(place + emotion_type + '/' + appending + source_name[0:-4] + '.jpg', image)
    else:
        cv2.imwrite(place + emotion_type + '/' + appending + source_name[0:-4] + '.jpg', image)


for one_kind_of_emotion_list in emotion_data:
    for (type, path, name) in one_kind_of_emotion_list:
        if type in testing_target:
            write_image(training_image_dir, crop, type, path, name)

print('\n')
for data in test_data:
    for(type, path, name) in data:
        if type in testing_target:
            write_image(testing_image_dir, crop, '', path, name, appending=type)

print('finished')








