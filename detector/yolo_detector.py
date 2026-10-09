from pathlib import Path

from ultralytics import YOLO


class YOLODetector:
    """
    YOLO model wrapper.

    Responsible for loading the pretrained model
    and performing object detection/tracking.
    """

    def __init__(
        self,
        model_path: str = "models/yolov8n.pt",
        confidence: float = 0.40,
    ):
        self.model_path = model_path
        self.confidence = confidence

        self._ensure_model_directory()

        print("Loading YOLO model...")

        self.model = YOLO(model_path)

        print("YOLO model loaded successfully.")

    @staticmethod
    def _ensure_model_directory():
        Path("models").mkdir(
            parents=True,
            exist_ok=True,
        )

    def track(self, frame):
        """
        Run YOLO detection + tracking.

        BoT-SORT is used as the tracking algorithm.
        persist=True maintains tracking IDs across frames.
        """

        results = self.model.track(
            source=frame,
            persist=True,
            tracker="botsort.yaml",
            conf=self.confidence,
            verbose=False,
        )

        return results[0]