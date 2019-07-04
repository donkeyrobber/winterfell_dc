setup:
	docker-compose build
	echo "giving postgres a second or two..."
	sleep 10
	docker-compose run web manage.py migrate
	docker-compose run web manage.py loaddata items.yaml
	docker-compose run web manage.py loaddata orders.yaml
run:
	docker-compose up
test:
	docker-compose run web manage.py test
lint:
	docker-compose run --entrypoint="flake8" web .
