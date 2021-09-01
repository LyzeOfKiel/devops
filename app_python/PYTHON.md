# Used best practices

## Python app

* Use prod ready web-framework - `Flask`
* `requirements.txt` file with all used dependencies for easy installation and build
* Use `.gitignore` file to remove unnecessary cache and build files/folders
* Use prod ready WSGI HTTP server - `gunicorn`
* Use server configuration file (`gunicorn.conf.py`) instead of CLI arguments
* Use flexible `Jinja2` templates for rendering instead of strings with HTML
* Use source code linter. `Pylint` in our case

## Unit tests

* Tests should be fast, simple and independent, i.e. each
    test coversonly one specific part of application
* Test should not duplicate logic of tested implementation
* Generally, tests should be deterministic
* Popular test framework. Pytest in our case
