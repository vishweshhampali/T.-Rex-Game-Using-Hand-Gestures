# T.-Rex-Game-Using-Hand-Gestures
The code implements a real-time object detection algorithm to simulate jumps in Google Chrome's T-Rex game. Here's a breakdown of the key steps:

1. Region of Interest (ROI) and Preprocessing:</br>
It captures a live video feed and focuses on a specific region where cacti appear (likely the bottom third of the screen).
The image is blurred to reduce noise and converted to HSV color space, making object detection easier.

2. Cacti Detection:</br>
A color mask is created by filtering for a defined range of HSV values that correspond to the color of cacti.
This mask is binarized and processed to enhance the shapes of potential cacti.

3. Finding the Largest Cacti:</br>
The algorithm identifies all contours (outlines of objects) in the processed image.
It iterates through these contours and finds the one with the largest area, which is likely the closest and most threatening cactus.

4. Jump Trigger:</br>
If the area of the largest contour exceeds a predefined threshold (indicating a large and imminent cactus), the code simulates a jump action by pressing the space key using the pyautogui library.

5. Feedback and Visualization:</br>
The code displays the original video feed with a bounding box around the detected cactus for visualization.
It also prints messages like "JUMP" when a jump is triggered.
Overall, the algorithm follows a classic object detection approach. It isolates a relevant region, filters for specific object colors, identifies the most prominent object, and triggers an action based on its size. This allows the code to automate jumps in the T-Rex game, reacting to approaching cacti before a collision occurs.
