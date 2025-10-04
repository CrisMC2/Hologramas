import vtk
import trimesh

class ConvertFormat():
    def __init__(self):
        pass
    
    def trimesh_to_vtk(self, mesh: trimesh) -> vtk.vtkPolyData:
        #Convertir vértices a vtkPoints
        points = vtk.vtkPoints()
        
        for vertex in mesh.vertices:
            points.InsertNextPoint(vertex.tolist())
        
        #Convertir caras a vtkCellArray
        triangles = vtk.vtkCellArray()
        
        for face in mesh.faces:
            triangle = vtk.vtkTriangle()
            
            for i in range(3):
                triangle.GetPointIds().SetId(i, int(face[i]))
            
            triangles.InsertNextCell(triangle)
        
        #Crear PolyDataMapper
        polydata = vtk.vtkPolyData()
        polydata.SetPoints(points)
        polydata.SetPolys(triangles)
        
        return polydata