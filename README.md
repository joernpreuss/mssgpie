# mssgpie

Message parsing and categorization application built with Django 4.2 LTS.

## Tech Stack
- Python 3.11+
- Django 4.2 LTS
- PostgreSQL
- uv (package manager)
- pytest

## Setup

### 1. Install uv (if not already installed)
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Install Dependencies
```bash
uv sync
```

### 3. Configure Environment
```bash
cp .env.example .env
# Edit .env with your database credentials and secret key
```

### 4. Start PostgreSQL (Docker)
```bash
docker-compose up -d
```

The database will be available at `localhost:5432` with credentials from docker-compose.yml.

### 5. Run Migrations
```bash
uv run python manage.py migrate
```

### 6. Create Superuser
```bash
uv run python manage.py createsuperuser
```

### 7. Run Development Server
```bash
uv run python manage.py runserver
```

Access the admin panel at: http://localhost:8000/admin/

## API Endpoints

### Messages
- `GET /messages/` - List all messages (paginated, 20 per page)
- `GET /messages/<id>/` - Message detail view

### Admin
- `/admin/` - Django admin interface for managing messages and categories

## Project Structure

```
mssgpie/
├── mssgpie/          # Django project settings
│   ├── settings.py   # Main configuration (uses django-environ)
│   ├── urls.py       # Root URL configuration
│   └── wsgi.py       # WSGI configuration
├── messages/         # Messages Django app
│   ├── models.py     # Message and Category models
│   ├── views.py      # ListView and DetailView for messages
│   ├── admin.py      # Admin configuration
│   └── urls.py       # App URL patterns
├── manage.py         # Django management script
├── pyproject.toml    # Project dependencies
└── .env              # Environment variables (not in git)
```

## Development

For more details, see [SPEC.md](SPEC.md).
