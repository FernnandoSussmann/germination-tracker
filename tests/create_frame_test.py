import pytest
from unittest import mock
from germination_tracker.video_capture_administrator import VideoCaptureAdministrator
from germination_tracker.exceptions.frame_loader_exception import FrameLoadError


@mock.patch("cv2.VideoCapture.__new__")
def test_create_frame(video_capture):
    frame = mock.Mock()
    video_capture.return_value.read.return_value = ("ok", frame)

    video_capture_adm = VideoCaptureAdministrator(
        cam_index=1, destination_folder="", filename=""
    )

    video_capture_adm.capture()

    video_capture.return_value.read.assert_called_once()
    video_capture_adm.ret == "ok"
    video_capture_adm.frame == frame


@mock.patch("cv2.VideoCapture.__new__")
def test_create_frame_exception(video_capture):
    video_capture.return_value.read.return_value = (None, None)

    with pytest.raises(
        FrameLoadError, match="Image could not be capture for an unknown reasons.*"
    ):
        video_capture_adm = VideoCaptureAdministrator(
            cam_index=1, destination_folder="", filename=""
        )

        video_capture_adm.capture()
