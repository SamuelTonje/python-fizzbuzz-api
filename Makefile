.PHONY: docker-clean
clean: ## Destroy all Docker containers, images, volumes and networks
	@echo "Suppression complète de Docker (conteneurs, images, volumes, réseaux)..."
	@docker rm -f $$(docker ps -aq) 2>/dev/null || true
	@docker volume rm $$(docker volume ls -q) 2>/dev/null || true
	@docker system prune -a --volumes -f
	@docker network prune -f
	@echo "Docker complètement nettoyé !"
