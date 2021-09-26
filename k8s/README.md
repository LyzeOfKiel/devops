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

## Helm

```bash
helm package app-python
helm package app-rust

helm install app-python ./app-python-0.1.0.tgz
helm install app-rust ./app-rust-0.1.0.tgz
```

![](./img/helm.png)

## Resource management

If we try to specify memory limit less then 6MB we will get the `CreateContainerError`:

![](./img/memory_error.png)

If there is not enogh memory for python application we will see `OOMKilled`:

![](./img/oom_killed.png)

Otherwise everything works correctly:

![](./img/memory_enough.png)
