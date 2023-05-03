package server.test;

import java.io.FileInputStream;
import java.io.IOException;

class ClassName {

    public void readFile() {
        FileInputStream fis = null;
        try {
            fis = new FileInputStream("file.txt");
            int data = fis.read();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}
