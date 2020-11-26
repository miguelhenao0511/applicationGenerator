# Application generator

## Requirements

 - Python >= 3.8


## How to use

 - Activate virtual env 
 	* for windows use command: venv\\Scripts\\activate.bat 
 	* for linux or macOS use command: venv/bin/activate
 - Run the application with command: python manage.py runserver
 - The index view is a form with a input file, upload here the .bpmn diagram (create diagram here https://bpmn.io/)
 - Wait while the application is generated
 - The out application save in applicationGenerator/resources/out_application/application

## Run out application

 - Activate virtual env 
 	* for windows use command: venv\\Scripts\\activate.bat 
 	* for linux or macOS use command: venv/bin/activate
 - Make migration with command: python manage.py makemigrations
 - Generate database structure with command: python manage.py migrate
 - Run application with command: python manage.py runserver
 	* If application generator is running run server in other port with command: python manage.py runserver 8020