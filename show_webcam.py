import cv2
import time
import mediapipe as mp
from mediapipe.python.solutions.pose import PoseLandmark
from mediapipe.python.solutions.drawing_utils import DrawingSpec

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(model_complexity=0, min_detection_confidence=0.5, min_tracking_confidence=0.5)

cap = cv2.VideoCapture(0)

p_time = 0
c_time = 0

while True:
    ret, image = cap.read()

    if not ret:
        break

    #image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    results = pose.process(image)

    mp_drawing.draw_landmarks(
            image,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS)

    c_time = time.time()
    fps = 1/(c_time-p_time)
    p_time = c_time

    cv2.putText(image, str(int(fps)), (10, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 1)

    cv2.imshow('Video desde Jetson Nano', image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
