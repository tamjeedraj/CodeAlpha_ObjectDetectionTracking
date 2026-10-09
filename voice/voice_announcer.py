import queue
import threading
import time

import pyttsx3


class VoiceAnnouncer:
    """Announce the actual detected object name using Windows TTS."""

    def __init__(self, cooldown=4.0):
        self.cooldown = cooldown
        self.last_announced = {}
        self.speech_queue = queue.Queue()
        self.running = True

        self.worker = threading.Thread(
            target=self._speech_worker,
            daemon=True,
        )
        self.worker.start()

    def _speech_worker(self):
        engine = None

        try:
            engine = pyttsx3.init("sapi5")
            engine.setProperty("rate", 165)
            engine.setProperty("volume", 1.0)

            voices = engine.getProperty("voices")

            if voices:
                selected_voice = next(
                    (
                        voice for voice in voices
                        if "english" in voice.name.lower()
                    ),
                    voices[0],
                )
                engine.setProperty("voice", selected_voice.id)

            while True:
                message = self.speech_queue.get()

                try:
                    if message is None:
                        break

                    print(f"🔊 Speaking: {message}")
                    engine.say(message)
                    engine.runAndWait()

                except Exception as error:
                    print(f"❌ Voice error: {error}")

                finally:
                    self.speech_queue.task_done()

        except Exception as error:
            print(f"❌ Could not initialize voice engine: {error}")

        finally:
            if engine is not None:
                try:
                    engine.stop()
                except Exception:
                    pass

    def announce(self, object_name):
        if not self.running or not object_name:
            return

        object_name = str(object_name).strip().lower()
        current_time = time.time()

        last_time = self.last_announced.get(object_name, 0)

        if current_time - last_time < self.cooldown:
            return

        self.last_announced[object_name] = current_time

        message = f"{object_name} detected"

        print(f"🎯 Detected: {object_name}")
        self.speech_queue.put(message)

    def stop(self):
        if self.running:
            self.running = False
            self.speech_queue.put(None)