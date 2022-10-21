import numpy as np 
import laspy
import open3d as o3d

def readLas(filename):
	las = laspy.read(filename)
	point_data = np.stack([las.X, las.Y, las.Z], axis=0).transpose((1, 0))
	return point_data


def visualizeLAS(point_data):
	geom = o3d.geometry.PointCloud()
	geom.points = o3d.utility.Vector3dVector(point_data)
	o3d.visualization.draw_geometries([geom])


def main():
	filename = "/Users/peinanwang/VancouverLAS/sample_data/downtownLAS/4910E_54580N.las"
	visualizeLAS(readLas(filename))


if __name__ == "__main__":
	main()
