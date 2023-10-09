ins-terr:
	pip install terraform-local

start-localstack:
	docker-compose up


tf-init:
	cd services
	tflocal init -upgrade

tf-plan:
	cd services
	tflocal plan

tf-apply:
	cd services
	tflocal apply


see_resources_as_graph:
#  see results in https://dreampuf.github.io/GraphvizOnline/
	tflocal graph



