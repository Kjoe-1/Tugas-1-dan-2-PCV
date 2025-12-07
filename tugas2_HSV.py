import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Rentang warna biru dalam HSV
lower_black = np.array([0, 0, 0])
upper_black = np.array([180, 255, 50])

kernel = np.ones((5, 5), np.uint8)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Konversi ke HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Threshold
    mask = cv2.inRange(hsv, lower_black, upper_black)

    # Opening -> menghilangkan noise kecil
    mask_open = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    # Closing -> menutup lubang kecil di objek
    mask_clean = cv2.morphologyEx(mask_open, cv2.MORPH_CLOSE, kernel)

    # Cari kontur
    contours, _ = cv2.findContours(mask_clean, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    detected = False
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 800:  # batas minimum area objek
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)
            detected = True

    if detected:
        cv2.putText(frame, "Objek Hitam Terdeteksi!", (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 0, 0), 3)

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask_clean)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
