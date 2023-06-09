import cv2
import os
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

    def __validate_frame(self, frame):
        if frame is None:
            raise FrameLoadError("Frame with None value", Exception())


    def capture(self):
        cam = cv2.VideoCapture(self.cam_index)

        try:
            ret, frame = cam.read()
            self.__validate_frame(frame)
        except FrameLoadError as ferr:
            raise ferr
        except Exception as e:
            raise FrameLoadError(str(e), e)
        
        self.ret = ret
        self.frame = frame
    
    def save_picture(self):
        self.__validate_frame(self.frame)
        full_path = os.path.join(self.destination_folder, self.filename)
        cv2.imwrite(full_path, self.frame)
