
# Bug Classification Framework

This project is a classification tool that uses ChatGPT and Infer to classify Java files. It has a graphical user interface (GUI) that allows users to select a .java file and get the classification results by clicking a button.

## Getting started
To get started, you need to follow the steps below:

### Prerequisites
You need to have the following software installed on your system:

* Python (version 3.6 or higher)
* PyQt5 (version 5.15 or higher)
* Java (version 8 or higher)

### Installing
* Clone the repository to your local machine using the following command:
```bash
git clone <repo-url>
```

* Navigate to the client folder:
```bash
cd client
```

* Create a virtual environment:
```bash
python3 -m venv env
```

* Activate the virtual environment:
```bash
source env/bin/activate
```

* Install PyQt5:
```bash
pip install PyQt5
```

### Running the project
* Make sure you are in the client folder and your virtual environment is activated.
* Run the main.py file with the following command:

```css
python main.py
```
* The GUI will open. Select a .java file using the "Browse" button.
* Click the "Classify" button to get the classification results.