build:
	docker build  . --rm -t app
start:
	docker run --rm -it -e PORT_APP=3000 \
	-e DATABASE_PASSWORD=<database_password> \
	-e DATABASE_NAME=<database_name> \
	-e DATABASE_USER=<database_user> --name app -p 3000:3000 app
test:
	docker build  -f Dockerfile.test . --rm  -t app-test
	docker run --rm -it app-test
