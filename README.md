# Pull-Ups-Counter
🏋️ Pull-Up Counter Using Python + OpenCV

A real-time pull-up counting system built using Python, OpenCV, and a Deep Learning pose estimation model.
The program detects your body joints using the OpenPose DNN model and counts pull-ups by tracking elbow angles.

🚀 Features

🎥 Real-time camera tracking

🤖 OpenPose-based body keypoint detection

📐 Elbow-angle based pull-up detection

🔢 Automatic repetition counter

💻 Easy to run in VS Code

📦 Installation

Install the required libraries:

pip install opencv-python numpy

📁 Required Model Files

Download these two files and place them in your project folder:

pose_deploy_linevec.prototxt

pose_iter_584000.caffemodel

Download:
👉 https://github.com/CMU-Perceptual-Computing-Lab/openpose_models

Your folder should look like:

pullup_project/
    pullup_counter.py
    pose_deploy_linevec.prototxt
    pose_iter_584000.caffemodel

▶️ How to Run
python pullup_counter.py


Press Q to exit.

🧠 How It Works

Opens your webcam

Detects shoulder, elbow, and wrist keypoints

Calculates elbow angle

Detects down → up motion

Counts 1 pull-up per cycle

🛠 Tech Stack

Python

OpenCV

NumPy

OpenPose DNN (Caffe Model)

🎯 Future Improvements

Add voice feedback

Accuracy improvements

Add GUI interface

Save workout stats

⭐ Support

If you like this project, consider giving it a ⭐ star on GitHub.

If you want, I can also make:

A short GIF demo

A project banner

Better formatting with badges
