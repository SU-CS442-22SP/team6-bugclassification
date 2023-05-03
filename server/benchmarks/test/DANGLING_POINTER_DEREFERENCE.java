package server.test;

class AClass {
    private Object object;

    public void setObject(Object object) {
        this.object = object;
    }

    public void dereference() {
        System.out.println("Object: " + object.toString());
    }
}

