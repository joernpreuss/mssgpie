# Claude Code Instructions for mssgpie

## Project Context
- Django 4.2 LTS project
- Use `uv` for all package management (`uv add`, `uv sync`, `uv run`)
- PostgreSQL database

## Coding Standards
- Follow Django best practices
- Use `models.Model` for all Django models
- Always include `__str__` methods and Meta classes
- Use type hints where appropriate

## Git Workflow
- Small, focused commits
- One feature/fix per commit
- Use conventional commit messages

## Django Commands
Always use `uv run` prefix:
- `uv run python manage.py migrate`
- `uv run python manage.py makemigrations`
- `uv run python manage.py runserver`
- `uv run python manage.py test`
