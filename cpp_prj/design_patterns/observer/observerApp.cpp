/*
File Name   : observer.cpp
Author      : Pradeep S
*/

#include "observer.cpp"
#include <iostream>
using namespace std;

int main()
{
    std::cout << "Main Function" << std::endl;
    observer *m_pobject = new observer();
    delete m_pobject;

    return 0;
}