# HTTP time server

## Endpoints

`/` - get current Moscow time
`/visits` - get a list of all `/` visitors ip and corresponding time

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
