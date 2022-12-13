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

RGB = 255

FRAME_SIZE = 1080

'''
LAS_Processor class is used to process the LAS file, generate a point cloud, create a 2D image, and 3D rendering
'''
class LAS_Processor:
    
    def __init__(self, file_path):
        
        self.__file_path = file_path
        self.__point_cloud_matrices = []
        self.__point_stats = {}
        self.__geom_list = []
        
    '''
    This method will iterate through the points to 
    1) create a list of matrices for each classification
    2) update the point statistics (i.e. number of points of each classification)
    '''
    def process(self):
        
        las = laspy.read(self.__file_path)
        point_data = np.stack([las.X, las.Y, las.Z, las.classification], axis=0).transpose(1, 0)
        
        # Initialize a list of 19 elements; 
        # Each element is an empty matrix(list)
        # and will be used to store point cloud data of one classification
       
        for classification in LAS_CLASSIFICATION:
            self.__point_cloud_matrices.append([])
            self.__point_stats[classification] = 0
            
        for point in point_data:
            i = point[3] # the classification code (0 - 18)
          
            # add an array of XYZ coordinates to the i-th matrix 
            self.__point_cloud_matrices[i].append([point[0], point[1], point[2]])
            
            # incrememnt the number of points of the classification code i
            self.__point_stats[i] += 1
               
        
    def prepare_geometry(self):
        
        point_cloud_matrices = self.__point_cloud_matrices
        
        # Assign color value each geometry object and add it to the list
        for i in range(len(point_cloud_matrices)):
            
            geom = o3d.geometry.PointCloud()
            
            geom.points = o3d.utility.Vector3dVector(point_cloud_matrices[i])
            
            color = CLASSIFICATION_COLORS[LAS_CLASSIFICATION[i]]
            
            geom.paint_uniform_color([color[0]/RGB, 
                                      color[1]/RGB, 
                                      color[2]/RGB])
            
            self.__geom_list.append(geom)


    def get_point_statistics(self):
        
        return self.__point_stats
    

    def output_image(self):
        
        # Initialze a Visualizer object
        vis = o3d.visualization.Visualizer()
        # Create a window for the Visualizer object and set it to be invisible
        vis.create_window(width=FRAME_SIZE, height=FRAME_SIZE, visible=False)
        
        # Add geometry objects to the Visualizer object
        for geom in self.__geom_list:
            vis.add_geometry(geom)
            vis.update_geometry(geom)  
        
        # Update the Visualizer object
        vis.poll_events()
        vis.update_renderer()
        
        # Save the image to a file
        vis.capture_screen_image('./static/images/img.png')
        print("Image saved to ./static/images/img.png")
        
        # Close the window
        vis.destroy_window()
    

    def visualize(self):
    
        # webrtc_server.enable_webrtc() DOES NOT work on Apple M1/M2 chips
        # When runnning view.py on M1/M2 macbooks or any other ARM devices, 
        # please comment out the following line. 
        # By doing so, the 3D rendering will be displayed in a seperated window
        # instead of a web browser.
        o3d.visualization.webrtc_server.enable_webrtc()
        
        o3d.visualization.draw(self.__geom_list)


if __name__ == "__main__":
    file_path = './static/files/' + sys.argv[1]
    las_processor = LAS_Processor(file_path)
    las_processor.process()   
    las_processor.prepare_geometry()
    las_processor.output_image()
    las_processor.visualize()