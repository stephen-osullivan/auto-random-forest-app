install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

install-train:
	pip install --upgrade pip &&\
		pip install -r requirements_train.txt

lint:
	pylint --disable=R,C app.py

test:
	python -m pytest -vv