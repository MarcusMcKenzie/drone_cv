# Video_With_Pose_Recognition

 Receives video stream from drone camera and performs pose recognition processing through PC
 
## Prerequisites

- Python2.7
- pip
- Python OpenCV
- Numpy 
- PIL
- libboost-python
- Tkinter
- homebrew(for mac)
- Python h264 decoder
    - <https://github.com/DaWelter/h264decoder>
    
    
## Run the program
- **Step1**. Turn on drone and connect computer to drone wifi.


- **Step2**. Open project folder in terminal and run:
    
    ```
    python main.py
    ```

- **Step3**. UI will be displayed, which will allow for control of drone. UI allows to:

    - Watch live video stream from the drone camera;
    - Take snapshot and save jpg to local folder;
    - Open Command Panel, which allows you to:
        - Take Off
        - Land
        - Flip (in forward, backward, left and right direction)
        - Control drone using keyboard inputs:
            - **[key-Up]** move forward 20cm
            - **[key-Down]** move backward 20cm
            - **[key-Left]** move left 20 cm
            - **[key-Right]** move right 20 cm
            - **[key-w]** move up 20cm
            - **[key-s]** move down 20cm
            - **[key-a]** rotate counter-clockwise by 30 degree
            - **[key-d]** rotate clockwise by 30 degree
        
    - Turn on **Pose Recognition** mode. 
          - Figure based on user will appear on the screen. Raise arms UP or FLAT ( "Y" or "T" ) to move drone forward 0.5 meters. 
          - Raise both your arm DOWN ( '/|\' ), to move drone back 0.5 meters. 
          - Raise your arms so that they are bending in a V-shape( 'v|v' ),to make drone land.
