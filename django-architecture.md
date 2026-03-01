# Django Architecture Overview

## What is Django?
Django is a high-level Python web framework used for rapid development and clean design.

## MVT Architecture

Django follows MVT pattern:

1. Model
   - Handles database logic
   - Defines data structure

2. View
   - Handles business logic
   - Connects model and template

3. Template
   - Handles UI (HTML)

## Request Flow

User → URL → View → Model → Template → Response

## Important Files in Django Project

- manage.py
- settings.py
- urls.py
- views.py
- models.py
- templates/
- static/

## Why Django is Powerful

- Built-in admin panel
- ORM (No raw SQL required)
- Authentication system
- Scalable
