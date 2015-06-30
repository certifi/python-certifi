from invoke import task, run

@task
def update():
    run("curl https://mkcert.org/generate/ -o certifi/cacert.pem")
