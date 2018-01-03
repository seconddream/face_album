import sqlite3, os
from model.person import Person
from model.picture import Picture
from model.face import Face


conn = sqlite3.connect(os.path.join('data','db', 'fa_db.db'))
cursor = conn.cursor()

def closeConnection():
    if conn:
        conn.close()

def getPicWithPersonAndEmotion(id, emotion):
    picture_list = []
    try:
        cursor.execute('''SELECT 
                            pictures.id,
                            pictures.pic_file_path,
                            pictures.thumbnail_path,
                            pictures.add_date
                          FROM face_in_pic
                          LEFT JOIN pictures
                          ON face_in_pic.picture_id = pictures.id
                          WHERE face_in_pic.person_tag_id=? AND face_in_pic.emotion=?''', (id, emotion))
        conn.commit()
        rows = cursor.fetchall()
        print(len(rows))
        for id, pic_file_path, thumbnail_path, add_date in rows:
            p = Picture(id=id,
                        file_path=pic_file_path,
                        thumbnail_path=thumbnail_path,
                        add_date=add_date, )
            picture_list.append(p)
        return picture_list
    except Exception as err:
        print(f'[DatabaseManager/getPicWithPersonAndEmotion]: {err}')
        return None

def createNewPerson(name, thumbnail_path):
    try:
        cursor.execute('INSERT INTO person_tag VALUES (NULL,?,?)',(name, thumbnail_path))
        conn.commit()
        return Person(cursor.lastrowid, name, thumbnail_path)
    except Exception as err:
        print(f'[DatabaseManager/write_person]: {err}')
        return None

def getAllPerson():
    person_list = []
    try:
        cursor.execute('SELECT * FROM person_tag')
        conn.commit()
        rows = cursor.fetchall()
        if rows:
            for id, name, thumbnail_path in rows:
                person = Person(id, name, thumbnail_path)
                person_list.append(person)
            return person_list
        else:
            return None
    except Exception as err:
        print(f'[DatabaseManager/getAllPerson]: {err}')
        return None


def updatePerson(person):
    try:
        cursor.execute('UPDATE person_tag SET name=? WHERE id=?', (person.name, person.id))
        conn.commit()
    except Exception as err:
        print(f'[DatabaseManager/UpdatePerson]: {err}')
        return None

def deletePerson(person):
    try:
        cursor.execute('UPDATE face_in_pic SET person_tag_id=?, verified=? WHERE person_tag_id=?', (None, -1, person.id))
        cursor.execute('DELETE FROM person_tag WHERE id=?', (person.id,))
        conn.commit()
    except Exception as err:
        print(f'[DatabaseManager/deletePerson]: {err}')


def getPersonById(id):
    if id:
        try:
            cursor.execute('SELECT * FROM person_tag WHERE id=?', (id,))
            conn.commit()
            row = cursor.fetchone()
            if row:
                _, name, thumbnail_path = row
                person = Person(id, name, thumbnail_path)
                return person
        except Exception as err:
            print(f'[DatabaseManager/get_person_by_id]: {err}')
            return None
    else:
        print(f'[DatabaseManager/get_person_by_id]: id missing')
        return None

def getPersonByName(name):
    if name:
        try:
            cursor.execute('SELECT * FROM person_tag WHERE name=?', (name,))
            conn.commit()
            row = cursor.fetchone()
            if row:
                id, _, thumbnail_path = row
                person = Person(id, name, thumbnail_path)
                return person
            else:
                return None
        except Exception as err:
            print(f'[DatabaseManager/getPersonByName]: {err}')
            return None
    else:
        print(f'[DatabaseManager/getPersonByName]: name missing')
        return None

def createPicture(file_path, thumbnail_path, add_date):
    if file_path and thumbnail_path and add_date:
        try:
            cursor.execute('INSERT INTO pictures VALUES (NULL,?,?,?)',
                                  (file_path, thumbnail_path, add_date))
            conn.commit()
            return Picture(id=cursor.lastrowid, file_path=file_path, thumbnail_path= thumbnail_path, add_date=add_date)
        except Exception as err:
            print(f'[DatabaseManager/write_picture]: {err}')
            return None
    else:
        print(f'[DatabaseManager/createPicture]: arguments not complete')

def getAllPictures():
    picture_list = []
    try:
        cursor.execute('SELECT * FROM pictures')
        conn.commit()
        rows = cursor.fetchall()
        for id, pic_file_path, thumbnail_path, add_date in rows:
            p = Picture(id=id,
                        file_path=pic_file_path,
                        thumbnail_path=thumbnail_path,
                        add_date=add_date,)
            picture_list.append(p)
        return picture_list
    except Exception as err:
        print(f'[DatabaseManager/getAllPic]: {err}')
        return None

def getPictureByID(pic_id):
    try:
        cursor.execute('SELECT * FROM pictures WHERE id =?', (pic_id,))
        conn.commit()
        row = cursor.fetchone()
        if row:
            id, pic_file_path, thumbnail_path, add_date = row
            picture = Picture(id=id, file_path=pic_file_path, thumbnail_path=thumbnail_path, add_date=add_date)
            return picture
    except Exception as err:
        print(f'[DatabaseManager/getAllPic]: {err}')
        return None

def createFaceInPic(picture_id=None, x=None, y=None, w=None, h=None, sample_path=None, emotion=None):
    if picture_id:
        try:
            cursor.execute('INSERT INTO face_in_pic VALUES (NULL,NULL ,?,?,?,?,?,? ,?, -1)',
                                ( picture_id, x, y, w, h, emotion, sample_path))
            conn.commit()
            return cursor.lastrowid
        except Exception as err:
            print(f'[DatabaseManager/update_face_in_pic]: {err}')
            return None
    else:
        print(f'[DatabaseManager/update_face_in_pic]: picture must not be None')
        return None

def getAllFaceInPic():
    face_list = []
    try:
        cursor.execute('SELECT * FROM face_in_pic')
        conn.commit()
        rows = cursor.fetchall()
        if rows:
            for id, person_id, picture_id, x, y, w, h, emotion, sample_path, verified in rows:
                face = Face(id, person_id, picture_id, x, y, w, h, emotion, sample_path, verified)
                face_list.append(face)
            return face_list
        else:
            return None
    except Exception as err:
        print(f'[DatabaseManager/UpdatePerson]: {err}')
        return None


def deleteFaceInPic(face_id):
    try:
        cursor.execute('DELETE FROM face_in_pic WHERE face_in_pic.id = ?', (face_id,))
        conn.commit()
    except Exception as err:
        print(f'[DatabaseManager/deleteFaceInPic]: {err}')

def updateFaceInPic(face):
    try:
        cursor.execute('UPDATE face_in_pic SET person_tag_id=?, emotion=?, verified=? WHERE id=?', (face.person_id, face.emotion, face.verified, face.id))
        conn.commit()
    except Exception as err:
        print(f'[DatabaseManager/updateFaceInPic]: {err}')
        return None

def getFaceInPic(pic_id):
    if pic_id:
        face_list = []
        try:
            cursor.execute('SELECT * FROM face_in_pic WHERE picture_id=?',(pic_id,))
            conn.commit()
            rows = cursor.fetchall()
            for id, person_id, picture_id, x, y, w, h, emotion, sample_path, verified in rows:
                face = Face(id, person_id,picture_id, x, y, w, h, emotion, sample_path, verified)
                face_list.append(face)
            return face_list
        except Exception as err:
            print(f'[DatabaseManager/get_face_in_pic]: {err}')
            return None
    else:
        print(f'[DatabaseManager/get_face_in_pic]: pic_id must not be none')
        return None




# class DatabaseManager:
#
#     def __init__(self):
#         try:
#             self.conn = sqlite3.connect(os.path.join('data', 'db', 'fa_db.db'))
#             self.cursor = self.conn.cursor()
#         except Exception as err:
#             print(f'[DatabaseManager]: {err}')
#
#     def closeConnection(self):
#         if self.conn:
#             self.conn.close()
#
#
#     def findPictureWithFace(self, person_tag_id):
#         if person_tag_id:
#             try:
#                 self.cursor.execute('''
#                         SELECT
#                           face_in_pic.*,
#                           person_tag.first_name,
#                           person_tag.last_name,
#                           person_tag.thumbnail_path,
#                           pictures.pic_file_path,
#                           pictures.thumbnail_path,
#                           pictures.add_date,
#                           pictures.created_data
#                         FROM
#                           ((face_in_pic
#                             LEFT JOIN person_tag)
#                             LEFT JOIN pictures)
#                             WHERE face_in_pic.person_tag_id = ?
#                             AND face_in_pic.person_tag_id == person_tag.id
#                             AND face_in_pic.picture_id == pictures.id
#                             GROUP BY  face_in_pic.id
#                             ''',
#                             (person_tag_id,))
#                 self.conn.commit()
#                 rows = self.cursor.fetchall()
#                 return rows
#             except Exception as err:
#                 print(f'[DatabaseManager/find_picture_with_face]: {err}')
#                 return False
#
#     def findPictureWithEmotion(self, emotion):
#         if emotion:
#             try:
#                 self.cursor.execute('''
#                     SELECT
#                       face_in_pic.*,
#                       person_tag.first_name,
#                       person_tag.last_name,
#                       person_tag.thumbnail_path,
#                       pictures.pic_file_path,
#                       pictures.thumbnail_path,
#                       pictures.add_date,
#                       pictures.created_data
#                     FROM
#                       ((face_in_pic
#                           LEFT JOIN person_tag ON face_in_pic.id = person_tag.id)
#                           LEFT JOIN pictures ON face_in_pic.id = pictures.id)
#                     WHERE face_in_pic.emotion = ?''',
#                     (emotion,))
#                 self.conn.commit()
#                 rows = self.cursor.fetchall()
#                 return rows
#             except Exception as err:
#                 print(f'[DatabaseManager/find_picture_with_emotion]: {err}')
#                 return False


