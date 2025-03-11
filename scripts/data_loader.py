import os
import cv2
import numpy as np 
import open3d as o3d 
from scripts.config import IMG_DIR, LIDAR_DIR

def load_image(idx):
    img_path = os.path.join(IMG_DIR, f"{idx:06d}.png")
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

def load_lidar(idx):
    lidar_path = os.path.join(LIDAR_DIR, f"{idx:06d}.bin")
    points = np.fromfile(lidar_path, dtype=np.float32).reshape(-1, 4)
    return points

def load_point_cloud(idx):
    points = load_lidar(idx)
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points[:, :3])
    return pcd
