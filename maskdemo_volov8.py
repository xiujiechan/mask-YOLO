import cv2
import torch
import numpy as np
from ultralytics import YOLO

video_path = r"C:\Users\USER\Desktop\chen\Day8_2024-20240218T015814Z-001\Day8_2024\dance_0821.mp4"

cap = cv2.VideoCapture(video_path)

model = YOLO('yolov8n.pt')

x_line = 600

while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    if success:

        # Run YOLOv8 inference on the frame
        resized_frame = cv2.resize(frame, (1280, 720), interpolation=cv2.INTER_LINEAR)
        cv2.line(resized_frame, (0, x_line), (width, x_line), (255, 0, 0), 10)

        # Visualize the results on the frame
        results = model(resized_frame, conf=0.5, cls=0)

        annotated_frame = results[0].plot()

        # Display the annotated frame
        cv2.imshow("YOLOv8 Inference", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    else:
        # Break the loop if the end of the video is reached
        break

cap.release()
cv2.destroyAllWindows()