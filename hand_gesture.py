import cv2
import mediapipe as mp
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7) as hands:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        h, w, c = frame.shape
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)

        finger_count = 0

        if results.multi_hand_landmarks:
            for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                landmarks = hand_landmarks.landmark
                label = handedness.classification[0].label 

             
                finger_tips = [8, 12, 16, 20]
                finger_pips = [6, 10, 14, 18]

                for tip, pip in zip(finger_tips, finger_pips):
                    if landmarks[tip].y < landmarks[pip].y:
                        finger_count += 1

               
                if label == "Right":  
                    if landmarks[4].x < landmarks[3].x:
                        finger_count += 1
                else:  # Left hand
                    if landmarks[4].x > landmarks[3].x:
                        finger_count += 1

                cv2.putText(frame, f"{label} Hand", (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

        cv2.putText(frame, f"Fingers: {finger_count}", (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)

        cv2.imshow("Hand Gesture Recognition", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
