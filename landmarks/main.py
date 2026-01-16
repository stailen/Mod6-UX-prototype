#landmark model
#model uses rgb
from flatbuffers.flexbuffers import Object
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
model_path = '/home/seba/Nextcloud/UNI/TCS/M6/UX/Mod6-UX-prototype/landmarks/model/pose_landmarker_heavy.task'

#cv video capture
#cv uses bgr
import cv2
cap = None
img_frame = None

#landmark init
BaseOptions = mp.tasks.BaseOptions
PoseLandmarker = mp.tasks.vision.PoseLandmarker
PoseLandmarkerOptions = mp.tasks.vision.PoseLandmarkerOptions
PoseLandmarkerResult = mp.tasks.vision.PoseLandmarkerResult
VisionRunningMode = mp.tasks.vision.RunningMode

#data storage
score = 0
prev_results = None

#callback
def proc_result(result: PoseLandmarkerResult, output_image: mp.Image, timestamp_ms: int): # type: ignore
    img = output_image.numpy_view().copy()
    out_h, out_w = img.shape[:2]
    global prev_results
    global score

    if not result.pose_landmarks:
        return
    for pose_landmarks in result.pose_landmarks:
        # draw keypoints
        for idx, lm in enumerate(pose_landmarks):
            px = int(lm.x * out_w)
            py = int(lm.y * out_h)
            if prev_results is not None:
                prev_current_lm = prev_results.pose_landmarks[0][idx]
                delta_x = abs(prev_current_lm.x - lm.x) * out_w 
                delta_y = abs(prev_current_lm.y - lm.y) * out_h 
                score += (delta_x + delta_y) * abs(lm.z)
                prev_results = result
            else:
                prev_results = result
            #skip points that are outside the image bounds
            if 0 <= px < out_w and 0 <= py < out_h:
                cv2.circle(img, (px, py), radius=3, color=(0,255,0), thickness=-1)

    img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    global img_frame 
    img_frame = img_bgr
    return

def main() -> int:
    try:
        options = PoseLandmarkerOptions(
            base_options=BaseOptions(model_asset_path=model_path),
            running_mode=VisionRunningMode.LIVE_STREAM,
            result_callback=proc_result)

        global cap
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            raise RuntimeError("Cannot open camera")

        with PoseLandmarker.create_from_options(options) as landmarker:
            #loop for calculating frame
            frame_counter = 0
            while True:
                ret, frame = cap.read()
                if not ret:
                    print("Frame read failed, exiting")
                    break
                mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
                landmarker.detect_async(mp_image, frame_counter)
                frame_counter += 1
                if img_frame is not None:
                    cv2.imshow("annotated", img_frame)
                else:
                    cv2.imshow("annotated", frame)

                if cv2.waitKey(delay=1) & 0xFF == 27:  # ESC to quit
                    print("congrats your score is: ", score)
                    return score
    finally:
        if cap is not None:
            cap.release()
            cv2.destroyAllWindows()