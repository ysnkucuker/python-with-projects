import cv2

# Load Haar Cascade face detection model
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Open default camera
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Camera could not be opened.")
    exit()

window_name = "Face Detection"
cv2.namedWindow(window_name)

while True:
    ret, frame = camera.read()
    if not ret:
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    # Draw rectangles
    for (x, y, w, h) in faces:
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

    cv2.imshow(window_name, frame)

    # Exit if 'q' pressed OR window closed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    # 🔴 Detect window close (X button)
    if cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
        break

# Release resources
camera.release()
cv2.destroyAllWindows()
