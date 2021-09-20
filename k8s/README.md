# Deployment description

## CLI deployment

```bash
kubectl create deployment app-python --image=lok52/app_python:latest
kubectl expose deployment app-python --type=LoadBalancer --port=8000
```

![](./img/cli.png)

## Deployment via configuration files

```bash
kubectl apply -f k8s/app-python/
```

![](./img/conf_app_python.png)

## Bonus: deployment of extra app

```bash
kubectl apply -R -f ./k8s
```

![](./img/conf.png)
