## The project was made with python and django 3. The main classes are:
num_to_english_util.py<br/>
http_util.py<br/>
number.py<br/>
exceptions.py<br/>

## settings.py
Has been configured to be put into production

## Proction
The test description talks about what I would do to make the endpoint available to other developers.
Just as an example I created the "hypothetical_configurations" folder with files like Dockerfile and others to run the project using Gunicorn, nginx and supervisord

Remembering, the files were made based on other projects that I work just as an example, the Dockerfile has not been tested and some kind of error inside is expected.
