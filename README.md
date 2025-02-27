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
│  data.py
│  keypoint_classification.ipynb
│  
├─model
│  ├─keypoint_classifier
│  │  │  data_collection.csv   
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
* Right + Open = Forward
* Left + Open = Backward
* Left  + Pointer = Turn clockwise / left
* Right + Pointer = Turn anticlockwise / right
* Close / OK = Stop

Possible configuration options based on user preferences: 
#### (i)	Speed of robot movement
* CRUISING_SPEED (default at 1.0)
* TURN_SPEED (default at CRUISING_SPEED/2)
#### (ii) Frame per second (in equivalent to sensitivity of live video streaming inference)
* camera_sensitivity (default at 500, which is translated to 2 frames per second).

### data.py 
Intended for keypoint data collection through camera. By running this file, you will first be prompted to input label class (integer), then, local camera will be activated. You can then show the hand gesture corresponding to the input label class. Keypoints data (a list of 21 pairs of numbers) will be generated and stored under model/keypoint_classifier/data_collection.csv.

### keypoint_classification.ipynb
This is a model training script for hand gestures recognition based on input keypoint list and labels.

### model/keypoint_classifier
This directory stores files related to hand sign recognition.<br>
The following files are stored.
* Training data(keypoint.csv) - first column is the label (integer from 0 to 3). Remaining columns are the keypoints coordinates, generated and preprocessed by Mediapipe library. 
* Trained model(keypoint_classifier.tflite) - trained model will be saved here.
* Label data(keypoint_classifier_label.csv) - label data (Open, Close, Pointer, OK)
* Inference module(keypoint_classifier.py)
* Customized training data(data_collection.csv) - similar to Training data, but data can be collected live by running data.py file under main folder.

Hand landmark model bundle that detects the keypoint locatization of 21 hand-knuckle coordinates within the detected hand regions. According to Mediapipe documentation, the model was trained on around 30k real-world images, as well as several rendered synthetic hand models imposed over various backgrounds.
![image](https://github.com/jiawenchim/ITI108_Webot_with_hand_gestures_controller/assets/142727228/2f7d4a14-bb6b-4e36-97fd-59662ef42984)


### utils/cvfpscalc.py
This is a module for FPS measurement.

# Training
* Keypoint data collected go through following preprocessing: Landmark coordinates -> convert to relative coordinates from ID:0 -> flatten to one-dimensional array ->  normalize to maximum value)
* Google Mediapipe hand landmarks library is used as feature extractor. Subsequenty, the extracted hand landmarks features will be used as input to a predictive classifier made up of Dense layers.
![image](https://github.com/jiawenchim/ITI108_Webot_with_hand_gestures_controller/assets/142727228/417bbffe-f9f2-4e77-890b-7d7ee4c7b8e1)

