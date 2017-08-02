from datetime import datetime
d = datetime.now();
print("{:%Y-%m-%d %H:%M:%S}".format(d));


def calculate_temperatures(kelvin):
    celsius = kelvin - 273;
    fahrenheit = celsius * 9 / 5 + 32;
    return (celsius, fahrenheit)

(c,f) = calculate_temperatures(340);
print("celsius:",c);
print("fahrenheit",f);

class Person:
    ''' This class represents a person object'''

    def __init__(self,name,tel):
        self.name = name;
        self.tel = tel;

p = Person("robert","12345");
print("p.name:",p.name);
print("p.tel:",p.tel);


class Person1:
    '''This class repersents a person object'''

    def __init__(self,first_name,surname,tel):
        self.first_name = first_name;
        self.surname = surname;
        self.tel = tel;

    def full_name(self):
        return self.first_name + " " + self.surname;

pe =Person1("robert","hsu","12345");
print("full_name",pe.full_name());

class Employee(Person1):
    def __init__(self,first_name,surname,tel,salary):
        super().__init__(first_name,surname,tel);
        self.salary = salary;

    def give_raise(self,amount):
        self.salary = self.salary + amount


employee = Employee("jane","hsu","5678",20000);
employee.give_raise(5000);
print(employee.salary);
print(employee.full_name());
