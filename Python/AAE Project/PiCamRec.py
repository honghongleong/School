from picamera import PiCamera
from time import sleep
from datetime import *
import time

date = datetime.now().strftime('%y_%m_%d')

camera = PiCamera()
camera.resolution = (1920, 1080)
camera.framerate = 25
time.sleep(10) # Camera warm-up time
camera.start_preview()
filename = "Img_" + date + ".h264"
camera.start_recording(filename)
sleep(5)
camera.stop_recording()
camera.stop_preview()
print("Recorded%s" %filename)#Need spacing for Captured*Img_
