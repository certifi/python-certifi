update:
	curl http://ci.kennethreitz.org/job/ca-bundle/lastSuccessfulBuild/artifact/cacerts.pem -o certifi/cacert.pem

publish:
	python setup.py register
	python setup.py sdist upload
	python setup.py bdist_wheel upload
