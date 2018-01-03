import os

haarcascade_path = os.path.join('data', 'haarcascade_frontalface_default.xml')
person_thumbnail_path = os.path.join('data', 'images', 'person')
crop_scale_factor = 1.2
crop_mini_neighbours = 10
crop_ratio = 0.03


picture_path = os.path.join('data', 'images', 'photos')
picture_thumbnail_path = os.path.join('data', 'images', 'thumbnails')
picture_thumbnail_width = 200

face_recognizer_model_path = os.path.join('data','frmodel.xml')
face_training_image_path = os.path.join('data', 'images', 'person', 'training')
face_training_image_size = (150, 150)
face_training_image_blur_ksize = (5, 5)
face_temp_image_path = os.path.join('data', 'images', 'person', 'temp')
face_image_path = os.path.join('data','images','person')
emoji_path = os.path.join('data', 'images', 'emoji')