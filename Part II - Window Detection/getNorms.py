import open3d as o3d
#输入点云
pcd = o3d.io.read_point_cloud("pointcloud/dby/dongbeiya_1024 - Cloud.ply")
# pcd = o3d.io.read_point_cloud("pointcloud/gym/gym_1024 - Cloud.ply")
print(pcd)
pcd.estimate_normals(
    search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.01, max_nn=100))
# o3d.io.write_point_cloud('normed_gym.ply',pcd,print_progress=True)
o3d.io.write_point_cloud('pointcloud/dby/normed_dby.ply',pcd,print_progress=True)
