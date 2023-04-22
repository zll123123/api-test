run:
	python3 -m black .
	python3 main.py 

push:
	python3 -m black .
	git add . && git commit -m "csv文件中的空值不传入接口处理" && git push

reqs:
	pipreqs ./ --force --encoding='utf-8-sig'

install:
	python3 -m pip install -r requirements.txt

