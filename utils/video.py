from pathlib import Path

import cv2


class VideoManager:
    """
    Handles webcam/video input and optional output recording.
    """

    def __init__(
        self,
        source=0,
        save_output=False,
        output_path="output/tracked_output.mp4",
    ):

        self.source = source
        self.save_output = save_output
        self.output_path = output_path

        self.capture = None
        self.writer = None

    def open(self):

        self.capture = cv2.VideoCapture(
            self.source
        )

        if not self.capture.isOpened():
            return False

        if self.save_output:

            Path("output").mkdir(
                parents=True,
                exist_ok=True,
            )

            width = int(
                self.capture.get(
                    cv2.CAP_PROP_FRAME_WIDTH
                )
            )

            height = int(
                self.capture.get(
                    cv2.CAP_PROP_FRAME_HEIGHT
                )
            )

            fps = self.capture.get(
                cv2.CAP_PROP_FPS
            )

            # Webcam sometimes returns 0 FPS
            if fps <= 0:
                fps = 30.0

            fourcc = cv2.VideoWriter_fourcc(
                *"mp4v"
            )

            self.writer = cv2.VideoWriter(
                self.output_path,
                fourcc,
                fps,
                (width, height),
            )

        return True

    def read(self):

        if self.capture is None:
            return False, None

        return self.capture.read()

    def write(self, frame):

        if self.writer is not None:

            self.writer.write(frame)

    def release(self):

        if self.capture is not None:
            self.capture.release()

        if self.writer is not None:
            self.writer.release()

        cv2.destroyAllWindows()