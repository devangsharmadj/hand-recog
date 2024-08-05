import cv2
import time
import HandTrackingModule as htm
import math
import subprocess
def set_brightness(level):
    """
    Sets the brightness level on a Mac.
    
    Args:
    level (int): A value between 0 and 100 representing the brightness level.
    """
    if level < 0 or level > 100:
        raise ValueError("Brightness level must be between 0 and 100")
    
    # Convert the level to a float value between 0 and 1
    level = level / 100.0
    
    # AppleScript to set brightness
    script = f"""
    tell application "System Events"
        repeat with disp in (a reference to every display)
            set brightness of disp to {level}
        end repeat
    end tell
    """
    
    # Run the AppleScript using osascript
    subprocess.run(["osascript", "-e", script])

set_brightness(100)
wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0
vol = 50
# detector = htm.handDetector(detectionCon=0.75)
detector = htm.handDetector()
while True: 
    success, img = cap.read()

    img = detector.findHands(img)
    lmlist = detector.findPosition(img, draw = False)

    #print(lmlist)
    # Thumb x, y:

    if len(lmlist) != 0:
        tx, ty = lmlist[4][1], lmlist[4][2]
        ix, iy = lmlist[8][1], lmlist[8][2]

        dist = math.sqrt(((tx - ix)**2) + ((ty - iy) ** 2))
        # print(dist)

        max_dist, min_dist = 300, 0
        max_vol, min_vol = 100,0 
        vol = (((dist - min_dist) * 100) / 270) + min_vol
        if vol > 100: 
            vol = 100
        set_brightness(vol)
        
        
    cv2.putText(img, f"VOL: {int(vol)}", (50, 70), cv2.FONT_HERSHEY_PLAIN, 
                3, (255, 0, 0), 3)
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(img, f"FPS: {int(fps)}", (400, 70), cv2.FONT_HERSHEY_PLAIN, 
                3, (255, 0, 0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
