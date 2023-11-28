
var p=new Object();
//now we have an object "p"
//now property or behavior defined at this point

console.log('p',p);

//now we can attach properties to the object
p.name='Sanjay';
p.email='sanjay@gmail.com';

p.eat=function(food){
    console.log(`${this.name} eats ${food}`);

};

p.move=function(from,to){
    console.log(`${this.name} Moves to ${from} to ${to}`);
};

p.eat('breakfast');
p.move('home','office');