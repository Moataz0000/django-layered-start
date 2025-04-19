# Django Layered Start 🏗️

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/Django-4.0+-green.svg)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Django starter project that applies **clean architecture** principles through a structured layered approach to build more maintainable web applications.

## 🏛️ Architecture Overview

This project provides a structured layered architecture that separates concerns:

```
your_app/
├── presentation/       # Handles how data is presented to the user
│   ├── views.py        # View functions/classes
│   ├── urls.py         # URL routing
│   └── serializers.py  # API serializers
│
├── application/        # Contains business logic and use cases
│   └── services.py     # Service classes/functions
│
├── domain/             # Core domain logic and business rules
│   ├── validators.py   # Domain validation
│   ├── selectors.py    # Query operations
│   └── utilities.py    # Domain-specific utilities
│
└── infrastructure/     # External interfaces like DB, APIs, etc.
    └── models.py       # Django ORM models
```

## ✨ Features

- **Clean Organization**: Separates your code into logical layers
- **Improved Maintainability**: Makes your code easier to understand and modify
- **Better Testability**: Simplifies unit testing by separating concerns
- **Enhanced Collaboration**: Developers can work on different layers simultaneously
- **Environment Setup**: Includes a ready-to-use `.env` file structure
- **Requirements Management**: Separate files for local and production dependencies

## 🚀 Getting Started

### Installation

```bash
pip install django-layered-start
```

### Project Setup

```bash
# Create a new Django project
python -m django_layered_start startproject myproject

# Create a new app with layered structure
python -m django_layered_start startapp myapp
```

### Project Structure

After creating a project and app, you'll have a structure like:

```
myproject/
├── manage.py
├── myproject/
│   └── settings.py, urls.py, etc.
├── myapp/
│   ├── presentation/
│   ├── application/
│   ├── domain/
│   └── infrastructure/
└── requirements/
    ├── local.text
    └── production.text
```

## 🔍 Usage Guidelines

### Presentation Layer

The presentation layer handles how data is presented to users and how they interact with your application. It includes:

- **Views**: Django view functions or class-based views
- **URLs**: URL routing patterns
- **Serializers**: For API response formatting (using Django REST Framework)

### Application Layer

The application layer contains business logic and use cases. It orchestrates the flow of data and implements business rules:

- **Services**: Functions that implement business operations and use cases

### Domain Layer

The domain layer represents your core business logic and rules:

- **Validators**: Domain validation rules
- **Selectors**: Query operations for retrieving domain entities
- **Utilities**: Helper functions specific to your domain

### Infrastructure Layer

The infrastructure layer handles external interfaces and technical details:

- **Models**: Django ORM models for database access

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

