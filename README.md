![app_python](https://github.com/LyzeOfKiel/devops/actions/workflows/app_python.yml/badge.svg)

# DevOps Lab 1

## Structure

There are two separate modules in this project:

* **app_python** - Flask HTTP server which shows current time in Moscow timeone

* **app_rust** - Rocket HTTP server which shows current time in Moscow timeone

You can find more info about each project
in corresponding folders.

## Lint

Lint project markdown files using
[mdl](https://github.com/markdownlint/markdownlint) linter:

```bash
mdl .
```

Lint Dockerfiles using [Hadolint](https://github.com/hadolint/hadolint) linter:

```bash
hadolint **/Dockerfile
```

Lint `app_python` using [Pylint](https://github.com/PyCQA/pylint/):

```bash
pylint --rcfile app_python/.pylintrc app_python/
```

## Unit tests

```bash
pytest app_python/
```

## Build and run

```bash
docker-compose build
docker-compose up
```

