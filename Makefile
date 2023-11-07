run:
	python3 -m black .
	python3 apitest/main.py

push:
	python3 -m black .
	git add . && git commit -m "完善初始化数据库部分" && git push

reqs:
	pipreqs ./ --force --encoding='utf-8'

install:
	python3 -m pip install -r requirements.txt


