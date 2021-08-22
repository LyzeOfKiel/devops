# DevOps Lab 1

## Structure

There are two separate modules in this project:

* **app_python** - Flask HTTP server which shows current time in Moscow timeone

* **app_rust** - Rocket HTTP server which shows current time in Moscow timeone

You can find more info about each project (how to run, lint, etc.) in corresponding folders.

## Lint

Lint project markdown files using [mdl](https://github.com/markdownlint/markdownlint) linter:

```bash
mdl .
```

Lint Dockerfiles using [Hadolint](https://github.com/hadolint/hadolint) linter:

```bash
hadolint **/Dockerfile
```
