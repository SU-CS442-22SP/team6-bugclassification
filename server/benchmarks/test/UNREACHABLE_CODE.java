package server.test;

class MyClass {
    public void method() {
        System.out.println("Hello");
        return;
        System.out.println("World"); // Unreachable code
    }

}
