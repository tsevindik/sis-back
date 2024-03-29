### Jenkins
- Install Jenkins
```
wget -q -O - https://pkg.jenkins.io/debian/jenkins-ci.org.key | sudo apt-key add -
sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt-get update
sudo apt-get install jenkins
```
- By using its user interface (8080 port by default) create new item which is **a freestyle project**
- Following options have importance:
- **General**
```
GitHub project:
- Project url: https://github.com/tsevindik/sis-back/
```
- **Source Code Management**
```
Git:
- Repositories:
    - Repository URL: https://github.com/tsevindik/sis-back.git (Add credidentals)
- Branches to build:
    - Branch Specifier: */production
- Repository browser: githubweb
    - URL: https://github.com/tsevindik/sis-back
```
- **Build Triggers**
```
- GitHub hook trigger
```
- **Build Environment**
```
- Delete workspace before build starts
```
- **Build**
```
- Execute shell:
    - Command:
    . /home/ubuntu/.bashrc
    . /home/ubuntu/.virtualenvs/sis/bin/activate
    pip3 install -r ./setup/require/venv/test.txt
    cp ./setup/env/test.env .env
    python manage.py migrate
    python manage.py jenkins --enable-coverage
```
- **Post-build Actions**
```
- Publish Cobertura Coverage Report:
    - Cobertura xml report pattern: reports/coverage.xml
- Publish JUnit test result report:
    - Test report XMLs: reports/junit.xml
- Publish SLOCCount analysis results:
    - SLOCCount reports: reports/sloccount.report
- Report Violations:
    - pep8: reports/pep8.report
    - pylint: reports/pyflakes.report, reports/pylint.report, reports/flake8.report
- Set GitHub commit status

```
- For setting GitHub commit status go Github **settings > personal access tokens** and generate new token
- Go to Jenkins server, **manage jenkins > configure system** and add GitHub server by using generated token
