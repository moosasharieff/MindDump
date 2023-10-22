# MindDump
MindDump is an application which lets its user dump all their frustration and lets them review their outburst.

## Installation and Running the project
1. Clone the project - `git clone https://github.com/moosasharieff/MindDump.git`
2. Update the migrations
  ```
  python3 manage.py migrate
  python3 manage.py makemigrations
  python3 manage.py migrate
  ```
3. Run the application - `python3 manage.py runserver`

----------------------------------
----------------------------------
#### Important :
  
<details>
<summary>(1) Always run below commands when ever you update models of the project. This updates the Schema of the database.</summary>

  ```
  python3 manage.py migrate 
  python3 manage.py makemigrations
  python3 manage.py migrate
  ```
</details>