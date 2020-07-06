# drone_cv
Object Detection, Tracking & Following with Quadrocopter

### Programs

This repo consists of four different ways to interact with and control the drone. The file named drone_state.py provides information about the drone's status data. All of these programs utilize Python 2.7, expecpt for the Detection_and_Tracking program, which utilizes Python 3.5.

* **Single_Test** <br>
Simple testing porgram that allows for the design of a series of command combinations by writing a text script, for the drone to execute.  

* **Drone_video** <br>
Receive video stream data from the drone, decode the video through the h264 decoding library, and display it on a GUI interface. Also contains a control panel that can be used to control the drone during the test. 

* **Drone_Video_With_Pose_Recognition** <br>
Uses the decoded video data，and extracts frame images to determine the posture of the user, using OpenPose, and uses these poses to control the actions of the drone.

* **Detection_and_Tracking** <br>
Uses OpenCV to detect and track an object within the drone's camera frame. Based on the location of the object in the frame, the drone will move parallel with the object, so that the object is in the center of the frame. 
