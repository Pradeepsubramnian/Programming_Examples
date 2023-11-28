
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

public class Customer {

    public Customer() {
    }

    public string name;

    public string password;

    private Address primaryAddress;
    private Order[] orders;


    /// <summary>
    /// @param name 
    /// @param password 
    /// @return
    /// </summary>
    public bool login(string name, string password) {
        // TODO implement here
        return False;
    }

}