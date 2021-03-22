.PHONY: down
down: docker-compose.yaml
	@echo "$@"
	docker-compose down

.PHONY: run
run: down build docker-compose.yaml
	@echo "$@"
	docker-compose up

.PHONY: build
build: build_selenium_docker
	@echo "$@"

.PHONY: build_ocr
build_selenium_docker: Dockerfile
	@echo "$@"
	docker build -f Dockerfile -t selenium_docker:test  .
