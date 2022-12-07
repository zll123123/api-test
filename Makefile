run:
	python3 -m black .
	python3 main.py

push:
	python3 -m black .
	git add . && git commit -m "统一使用相对路径&csv数据使用;分割解析" && git push

reqs:
	pipreqs ./ --force --encoding='utf-8-sig'

install:
	python3 -m pip install -r requirements.txt
