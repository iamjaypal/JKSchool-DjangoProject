

# **Student Management System**

A comprehensive **Student Management System** built using **Django**, designed to manage student information, including enrollment, attendance, grades, and other administrative functionalities. This application is ideal for schools or educational institutions looking for a streamlined solution to manage student data.

## **Features**
- **Student Enrollment**: Manage student registration and update student details.
- **Responsive UI**: Mobile-friendly design using HTML/CSS or integrated frontend frameworks.

## **Technologies Used**
- **Backend**: Django (Python), Django ORM
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap (or other UI libraries you used)
- **Database**: PostgreSQL (or SQLite during development)
- **Version Control**: Git
- **Deployment**: Docker (if Dockerized), Nginx, Gunicorn (for production)
- **Testing**: Django's built-in testing framework


## **Installation**
Follow the steps below to get the project up and running on your local machine:

### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/student-management-system.git
cd student-management-system
```

### **2. Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **3. Install Dependencies**
```bash
asgiref==3.8.1
distlib==0.3.9     
Django==5.1.1
filelock==3.18.0
gunicorn==23.0.0
packaging==25.0
pillow==10.4.0
platformdirs==4.3.7
sqlparse==0.5.1
tzdata==2024.1
virtualenv==20.29.3
virtualenvwrapper-win==1.2.7
whitenoise==6.7.0
```

### **4. Set Up Database**
Make sure to set up your database (e.g., PostgreSQL) and update the `DATABASES` configuration in `student_management/settings.py`.

### **5. Run Migrations**
```bash
python manage.py migrate
```

### **6. Run the Application**
```bash
python manage.py runserver
```
Visit `http://localhost:8000` to access the app.

```

Make sure to configure settings like database, static files, and email backend properly for production.

## **Running the Project with Docker (Optional)**
If you've Dockerized the project, you can run it as follows:

```bash
docker-compose up --build
```
This will build the Docker image and run the Django application and the PostgreSQL service.

## **Video Links**
Watch the videos to learn in proper way.
https://drive.google.com/file/d/19m7z2sKFOUTvB05CbIheQgURWOAv-vh0/view?usp=sharing






