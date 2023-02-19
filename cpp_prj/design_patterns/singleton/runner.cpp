/*
File Name: runner.cpp
Author   : Pradeep S
*/

#include "singleton.cpp"
#include <iostream>
using namespace std;

int main()
{
    std::cout << "Main Function" << std::endl;
    singleton *m_pobject = singleton::createInstance();

    return 0;
}