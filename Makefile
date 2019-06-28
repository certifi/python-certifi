update:
	curl -s https://mkcert.org/generate/ > certifi/cacert.pem
	echo "\n# Skytap ROOTCA \n#\n#" >> certifi/cacert.pem
	curl -s http://tuk8packages1.qa.skytap.com/static/skytap_ca_cert/skytap-ca.crt >> certifi/cacert.pem

publish:
	python setup.py sdist bdist_wheel
	twine upload --skip-existing --sign dist/*
