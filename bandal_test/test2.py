from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import AveragePooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing.image import ImageDataGenerator

IMG_SIZE = 24
def train(train_generator, val_generator):
	STEP_SIZE_TRAIN=train_generator.n//train_generator.batch_size
	STEP_SIZE_VALID=val_generator.n//val_generator.batch_size

	model = Sequential()

	model.add(Conv2D(filters=6, kernel_size=(3, 3), activation='relu', input_shape=(IMG_SIZE,IMG_SIZE,1)))
	model.add(AveragePooling2D())

	model.add(Conv2D(filters=16, kernel_size=(3, 3), activation='relu'))
	model.add(AveragePooling2D())

	model.add(Flatten())

	model.add(Dense(units=120, activation='relu'))

	model.add(Dense(units=84, activation='relu'))

	model.add(Dense(units=1, activation = 'sigmoid'))


	model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

	print('[LOG] Training CNN')
  
	model.fit_generator(generator=train_generator,
						steps_per_epoch=STEP_SIZE_TRAIN,
						validation_data=val_generator,
						validation_steps=STEP_SIZE_VALID,
	                    epochs=20
	)
	return model

	

def detect_and_display(model, video_capture, face_detector, open_eyes_detector, left_eye_detector, right_eye_detector, data, eyes_detected):
    frame = video_capture.read()
    # resize the frame
    frame = cv2.resize(frame, (0, 0), fx=0.6, fy=0.6)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
    # Detect faces
    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(50, 50),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

	# for each detected face
	for (x,y,w,h) in faces:
		# Encode the face into a 128-d embeddings vector
		encoding = face_recognition.face_encodings(rgb, [(y, x+w, y+h, x)])[0]

		# Compare the vector with all known faces encodings
		matches = face_recognition.compare_faces(data["encodings"], encoding)

		# For now we don't know the person name
		name = "Unknown"

		# If there is at least one match:
		if True in matches:
			matchedIdxs = [i for (i, b) in enumerate(matches) if b]
			counts = {}
			for i in matchedIdxs:
				name = data["names"][i]
				counts[name] = counts.get(name, 0) + 1

			# The known encoding with the most number of matches corresponds to the detected face name
			name = max(counts, key=counts.get)

		face = frame[y:y+h,x:x+w]
		gray_face = gray[y:y+h,x:x+w]

		eyes = []
            
		# Eyes detection
		# check first if eyes are open (with glasses taking into account)
		open_eyes_glasses = open_eyes_detector.detectMultiScale(
			gray_face,
			scaleFactor=1.1,
			minNeighbors=5,
			minSize=(30, 30),
			flags = cv2.CASCADE_SCALE_IMAGE
		)
		# if open_eyes_glasses detect eyes then they are open 
		if len(open_eyes_glasses) == 2:
			eyes_detected[name]+='1'
			for (ex,ey,ew,eh) in open_eyes_glasses:
				cv2.rectangle(face,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            
		# otherwise try detecting eyes using left and right_eye_detector
		# which can detect open and closed eyes                
		else:
			# separate the face into left and right sides
			left_face = frame[y:y+h, x+int(w/2):x+w]
			left_face_gray = gray[y:y+h, x+int(w/2):x+w]

			right_face = frame[y:y+h, x:x+int(w/2)]
			right_face_gray = gray[y:y+h, x:x+int(w/2)]

			# Detect the left eye
			left_eye = left_eye_detector.detectMultiScale(
				left_face_gray,
				scaleFactor=1.1,
				minNeighbors=5,
				minSize=(30, 30),
				flags = cv2.CASCADE_SCALE_IMAGE
			)

			# Detect the right eye
			right_eye = right_eye_detector.detectMultiScale(
				right_face_gray,
				scaleFactor=1.1,
				minNeighbors=5,
				minSize=(30, 30),
				flags = cv2.CASCADE_SCALE_IMAGE
			)

			eye_status = '1' # we suppose the eyes are open

			# For each eye check wether the eye is closed.
			# If one is closed we conclude the eyes are closed
			for (ex,ey,ew,eh) in right_eye:
				color = (0,255,0)
				pred = predict(right_face[ey:ey+eh,ex:ex+ew],model)
				if pred == 'closed':
					eye_status='0'
					color = (0,0,255)
				cv2.rectangle(right_face,(ex,ey),(ex+ew,ey+eh),color,2)
			for (ex,ey,ew,eh) in left_eye:
				color = (0,255,0)
				pred = predict(left_face[ey:ey+eh,ex:ex+ew],model)
				if pred == 'closed':
					eye_status='0'
					color = (0,0,255)
				cv2.rectangle(left_face,(ex,ey),(ex+ew,ey+eh),color,2)
			eyes_detected[name] += eye_status

		# Each time, we check if the person has blinked
		# If yes, we display its name
		if isBlinking(eyes_detected[name],3):
			cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
			# Display name
			y = y - 15 if y - 15 > 15 else y + 15
			cv2.putText(frame, name, (x, y), cv2.FONT_HERSHEY_SIMPLEX,0.75, (0, 255, 0), 2)

	return frame