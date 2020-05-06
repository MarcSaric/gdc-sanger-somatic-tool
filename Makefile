MODULE = gdc_sanger_tools
.PHONY: init init-* lint requirements
init: init-pip

init-pip:
	@echo
	@echo -- Installing pip packages --
	pip3 install --no-cache-dir -r requirements.txt

lint:
	@echo
	@echo -- Lint --
	python3 -m flake8 \
		--ignore=E501,F401,E302,E502,E126,E731,W503,W605,F841,C901 \
		${MODULE}/

requirements:
	python3 setup.py -q capture_requirements --dev
	pip-compile -o requirements.txt requirements.in

.PHONY: test test-*

test: lint test-unit

test-unit:
	@echo
	@echo -- Unit Test --
	python3 -m pytest --cov=${MODULE} tests/

