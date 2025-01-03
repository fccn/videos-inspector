
DOCKER_COMPOSE = docker compose

up:
	$(DOCKER_COMPOSE) up
.PHONY: up

down:
	$(DOCKER_COMPOSE) down
.PHONY: up

rmi:
	docker rmi app:dev
.PHONY: up