import pytest
from unittest import mock


@mock.patch("cv2.VideoCapture.__new__")
def test_init_frame(video_capture):
    frame = mock.Mock()
    video_capture.return_value.read.return_value = ("ok", frame)

    video_capture_adm = VideoCaptureAdministrator(
        cam_index=1, destination_folder="", filename=""
    )

    video_capture_adm.init_capture()

    
    video_capture.return_value.read.assert_called_once()
    video_capture_adm.ret == "ok"
    video_capture_adm.frame == frame


@mock.patch("cv2.VideoCapture.__new__")
def test_init_frame_exception(video_capture):
    video_capture.return_value.read.return_value = (None, None)

    with pytest.raises(FrameLoadError, match=".* could not be initilized for an unknown reason.*"):
        video_capture_adm = VideoCaptureAdministrator(
            cam_index=1, destination_folder="", filename=""
        )

        video_capture_adm.init_capture()