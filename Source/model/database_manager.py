import sqlite3, os
from model.singleton import Singleton
from model.person import Person
from model.picture import Picture


@Singleton
class DatabaseManager:

    def __init__(self):
        try:
            self.conn = sqlite3.connect(os.path.join('data', 'db', 'fa_db.db'))
            self.cursor = self.conn.cursor()
        except Exception as err:
            print(f'[DatabaseManager]: {err}')

    def closeConnection(self):
        if self.conn:
            self.conn.close()

    # function for person
    def writePerson(self, first_name=None, last_name=None, thumbnail_path=None):
        if first_name and last_name and thumbnail_path:
            try:
                self.cursor.execute('INSERT INTO person_tag VALUES (NULL,?,?,?)',(first_name, last_name, thumbnail_path))
                self.conn.commit()
                return Person(self.cursor.lastrowid, first_name, last_name, thumbnail_path)
            except Exception as err:
                print(f'[DatabaseManager/write_person]: {err}')
                return None

    def getPersonById(self, person_id=None):
        person_list = []
        if person_id:
            try:
                self.cursor.execute('SELECT * FROM person_tag WHERE id=?', (person_id,))
                self.conn.commit()
                row = self.cursor.fetchone()
                if row:
                    id, first_name, last_name, thumbnail_path = row
                    p = Person(id, first_name, last_name, thumbnail_path)
                    person_list.append(p)
                return person_list
            except Exception as err:
                print(f'[DatabaseManager/get_person_by_id]: {err}')
                return None
        else:
            try:
                self.cursor.execute('SELECT * FROM person_tag')
                self.conn.commit()
                rows = self.cursor.fetchall()
                for row in rows:
                    id, first_name, last_name, thumbnail_path = row
                    p = Person(id, first_name, last_name, thumbnail_path)
                    person_list.append(p)
                return person_list
            except Exception as err:
                print(f'[DatabaseManager]: {err}')
                return None

    # function for pictures
    def writePicture(self, pic_file_path=None, thumbnail_path=None, add_date=None, created_data=None):
        if pic_file_path and thumbnail_path and add_date and created_data:
            try:
                self.cursor.execute('INSERT INTO pictures VALUES (NULL,?,?,?,?)',
                                  (pic_file_path, thumbnail_path, add_date, created_data))
                self.conn.commit()
                return Picture(photo_id=self.cursor.lastrowid, pic_file_path=pic_file_path, thumbnail_path= thumbnail_path, add_date=add_date, created_date=created_data, face_in_pic=None)
            except Exception as err:
                print(f'[DatabaseManager/write_picture]: {err}')
                return None

    def updateFaceInPic(self, person_tag_id=None, emotion_tag_id=None, picture_id=None):
        if person_tag_id and emotion_tag_id and picture_id:
            try:
                self.cursor.execute('INSERT INTO face_in_pic VALUES (NULL,?,?,?)',
                                    (person_tag_id, emotion_tag_id, picture_id))
                self.conn.commit()
                return True
            except Exception as err:
                print(f'[DatabaseManager/update_face_in_pic]: {err}')
                return False

    def getFaceInPic(self, pic_id):
        if pic_id:
            try:
                self.cursor.execute('''SELECT
                            face_in_pic.person_tag_id,
                            face_in_pic.emotion_tag_id,
                            face_in_pic.picture_id,
                            person_tag.first_name,
                            person_tag.last_name,
                            person_tag.thumbnail_path
                          FROM 
                            face_in_pic LEFT JOIN person_tag 
                          WHERE 
                            face_in_pic.picture_id = ? 
                          AND 
                            face_in_pic.person_tag_id == person_tag.id
                          ''',
                                    (pic_id,))
                self.conn.commit()
                rows = self.cursor.fetchall()
                return rows
            except Exception as err:
                print(f'[DatabaseManager/get_face_in_pic]: {err}')
                return False

    def findPictureWithFace(self, person_tag_id):
        if person_tag_id:
            try:
                self.cursor.execute('''
                        SELECT 
                          face_in_pic.*, 
                          person_tag.first_name, 
                          person_tag.last_name, 
                          person_tag.thumbnail_path, 
                          pictures.pic_file_path, 
                          pictures.thumbnail_path, 
                          pictures.add_date, 
                          pictures.created_data 
                        FROM 
                          ((face_in_pic 
                            LEFT JOIN person_tag) 
                            LEFT JOIN pictures) 
                            WHERE face_in_pic.person_tag_id = ?
                            AND face_in_pic.person_tag_id == person_tag.id
                            AND face_in_pic.picture_id == pictures.id
                            GROUP BY  face_in_pic.id
                            ''',
                            (person_tag_id,))
                self.conn.commit()
                rows = self.cursor.fetchall()
                return rows
            except Exception as err:
                print(f'[DatabaseManager/find_picture_with_face]: {err}')
                return False

    def findPictureWithEmotion(self, emotion_tag_id):
        if emotion_tag_id:
            try:
                self.cursor.execute('''
                    SELECT 
                      face_in_pic.*, 
                      person_tag.first_name, 
                      person_tag.last_name, 
                      person_tag.thumbnail_path, 
                      pictures.pic_file_path, 
                      pictures.thumbnail_path, 
                      pictures.add_date, 
                      pictures.created_data 
                    FROM 
                      ((face_in_pic 
                          LEFT JOIN person_tag ON face_in_pic.id = person_tag.id) 
                          LEFT JOIN pictures ON face_in_pic.id = pictures.id) 
                    WHERE face_in_pic.emotion_tag_id = ?''',
                    (emotion_tag_id,))
                self.conn.commit()
                rows = self.cursor.fetchall()
                return rows
            except Exception as err:
                print(f'[DatabaseManager/find_picture_with_emotion]: {err}')
                return False


