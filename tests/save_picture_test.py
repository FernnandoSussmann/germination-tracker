from unittest import mock
from germination_tracker.video_capture_administrator import VideoCaptureAdministrator


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
