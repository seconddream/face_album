from model.database_manager import DatabaseManager
from datetime import datetime

db = DatabaseManager.getInstance()

# p = db.writePicture(pic_file_path='abjuu/abc.png', thumbnail_path='jhhhzzj/hh.png', add_date=datetime.now(), created_data=datetime.now())
# print(p)

# t = db.updateFaceInPic(person_tag_id=1, emotion_tag_id=3, picture_id=2)
# print(t)

f = db.findPictureWithFace(person_tag_id=1)
for h in f:
    print(h)

print('----')

f = db.findPictureWithEmotion(emotion_tag_id=3)
for h in f:
    print(h)



db.closeConnection()

