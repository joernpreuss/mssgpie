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

### 4. Database Setup
Create a PostgreSQL database:
```bash
createdb mssgpie
```

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

## Development

More documentation coming soon...
