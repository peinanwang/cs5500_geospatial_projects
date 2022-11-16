# Geospatial Data Visualization

### Project Overview
This is a project for Northeastern University's CS5500 - Foundations of Software Engineering. We are building a web application for to visualize point cloud data. Users can update point cloud data (limited to .las file format) and they will be able to see point cloud information and 3d renderings. 

Currently, the point cloud data type is limited to .las format, and the LAS file need to be classfied following the LAS classification standards:

0. Never Classified
1. Unassigned
2. Ground
3. Low Vegetation
4. Medium Vegetation
5. High Vegetation
6. Building
7. Noise
8. Model Key/Reserved
9. Water
10. Rail
11. Road Surface
12. Overlap/Reserved
13. Wire - Guard
14. Wire - Conductor
15. Transmission Tower
16. Wire - Connector
17. Bridge Deck
18. High Noise

Please visit our <a href="https://peinanwang.github.io/Geospatial_Project_Blog/index.html">project blog</a> for more information. 

### User Stories

As an urban planner, I want to have a 3D view of the city, including features like roads, parks, buildings, etc. So I can make better decisions on city planning. After uploading the Lidar point cloud, a 3D rendering will be generated in the user interface. It supports basic functionalities like click and drag, zoom in and zoom out, so I can use it to show my design idea.

If the point cloud data that I have are already classified, each class will be colored differently. My main focus is to tell:
- How much of the area is occupied by man-made structure/development (e.g. buildings, roads, bridge)
- Where are all the vegetation features located (e.g. grass, shrubs, trees)
- A clear display of the road systems
- A clear display of the powerline infrastructure (e.g. power tower, distribution line). This is an important factor to consider when I make urban development plan.

As an architect, I want to access various kinds of information when I crop a certain area of land. The information includes building coverage ratio, residential density, and afforested area. With the help of terrestrial equipment, I can also have a view of infrastructure and population, so that I can make a more elaborate analysis on site research and present more convincing data for my project.

As a civil engineer, I want regional distribution and topographic maps to help me with road planning. In the map, I need the distribution of existing buildings and roads. Also, the areas of farmlands, rivers and forests are also important. Besides these, I need the map of topography including altitude information to help me design.

### Contributors
- Yuhao Hua - Backend development using Python Flask
- Peinan Wang - Point cloud data processing and backend development 
- Luocheng Zhu - Frontend development


### User Interface and Workflow Design

1. Select file (restricted on file type)

2. Click the "Submit" button to submit file

3. Once a file is submitted successfully, some message will be displayed; point cloud data information will be displayed in the table. Step 4) - 6) will be disabled until the file is uploaded and saved successfully. 

4. Click the "Visualize" button to start the visualization process. (The visualization script is running on the backend. A progress bar will be added to track the process). Step 5) will be disabled until the visualization is ready. 

5. Click the "To see the rendering" link to see the visualization rendering. Users will be directed to localhost:8888 to see the open3d webrtc window. 

6. Click the "Stop Current Visualization" button to terminate the running visualization scripts. 

Step 4) - 6) will be a "loop". We can click the "Visualize" button ONLY when there is NO visualization script running.


<img width="1137" alt="Screen Shot 2022-11-15 at 5 07 04 PM" src="https://user-images.githubusercontent.com/105306727/202061678-61d002cd-db3a-4371-acf7-4bd3d4b1fff6.png">
<img width="1308" alt="Screen Shot 2022-11-08 at 5 37 28 PM" src="https://user-images.githubusercontent.com/105306727/202061726-53dae4c4-c021-47bd-a745-1fe2416b1b9c.png">





