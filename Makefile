run:
	python3 -m black .
	python3 main.py 

push:
	python3 -m black .
	git add . && git commit -m "基本完成自动部署脚本" && git push

reqs:
	pipreqs ./ --force --encoding='utf-8-sig'

install:
	python3 -m pip install -r requirements.txt
