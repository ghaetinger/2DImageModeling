**2DImageModeling**
===============
Concept
---------------
The idea behind taking a photo and *bump mapping* it into a 3D object is mainly to test the limits of *Wavefront's* ".obj" file. Using a *big sized* images ends up creating a 3D object with a huge number of vertices as, in this script's execution, `the number of vertices on the ".obj" is equivalent to 2x the number of pixels in the image`.
Another aspiration for the creation and use of this simple script is to turn my job of *3D modeling* easier. I find it easier to draw and paint shadows than to edit triangle meshes for a specific object creation.

Use
--------------
The execution must be through python interpretation of the file `OBJ_Maker.py` using *python 3.0*. Execution flows as it shows in the execution exemple.

The user interface is quite simple. The script only needs **2** informations from the users:
* `The input image's name` (the file must be contained by the archive ".../src/images" and the input must be a ".jpg" file)
* `The output file name` (the file will be under the name given y the input + ".obj" in the ".../src/objects" archive)

![UI](https://github.com/GuilhermeHaetinger/2DImageModeling/blob/readme-tests/UI_exemple.png "UI")

Result
--------------
The script is an easy executable that gives a fair result. After getting a raw result, improving it by smoothing its surface can turn into something rather good looking.

![Raw Result (left - result, right - picture used)](https://github.com/GuilhermeHaetinger/2DImageModeling/raw-nose.jpeg "Raw nose")

![Improved Result](https://github.com/GuilhermeHaetinger/2DImageModeling/good-nose.jpeg "Improved nose")

Conclusions
--------------
The script can be developed to calculate the variation between vertices to stablish a smoother surface with less errors(as I would call them : *mountain peaks*). This could lead to a actually *market worthy* software for artist(mostly 2D artists).

