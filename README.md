To get started, you'll need to create a folder to store activities for this course. I used the folder name ```activities```. 
Navigate to this folder in git bash. On this page, click on the "Code" button and under the "SSH" heading, click the "copy" button.
In the console, run

```
git clone your_url_here
```

where ```your_url_here``` is the copied address. This will download a copy of the assignment. It'll be in a subfolder that begins with ```activity-2```.
Navigate to this folder.  Run the command

```
py -3.7 -m venv virtualenv
```

to create a virtual environment for this activity. To activate this virtual environment, run

```
source virtualenv/Scripts/activate
```

For this activity, you will need to make sure the Gecko Driver is installed in your scripts folder.
You will also need to install selenium:

```
pip install "selenium<4"
```

Run the command:
```
python functional_tests.py
```

This should display an error.

Your task is to modify ```my_page.html``` so that it can pass all the tests in ```functional_tests.py```. I have placed comments in ```my_page.html`` help guide you toward this. I also include ```my_page.css```, which specifies the display properties of our html document. After you have passed all the tests, feel free to play around with the these files to make a more appealing web page. Just be sure that any changes you make don't cause you to fail the test.
