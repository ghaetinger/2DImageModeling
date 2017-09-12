#include <iostream>
#include <vector>
#include <string>
#include <stdlib.h>
#include <GL/glew.h>
#include <GL/glut.h>
#include <GL/gl.h>
#include <GL/glu.h>
#include <GL/glext.h>
#include <fstream>

using namespace::std;

void readFile(vector<int*> *coord){

    int buf1, buf2, buf3;
    string line;
    ifstream myfile ("PICTURE_GREY_VALUES.txt");
    int i=0;
    if (myfile.is_open())
    {
        while ( getline (myfile,line) )
        {

            int *lineBuf = new int[3] {0,0,0};
            int pos = line.find("|");
            buf1 = atoi(line.substr(0, pos).c_str());
            int pos2 = (line.substr(pos+1)).find("|") + pos;
            buf2 = atoi(line.substr(pos+1, pos2).c_str());
            buf3 = atoi(line.substr(pos2+2).c_str());
            lineBuf[0] = buf1;
            lineBuf[1] = buf2;
            lineBuf[2] = buf3;

            coord->push_back(lineBuf);
            i++;
        }
        myfile.close();
    }
}


int main() {

    vector<int*> coord;
    readFile(&coord);

    int size = coord.size();
    int coordArr[size][3];

    for(int i = 0; i<coord.size(); i++){
        for(int j = 0; j<3; j++){
            coordArr[i][j] = coord.at(i)[j];
            cout << (coord.at(i))[j] << "|";
        }
        cout << "\n";
    }

    return 0;
}