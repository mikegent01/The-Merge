bl_info = {
    "name": "Meshy for Blender",
    "author": "Meshy",
    "description": "Meshy for Blender",
    "blender": (3, 0, 0),
    "version": (0, 1, 3),
    "category": "3D View",
    "location": "View3D",
}

from . import MeshyPanel
modules = (MeshyPanel,)


def register():
    print(__name__)
    for module in modules:
        module.register()


def unregister():
    for module in reversed(modules):
        module.unregister()
