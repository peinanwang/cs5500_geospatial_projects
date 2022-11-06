import open3d as o3d
import laspy
import numpy as np

'''
Detail for LAS classification code can be found at:
https://desktop.arcgis.com/en/arcmap/10.3/manage-data/las-dataset/lidar-point-classification.htm

Code 8 and 12 will not be used for this project
'''

LAS_CLASSIFICATION = {0 : "Never Classified", 
                      1 : "Unassigned",
                      2 : "Ground",
                      3 : "Low Vegetation",
                      4 : "Medium Vegetation",
                      5 : "High Vegetation", 
                      6 : "Building",
                      7 : "Noise",
                      8 : "Model Key/Reserved", 
                      9 : "Water", 
                      10: "Rail",
                      11: "Road Surface",
                      12: "Overlap/Reserved",
                      13: "Wire - Guard", 
                      14: "Wire - Conductor", 
                      15: "Transmission Tower",
                      16: "Wire - Connector", 
                      17: "Bridge Deck", 
                      18: "High Noise"}

CLASSIFICATION_COLORS = {"Never Classified" : [204, 255, 255],# light blue
                         "Unassigned" : [255, 204, 255],      # light pink
                         "Ground" : [204, 153, 0],            # light brown
                         "Low Vegetation" : [153, 255, 51],   # light green
                         "Medium Vegetation" : [51, 204, 51], # green
                         "High Vegetation" : [51, 153, 51],   # dark green
                         "Building" : [255, 102, 0],          # orange
                         "Noise" : [255, 255, 204],           # light yellow (almost white)
                         "Model Key/Reserved" : [51, 51, 0],  # dark green (almost black)       
                         "Water" : [0, 102, 255],             # blue
                         "Rail" : [0, 0, 102],                # dark blue
                         "Road Surface" : [102, 102, 153],    # dark grey
                         "Overlap/Reserved" : [51, 51, 0],    # dark green (almost black)  
                         "Wire - Guard" : [204, 0, 204],      # purple
                         "Wire - Conductor" : [204, 0, 204],  # purple
                         "Transmission Tower" : [204, 0, 204],# purple
                         "Wire - Connector" : [204, 0, 204],  # purple
                         "Bridge Deck" : [255, 0, 0],         # red
                         "High Noise" : [255, 255, 204]       # light yellow (almost white)
                        }

NATURAL_FEATURES = [3, 4, 5]

POWERLINES = [13, 14, 16]

UNNATURAL_STRUCTURES = [6, 11, 17]

RGB = 255



def visualize_in_browser(filename):
    o3d.visualization.webrtc_server.enable_webrtc()

    las = laspy.read('./static/files/' + filename)
    #las = laspy.read(filename)
    
    point_data = np.stack([las.X, las.Y, las.Z, las.classification], axis=0).transpose(1, 0)
    
    point_coordinates = []
    point_colors = []
    
    for i in range(len(point_data)):
        
        x = point_data[i][0]
        y = point_data[i][1]
        z = point_data[i][2]
        classification = point_data[i][3]
        
        feature_type = LAS_CLASSIFICATION[classification]
        color = CLASSIFICATION_COLORS[feature_type]
        
        point_colors.append([color[0]/RGB, 
                             color[1]/RGB, 
                             color[2]/RGB])
        
        point_coordinates.append([x, y, z])
    
    
    
    ############
    
    print("\n")
    print(f"number of points: {len(point_data)}")
    print(f"number of coordinates: {len(point_coordinates)}")
    print("\n")
    
    ############
    
    
    geom = o3d.geometry.PointCloud()
    
    geom.points = o3d.utility.Vector3dVector(point_coordinates)
    geom.colors = o3d.utility.Vector3dVector(point_colors)
    
    o3d.visualization.draw(geom)
    
    
    # Code below is the example provided in Open3d Doc -- Rendering a cube
  
    # cube_red = o3d.geometry.TriangleMesh.create_box(1, 2, 4)
    # cube_red.compute_vertex_normals()
    # cube_red.paint_uniform_color((1.0, 0.0, 0.0))
    
    # o3d.visualization.draw(cube_red)
