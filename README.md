<a name="readme-top"></a>
[![Contributors][contributors-shield]][contributors-url] [![Forks][forks-shield]][fork-url]


# Visualizations of Citywide LiDAR Dataset Using Open3D

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#contributors">Contributors</a>
    </li>
    <li>
      <a href="#project-overview">Project Overview</a>
    </li>
    <li><a href="#user-stories">User Stories</a></li>
    <li>
      <a href="#minimum-viable-products">Minimum Viable Products</a>
      <ul>
        <li><a href="#user-interface-and-workflow-design">User Interface and Workflow Design</a></li>
        <li><a href="#sample-results">Sample Results</a></li>
        <li><a href="#limitations">Limitations</a></li>
        <li><a href="#useful-python-scripts">Useful Python Scripts</a></li>
      </ul>
    </li>    
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li>
      <a href="#future-works">Future Works</a>
    </li>
  </ol>
</details>

## Contributors
Peinan Wang <a href='https://www.linkedin.com/in/patrick-peinan-wang-3809158a/'>(LinkedIn)</a>:     Backend Development; Point Cloud Visualization 

Yuhao Hua <a href='https://www.linkedin.com/in/yuhao-glenn-hua-892377174/'>(LinkedIn)</a>:     Backend Development; Unit Testing

Luocheng Zhu <a href='https://www.linkedin.com/in/luocheng-zhu-018aa125a/'>(LinkedIn)</a>:     Frontend Development

## Project Overview
This is a team project for Northeastern University's <b>CS 5500 - Foundations of Software Engineering</b>. 

Many professionals, such as urban planners, civil engineers, and environmental consultants, use geospatial information (e.g., building locations, terrain, vegetation, etc.) to make decisions. It is not always easy to obtain such information directly from online resources like Google Maps, especially when the site of interest is in a rural area or suburban. As a result, LiDAR (Light Detection and Ranging) technology has been widely used in the industry for geospatial data collection. In this project, we will build a web application to visualize and analyze LiDAR point cloud data. After uploading the point cloud data, users will be able to: 

- See the 2D visualization of the point cloud data; 
- See the 3D visualization of the area in an interactive mode;
- Check coverage and distribution of different features. 
 
Please visit our <a href="https://peinanwang.github.io/Geospatial_Project_Blog/index.html">Project Blog</a> for the demo video and more details regarding the project's progress.
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## User Stories

As an <em><b>urban planner</b></em>, I want to have a 3D view of the city, including features like roads, parks, buildings, etc. So I can make better decisions on city planning. After uploading the Lidar point cloud, a 3D rendering will be generated in the user interface. It supports basic functionalities like click and drag, zoom-in and zoom-out, so I can use it to show my design idea.

If the point cloud data that I have are already classified, each class will be colored differently. My main focus is to tell:
- How much of the area is occupied by man-made structures/development (e.g. buildings, roads, bridges)
- Where are all the vegetation features located (e.g. grass, shrubs, trees)
- A clear display of the road systems
- A clear display of the powerline infrastructure (e.g. power tower, distribution line). This is an important factor to consider when I make urban development plans.

As an <em><b>architect</b></em>, I want to access various kinds of information when I crop a certain area of land. The information includes building coverage ratio, residential density, and afforested area. With the help of terrestrial equipment, I can also have a view of infrastructure and population, so that I can make a more elaborate analysis of site research and present more convincing data for my project.

As a <em><b>civil engineer</b></em>, I need to obtain site information such as ground type and topographic features, which can help me make decisions in road planning and location selection. In the map, I need to know the distribution of existing buildings, roads and powerlines. Also, the locations of farmlands, rivers and forests are important to me as well. It will be great if all the information is displayed in 3D so that I can see the terrain clearly and observe more details of the site. 
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Minimum Viable Products
We have developed the <b>view.<span></span>py</b> file that supports all key features (i.e., 2D Visualization, 3D Visualization, feature analysis). This serves as the Proof of Concept for the proposed web application. Following the set-up instructions in <a href="#getting-started"> Getting Started</a>, we can run <b>view.<span></span>py</b> locally and see the visualization <a href="#sample-results">results</a>, subject to <a href="#limitations">limitations</a>. 

More <a href="#future-works">future works</a> are needed for <b>view.<span></span>py</b> to be a fully functional website. 
<p align="right">(<a href="#readme-top">back to top</a>)</p>

### User Interface and Workflow Design

1. Select a pre-classified LAS file

2. Click the "Submit" button to submit the file

3. Once a file is submitted successfully, a message will be displayed; Step 4) - 6) will be disabled until the file is uploaded and saved successfully. 

4. Click the "Visualize" button to start the visualization process. Point cloud data information will be displayed in the table. 2D image of the site will be displayed. 

5. Click the "View 3D Rendering" button to see the visualization rendering. Users will be directed to localhost:8888 to see the open3d webrtc window. 

6. Click the "Stop Visualization" button to terminate the running visualization scripts.

Step 4) - 6) will be a "loop". We can click the "Visualize" button ONLY when there is NO visualization script running. Refreshing the web page will terminate the visualization script and clear the outputs. 

<img width="1397" alt="web_page" src="https://user-images.githubusercontent.com/105306727/208507948-eb8349e3-29ac-4a35-bd1f-b00a59c207cd.png">

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Sample Results
We used the LiDAR dataset of a neighborhood in Surrey, BC (surveyed in 2013) as our sample data. The sample point cloud data can be found at <a href="https://www.surrey.ca/services-payments/online-services/open-data/bulk-data">Bulk Data - City of Surrey</a>. We have uploaded this sample data on the website (hosted locally) and produced the following results. For more details, please check out the Demo Video in our <a href="https://peinanwang.github.io/Geospatial_Project_Blog/index.html">Project Blog</a> 

<img width="1238" alt="visualized_result" src="https://user-images.githubusercontent.com/105306727/208507889-7ea6898b-404e-48a3-b066-6260a8142553.png">

<img width="1099" alt="Screen Shot 2022-11-17 at 12 40 27 PM" src="https://user-images.githubusercontent.com/105306727/202593892-9f6a8ba6-9584-46f2-87aa-4bb55b763620.png">

<img width="1284" alt="Screen Shot 2022-11-17 at 12 41 08 PM" src="https://user-images.githubusercontent.com/105306727/202593926-f2250e77-fa32-4d6c-a78c-ba844ec2db47.png">

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Limitations
1) Currently this tool can only process LAS files, and the point cloud data need to be pre-classified. For the best user experience, the file size should be under 250 MB. 
2) Web visualization function is not supported on ARM devices (e.g. M1/M2 Macbook). <a href="http://www.open3d.org/docs/release/tutorial/visualization/web_visualizer.html">(Reference)</a>
3) We faced some technical difficulties when we tried to deploy the website (the Dockerfile in this repo is still incomplete):
    - Open3D is not built properly in Dockerfile. Installing Open3D requires extra dependencies in Dockerfile. <a href="http://www.open3d.org/docs/release/docker.html">(Reference)</a>
    - Currently functions in the <b>LAS_Processor.py</b> file do not work on a headless server. We followed the instruction in Open3d 0.16.0 documentation but we were not able to reproduce the headless rendering function. <a href="http://www.open3d.org/docs/release/tutorial/visualization/headless_rendering.html">(Reference)</a>
    - Web visualization (webrtc_server) may not work for external IPs. (It is supposed to work but we have not tested it yet). <a href="http://www.open3d.org/docs/release/tutorial/visualization/web_visualizer.html">(Reference)</a>
<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Useful Python Scripts
Since our web application is still a Proof of Concept pending deployment, one can only use our product on local devices with all dependencies and GPU graphic capacity. As a result, for research or demonstration purposes, it makes sense to just run some simple Python scripts. The <b>data_processing</b> folder includes Python programs to visualize a LAS file(<b>visualize_classification.<span></span>py</b>) and to merge multiple LAS files (<b>mergeLAS.<span></span>py</b>)

<img width="248" alt="Screenshot 2022-12-19 at 11 11 34 AM" src="https://user-images.githubusercontent.com/105306727/208508046-669cb62d-3a58-4b4e-9357-cb15ca719e53.png">

City of Vancouver provided the LiDAR dataset of the entire city at its <a href="https://opendata.vancouver.ca/explore/dataset/lidar-2018/information/">Open Data Portal</a>. We have written python scripts (in the <b>LAS_downloading</b> folder). Here are some locally-rendered results:
<img width="2473" alt="visualized_classification1" src="https://user-images.githubusercontent.com/105306727/208509981-507c4bd7-5a7b-458e-b421-6cdeed6f6e67.png">
<img width="1364" alt="Screenshot 2022-12-19 at 12 03 42 PM" src="https://user-images.githubusercontent.com/105306727/208510524-140b78c5-180c-42bb-b91e-58ffe1d0bbf8.png">

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started
### Prerequisite
We are using Open3D 0.16.0, which only supports Python 3.10 and above. This project is developed in a Python 3.10.8 virtual environment. Since Open3D is the only limiting factor for the minimum environment requirements, we recommend checking Open3D's official <a href="http://www.open3d.org/docs/release/getting_started.html">documentation</a> for more information. You may need to install some additional dependencies for Open3D to work properly. 
### Installation
All Python modules required for this project are included in the requirements.txt. We recommend running the following command in a virtual environment. 

```sh
  pip install -r requirements.txt
```
## Future Works
The following future works need to be done. This project has been <a href="https://github.com/peinanwang/cs5500_geospatial_projects">forked</a>. Continuous contributions and improvements will be made in 2023. 

<b>Frontend Features</b>

- [ ] Add a progress bar for the file-uploading process
- [ ] Add a progress bar for the visualization process
- [ ] Add a log-in function to support user registration

<b>Website Deployment</b>
- [ ] Solve the headless rendering issue of Open3D
- [ ] Write a Dockerfile that can set up the Open3D environment properly
- [ ] Deploy the website on a headless server
- [ ] Ensure the Web Visualizer works

<b>Backend</b>
- [ ] Improve the rendering speed (e.g. ignore some points)

<b>Extended Functionalities</b>
- [ ] Support rendering multiple files
- [ ] Support LAS file classification (Machine Learning model needed)
- [ ] Support object selection 
- [ ] Add filters for selecting certain feature types

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[contributors-url]: https://github.com/WuxiGuy/cs5500_geospatial_projects/graphs/contributors
[contributors-shield]: https://img.shields.io/github/contributors/WuxiGuy/cs5500_geospatial_projects.svg?style=for-the-badge
[fork-url]: https://github.com/peinanwang/cs5500_geospatial_projects/tree/main
[forks-shield]: https://img.shields.io/github/forks/WuxiGuy/cs5500_geospatial_projects.svg?style=for-the-badge
