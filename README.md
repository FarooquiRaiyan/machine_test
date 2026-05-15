Installation Guide

Step 1: Clone the Git Repo on terminal VSCode
git clone https://github.com/FarooquiRaiyan/machine_test.git

Step 2: Move to the folder 
cd machine_test

Step 3: Create Virtual Environment
python -m venv venv

Step 4: Activate the Virtual Enivorment
venv\Scripts\activate

step 5: Install the Packages from requiremnts.txt
pip install -r requirements.txt

step 6 : Create a database
CREATE DATABASE fastapi;

Step 7 : create .env file and update here the username , password , port no and database name 
DB_URL=mysql+pymysql://USERNAME:PASSWORD@HOST:PORT/DATABASE_NAME

step 8 : Execute the main py
uvicoirn main:app --reload

Now check if it swoking 
runs on
http://127.0.0.1:8000

Swagger Docs at 
http://127.0.0.1:8000/docs
