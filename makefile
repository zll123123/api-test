run:
	yapf -ri ./
	python3 main.py

push:
	git add . && git commit -m "chendong" && git push