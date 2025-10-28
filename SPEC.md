# mssgpie - Implementation Spec

## Zweck
Universeller Text-Klassifizierer für Nachrichten-Parsing und Kategorisierung.

## Tech Stack
- Python 3.11+
- Django 4.2 LTS
- PostgreSQL
- pytest

## Phase 1: Core
### Datenmodell
```python
from django.db import models

class Message(models.Model):
    # id wird automatisch erstellt
    text = models.TextField()
    sender = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    metadata = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.sender or 'Unknown'} at {self.created_at}"

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    patterns = models.JSONField(default=list)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
```

### API Endpoints
- POST /messages - Text eingeben, automatisch parsen
- GET /messages - Liste mit Filtern
- GET /messages/{id} - Details
- GET /similar/{id} - Ähnliche Nachrichten

### Parser
- Regex für Strukturerkennung
- Extrahiert: Sender, Datum, relevante Metadaten
- Erweiterbar für neue Patterns

## Phase 2: Intelligence
- Textähnlichkeit (TF-IDF → cosine similarity)
- Clustering ähnlicher Nachrichten
- Pattern-Matching für Kategorisierung

## Struktur
```
/mssgpie (Django project)
  /messages (Django app)
    /models
    /views
    /parsers
  /tests
pyproject.toml
.env.example
README.md
```
