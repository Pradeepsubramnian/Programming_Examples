/*
File Name: singleton.h
Author   : Pradeep S
*/
#include <iostream>
using namespace std;
class singleton
{
    singleton();
    ~singleton();

    static singleton *m_psingleton;

    public:
    static singleton* createInstance();

};