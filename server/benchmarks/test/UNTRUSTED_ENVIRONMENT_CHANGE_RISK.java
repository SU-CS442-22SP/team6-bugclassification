package server.test;

class MyClass {
    public void changeEnv(String newEnvVarValue) {
        System.setProperty("java.library.path", newEnvVarValue);
    }

}
