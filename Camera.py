import cv2

class Cam:
    def __init__(self):
        camera_num = 1

    def get_camera_feed(self):
        cap = cv2.VideoCapture(1)
        while cap.isOpened():
            ret, frame = cap.read()

            # filter function implier goes here

            cv2.imshow('Photo Booth', frame)


            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
