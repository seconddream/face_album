# from model.facial_expression import ExpressionDetector
# import model.settings as settings
# import os
#
# ed = ExpressionDetector()
# test_file_name_list = [f for f in os.listdir(settings.face_training_image_path) if f !='.DS_Store']
# test_file_path_list = [os.path.join(settings.face_training_image_path, f) for f in test_file_name_list]
#
# for f in test_file_path_list:
#     ed.test_emotion(f)

import model.database_manager as DB

pictures = DB.getPicWithPersonAndEmotion(17, 'happy')
for p in pictures:
    print(p)