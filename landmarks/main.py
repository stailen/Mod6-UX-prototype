#landmark model
#model uses rgb
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
model_path = 'landmarks\\model\\pose_landmarker_heavy.task'

#cv video capture
#cv uses bgr
import cv2
cap = cv2.VideoCapture(0)
img_frame = None
if not cap.isOpened():
    raise RuntimeError("Cannot open camera")

#landmark init
BaseOptions = mp.tasks.BaseOptions
PoseLandmarker = mp.tasks.vision.PoseLandmarker
PoseLandmarkerOptions = mp.tasks.vision.PoseLandmarkerOptions
PoseLandmarkerResult = mp.tasks.vision.PoseLandmarkerResult
VisionRunningMode = mp.tasks.vision.RunningMode

#callback
def proc_result(result: PoseLandmarkerResult, output_image: mp.Image, timestamp_ms: int): # type: ignore
    img = output_image.numpy_view().copy()
    out_h, out_w = img.shape[:2]

    if not result.pose_landmarks:
        return
    for pose_landmarks in result.pose_landmarks:
        # draw keypoints
        for lm in pose_landmarks:
            px = int(lm.x * out_w)
            py = int(lm.y * out_h)
            #skip points that are outside the image bounds
            if 0 <= px < out_w and 0 <= py < out_h:
                cv2.circle(img, (px, py), radius=3, color=(0,255,0), thickness=-1)

    img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    global img_frame 
    img_frame = img_bgr
    return

options = PoseLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=proc_result)

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
        if cv2.waitKey(1) & 0xFF == 27:  # ESC to quit
            break
cap.release()
cv2.destroyAllWindows()