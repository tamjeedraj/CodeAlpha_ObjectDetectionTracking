class ObjectTracker:
    """
    Handles object detection and tracking using the YOLO detector.
    Extracts actual detected object names for voice announcements.
    """

    def __init__(self, detector):
        self.detector = detector

    def process(self, frame):
        """Detect and track objects in the given frame."""
        return self.detector.track(frame)

    def get_detected_object_names(self, result):
        """Return unique, normalized object names detected in the frame."""

        object_names = set()

        if result is None or result.boxes is None:
            return object_names

        for box in result.boxes:
            try:
                class_id = int(box.cls[0].item())
                object_name = result.names.get(
                    class_id,
                    str(class_id),
                )

                object_name = str(object_name).strip().lower()

                if object_name:
                    object_names.add(object_name)

            except (AttributeError, IndexError, TypeError, ValueError):
                continue

        return object_names