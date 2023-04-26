import cv2
from germination_tracker.exceptions.frame_loader_exception import FrameLoadError



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

    def validate_frame(self, frame):
        if frame is None:
            raise FrameLoadError("Frame with None value")


    def capture(self):
        cam = cv2.VideoCapture(self.cam_index)

        try:
            ret, frame = cam.read()
            self.validate_frame(frame)
        except FrameLoadError as ferr:
            raise ferr
        except Exception as e:
            raise FrameLoadError(str(e), e)
        
        self.ret = ret
        self.frame = frame

