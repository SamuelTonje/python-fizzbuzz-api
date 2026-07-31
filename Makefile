.PHONY: help run-app up down restart build logs bash test ruff migration migrate rollback clean


help:
	@echo "Available commands:"
	@echo "  make run-app      Build, start, migrate, lint and test"
	@echo "  make up           Start application"
	@echo "  make down         Stop application"
	@echo "  make build        Build containers"
	@echo "  make logs         Show logs"
	@echo "  make bash         Open shell"
	@echo "  make test         Run tests"
	@echo "  make ruff         Run linting"
	@echo "  make migration    Create migration"
	@echo "  make migrate      Apply migrations"
	@echo "  make rollback     Rollback migration"
	@echo "  make clean        Clean project"


run-app: build up migrate ruff test
	@echo "Application ready 🚀"


build:
	docker compose build


up:
	docker compose up -d


down:
	docker compose down


restart:
	docker compose restart


logs:
	docker compose logs -f


bash:
	docker compose exec python bash


migrate:
	docker compose exec python alembic upgrade head


migration:
ifndef m
	$(error Migration name is required. Usage: make migration m="create statistics table")
endif
	docker compose exec python alembic revision --autogenerate -m "$(m)"


rollback:
	docker compose exec python alembic downgrade -1


ruff:
	docker compose exec python ruff check .


test:
	docker compose exec python pytest


clean:
	@echo "Cleaning project resources..."
	docker compose down -v --remove-orphans
	@echo "Done."