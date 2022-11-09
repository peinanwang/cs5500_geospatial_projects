import open3d as o3d
import open3d.visualization.gui as gui
import open3d.visualization.rendering as rendering


class VisualizationApp:
    def __init__(self) -> None:
        
        gui.Application.instance.initialize()
        
        self.window = gui.Application.instance.create_window("Geospatial Rendering")
        self.scene = gui.SceneWidget()
        self.scene.scene = rendering.Open3DScene(self.window.renderer)
        
        self.window.add_child(self.scene)
        
        cube_red = o3d.geometry.TriangleMesh.create_box(1, 2, 4)
        cube_red.compute_vertex_normals()
        cube_red.paint_uniform_color((1.0, 0.0, 0.0))
        material = rendering.MaterialRecord()
        material.shader = "defaultLit"
        
        self.scene.scene.add_geometry("CubeRed", cube_red, material)
        
        bounds = cube_red.get_axis_aligned_bounding_box()
        self.scene.setup_camera(60, bounds, bounds.get_center())
    
    def run(self):
        
        gui.Application.instance.run()


if __name__ == "__main__":
    app = VisualizationApp()
    app.run()