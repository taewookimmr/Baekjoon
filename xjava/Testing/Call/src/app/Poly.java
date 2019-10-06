package app;

public class Poly {
    public static void main(String[] args) throws Exception {

        Person stu = new Person();
        stu.show();
        stu = new Student();
        stu.show();
        stu = new Batman();
        stu.show();
        System.out.println(stu.getClass());

    }

}

class Person{
    void show(){
        System.out.println("person");
    }
}

class Student extends Person{
    void show(){
        System.out.println("student");
    }
}

class Batman extends Person{
    void show(){
        System.out.println("I'm Batman");
    }
}