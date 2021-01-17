import face_recognition
import cv2
import numpy as np
import pymysql as sql
import pandas as pd
import time

conn = sql.connect(
    host = 'bcc-database.cxmkpfyh3g9z.ap-northeast-2.rds.amazonaws.com',
    user = 'jeonghyun',
    password = '',
    port = 3306,
    database = 'bcc-schema',
    charset='utf8')

cursor = conn.cursor()
# query = "insert into student (sid, sname, department) values (20169, '노르만디', '경영')"
# query = "update student set sname = " + name + " where sid = " + sid

subnum = input('\n 수업코드를 입력해주세요. ==>  ')
week = input('\n 차수를 입력해주세요 ==> ')

query = "update enroll set w" + week + " = '결석' where subnum = " + subnum
cursor.execute(query)
conn.commit()
video_capture = cv2.VideoCapture(1)
print("출석체크가 시작되었습니다.")
start_time = time.time() # 시작 시간 체크

jeong_face_encoding = face_recognition.face_encodings(face_recognition.load_image_file("./image/20162.jpg"))[0]
ha_face_encoding = face_recognition.face_encodings(face_recognition.load_image_file("./image/20163.jpg"))[0]
jong_face_encoding = face_recognition.face_encodings(face_recognition.load_image_file("./image/20164.jpg"))[0]
min_face_encoding = face_recognition.face_encodings(face_recognition.load_image_file("./image/20165.jpg"))[0]
bum_face_encoding = face_recognition.face_encodings(face_recognition.load_image_file("./image/20167.jpg"))[0]
tae_face_encoding = face_recognition.face_encodings(face_recognition.load_image_file("./image/20168.jpg"))[0]
ga_face_encoding = face_recognition.face_encodings(face_recognition.load_image_file("./image/20169.jpg"))[0]

known_face_encodings = [
    jeong_face_encoding,
    ha_face_encoding,
    jong_face_encoding,
    min_face_encoding,
    bum_face_encoding,
    tae_face_encoding,
    ga_face_encoding
]
known_face_names = [
    "20162",
    "20163",
    "20164",
    "20165",
    "20167",
    "20168",
    "20169"
]

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True


while True:
    if (time.time() - start_time <= 600) :
        ret, frame = video_capture.read()

        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        rgb_small_frame = small_frame[:, :, ::-1]

        if process_this_frame:
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                    query = "update enroll set w" + week + " = '출석' where subnum = " + subnum + " and sid = " + name + " and w" + week + " = '결석'"
                    cursor.execute(query)
                    conn.commit()
                    print("%s 학생의 출석이 완료되었습니다."%name)

                face_names.append(name)

        process_this_frame = not process_this_frame

        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    else :
        ret, frame = video_capture.read()

        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        rgb_small_frame = small_frame[:, :, ::-1]

        if process_this_frame:
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                    query = "update enroll set w" + week + " = '지각' where subnum = " + subnum + " and sid = " + name + " and w" + week + " = '결석'"
                    cursor.execute(query)
                    conn.commit()
                    print("%s 학생의 지각 출석이 반영되었습니다."%name)

                face_names.append(name)

        process_this_frame = not process_this_frame

        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

video_capture.release()
cv2.destroyAllWindows()

conn.close()