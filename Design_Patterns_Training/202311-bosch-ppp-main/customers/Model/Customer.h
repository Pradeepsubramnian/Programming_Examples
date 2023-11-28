/**
 * Project Untitled
 */


#ifndef _CUSTOMER_H
#define _CUSTOMER_H
#include "Address.h"

class Customer {
public: 
    string name;
    string password;
    Address addresses[];
    
/**
 * @param name
 * @param password
 */
bool login(string name, string password);
};

#endif //_CUSTOMER_H