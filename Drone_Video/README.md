# Drone_Video
Allows drone to receive video stream from drone camera, decodes the video stream and displays the image in the GUI.

<br>

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


- **Step2**. Open project folder in terminal and run the main script:
    
    ```
    python main.py
    ```

- **Step3**. UI will be displayed, which allows for control of drone. UI allows to:

    - Watch live video stream from the drone camera;
    - Take snapshot and save jpg to local folder;
    - Open Command Panel, which allows for:
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
     
