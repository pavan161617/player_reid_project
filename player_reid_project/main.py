import cv2
import numpy as np
from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort

# Load YOLOv11 model
model = YOLO('model/yolov11.pt')  # Ensure the model file is in the 'model/' folder

# Initialize Deep SORT Tracker
tracker = DeepSort(max_age=30)

# Load video
video_path = 'videos/15sec_input_720p.mp4'
cap = cv2.VideoCapture(video_path)

# Get video properties
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define output writer
out = cv2.VideoWriter(
    'output/reid_output.mp4',
    cv2.VideoWriter_fourcc(*'mp4v'),
    fps,
    (width, height)
)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    detections = []

    # Perform detection
    results = model(frame)[0]  # Get first result

    for box in results.boxes:
        cls_id = int(box.cls[0])  # Class ID
        if cls_id == 0:  # Only detect players
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            bbox = [x1, y1, x2 - x1, y2 - y1]  # Convert to (x, y, w, h)
            detections.append((bbox, conf, 'player'))

    # Update tracker
    tracks = tracker.update_tracks(detections, frame=frame)

    # Draw results
    for track in tracks:
        if not track.is_confirmed():
            continue
        track_id = track.track_id
        l, t, r, b = map(int, track.to_ltrb())

        # Draw bounding box
        cv2.rectangle(frame, (l, t), (r, b), (0, 255, 0), 2)
        cv2.putText(frame, f'ID {track_id}', (l, t - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # Save and show
    out.write(frame)
    cv2.imshow("Player Re-Identification", frame)
    if cv2.waitKey(1) == ord('q'):
        break

# Release everything
cap.release()
out.release()
cv2.destroyAllWindows()
