# Matched
1.git checkout -b <chooseyourbranchname>

2.in pycharm : file -> settings -> create a python interpreter and use venv
3. open the requirements file and run it:
      pip install -r requirements.txt
4. run the migrations:
   ./manage.py migrate
5. run the setup scripts to populate the database(users,groups,jobs)
   ./manage.py runscript setup
5.now you are ready to launch the site:
  ./manage.py runserver
