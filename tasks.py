from invoke import task, run

@task
def update():
    run("curl http://ci.kennethreitz.org/job/ca-bundle/lastSuccessfulBuild/artifact/cacerts.pem -o certifi/cacert.pem")
