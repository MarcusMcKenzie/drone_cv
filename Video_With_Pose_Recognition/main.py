import drone
from drone_control_ui import TelloUI


def main():

    tello = drone.Tello('', 8889)  
    vplayer = TelloUI(tello,"./img/")
    
	# start the Tkinter mainloop
    vplayer.root.mainloop() 

if __name__ == "__main__":
    main()
