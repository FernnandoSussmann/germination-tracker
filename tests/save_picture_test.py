from unittest import mock
import pytest
from germination_tracker.video_capture_administrator import VideoCaptureAdministrator
from germination_tracker.exceptions.frame_loader_exception import FrameLoadError



@mock.patch("cv2.imwrite", autospec=True)
def test_save_picture(writer):
    frame = mock.Mock()
    destination_folder = "/tmp/tests/pictures"
    filename = "test_pic.png"

    video_capture_adm = VideoCaptureAdministrator(
        cam_index=1, destination_folder=destination_folder, filename=filename
    )

    video_capture_adm.frame = frame

    video_capture_adm.save_picture()

    writer.assert_called_with(
        f"{destination_folder}/{filename}",
        frame,
    )


@mock.patch("cv2.imwrite", autospec=True)
def test_save_picture_exception(writer):
    destination_folder = "/tmp/tests/pictures"
    filename = "test_pic.png"

    video_capture_adm = VideoCaptureAdministrator(
        cam_index=1, destination_folder=destination_folder, filename=filename
    )

    video_capture_adm.frame = None
    with pytest.raises(
        FrameLoadError, match="Image could not be capture for an unknown reasons: Frame with None value"
    ):
        video_capture_adm.save_picture()
