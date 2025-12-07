import cv2
import numpy as np

# Sharpening kernel
sharpen_kernel = np.array([
    [ 0, -1,  0],
    [-1,  5, -1],
    [ 0, -1,  0]
])

mode = 0
mode_text = "Normal"
print("Tekan 1=Average5x5, 2=Gaussian, 3=Sharpen, 4=Average9x9, 0=Normal, q=Quit")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    output = frame.copy()

    # === FILTER SELEKSI MODE ===
    if mode == 1:
        output = cv2.blur(frame, (5, 5))
        mode_text = "Average Blur (5x5)"

    elif mode == 2:
        # Gaussian blur tanpa ukuran kernel
        output = cv2.GaussianBlur(frame, (0, 0), sigmaX=1)
        mode_text = "Gaussian Blur"

    elif mode == 3:
        output = cv2.filter2D(frame, -1, sharpen_kernel)
        mode_text = "Sharpening"

    elif mode == 4:
        output = cv2.blur(frame, (9, 9))
        mode_text = "Average Blur (9x9)"

    else:
        mode_text = "Normal"

    # === TAMPILKAN TEKS MODE DI ATAS VIDEO ===
    cv2.putText(output,
                f"Mode: {mode_text}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 255),
                2,
                cv2.LINE_AA)

    cv2.imshow("Camera", output)

    key = cv2.waitKey(1) & 0xFF

    # CONTROL MODE
    if key == ord('1'):
        mode = 1
    elif key == ord('2'):
        mode = 2
    elif key == ord('3'):
        mode = 3
    elif key == ord('4'):
        mode = 4
    elif key == ord('0'):
        mode = 0
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
