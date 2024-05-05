# CM Blogs

## Steps to Run Project
To run a Django project, you typically follow these steps: <br>
if your are windows, Use `Git Bash` for running below 2 (creating env and git clone) commands. for other commands use `Powershell` or  `Command Prompt`<br>
Linux User can use `terminal`.

### 1. Setup Virtual Environment (Optional but Recommended):<br>
   Create a virtual environment to isolate your project's dependencies and activate environment <br>
   ```
   pip install virtualenv
   python -m venv django-development
   source django-development/Scripts/activate
   ```
   

### 2. Clone Project (If necessary):<br>
Clone the Django project repository from a version control system like Git if it's not already on your local machine.
```
git clone https://github.com/chanchalkmaurya/CM-Blogs.git
```

### Windows user 
**Run all the below commands on Powershell or 'Command Prompt'. Do not run it in `Git Bash`.**
1. Open the `Powershell` or `Command Prompt`.
2. Go to Projects Root Directory <br>
![Screenshot 2024-05-05 015010](https://github.com/chanchalkmaurya/CM-Blogs/assets/73050886/84f54bba-1675-4750-8813-4f1c79e7f74d)

3. activate the environment
   ```
   ..\django-development\Scripts\activate
   ```

### 3. Install Dependencies:
Install project dependencies by running:
```
pip install -r requirement.txt
```
This command will install all dependencies listed in the requirements.txt file.

### 4. Setup Environment File
Create a `.env` file where settings.py resides. [if .env file is not there] <br>
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

### 5. Run Migrations:
Apply database migrations by running:
```
python manage.py makemigrations usersApp
python manage.py makemigrations blogApp
python manage.py migrate
```

   
### 6. Create Superuser (Optional):
If your project includes authentication, you may want to create a superuser:
```
python manage.py createsuperuser
```

### 7. Start Development Server:
Run the Django development server:
```
python manage.py runserver
```

### 8. Access the Application:
Open a web browser and navigate to the URL provided by the Django development server (usually http://127.0.0.1:8000/).
<br><br><br>

# if you're still stuck somewhere?
Click to watch Video:
https://youtu.be/zPsSqb2ojrI


<br><br><br>

# Features of this Project:
Features of the Django Blog Application:

### 1. User Registration:
* Registration form with fields for username, email address, and password.
* Form validation to ensure correct data entry.
* Secure storage of user information in the database.

### 2. User Login and Authentication:
* Login page for users to enter their credentials.
* Authentication mechanism to verify user credentials.
* Error handling for invalid login attempts.
* Redirect to the home page upon successful login.
* Blog Post Creation and Editing:
* Page to view all blogs written by the logged-in user.
### 3. Form for creating and editing blog posts.
* Form fields for title, content, and author of the blog post.
* Validation of form data before saving to the database.
### 4. Blog Post Listing:
* Page displaying a list of all blog posts.
* Each post includes title, content, author, and publication date.
* Pagination for long lists of blog posts to improve usability.
### 5. Authorization and Ownership:
* Authorization checks to ensure only the owner can edit or delete a blog post.
* Proper handling of authorization to prevent unauthorized access to blog posts.
### 6. Readme with Installation Steps:
* Detailed instructions on how to set up and run the project.
* Installation steps for required dependencies.
* Configuration steps for database and Django settings.



## Demo Video
https://youtu.be/l-TMZ6JrlrI
