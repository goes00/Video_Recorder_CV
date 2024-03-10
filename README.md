# Video_Recorder_CV
Simple video recorder using OpenCV

# Functions
1. You can record video with space.
     Default mode is Preview mode. You can switch mode to Record mode. Record -> Preview switching is also available.
   
     Recording... is printed when Recorder is Recording mode.
     ![image](https://github.com/goes00/Video_Recorder_CV/assets/144883897/5eb330a0-5675-4fd6-b623-cf9b47bc3869)

2. You can choose FPS.
     (,)key sets your Preview mode's FPS and Record mode's FPS as 30(default).
   
     (.)key sets your Preview mode's FPS and Record mode's FPS as 60.
   
   **!!CAUTION!!** Recorded video has the FPS when Record starts. Even if you change the FPS while recording, the FPS of recorded video will *NOT* change but when you switch FPS again, video will be cut the gap of 30FPS and 60FPS.
3. To exit this recorder, press ESC to exit.
4. Camera's default address is CCTV, but you can change to your webcam or something else.
5. Codec is XVID. Output video is recorded with AVI.

Sample image:
![image](https://github.com/goes00/Video_Recorder_CV/assets/144883897/e9445e57-9f40-4a53-819b-9ceb06765733)
