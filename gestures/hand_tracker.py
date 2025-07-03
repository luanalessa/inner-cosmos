import cv2
import mediapipe as mp

class HandTracker:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.6
        )
        self.results = None

    def get_hand_positions(self, frame):
        self.update(frame)  # ESSENCIAL!

        hand_positions = []

        if self.results.multi_hand_landmarks:
            for hand_landmarks in self.results.multi_hand_landmarks:
                hand = []
                for lm in hand_landmarks.landmark:
                    hand.append((lm.x, lm.y))
                hand_positions.append(hand)

        return hand_positions


    def get_index_finger_position(self, frame):
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.hands.process(frame_rgb)

        if result.multi_hand_landmarks:
            for hand_landmarks, hand_class in zip(result.multi_hand_landmarks, result.multi_handedness):
                if hand_class.classification[0].label == 'Right':
                    point = hand_landmarks.landmark[8]  # dedo indicador
                    return point.x, point.y
        return None
    
    def is_left_hand_pinch(self):
        if self.results.multi_hand_landmarks and self.results.multi_handedness:
            for idx, hand_info in enumerate(self.results.multi_handedness):
                label = hand_info.classification[0].label
                if label == "Left":
                    landmarks = self.results.multi_hand_landmarks[idx].landmark
                    thumb = landmarks[self.mp_hands.HandLandmark.THUMB_TIP]
                    index = landmarks[self.mp_hands.HandLandmark.INDEX_FINGER_TIP]
                    dist = ((thumb.x - index.x) ** 2 + (thumb.y - index.y) ** 2) ** 0.5
                    return dist < 0.05
        return False
    
    def is_right_hand_pinch(self):
        if self.results.multi_hand_landmarks and self.results.multi_handedness:
            for idx, hand_info in enumerate(self.results.multi_handedness):
                label = hand_info.classification[0].label
                if label == "Right":
                    landmarks = self.results.multi_hand_landmarks[idx].landmark
                    thumb = landmarks[self.mp_hands.HandLandmark.THUMB_TIP]
                    index = landmarks[self.mp_hands.HandLandmark.INDEX_FINGER_TIP]
                    dist = ((thumb.x - index.x) ** 2 + (thumb.y - index.y) ** 2) ** 0.5
                    return dist < 0.04  # Pode ajustar a sensibilidade
        return False

    def update(self, frame):
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(frame_rgb)


