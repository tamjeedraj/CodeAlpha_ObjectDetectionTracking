import cv2


def draw_detections(frame, result):

    if result.boxes is None:
        return frame

    boxes = result.boxes

    names = result.names

    for box in boxes:

        # -------------------------------------------------
        # Coordinates
        # -------------------------------------------------

        x1, y1, x2, y2 = map(
            int,
            box.xyxy[0].tolist(),
        )

        # -------------------------------------------------
        # Class
        # -------------------------------------------------

        class_id = int(
            box.cls[0].item()
        )

        object_name = names[class_id]

        # -------------------------------------------------
        # Confidence
        # -------------------------------------------------

        confidence = float(
            box.conf[0].item()
        )

        # -------------------------------------------------
        # Tracking ID
        # -------------------------------------------------

        track_id = None

        if box.id is not None:

            track_id = int(
                box.id[0].item()
            )

        # -------------------------------------------------
        # Color
        # -------------------------------------------------

        color = (
            0,
            255,
            0,
        )

        # -------------------------------------------------
        # Bounding box
        # -------------------------------------------------

        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            color,
            2,
        )

        # -------------------------------------------------
        # Label
        # -------------------------------------------------

        if track_id is not None:

            label = (
                f"{object_name} "
                f"ID:{track_id} "
                f"{confidence:.0%}"
            )

        else:

            label = (
                f"{object_name} "
                f"{confidence:.0%}"
            )

        # -------------------------------------------------
        # Text dimensions
        # -------------------------------------------------

        (
            text_width,
            text_height,
        ), _ = cv2.getTextSize(
            label,
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            2,
        )

        # -------------------------------------------------
        # Text background
        # -------------------------------------------------

        cv2.rectangle(
            frame,
            (x1, y1 - text_height - 10),
            (
                x1 + text_width,
                y1,
            ),
            color,
            -1,
        )

        # -------------------------------------------------
        # Text
        # -------------------------------------------------

        cv2.putText(
            frame,
            label,
            (
                x1,
                y1 - 5,
            ),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 0, 0),
            2,
        )

    return frame


def draw_fps(frame, fps):

    text = f"FPS: {fps:.1f}"

    cv2.putText(
        frame,
        text,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 255),
        2,
    )

    return frame


def draw_status(frame, status):

    text = f"Voice: {status}"

    cv2.putText(
        frame,
        text,
        (20, 75),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.65,
        (255, 255, 0),
        2,
    )

    return frame