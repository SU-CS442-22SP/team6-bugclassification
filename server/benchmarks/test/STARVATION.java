package server.test;

class MyClass {
    private final Object lock = new Object();

    public void highPriorityTask() {
        synchronized (lock) {
            // Long running task
        }
    }

    public void lowPriorityTask() {
        synchronized (lock) {
            // Short task
        }
    }
}
