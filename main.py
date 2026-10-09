import argparse
import time

import cv2

from detector.yolo_detector import YOLODetector
from tracker.object_tracker import ObjectTracker
from utils.video import VideoManager
from utils.visualization import draw_detections, draw_fps, draw_status
from voice.voice_announcer import VoiceAnnouncer


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="AI Object Detection, Tracking & Voice Alert System"
    )

    parser.add_argument(
        "--source",
        default="0",
        help="Video source: 0 for webcam or path to video file",
    )

    parser.add_argument(
        "--model",
        default="models/yolov8n.pt",
        help="Path to YOLO model",
    )

    parser.add_argument(
        "--confidence",
        type=float,
        default=0.40,
        help="Minimum detection confidence",
    )

    parser.add_argument(
        "--voice",
        action="store_true",
        help="Enable voice announcements",
    )

    parser.add_argument(
        "--save",
        action="store_true",
        help="Save processed video",
    )

    return parser.parse_args()


def main():
    args = parse_arguments()

    # ---------------------------------------------------------
    # Video source
    # ---------------------------------------------------------

    source = int(args.source) if args.source.isdigit() else args.source

    video = VideoManager(
        source=source,
        save_output=args.save,
    )

    if not video.open():
        print("❌ Could not open video source.")
        return

    # ---------------------------------------------------------
    # YOLO detector
    # ---------------------------------------------------------

    detector = YOLODetector(
        model_path=args.model,
        confidence=args.confidence,
    )

    # ---------------------------------------------------------
    # Object tracker
    # ---------------------------------------------------------

    tracker = ObjectTracker(detector)

    # ---------------------------------------------------------
    # Voice system
    # ---------------------------------------------------------

    announcer = None

    if args.voice:
        announcer = VoiceAnnouncer(
            cooldown=5
        )

    # ---------------------------------------------------------
    # FPS
    # ---------------------------------------------------------

    previous_time = time.time()

    print("=" * 60)
    print("AI OBJECT DETECTION, TRACKING & VOICE ALERT SYSTEM")
    print("=" * 60)
    print(f"Source       : {source}")
    print(f"Confidence   : {args.confidence}")
    print(f"Voice        : {'Enabled' if args.voice else 'Disabled'}")
    print(f"Save output  : {'Enabled' if args.save else 'Disabled'}")
    print("=" * 60)
    print("Press Q to quit.")

    try:

        while True:

            # -------------------------------------------------
            # Read frame
            # -------------------------------------------------

            success, frame = video.read()

            if not success:
                print("Video ended or frame could not be read.")
                break

            # -------------------------------------------------
            # Detection + Tracking
            # -------------------------------------------------

            result = tracker.process(frame)

            # -------------------------------------------------
            # Voice announcement
            # -------------------------------------------------

            if announcer is not None:

                detected_objects = tracker.get_detected_object_names(
                    result
                )

                for object_name in detected_objects:
                    announcer.announce(object_name)

            # -------------------------------------------------
            # Draw detections
            # -------------------------------------------------

            frame = draw_detections(
                frame,
                result,
            )

            # -------------------------------------------------
            # FPS calculation
            # -------------------------------------------------

            current_time = time.time()

            elapsed = current_time - previous_time

            fps = 1.0 / max(elapsed, 0.001)

            previous_time = current_time

            frame = draw_fps(
                frame,
                fps,
            )

            # -------------------------------------------------
            # Status
            # -------------------------------------------------

            status = "VOICE ON" if announcer else "VOICE OFF"

            frame = draw_status(
                frame,
                status,
            )

            # -------------------------------------------------
            # Save frame
            # -------------------------------------------------

            video.write(frame)

            # -------------------------------------------------
            # Display
            # -------------------------------------------------

            cv2.imshow(
                "CodeAlpha - Object Detection & Tracking",
                frame,
            )

            # -------------------------------------------------
            # Quit
            # -------------------------------------------------

            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):
                break

    except KeyboardInterrupt:
        print("\nApplication interrupted.")

    finally:

        video.release()

        if announcer is not None:
            announcer.stop()

        print("Application closed successfully.")


if __name__ == "__main__":
    main()