import os

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
TRAINING_DIR = os.path.join(DATA_DIR, 'training')
IMG_DIR = os.path.join(TRAINING_DIR,'image_2')
LIDAR_DIR = os.path.join(TRAINING_DIR, 'velodyne_points')
CALIB_DIR = os.path.join(TRAINING_DIR, 'calib')

# Visualization settings
POINT_SIZE = 2