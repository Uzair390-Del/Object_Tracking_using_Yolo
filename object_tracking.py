# from ultralytics import YOLO

# # #load yolo11n pretrained model
# # model=YOLO("yolo11n.pt")

# # #tracking with default tracker bot-sort
# # # results = model.track(source="Resources\\Videos\\7.mp4", save=True, show=True)

# # #tracking with byte-track
# # results=model.track(source="Resources\\Videos\\video8.mp4",save=True,show=True, tracker= "bytetrack.yaml",conf =0.20, iou=0.3)

# ------------------------------------------------------$

#Python Script using OpenCV-Python (cv2) and YOLO11 to run Object Tracking on Video Frames and on Live Webcam Feed

#Import All the Required Libraries
# import cv2
# from ultralytics import YOLO

# model=YOLO("yolo11n.pt")

# # create a video capture object 

# cap=cv2.VideoCapture("Resources\\Videos\\video5.mp4")

# # # for live webcam 
# # cap=cv2.VideoCapture(0)

# # loop through video frames

# while True:
#     ret,frame=cap.read()
#     if ret:
#         # run yolo 11 on the captured frame
#         results=model.track(frame,persist=True)
#         # visualize the results on the fram
#         anotated_frame=results[0].plot()
#         # # show the anotated frame
#         # cv2.imshow("Yolo11 tracking",anotated_frame)

#         # # if cv2.waitkey(1) & 0xff==ord('q'):
#         # #     break
#         # Check if OpenCV can display windows (GUI support)
#     try:
#         cv2.imshow("YOLO11 Tracking", anotated_frame)
#         # Wait for 1ms and break if 'q' is pressed
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     except Exception as e:
#         print("GUI not supported:", e)
#         break  # Exit if display fails
# cap.release()
# cv2.destroyAllWindows()


# ---------------------------------------------

# for live webcam 
import cv2
from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolo11n.pt")  # Ensure "yolo11n.pt" is in the same folder

# Open webcam (0 = default camera, change if you have multiple cameras)
cap = cv2.VideoCapture(0)

# Check if webcam opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Press 'Q' to quit...")

# Loop for live webcam feed
while True:
    # Read a frame from the webcam
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Run YOLO object tracking
    results = model.track(frame, persist=True)  # 'persist=True' keeps IDs between frames

    # Visualize results (draw bounding boxes & labels)
    annotated_frame = results[0].plot()

    # Display the annotated frame
    cv2.imshow("YOLO Live Webcam Tracking", annotated_frame)

    # Exit if 'Q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()