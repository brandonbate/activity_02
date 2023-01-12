To get started, you'll need to create a folder to store activities for this course. I used the folder name ```activities```. 
Navigate to this folder in git bash. Click on the "copy" button displayed on this git page.

<img src="instruction_pic.png"  width=30% height=30%>

In the console, run

```
git clone your_url_here
```

where ```your_url_here``` is the copied address. This will download a copy of the assignment. It'll be in a subfolder that begins with ```activity-1```.
Navigate to this folder.  Run the command

```
py -3.7 -m venv virtualenv
```

to create a virtual environment for this activity. To activate this virtual environment, run

```
source virtualenv/Scripts/activate
```

For this activity, you will need to install a python package. Run:

```
pip install pytest
```

Run the command:

```
python functional_tests.py
```

