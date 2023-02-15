from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3
from panda3d.core import *
import array

def create_gradient(sky_color, ground_color):
    
    vertex_format = GeomVertexFormat()
    array_format = GeomVertexArrayFormat()
    array_format.add_column(InternalName.get_vertex(), 3,
        GeomEnums.NT_float32, GeomEnums.C_point)
    vertex_format.add_array(array_format)
    array_format = GeomVertexArrayFormat()
    array_format.add_column(InternalName.make("color"), 4,
        GeomEnums.NT_uint8, GeomEnums.C_color)
    vertex_format.add_array(array_format)
    vertex_format = GeomVertexFormat.register_format(vertex_format)

    vertex_data = GeomVertexData("quad_data", vertex_format, GeomEnums.UH_static)
    vertex_data.unclean_set_num_rows(4)
    # create a simple quad
    values = array.array("f", [
        -.5, 0., -.5,
        .5, 0., -.5,
        -.5, 0., .5,
        .5, 0., .5
    ])
    pos_array = vertex_data.modify_array(0)
    memview = memoryview(pos_array).cast("B").cast("f")
    memview[:] = values
    color1 = tuple(int(round(c * 255)) for c in ground_color)
    color2 = tuple(int(round(c * 255)) for c in sky_color)
    values = array.array("B", color1 * 2 + color2 * 2)
    color_array = vertex_data.modify_array(1)
    memview = memoryview(color_array).cast("B")
    memview[:] = values

    tris_prim = GeomTriangles(GeomEnums.UH_static)
    indices = array.array("H", [
        0, 1, 2,
        1, 3, 2
    ])
    tris_array = tris_prim.modify_vertices()
    tris_array.unclean_set_num_rows(6)
    memview = memoryview(tris_array).cast("B").cast("H")
    memview[:] = indices

    geom = Geom(vertex_data)
    geom.add_primitive(tris_prim)
    node = GeomNode("quad")
    node.add_geom(geom)
    quad = NodePath(node)
    quad.set_light_off()
    quad.set_bin("background", 0)
    quad.set_depth_write(False)
    quad.set_depth_test(False)

    return quad


class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Disable the camera trackball controls.
        #self.disableMouse()

        # Load the environment model.
        #self.scene = self.loader.loadModel("avikus_boat.glb")
        self.myBoat = self.loader.loadModel("avikus_boat.glb")

        #self.scene = self.loader.loadModel("Models/Pion2.glb") # or use gltf
        # Reparent the model to render.
        self.myBoat.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        #self.scene.setScale(0.25, 0.25, 0.25)
        #self.scene.setPos(-8, 42, 0)
        
        sky_color = (0, 0, 1., 1.)
        ground_color = (0, 1., 0, 1.)
        self.background_gradient = create_gradient(sky_color, ground_color)
        self.background_gradient.reparent_to(self.camera)
        
        
        # Add the spinCameraTask procedure to the task manager.
        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")

        # Load and transform the panda actor.
        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(0.005, 0.005, 0.005)
        self.pandaActor.reparentTo(self.render)
            
        
        # Loop its animation.
        self.pandaActor.loop("walk")

        # Create the four lerp intervals needed for the panda to
        # walk back and forth.
        posInterval1 = self.pandaActor.posInterval(100,
                                                   Point3(0, -10, 0),
                                                   startPos=Point3(0, 10, 0))
        posInterval2 = self.pandaActor.posInterval(13,
                                                   Point3(0, 10, 0),
                                                   startPos=Point3(0, -10, 0))
        hprInterval1 = self.pandaActor.hprInterval(3,
                                                   Point3(180, 0, 0),
                                                   startHpr=Point3(0, 0, 0))
        hprInterval2 = self.pandaActor.hprInterval(3,
                                                   Point3(0, 0, 0),
                                                   startHpr=Point3(180, 0, 0))

        # Create and play the sequence that coordinates the intervals.
        self.pandaPace = Sequence(posInterval1, hprInterval1,
                                  posInterval2, hprInterval2,
                                  name="pandaPace")
        self.pandaPace.loop()

    # Define a procedure to move the camera.
    def spinCameraTask(self, task):
        # angleDegrees = task.time * 6.0
        angleRadians =(pi / 180.0)
        # self.camera.setPos(20 * sin(angleRadians), -20 * cos(angleRadians), 3)
        self.camera.setPos(0, 0, 30)
        # self.camera.setHpr(0, 0, -angleRadians)

        return Task.cont


app = MyApp()
app.run()