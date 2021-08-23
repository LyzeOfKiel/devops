# HTTP time server

## Run

### Directly on target machine

```bash
pip install -r requirements.txt
gunicorn -c gunicorn.conf.py
```

### Or with docker

```bash
docker build -t app_python .
docker run -d -p 8000:8000 app_python
```

## Lint

Using [Pylint](https://github.com/PyCQA/pylint/):

```bash
pylint ./*.py
```
