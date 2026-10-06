# Hangarin

A Django web application built as an individual midterm project for a Python and Django course. Hangarin is also installable on mobile phones and desktops as a Progressive Web App (PWA).

**See through this link:** https://vanii.pythonanywhere.com/

## Features

- Create, view, update, and delete records (CRUD), including priorities
- Admin dashboard for managing data
- Sample data generation with Faker
- Installable as a PWA (home screen icon, standalone display, service worker)
- Deployed on PythonAnywhere

## Tech Stack

| Area | Tools |
| --- | --- |
| Language | Python 3.13 |
| Framework | Django |
| PWA | django-pwa |
| Test data | Faker |
| Hosting | PythonAnywhere |

## Project Structure

```
Hangarin/
├── hangarinsite/        # Django project folder (contains manage.py)
│   ├── hangarinsite/    # Project settings and root URLs
│   ├── hangarin/        # Main app (models, views, urls, templates)
│   └── static/          # CSS, JS, images, PWA icons, serviceworker.js
├── .gitignore
└── README.md
```

## Getting Started (Local)

### 1. Clone the repository

```bash
git clone https://github.com/Krakenxz-12/Hangarin.git
cd Hangarin/hangarinsite
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install django django-pwa faker
```

### 4. Set up the database

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 5. (Optional) Add sample data

```bash
python manage.py <your-seed-command>
```

### 6. Run the server

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Progressive Web App (PWA)

Hangarin uses [django-pwa](https://pypi.org/project/django-pwa/) to provide a web manifest and service worker.

- Settings are in `settings.py` under `PWA_APP_*`
- The service worker is at `static/js/serviceworker.js`
- App icons are in `static/img/`

**To install on your phone:** open the live site in Chrome (Android) or Safari (iPhone) and choose **Add to Home Screen**.

## Deployment on PythonAnywhere

1. Pull the latest code in a Bash console:
   ```bash
   cd ~/Hangarin/hangarinsite
   git pull
   ```
2. Install dependencies in the virtualenv:
   ```bash
   pip install django-pwa faker
   ```
3. Apply migrations and collect static files:
   ```bash
   python manage.py migrate
   python manage.py collectstatic
   ```
4. On the **Web** tab, map `/static/` to your `STATIC_ROOT` folder.
5. Click **Reload**.

## Author
<table>
    <tr>
    <td align = "center" width = "100">
    <a href="https://github.com/Krakenxz-12">
    <img src = "https://avatars.githubusercontent.com/u/229779464?v=4" alt= "Pau Photo"
    width = "150"
    style = "border-radius: 70%;">
</a>
    <p>
        <b>Name: Paulene Faith L. Magsadia</b><br>
        <nobr><b>Email: 202480133@psu.palawan.edu.ph</nobr></b>
    </p>

<a href="https://www.facebook.com/pau.magsadia">
    <img src = "img/Facebook.png" alt = "Facebook icon" width = "30">
</a>    
<a href="https://github.com/Krakenxz-12">
    <img src = "img/Github_black.png" alt = "Github icon" width = "30">
</a> 
</td>

<div style = "padding-top: 30px"></div>
<td width = "100">&nbsp;</td>

</table>

## License

This project was made for educational purposes.
