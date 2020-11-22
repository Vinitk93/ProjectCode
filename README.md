# SMILE DETECTION

Architecture


1. The library used is open cv.

2. There are 2 classifiers used, one for frontal face and another for smile detection. The classifiers are directly installed from Github.

3. The method used is VideoCapture to read the current frame from webcam video stream.

4. The picture is then converted to Grayscale image. The reason behind this is only 1 channel is used instead of 4 which makes it faster.

5. The face is detected using the 1st classifier i.e. frontal face.

6. In order to detect smile, the detected face in Step 5 is converted to Rectangular structure and later second classifier is applied i.e. smile.

7. The Cleanup method are applied in the end to clear all the windows after use.
