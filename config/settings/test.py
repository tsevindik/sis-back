from .common import *

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS")

TEST_APPS = (
    'django_jenkins',
)

INSTALLED_APPS += TEST_APPS

JENKINS_TASKS = (
    'django_jenkins.tasks.run_pylint',
    'django_jenkins.tasks.run_pep8',
    'django_jenkins.tasks.run_pyflakes',
    'django_jenkins.tasks.run_flake8',
    'django_jenkins.tasks.run_sloccount',
)
