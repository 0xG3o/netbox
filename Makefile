.PHONY: help dev up down restart logs shell migrate collectstatic

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-15s %s\n", $$1, $$2}'

dev: ## Start development environment
	docker-compose -f docker-compose.dev.yml up

up: ## Start containers in background
	docker-compose -f docker-compose.dev.yml up -d

down: ## Stop and remove containers
	docker-compose -f docker-compose.dev.yml down

restart: ## Restart NetBox services (picks up .env changes)
	docker-compose -f docker-compose.dev.yml restart netbox netbox-worker
	@echo "✅ Restarted NetBox services - .env changes applied"

rebuild: ## Rebuild and restart (for code/plugin changes)
	docker-compose -f docker-compose.dev.yml up --build -d
	@echo "✅ Rebuilt and restarted - plugin code changes applied"

logs: ## Show logs (Ctrl+C to exit)
	docker-compose -f docker-compose.dev.yml logs -f netbox netbox-worker

shell: ## Open Django shell
	docker exec -it netbox-dev python manage.py shell

bash: ## Open bash shell in container
	docker exec -it netbox-dev bash

migrate: ## Run database migrations
	docker exec -it netbox-dev python manage.py migrate

collectstatic: ## Collect static files
	docker exec -it netbox-dev python manage.py collectstatic --no-input

createsuperuser: ## Create a superuser
	docker exec -it netbox-dev python manage.py createsuperuser

secretkey: ## Generate a new SECRET_KEY
	docker exec -it netbox-dev python generate_secret_key.py

clean: ## Remove all containers, volumes, and images
	docker-compose -f docker-compose.dev.yml down -v
	@echo "⚠️  All data has been removed"

status: ## Show running containers
	docker-compose -f docker-compose.dev.yml ps