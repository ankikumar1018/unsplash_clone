# Django Unsplash Clone

A Django-based web application that mimics some of the core functionalities of Unsplash, allowing users to view, download, and interact with images.

## Features

- User authentication (registration, login, logout)
- Image browsing and downloading
- Random image API endpoint
- Responsive design for various screen sizes

## Prerequisites

- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/django-unsplash-clone.git
   cd django-unsplash-clone
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

7. Visit `http://localhost:8000` in your web browser to see the application.

## Usage

- Register a new account or log in with existing credentials.
- Browse the image gallery on the home page.
- Click on images to view details and download options.
- Use the random image API endpoint: `http://localhost:8000/api/random/`
- Access your profile page to view and edit your information.

## Project Structure

```
unsplash_clone/
├── manage.py
├── unsplash_clone/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── images/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
├── templates/
│   ├── base.html
│   ├── image_list.html
|   ├── login.html
│   ├── register.html
│   └── profile.html
└── static/
    └── css/
        └── style.css
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Django framework
- Django Rest Framework
- Inspiration from Unsplash

## TODO

- Implement image upload functionality
- Add tagging system for images
- Implement search functionality
- Add pagination for image list
- Implement user favorites or collections
