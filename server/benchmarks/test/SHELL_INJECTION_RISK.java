package server.test;

import java.io.IOException;

class MyClass {

    public void exec(String command) {
        try {
            Runtime.getRuntime().exec("cmd.exe /C " + command);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}
