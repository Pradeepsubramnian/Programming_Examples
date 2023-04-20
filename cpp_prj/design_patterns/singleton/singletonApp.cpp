/*
File Name   : singletonApp.cpp
Author      : Pradeep S
*/

#include "singleton.cpp"
#include <iostream>
using namespace std;

int main()
{
    std::cout << "Main Function" << std::endl;
    singleton *m_pobject = singleton::createInstance();
    m_pobject->deleteInstance();

    return 0;
}