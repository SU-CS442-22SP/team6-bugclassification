package server.test;

class Parent {
    public void method(String param) {
    }
}

class Child extends Parent {
    @Override
    public void method(@NonNull String param) {
    }
}

