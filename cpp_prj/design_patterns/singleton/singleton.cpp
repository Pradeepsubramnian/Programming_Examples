/*
File Name: singleton.cpp
Author   : Pradeep S
*/
#include "singleton.h"
#include <iostream>
using namespace std;

singleton* singleton::m_psingleton = NULL;
singleton::singleton()
{
    std::cout << "singleton::singleton()" << std::endl;
}
singleton* singleton::createInstance()
{
    std::cout << "singleton::createInstance()" << std::endl;
    if(m_psingleton == NULL)
    {
        m_psingleton = new singleton;
    }
    return m_psingleton;
}
void singleton::deleteInstance()
{
    if(m_psingleton != NULL)
    {
        delete m_psingleton;
        std::cout << "singleton::deleteInstance()" << std::endl;
    }
}
singleton::~singleton()
{
    std::cout << "singleton::~singleton()" << std::endl;
}



