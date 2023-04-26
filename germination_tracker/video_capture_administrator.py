import cv2


class VideoCaptureAdministrator:
    def __init__(
        self,
        cam_index,
        destination_folder,
        filename,
    ) -> None:
        self.cam_index = cam_index
        self.destination_folder = destination_folder
        self.filename = filename
        self.ret = None
        self.frame = None

    def capture(self):
        cam = cv2.VideoCapture(self.cam_index)
        ret, frame = cam.read()
        self.ret = ret
        self.frame = frame

