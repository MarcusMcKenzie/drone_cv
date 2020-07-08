import drone
import cv2
import time


width = 320  
height = 240 
startCounter = 1   #  0 FOR FLIGHT 1 FOR TESTING


robot = drone.Tello()



print("address: ", robot.get_current_state())
print("me: ", robot.address)

#robot.connect()
robot.send_control_command("command")

robot.move_for = 0
robot.move_back = 0
robot.move_left = 0
robot.move_right = 0
robot.move_up = 0
robot.move_down = 0
robot.set_speed = 0
 
#print(robot.get_battery())


robot.streamoff()
robot.streamon()



while True:
 
   
    frame_read = robot.get_frame_read()
    

    myFrame = frame_read.frame
    #cv2.imwrite("myFrame", myFrame)
    img = cv2.resize(myFrame, (width, height))
 

    if startCounter == 0:
        robot.takeoff()
        time.sleep(1)
        robot.rotate_clockwise(90)
        time.sleep(1)
        
        
        
        robot.move("left", 35)
        #me.move_left(35)

        # move forward worked
        #me.move_back(35) not work
        # left/right no work
        #me.move_up(35) no work


        time.sleep(1)
        robot.land()
        startCounter = 1
 
    # # send velocity vals to motors
    # if me.send_rc_control:
    #     me.send_rc_control(me.left_right_velocity, me.for_back_velocity, me.up_down_velocity, me.yaw_velocity)
 
    cv2.imshow("MyResult", img)
 
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        robot.land()
        break