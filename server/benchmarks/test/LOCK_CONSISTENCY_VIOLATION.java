package server.test;

class MyClass {
    private final Object lock1 = new Object();
    private final Object lock2 = new Object();
    private int sharedResource;

    public void increment() {
        synchronized (lock1) {
            sharedResource++;
        }
    }

    public void decrement() {
        synchronized (lock2) {
            sharedResource--;
        }
    }
}
