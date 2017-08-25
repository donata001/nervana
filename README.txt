      1. install python
            $brew install python
     
      2.   install pip:
            $python get-pip.py
     
      3.   install  Django and dependencies:
            $pip install -r requirements.txt
   
      4.  install mysql
           $brew install mysql
   
      5.  create and set up mysql
           $mysql -u root


            mysql>create database housing;


            mysql>create user django@localhost IDENTIFIED BY ‘localhost’;


            mysql>grant usage on *.* to ‘django’@localhost identified by ‘localhost’;


            mysql>grant all privileges on housing.* to django@localhost;


      6. cd into the project root in which manage.py located
      	  $python manage.py migrate data
      	  
      	  if you see an exception about ContentTypes migrations, run this
          $python manage.py migrate ContentTypes
          
      
      7. export django settings
      	  $export DJANGO_SETTINGS_MODULE=Nervana.settings
      
      8. import house data into mysql and create predefined user
          $python -m data.utils


      9. start mysql server
          $/usr/local/bin/mysql.server start
   
      10. start Django server
         $python manage.py runserver


      11. open browser and go to http://localhost:8000/data/login
             username: open 
             password: sesame          