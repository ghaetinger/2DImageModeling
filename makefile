py_run:
	cd src && python image_processing.py

cpp_run: py_run
	cd src && g++ -lglut -lGL -lGLU -lGLEW -std=c++11 main.cpp -o out

run: cpp_run
	cd src && ./out
