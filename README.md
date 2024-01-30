# webot robot controller via hand gesture recognition using Mediapipe
The main goal of this project is to control Webot robot via hand gestures using MediaPipe (Python version).<br> 
<br> ❗ Reference: [original repo](https://github.com/kinivi/hand-gesture-recognition-mediapipe).
<br> 
![Demo](https://github.com/jiawenchim/images/blob/main/Webot%20demo%20(1).gif)

This repository contains the following contents.
* Program file
* Hand gesture recognition model(TFLite)
* Learning data for hand sign recognition and notebook for learning

# Requirements
* mediapipe 0.8.1
* OpenCV 3.4.2 or Later
* scikit-learn 0.23.2 or Later (Only if you want to display the confusion matrix) 
* matplotlib 3.3.2 or Later (Only if you want to display the confusion matrix)

# Demo
Here's how to run the demo using your webcam.
```bash
python app.py
```

The following options can be specified when running the demo.
* --device<br>Specifying the camera device number (Default：0)
* --width<br>Width at the time of camera capture (Default：960)
* --height<br>Height at the time of camera capture (Default：540)
* --min_detection_confidence<br>
Detection confidence threshold (Default：0.5)
* --min_tracking_confidence<br>
Tracking confidence threshold (Default：0.5)

# Directory
<pre>
│  app.py
│  keypoint_classification.ipynb
│  
├─model
│  ├─keypoint_classifier
│  │  │  keypoint.csv
│  │  │  keypoint_classifier.hdf5
│  │  │  keypoint_classifier.py
│  │  │  keypoint_classifier.tflite
│  │  └─ keypoint_classifier_label.csv        
└─utils
    └─cvfpscalc.py
</pre>
### app.py
Running app.py will establish connection to Webot simulation and activate live device camera. Webot robot can be controlled through hand gestures recognized by live inference of device camera video stream. 

Hand sign instruction:
|Input:Handedness +	Input:Gesture = Output|	
* Left + Open = Forward
* Right + Open = Backward
* Left  + Pointer = Turn clockwise / left
* Right + Pointer = Turn anticlockwise / right
* Close / OK = Stop

Possible configuration options based on user preferences: 
#### (i)	Speed of robot movement
* CRUISING_SPEED (default at 1.0)
* TURN_SPEED (default at CRUISING_SPEED/2)
#### (ii) Frame per second (in equivalent to sensitivity of live video streaming inference)
* camera_sensitivity (default at 500, which is translated to 2 frames per second).


### keypoint_classification.ipynb
This is a model training script for hand gestures recognition based on input keypoint list and labels.

### model/keypoint_classifier
This directory stores files related to hand sign recognition.<br>
The following files are stored.
* Training data(keypoint.csv) - first column is the label (integer from 0 to 3). Remaining columns are the keypoints coordinates, generated and preprocessed by Mediapipe library. 
* Trained model(keypoint_classifier.tflite) - trained model will be saved here.
* Label data(keypoint_classifier_label.csv) - label data (Open, Close, Pointer, OK)
* Inference module(keypoint_classifier.py)

Hand landmark model bundle that detects the keypoint locatization of 21 hand-knuckle coordinates within the detected hand regions. According to Mediapipe documentation, the model was trained on around 30k real-wrk images, as well as several rendered synthetic hand models imposed over various backgrounds.
![image](https://github.com/jiawenchim/ITI108_Webot_with_hand_gestures_controller/assets/142727228/2f7d4a14-bb6b-4e36-97fd-59662ef42984)


### utils/cvfpscalc.py
This is a module for FPS measurement.

# Training
Hand sign recognition and finger gesture recognition can add and change training data and retrain the model.
![image](https://github.com/jiawenchim/ITI108_Webot_with_hand_gestures_controller/assets/142727228/0a2591f1-885b-4f34-99eb-7f96e635836c)

