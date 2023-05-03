package server.test;

import java.util.ArrayList;
import java.util.List;

class MyClass {
    private List<String> data = new ArrayList<>();

    public void addData(String item) {
        data.add(item);
    }

    public void clearData() {
        data = null;
    }
}

