# Hatchway_Posts_API
REST API created using Python and the Django/Django REST Framework


## Installation
Note - I used Python 3.7.3 so depending on what you have installed/what you have aliased for your python, your python command might vary. I personally had my python aliased to python3 permanently.


1. Intially, it's usually recommended that you should create a virtual environment. So in terminal/bash/zsh/git bash/powershell run -   
    python3 -m venv venv  
    You can rename the second venv to whatever you want the name of your virtualenv to be.

2. Activate the virtual environment -  
    A. On Windows with powershell/git bash. Navigate to the folder that contains the venv folder -  
      venv\Scripts\activate  
     
    B. On linux shell. Navigate to the folder that contains the venv folder -  
      source venv/bin/activate
 
3. Once virtual environment is activated, install python package dependencies through pip. Make sure you're in the folder that has requirements.txt -   
    pip install -r requirements.txt


## Using the API

1. Once installation has been complete, navigate to the blogposts folder that has manage.py in it.  

2. Run the development server by using this command (note - make sure you have activated the virtual environment with the proper dependencies installed) through the shell of your choosing -   
  python3 manage.py runserver
  
3. Once the Django development server is up and running check in any browser with this url -   
    127.0.0.1:8000  
    It should kinda look like an error screen but the api/ endpoint should be listed.  
    
4. Calling the API can be done with the endpoint -   
    127.0.0.1:8000/api/posts/
    
5. Tags can be applied the the url endpoint in step #4 appended with tags query parameters along with sortBy (optional) and direction(optional). If no sortBy parameters are provided then the returned posts are going to be sorted by id value by default. If no direction is provided then the posts will be sorted by ascending order by default. Example urls are below -  
    A. 127.0.0.1:8000/api/posts/  
    B. 127.0.0.1:8000/api/posts/?tags=science,tech  
    C. 127.0.0.1:8000/api/posts/?tags=science,tech&sortBy=likes  
    D. 127.0.0.1:8000/api/posts/?tags=history,science&sortBy=reads&direction=desc  
    
6. Acceptable values for tags, sortBy, and direction query parameters -   
  A. tags - science, history, tech, startups, design, culture, politics, health  
  
  B. sortBy - id (this is the default value), reads, likes, popularity  
  
  C. direction - asc (ascending order), desc (descending order)  
  


## Running Unit Tests

1. To run tests (of which there are three), again make sure you have the virtual environment activated with all the dependencies installed.

2. Navigate to the blogposts folder in a shell or command prompt of your choice with "test.py" in it.

3. Run this command -   
  python manage.py test
  
4. The test running/results should be listed.
  
