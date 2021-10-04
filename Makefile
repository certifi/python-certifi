update:
	curl https://mkcert.org/generate/all/except/dst | ./strip-non-ascii > certifi/cacert.pem

publish:
	python setup.py sdist bdist_wheel
	twine upload --skip-existing --sign dist/*
