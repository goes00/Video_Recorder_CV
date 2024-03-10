import cv2

class VideoRecorder:
    def __init__(self, camera_url, output_file, preview_fps=30, record_fps=30):
        self.camera_url = camera_url
        self.output_file = output_file
        self.preview_fps = preview_fps
        self.record_fps = record_fps
        self.is_preview_mode = True
        self.capture = cv2.VideoCapture(self.camera_url)
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.out = None
        self.is_recording = False

    def start_preview(self):
        while True:
            ret, frame = self.capture.read()
            if not ret:
                print("Error reading frame")
                break
            
            if self.is_recording:
                self.out.write(frame)
                cv2.putText(frame, "Recording...", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            cv2.imshow('Preview', frame)

            key = cv2.waitKey(1000 // self.preview_fps)
            if key == 27:  # ESC key to exit
                break
            elif key == 32:  # Space key to toggle mode
                self.toggle_mode()
            elif key == 44: # Comma(,) key to set FPS as 30(default).
                self.preview_fps = 30
                self.record_fps = 30 # !!WARNING!! Video is recorded of FPS when recording starts.
            elif key == 46: # Period(.) key to set FPS as 60.
                self.preview_fps = 60
                self.record_fps = 60
            

        self.capture.release()
        if self.is_recording:
            self.out.release()
        cv2.destroyAllWindows()

    def start_recording(self):
        self.out = cv2.VideoWriter(self.output_file, self.fourcc, self.record_fps, (int(self.capture.get(3)), int(self.capture.get(4))))
        self.is_recording = True

    def stop_recording(self):
        self.is_recording = False
        self.out.release()

    def toggle_mode(self):
        if self.is_preview_mode:
            self.is_preview_mode = False
            self.start_recording()
        else:
            self.is_preview_mode = True
            self.stop_recording()
    


if __name__ == "__main__":
    camera_url = 'rtsp://210.99.70.120:1935/live/cctv001.stream'
    output_file = 'output.avi'

    recorder = VideoRecorder(camera_url, output_file)
    recorder.start_preview()
