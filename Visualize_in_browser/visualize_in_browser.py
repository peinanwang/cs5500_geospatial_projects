import open3d as o3d
import laspy
import numpy as np
import constant_variables


def visualize_in_browser():
    o3d.visualization.webrtc_server.enable_webrtc()

    las = laspy.read("sample_data.las")
    
    point_data = np.stack([las.X, las.Y, las.Z, las.classification], axis=0).transpose(1, 0)
    
    point_coordinates = []
    point_colors = []
    
    for i in range(len(point_data)):
        
        x = point_data[i][0]
        y = point_data[i][1]
        z = point_data[i][2]
        classification = point_data[i][3]
        
        feature_type = constant_variables.LAS_CLASSIFICATION[classification]
        color = constant_variables.CLASSIFICATION_COLORS[feature_type]
        
        point_colors.append([color[0]/constant_variables.RGB, 
                             color[1]/constant_variables.RGB, 
                             color[2]/constant_variables.RGB])
        
        point_coordinates.append([x, y, z])
    
    
    geom = o3d.geometry.PointCloud()
    
    geom.points = o3d.utility.Vector3dVector(point_coordinates)
    geom.colors = o3d.utility.Vector3dVector(point_colors)
    
    o3d.visualization.draw(geom)
    
    
    # Code below is the example provided in Open3d Doc -- Rendering a cube
  
    # cube_red = o3d.geometry.TriangleMesh.create_box(1, 2, 4)
    # cube_red.compute_vertex_normals()
    # cube_red.paint_uniform_color((1.0, 0.0, 0.0))
    
    # o3d.visualization.draw(cube_red)

visualize_in_browser()