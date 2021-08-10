import bpy
import math

def add_mesh(name, verts, faces, edges=None, col_name="Collection"):
    if edges is None:
        edges = []
    mesh = bpy.data.meshes.new(name)
    obj = bpy.data.objects.new(mesh.name, mesh)
    col = bpy.data.collections.get(col_name)
    col.objects.link(obj)
    bpy.context.view_layer.objects.active = obj
    mesh.from_pydata(verts, edges, faces)

def f(x,y):
    return (x + y**2)/ 100

verts = []
faces = []
count = 0
for i in range(-101,100):
    for j in range(-101,100):
        verts += [ (i,j,f(i,j))]
        verts += [ (i + 1, j, f(i+1,j))]
        verts += [ (i, j + 1, f(i,j+1))]
        verts += [ (i + 1, j + 1, f(i+1,j+1))]
        faces += [[count + 0, count + 2, count + 3, count + 1]]
        count += 4


add_mesh("myBeautifulMesh_1", verts, faces)
