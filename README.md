# RealTime Pose Estimation on Jetson Nano device

1. Follow the steps on [Get Started With Jetson Nano Developer Kit](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit) 

2. Install Python 3.8 from [Download Python](https://www.python.org/downloads/)

3. Install needed python packages:
```bash
pip install opencv-python==4.8.0.76
pip install mediapipe==0.10.3
```

4. Clone jetson-pose repository
```bash
git clone https://github.com/santiaznarez/jetson-pose.git
```

5. Run the following code to start estimating the pose on real-time with your webcam as input
```bash
cd jetson-pose
python3 pose_estimation.py
```

6. Otherwise, you can use the jupyter notebook **pose_estimation.ipynb** to run the code step by step.

## While being connected by SSH to the Jetson Nano

1. If you want to run the pose estimation script while accesing to the jetson nano by SSH you need to access with the *-X* flag.
```bash
ssh -X user@jetson_ip_address
```

2. Follow the step 3, 4 and 5 from the above section. Running openCV from the notebook wont work while being connected through SSH.


