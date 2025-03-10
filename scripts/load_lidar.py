import numpy as np 
import open3d as o3d

# Load LiDAR data
lidar = np.fromfile('../data/training/velodyne/000000.bin', dtype=np.float32).reshape(-1, 4)

# Create Open3D point cloud
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(lidar[:,:3])

# Visualize the LiDAR data
o3d.visualization.draw_geometries([pcd])

