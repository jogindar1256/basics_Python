import face_recognition
import cv2

def capture_face_image(filename):
    video_capture = cv2.VideoCapture(0)
    print("Press 'q' to capture a face image.")
    
    while True:
        ret, frame = video_capture.read()
        cv2.imshow('Capture Face', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            face_image = frame
            cv2.imwrite(filename, face_image)
            break
    
    video_capture.release()
    cv2.destroyAllWindows()
    print(f"Image saved as {filename}")

capture_face_image('user_face.jpg')
