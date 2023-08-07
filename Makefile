run:
	python3 -m black .
	python3 main.py 

push:
	python3 -m black .
	git add . && git commit -m "除设置平台方信息外其他接口均测试通过" && git push

reqs:
	pipreqs ./ --force --encoding='utf-8-sig'

install:
	python3 -m pip install -r requirements.txt

