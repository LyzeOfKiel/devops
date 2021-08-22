# HTTP time server

## Run

```bash
pip install -r requirements.txt
gunicorn -c gunicorn.conf.py
```

## Lint

Using [Pylint](https://github.com/PyCQA/pylint/):

```bash
pylint ./*.py
```


