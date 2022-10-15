# Machine_Learning_Project
# This is my first Machine Learning Project 
# software and account requirement

1. [GithubAccount](https://github.com/rohitpache29/Machine_Learning_Project)
2. [HerokuAccount](https://id.heroku.com/login)
3. [VScodeIDE](https://code.visualstudio.com/)
4. [GITCLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)


creating conda environment 
'''
conda create -p venv python==3.7 -y
'''

'''
conda activate venv/
'''

'''
pip install -r requirements.txt
'''

To add files to git

'''
git add .
or
git add file name
'''

to ignore file or folder from git we can write name of file/folder in .gitignore file 

To check git status
'''
git status
'''

To check all version maintained by git
'''
git log
'''

To create version/commit all changes by git
'''
git commit -m "massage"
'''

To send changes/version to github
'''
gir push origin main
'''

To check remote URL
'''
git remote -v
'''

To setup CI/CD pipeline in heroku we need 3 infomation

1. HEROKU_EMAIL =<>
2. HEROKU_API_KEY = <>
3. HEROKU_APP_NAME = <>


Build Docker Image
'''
docker build -t <Image_name>:<tag_name> .
'''

NOTE :Image name for docker muct be lowercase

To list docker image
'''
docker images 
'''

To run the  docker image 
'''
docker run -p 5000:5000 -e PORT=5000 687b40a805f7
'''

To check running containers in docker
'''
docker ps
'''

To stop docker container
'''
docker stop container_id
'''