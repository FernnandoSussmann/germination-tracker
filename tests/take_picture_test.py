from unittest import mock


@mock.patch("cv2.VideoCapture.__new__")
def test_take_picture(video_capture):
    frame = mock.Mock()
    destination_folder = "/tmp/tests/pictures"
    filename = "test_pic.png"

    video_capture_adm = VideoCaptureAdministrator(
        cam_index=1, destination_folder=destination_folder, filename=filename
    )

    video_capture.return_value.read.return_value = ("ok", frame)

    video_capture_adm.capture()
    video_capture_adm.take_picture()

    video_capture.assert_called_with(1)

    video_capture.return_value.imwrite.assert_called_with(
        f"{destination_folder}/{filename}",
        frame,
    )
