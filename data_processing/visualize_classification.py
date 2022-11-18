import numpy as np
import laspy
import open3d as o3d

import constant_variables

def readLas(filename):
	las = laspy.read(filename)
	return np.stack([las.X, las.Y, las.Z, las.classification], axis=0).transpose(1, 0)
    

def create_classification_matrices(point_data):
    
    # Initialize a list of 19 elements; 
    # Each element is an empty matrix(list)
    # and will be used to store point cloud data of one classification
    point_cloud_matrices = []
    for key in constant_variables.LAS_CLASSIFICATION:
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
        
        color = constant_variables.CLASSIFICATION_COLORS[constant_variables.LAS_CLASSIFICATION[i]]
        
        geom.paint_uniform_color([color[0]/constant_variables.RGB, 
                                  color[1]/constant_variables.RGB, 
                                  color[2]/constant_variables.RGB])
        
        geom_list.append(geom)
    
    return geom_list


def visualize_geometry(geom_list):
    o3d.visualization.draw_geometries(geom_list)
    

def main():
    filename = "sample_data.las"
    # filename = "/Users/peinanwang/VancouverLAS/sample_data/downtownLAS/downtown.las"
    # filename = "/Users/peinanwang/VancouverLAS/merge_file/out/park.las"
    visualize_geometry(prepare_geometry(create_classification_matrices(readLas(filename))))


if __name__ == "__main__":
	main()
