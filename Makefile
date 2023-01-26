build:
	docker build -t django-vue3 -f Dockerfile . 

run:
	docker run -p 8200:80 --name django-vue3 --rm  django-vue3

stop:
	docker stop django-vue3

push:
	docker build --platform=linux/amd64 -t codingforentrepreneurs/django-vue-3:latest -f Dockerfile . 
	docker push codingforentrepreneurs/django-vue-3