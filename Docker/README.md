# Run HiddenEye in Docker Compose

![docker](https://img.shields.io/badge/Docker-v19.03.12-blue?style=plastic&logo=docker)
![dockercompose](https://img.shields.io/badge/Docker_Compose-v1.25.4-orange?style=plastic&logo=docker)
![Maintainer](https://img.shields.io/badge/Maintainer-Equinockx-success?style=plastic&logo=terraform)

## Runnin within container

![running](https://github.com/MoisesTapia/HiddenEye/blob/Docker/Docker/images/start.png)
![link](https://github.com/MoisesTapia/HiddenEye/blob/Docker/Docker/images/URL.png)

## Requeriments

- [x] Docker
- [x] docker-compose

## Usage Mode

Clone the repo from Github

```bash
git clone https://github.com/DarkSecDevelopers/HiddenEye
cd HiddenEye/Docker
```

Run docker-compose

```bash
docker-compose up --build -d
```

'_Don not need redirection of ports 'cause the container is exposed to
internet_' <br> Verify of the container is running with:

```bash
docker-compose ps
```

![ps](https://github.com/MoisesTapia/HiddenEye/blob/Docker/Docker/images/ps.png)

Executing HiddenEye inside of container

```bash
docker-compose exec hidden python3 HiddenEye.py
```

![exec](https://github.com/MoisesTapia/HiddenEye/blob/Docker/Docker/images/executing.png)

## Persist Data

When we make or buils the service with `docker-compose up --build -d` this
persist the data templates in the same folder `WebTemplate`. If you add the new
Template in `WbeTemplate` this will be reflected in the container and you can
use it.

To add WebTemplate you juste need add them in this folder and done

- [x] `equinockx~/Webtemplate$ cp * Docker/Webtemplate`
- [x] WebTemplate

## First Start the services

```bash
docker-compose up --build -d
```

## Down the container

```bash
docker-compose down
```

## Stop the services

```bash
docker-compose stop
```

## Start the services

With this command docker-compose will initialize the service stopped

```bash
docker-compose start
```
