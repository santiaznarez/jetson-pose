import cv2
import time
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# Create a Pose instance with reduced complexity and confidence thresholds
pose = mp_pose.Pose(model_complexity=0, min_detection_confidence=0.2, min_tracking_confidence=0.2)

cap = cv2.VideoCapture(0)

# Set frame width and height
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
cap.set(cv2.CAP_PROP_FPS, 30)

p_time = 0
c_time = 0

while True:
    ret, image = cap.read()

    if not ret:
        break

    # Resize the frame for faster processing
    image = cv2.resize(image, (640, 480))

    results = pose.process(image)

    mp_drawing.draw_landmarks(
        image,
        results.pose_landmarks,
        mp_pose.POSE_CONNECTIONS)

    c_time = time.time()
    fps = 1 / (c_time - p_time)
    p_time = c_time

    cv2.putText(image, str(int(fps)), (10, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 1)

    cv2.imshow('Video from Jetson Nano', image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
