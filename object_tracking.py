from ultralytics import YOLO

#load yolo11n pretrained model
model=YOLO("yolo11n.pt")

#tracking with default tracker bot-sort
results=model.track(source="D:\Project_Developement\Object_Tracking_using_Yolo\Videos\video7.mp4",save=True,show=True)
