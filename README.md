# CM Blogs

## Steps to Run Project
To run a Django project, you typically follow these steps:

### 1. Setup Virtual Environment (Optional but Recommended):<br>
   Create a virtual environment to isolate your project's dependencies and activate environment <br>
   #### Windows
   ```
   pip install virtualenv
   python -m venv django-development
   .\django-development\Scripts\activate
   ```
   

### 2. Clone Project (If necessary):<br>
Clone the Django project repository from a version control system like Git if it's not already on your local machine.
```
git clone https://github.com/chanchalkmaurya/CM-Blogs.git
```
### 3. Navigate to Project Directory: <br>
Change directory (cd) to your Django project's root directory.
```
cd CM-Blogs
```

### 4. Install Dependencies:
Install project dependencies by running:
```
pip install -r requirement.txt
```
This command will install all dependencies listed in the requirements.txt file.

### 6. Setup Environment File
Create a `.env` file where settings.py resides.<br>
![Screenshot 2024-05-05 010702](https://github.com/chanchalkmaurya/CM-Blogs/assets/73050886/6ae9a08a-5a26-462f-92f6-37f9d4d70f06)

this files contains these environment variables:
```
DJANGO_SECRET_KEY=django-insecure-*=^nxjf@h6d3kmlz^1(-66(si^%2ri6nf$jw%m4macvmsk@7b6
DJANGO_DEBUG=True
DJANGO_NAME=blogdb
DJANGO_USER=root
DJANGO_PASSWORD=password
DJANGO_HOST=localhost
DJANGO_PORT=3306
```
change the environment values according to you. <br>
1. DJANGO_NAME => Your `Database Name`. <br>
2. DJANGO_USER => Your `username` <br>
3. DJANGO_PASSWORD => Your `db password` <br>
4. DJANGO_HOST => `localhost` if running locally. <br>
5. DJANGO_PORT=3306
<br>
### 6. Run Migrations:
Apply database migrations by running:
```
python manage.py makemigrations
python manage.py migrate
```
### 7. Create Superuser (Optional):
If your project includes authentication, you may want to create a superuser:
```
python manage.py createsuperuser
```

### 8. Start Development Server:
Run the Django development server:
```
python manage.py runserver
```

### 9. Access the Application:
Open a web browser and navigate to the URL provided by the Django development server (usually http://127.0.0.1:8000/).
