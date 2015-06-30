update:
	curl https://mkcert.org/generate/ -o certifi/cacert.pem

publish:
	python setup.py publish
