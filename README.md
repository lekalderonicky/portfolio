![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![CI](https://github.com/lekalderonicky/portfolio/actions/workflows/ci.yml/badge.svg)

# Simple Django Portfolio

This repository contains a minimal Django portfolio app (`portfolio`) that showcases projects and provides an admin interface to manage them.

Contents
 - `mysite/` — Django project settings and URLs
 - `portfolio/` — main app (models, views, templates, admin)
 - `templates/` — shared templates
 - `static/` — CSS & static assets
 - `media/` — uploaded images (created at runtime)
 - `scripts/` — helper scripts for setup/demo data

Requirements
- Python 3.10+ (this workspace used 3.13)
- pip
- Git

Quick install (Windows PowerShell)

1. Create and activate a virtual environment

```powershell
python -m venv .venv
# If Activate.ps1 is blocked, run PowerShell as Administrator once and: Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies

```powershell
.\.venv\Scripts\python -m pip install -r requirements.txt
```

3. Apply database migrations

```powershell
.\.venv\Scripts\python manage.py migrate
```

4. Create a superuser (admin)

```powershell
.\.venv\Scripts\python manage.py createsuperuser
```

Alternatively you can run the helper script included in `scripts/` to auto-create the sample superuser and demo data.

5. Run the development server

```powershell
.\.venv\Scripts\python manage.py runserver
```

Open http://127.0.0.1:8000/ to view the portfolio and http://127.0.0.1:8000/admin to manage projects.

Media and images

- Uploaded images are stored in the `media/` directory during development. The project is configured to serve `MEDIA_URL` in DEBUG mode.
- To upload project images, sign in to the admin and add/edit a Project.

Deployment notes

- The built-in development server is not suitable for production. For deployment you should use a WSGI/ASGI server (Gunicorn, uWSGI, Daphne) behind a reverse proxy and configure static/media serving (S3, CDN, or web server).
- SECRET_KEY must be kept secret in production and environment variables used for configuration.

Useful commands

- Run Django checks: `.\.venv\Scripts\python manage.py check`
- Create sample projects (provided script): `.\.venv\Scripts\python .\scripts\add_sample_projects.py`
- Create the scripted superuser: `.\.venv\Scripts\python .\scripts\create_superuser_fixed.py`

Troubleshooting

- If PowerShell refuses to run `Activate.ps1`, set the execution policy for the session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

- If the site can't be reached from another device on your LAN: ensure the dev server is bound to `0.0.0.0` and that the Windows Firewall allows inbound connections on the chosen port. For example:

```powershell
# start server bound to all interfaces
.\.venv\Scripts\python manage.py runserver 0.0.0.0:8000

# allow inbound port 8000 through Windows Firewall (Admin PowerShell)
# New-NetFirewallRule -DisplayName "Allow Django dev 8000" -Direction Inbound -LocalPort 8000 -Protocol TCP -Action Allow
```

Contributing

- Create a fork and open a pull request. The repo includes a `.gitignore` and minimal structure so it's ready to push.

License

- This project has no license file. Add a LICENSE if you want to make it open-source.

Contact

- Email: lekalderonicky@gmail.com

Enjoy — let me know if you'd like a CI pipeline added, a Dockerfile for local development, or templates for production deployment.
