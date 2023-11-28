
function createPerson(name,age){
    
    var p=new Object();
    p.name=name;
    p.age=age;
    
    p.eat=function(food){
        console.log(`${this.name} eats ${food}`);
    
    };
    
    p.move=function(from,to){
        console.log(`${this.name} Moves to ${from} to ${to}`);
    };

    return p;
};

function teachDriving(person,veichle){
    if(person.age<18)
        return console.log(`${person.name} you need to wait for ${18-person.age} years to learn driving`);

    console.log(`${person.name} Learns driving ${veichle}`);

    //teach driving
    if(person.licenses)
        return person.licenses.push(veichle);

    person.licenses=[veichle];

    person.drive=function(veichle){
        for(var v of person.licenses)
            if(v==veichle)
                return console.log(`${this.name} drives ${veichle}`);
        return console.log(`${this.name} you are not licenced to drive ${veichle}`);
    }

}


var sanjay=createPerson("Sanjay",50);
var shivanshi=createPerson("Shivanshi",16);

teachDriving(sanjay,"Car");
teachDriving(sanjay,"Motorcycle");
teachDriving(shivanshi,"Car"); //not allowed.


sanjay.drive('Car'); //OK
sanjay.drive('Truck'); //method called. prints message not licenced.

shivanshi.drive('Bike'); //NO SUCH method.