import open3d as o3d
import laspy
import numpy as np

def visualize_in_browser():
    o3d.visualization.webrtc_server.enable_webrtc()

    las = laspy.read("sample_data.las")
    data = np.stack([las.X, las.Y, las.Z], axis=0).transpose(1, 0)
    geom = o3d.geometry.PointCloud()
    
    geom.points = o3d.utility.Vector3dVector(data)
    geom.paint_uniform_color([0,0.55,0])
    # geom.color = o3d.utility.Vector3dVector(np.array())
    
    o3d.visualization.draw(geom)
    
    # cube_red = o3d.geometry.TriangleMesh.create_box(1, 2, 4)
    # cube_red.compute_vertex_normals()
    # cube_red.paint_uniform_color((1.0, 0.0, 0.0))
    
    # o3d.visualization.draw(cube_red)

visualize_in_browser()





