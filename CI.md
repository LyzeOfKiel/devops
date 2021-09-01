# CI best practices

## General

* Utilize cache from different build tools and dependencies for faster CI
* Use repository encrypted secrets during CI, e.g. for docker login
* Run jobs efficiently, i.e. require dependent jobs
    to be successful before running next ones
* Use popular and verified actions from Github marketplace

## Jenkins

* Use modules in actions instead of bash scripts
* Use temporary github token for Jenkins
* Use docker agent to simplify process and isolate environment
* With docker agent use specific image version
