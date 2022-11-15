import open3d as o3d
import laspy
import numpy as np
import sys

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

def readLas(file_path):
	las = laspy.read(file_path)
	return np.stack([las.X, las.Y, las.Z, las.classification], axis=0).transpose(1, 0)
    

def create_classification_matrices(point_data):
    
    # Initialize a list of 19 elements; 
    # Each element is an empty matrix(list)
    # and will be used to store point cloud data of one classification
    point_cloud_matrices = []
    for key in LAS_CLASSIFICATION:
        point_cloud_matrices.append([])

    for point in point_data:
        i = point[3] # the classification code (0 - 18)
        
        # add an array of XYZ coordinates to the i-th matrix 
        point_cloud_matrices[i].append([point[0], point[1], point[2]])
        
    return point_cloud_matrices


def prepare_geometry(point_cloud_matrices):
    
    # Initialize an empty list for open3d geometry objects 
    geom_list = []
    
    # Assign color value each geometry object and add it to the list
    for i in range(len(point_cloud_matrices)):
        
        geom = o3d.geometry.PointCloud()
        
        geom.points = o3d.utility.Vector3dVector(point_cloud_matrices[i])
        
        color = CLASSIFICATION_COLORS[LAS_CLASSIFICATION[i]]
        
        geom.paint_uniform_color([color[0]/RGB, 
                                  color[1]/RGB, 
                                  color[2]/RGB])
        
        geom_list.append(geom)
    
    return geom_list


def visualize_in_browser(file_path):
    o3d.visualization.webrtc_server.enable_webrtc()
    geom_list = prepare_geometry(create_classification_matrices(readLas(file_path)))
    o3d.visualization.draw(geom_list)


if __name__ == "__main__":
    file_path = './static/files/' + sys.argv[1]
    visualize_in_browser(file_path)