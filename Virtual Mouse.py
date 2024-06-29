import cv2
import HandTrackingModule as htm
import numpy as np
import time
import autopy

###############################
wCam, hCam = 640, 480
frameR = 100 #frame reduction
smoothening = 5
###############################
pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

detector = htm.handDetector(maxHands=1)
wScreen, hScreen = autopy.screen.size()
while True:
    #find hand landmarks
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    #Get the tip of the index and middle finger
    if len(lmList)!=0:
        x1, y1 = lmList[8][1:] #For index finger
        x2, y2 = lmList[12][1:] #For middle finger
        print(x1, y1, x2, y2)

        #check which fingers are up
        fingers = detector.fingersUp()
        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 0, 255), 2)

        #Only Index finger : moving mode
        if fingers[1]==1 and fingers[2]==0:

            #convert coordinates
            x3 = np.interp(x1, (frameR, wCam-frameR), (0, wScreen))
            y3 = np.interp(y1, (frameR, hCam-frameR), (0, hScreen))

            #Smooth values
            clocX = plocX+(x3-plocX) /smoothening
            clocY = plocY+(y3-plocY) /smoothening

            #Move mouse
            autopy.mouse.move(wScreen-clocX, hScreen-clocY)
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED,)
            plocX, plocY = clocX, clocY

        #Both index and Middle finger are up : clicking mode
        if fingers[1]==1 and fingers[2]==1:

            #finfing distance between two fingers
            length, img, lineInfo = detector.findDistance(8, 12, img)
            if length < 40:
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)

                #click mouse if distance is short
                autopy.mouse.click()

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)