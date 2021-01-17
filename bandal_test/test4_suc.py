import numpy as np
import cv2

font = cv2.FONT_HERSHEY_SIMPLEX
def faceDetect():
    eye_detect = False
    face_cascade = cv2.CascadeClassifier('haarcascade_frontface.xml')# 얼굴찾기 haar 파일
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')# 눈찾기 haar 파일
    info = ''

    try:
        cap = cv2.VideoCapture(1)
    except:
        print('카메라 로딩 실패')
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if eye_detect:
            info = 'Eye Detection On'
        else:
            info = 'Eye Detection Off'

        #얼굴인식 영상처리 그레이스케일 이미지로 바꿔줌
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        #카메라 영상 왼쪽위에 위에 셋팅된 info 의 내용 출력
        cv2.putText(frame, info, (5, 15), font, 0.5, (255, 0, 255), 1)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2) #사각형 범위
            cv2.putText(frame, 'Detected Face', (x-5, y-5), font, 0.5, (255, 255, 0), 2) #얼굴찾았다는 메시지
            if eye_detect: #눈찾기
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]
                eyes = eye_cascade.detectMultiScale(roi_gray)
                for(ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

        #이미지 화면 표시
        cv2.imshow('frame', frame)
        k = cv2.waitKey(30)

        #실행 중 키보드 i 를 누르면 눈찾기를 on, off한다.
        if k == ord('i'):
            eye_detect = not eye_detect
        #키입력 대기
        if k == 27:
            break

    #재생파일 종료
    cap.release()
    #윈도우 종료
    cv2.destroyAllWindows()

faceDetect()
        