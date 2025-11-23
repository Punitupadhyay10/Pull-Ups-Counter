import cv2
import numpy as np
import math

protoFile = "pose_deploy_linevec.prototxt"
weightsFile = "pose_iter_584000.caffemodel"

net = cv2.dnn.readNetFromCaffe(protoFile, weightsFile)

def calculate_angle(a, b, c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    ba = a - b
    bc = c - b

    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    angle = np.degrees(np.arccos(cosine_angle))
    return angle

cap = cv2.VideoCapture(0)

pullups = 0
stage = "down"

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    frameWidth = frame.shape[1]
    frameHeight = frame.shape[0]

    inpBlob = cv2.dnn.blobFromImage(frame, 1.0/255, (368, 368),
                                    (0, 0, 0), swapRB=False, crop=False)
    net.setInput(inpBlob)
    output = net.forward()

    H = output.shape[2]
    W = output.shape[3]

    points = []
    for i in range(5):
        probMap = output[0, i, :, :]
        minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)

        x = int((frameWidth * point[0]) / W)
        y = int((frameHeight * point[1]) / H)

        if prob > 0.2:
            points.append((x, y))
            cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)
        else:
            points.append(None)

    if points[2] and points[3] and points[4]:
        angle = calculate_angle(points[2], points[3], points[4])
        cv2.putText(frame, f"Angle: {int(angle)}", (10, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

        if angle > 150:
            stage = "down"
        if angle < 70 and stage == "down":
            pullups += 1
            stage = "up"

    cv2.putText(frame, f"Pull-ups: {pullups}", (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)

    cv2.imshow("Pull-up Counter", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
