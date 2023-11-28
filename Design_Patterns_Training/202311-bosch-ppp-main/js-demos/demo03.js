
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


var sanjay=createPerson("Sanjay",50);
var shivanshi=createPerson("Shivanshi",16);

sanjay.eat('Salad');
shivanshi.eat('Maggi');