# SAC-PRICE Financial Simulator

This web application simulates SAC and PRICE financing methods displaying a comparison using tables and charts that allow users to choose the best finance type.

## Setup

Clone the repository current repository:

```sh
git@github.com:lucassavioli/django-vue-financing.git
```

Navigate to the project directory:

```sh
cd django-vue-financing
```

Create a virtual environment:

```sh
python3 -m venv venv
```

## Install dependencies

#### Backend (Django)

Install the dependencies of the backend using the requirements.txt.

```sh
pip install -r requirements.txt
```

#### Frontend (Vue 3)

```sh
cd frontend && npm install
```

## Starting Django and React

Run migrations, and start the backend server:

```sh
python manage.py migrate
python manage.py runserver
```

Navigate to the frontend directory and run

```sh
cd frontend
npm run dev
```
