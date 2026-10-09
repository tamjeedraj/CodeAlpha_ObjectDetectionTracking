from pathlib import Path


def test_project_directories_exist():

    required_directories = [
        "detector",
        "tracker",
        "voice",
        "utils",
        "models",
        "input",
        "output",
        "screenshots",
        "tests",
    ]

    for directory in required_directories:

        assert Path(directory).exists()


def test_required_files_exist():

    required_files = [
        "main.py",
        "detector/yolo_detector.py",
        "tracker/object_tracker.py",
        "voice/voice_announcer.py",
        "utils/video.py",
        "utils/visualization.py",
    ]

    for file in required_files:

        assert Path(file).exists()