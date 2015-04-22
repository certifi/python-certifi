update:
	curl http://ci.kennethreitz.org/job/ca-bundle/lastSuccessfulBuild/artifact/cacerts.pem -o certifi/cacert.pem

publish:
	python setup.py publish
