# 🤖 AI Object Detection, Tracking & Voice Alert System

An AI-powered real-time object detection and tracking application developed using Python, YOLOv8, OpenCV, and BoT-SORT. The system detects objects through a webcam or video file, identifies their names, assigns tracking IDs, and announces detected objects using text-to-speech.

## ✨ Features

* 🎯 Real-time object detection using YOLOv8
* 📦 Object tracking using BoT-SORT
* 🆔 Unique tracking IDs for detected objects
* 🟩 Bounding boxes around detected objects
* 🏷️ Object names and confidence scores
* 🔊 Voice announcements of detected object names
* 📹 Webcam and video file support
* 📊 Real-time FPS display
* 💾 Option to save processed videos
* ⚙️ Configurable detection confidence
* 🧪 Automated project tests

## 🛠️ Technologies Used

| Technology   | Purpose                                   |
| ------------ | ----------------------------------------- |
| Python       | Main programming language                 |
| YOLOv8       | AI-based object detection                 |
| Ultralytics  | YOLO model and tracking integration       |
| OpenCV       | Video capture and image processing        |
| BoT-SORT     | Multi-object tracking                     |
| pyttsx3      | Text-to-speech announcements              |
| uv           | Python package and environment management |
| pytest       | Automated testing                         |
| Git & GitHub | Version control and project hosting       |

## 📁 Project Structure

```text
CodeAlpha_ObjectDetectionTracking/
│
├── main.py
│
├── detector/
│   ├── __init__.py
│   └── yolo_detector.py
│
├── tracker/
│   ├── __init__.py
│   └── object_tracker.py
│
├── voice/
│   ├── __init__.py
│   └── voice_announcer.py
│
├── utils/
│   ├── __init__.py
│   ├── video.py
│   └── visualization.py
│
├── models/
│   └── yolov8n.pt
│
├── input/
│   └── sample.mp4
│
├── output/
│   └── tracked_output.mp4
│
├── screenshots/
│   └── detection_demo.png
│
├── tests/
│   └── test_detection.py
│
├── .gitignore
├── pyproject.toml
├── uv.lock
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Setup

### 1. Install Python and uv

Install Python 3.10 or later and the `uv` package manager.

### 2. Open the project

Open the project folder in Visual Studio Code and open its terminal.

### 3. Install dependencies

```bash
uv sync
```

If dependencies have not yet been added to your project, run:

```bash
uv add ultralytics opencv-python pyttsx3 pytest
```

### 4. Run the application

Start object detection using your webcam:

```bash
uv run main.py
```

Enable voice announcements:

```bash
uv run main.py --voice
```

## 🎥 Run with a Video File

Place your video file inside the `input` folder.

Example:

```text
input/sample.mp4
```

Run detection and tracking on the video:

```bash
uv run main.py --source input/sample.mp4
```

Enable voice announcements:

```bash
uv run main.py --source input/sample.mp4 --voice
```

## 💾 Save the Processed Video

To save the annotated video in the `output` folder:

```bash
uv run main.py --voice --save
```

Output location:

```text
output/tracked_output.mp4
```

## 🎯 Adjust Detection Confidence

The default confidence threshold is `0.40`.

For a threshold of `0.50`, run:

```bash
uv run main.py --confidence 0.50
```

Higher thresholds can reduce low-confidence detections but may also miss some objects.

## 🔊 Voice Announcement System

The voice module uses `pyttsx3` to announce the names returned by the YOLO model.

Example announcements:

* "Person detected"
* "Car detected"
* "Dog detected"
* "Bottle detected"
* "Laptop detected"
* "Cell phone detected"

A cooldown mechanism helps prevent the same object class from being announced repeatedly.

**Note:** The system can identify only the object categories supported by the loaded model. Voice output also depends on the system's speech engine and installed voices.

## 🧠 How the Project Works

1. OpenCV captures a frame from the webcam or video file.
2. YOLOv8 processes the frame and detects objects.
3. BoT-SORT tracks objects across consecutive frames.
4. The application displays bounding boxes, object names, confidence scores, and tracking IDs.
5. The voice module announces detected object names when voice mode is enabled.
6. OpenCV displays the processed video.
7. Optionally, the application saves the annotated video.

### Architecture

```text
Webcam / Video File
        |
        v
   OpenCV Capture
        |
        v
   YOLOv8 Detection
        |
        v
  BoT-SORT Tracking
        |
        v
  Object Names + IDs
        |
        +-------------------+
        |                   |
        v                   v
 Visualization         Voice Announcer
        |                   |
        v                   v
 Bounding Boxes       Text-to-Speech
        |                   |
        +---------+---------+
                  |
                  v
          Final Live Output
```

## 🧪 Run Tests

Execute the automated tests:

```bash
uv run pytest
```

## ⌨️ Controls

| Key | Action               |
| --- | -------------------- |
| `Q` | Exit the application |

## 📸 Screenshots and Demo

Add screenshots of the working application to the `screenshots/` directory.

Example:

```markdown
![Object Detection Demo](screenshots/detection_demo.png)
```

You can also record a short demonstration showing the webcam detection, tracking IDs, and voice announcements.

## 🎓 CodeAlpha Internship

**Domain:** Artificial Intelligence

**Task:** Task 4 — Object Detection and Tracking

This project implements the core task requirements and adds voice announcements as an additional feature.

## 🚀 Future Improvements

* Support for additional detection models
* Better voice announcement prioritization
* User interface for webcam and video selection
* Configurable voice language and speech rate
* Object counting and tracking statistics
* Performance optimization for real-time processing

## 👨‍💻 Author

**Name:** Your Name

**GitHub:** Your GitHub Profile URL

**LinkedIn:** Your LinkedIn Profile URL

---

*Developed as an Artificial Intelligence internship project for CodeAlpha.*
