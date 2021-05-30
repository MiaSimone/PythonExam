# PythonExam
## Fruite Finder
This program will allow a user to upload a picture of a fruit which the machine will reconize and return the fruit as word. It will then serch the Rema 1000 shop for the fruit and get cost and other valuble information.

## Used technologies
- Selenium
- bs4
- PIL
- tensorflow
- keras
- os 

## Note!
When downloading the program you have to clone it into this https://github.com/Hartmannsolution/docker_notebooks/tree/master/notebooks at that location. 
Then run the program using the command "docker-compose up" in git bash at the root location of the notebook. In VSC you have to attach it to a remote container, and that has to be notebookserver. 

The program wasn't finished, but here is a guide to run the different componenets:
### To upload a picture
To upload a picture you have to open the program in VSC and in the terminal write "python upload_picture.py URL-OF-PICTURE" where you insert a url at URL-OF-PICTURE place. Fx:
#### python upload_picture.py https://madkurven.dk/wp-content/uploads/gala-apple.png
The picture will then be saved in the image folder, overwriting the image every time.

### To train the machine
Frist create the dataset by running the Create_Dataset.ipynb. This can take some time.
Second run the Train_Machine.ipynb, and please notice the result isn't very good.

### To atomaticly achive data from Rema 1000
Run the file Webscraping.ipynb.
(This dosen't work, we didn't finish)

Project name
Short description
List of used technologies
Installation guide (if any libraries need to be installed)
User guide (how to run the program)
Status (What has been done (and if anything: what was not done))
List of Challenges you have set up for your self (The things in your project you want to highlight)
