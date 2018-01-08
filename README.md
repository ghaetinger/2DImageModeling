**2DImageModeling**
===============
Concept
---------------
The idea behind taking a photo and *bump mapping* it into a 3D object is mainly to test the limits of *Wavefront's* ".obj" file. Using a *big sized* images ends up creating a 3D object with a huge number of vertices as, in this script's execution, **the number of vertices on the ".obj" is equivalent to 2x the number of pixels in the image**.
Another aspiration for the creation and use of this simple script is to turn my job of *3D modeling* easier. I find it easier to draw and paint shadows than to edit triangle meshes for a specific object creation.

Use
--------------
The user interface is quite simple. The script only needs **2** informations from the users:
* **The input image's name** (the file must be contained by the archive ".../src/images" and the input must contain name extension)
* **The output file name** (the file will be under the name given y the input + ".obj" in the ".../src/objects" archive)

![UI](https://github.com/GuilhermeHaetinger/2DImageModeling/blob/readme-tests/UI_exemple.png "UI")
