import cv2
import math
import time
from ultralytics import YOLO

# Initialize the webcam
cap = cv2.VideoCapture(0)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
frame_fps = int(cap.get(5))

# Define the codec and create VideoWriter object to save the video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_path = 'Test_output1.mp4'  # Adjust the path as necessary
out = cv2.VideoWriter(output_path, fourcc, frame_fps, (frame_width, frame_height))

# Load the YOLO model
model = YOLO("bestYolov8.pt")

# Define class names for mask classification
classNames = ["with_mask", "without_mask"]

while True:
    success, img = cap.read()
    if not success:
        break  # Exit loop if cannot read from webcam

    results = model(img, stream=True)

    # Process detections and draw bounding boxes
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = [int(v) for v in box.xyxy[0]]
            cls = int(box.cls[0])
            confidence = math.ceil((box.conf[0] * 100)) / 100

            # Determine color and thickness based on the class detected
            if classNames[cls] == "with_mask":
                color = (0, 255, 0)  # Green for "with_mask"
            else:
                color = (0, 0, 255)  # Red for "without_mask"
            thickness = 1  # Set thickness to 1 for both rectangle and text

            # Draw rectangle and text for each detection
            cv2.rectangle(img, (x1, y1), (x2, y2), color, thickness)
            cv2.putText(img, f'{classNames[cls]} {confidence}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, thickness)

    # Display the resulting frame
    cv2.imshow('Webcam', img)

    # Write the frame into the file 'output_video.mp4'
    out.write(img)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Break the loop when 'q' is pressed
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
