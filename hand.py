import cv2
import time
import HandTrackingModule as htm
import math
import os
import subprocess
def set_volume(volume_level):
    if 0 <= volume_level <= 100:
        os.system(f"osascript -e 'set volume output volume {volume_level}'")
    else:
        raise ValueError("Volume level must be between 0 and 100")

def get_current_volume():
    result = subprocess.run(
        ["osascript", "-e", "output volume of (get volume settings)"],
        capture_output=True,
        text=True
    )
    return int(result.stdout.strip())

# Example usage: set volume to 50%

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0
vol = get_current_volume()
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
        set_volume(vol)
        
        
    cv2.putText(img, f"VOL: {int(vol)}", (50, 70), cv2.FONT_HERSHEY_PLAIN, 
                3, (255, 0, 0), 3)
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(img, f"FPS: {int(fps)}", (400, 70), cv2.FONT_HERSHEY_PLAIN, 
                3, (255, 0, 0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
