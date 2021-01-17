%pylab inline
import face_recognition
import cv2
import matplotlib.patches as patches
from IPython.display import clear_output
from matplotlib.pyplot import imshow
import matplotlib.pylab as plt

video_capture = cv2.VideoCapture("/content/drive/My Drive/Colab Notebooks/ob/young3.mp4")

frame_count = 0

while video_capture.isOpened():
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Bail out when the video file ends
    if not ret:
        video_capture.release()
        break

 frame_count += 1
    if frame_count % 25 == 0:    
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Display video frame
        title("Input Stream")
        plt.imshow(frame)        

        # Find all the faces and face encodings in the current frame of video
        rgb_frame = frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_frame)

        # If faces were found, we will mark it on frame with blue dots
        for face_location in face_locations:       
            plt.plot(face_location[1], face_location[0], 'bo')
            plt.plot(face_location[1], face_location[2], 'bo')
            plt.plot(face_location[3], face_location[2], 'bo')
            plt.plot(face_location[3], face_location[0], 'bo')

        # Show frame...
        plt.show() 

        # ... and hold it until a new frame appears
        clear_output(wait=True)

        