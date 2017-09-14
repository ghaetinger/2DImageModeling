import grey_contraster as contrast
import _3D_modeler as modeler

matrix = contrast.generate_diagram()

obj_name  = raw_input("Type the name of the 3D object you wish to create: ")
modeler.create_obj(matrix, obj_name)