publish:clean
	python setup.py sdist
	twine upload dist/*
test:
	export PYTHONPATH=$(pwd);pytest ./tests --cov=splunk_log_handler
clean:
	rm -rf dist
	rm -rf *.egg-info	
