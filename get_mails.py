import re
import shutil
import os
import subprocess
def gemails(response):
    new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
    return new_emails
def create_dir(url):
    dir = os.getcwd()
    path = os.path.join(dir,url)
    if(os.path.exists(path)):
        subprocess.run(f'rmdir /s /q {path}' , shell=True)
        os.makedirs(path)
        os.chdir(path)
    else:
        os.makedirs(path)
        os.chdir(path)
def clust_dir(url):
    dir = os.getcwd()
    path = os.path.join(dir,url)
    if(os.path.exists(path)):
        subprocess.run(f'rmdir /s /q {path}' , shell=True)
        os.makedirs(path)
        os.chdir(path)
    else:
        os.makedirs(path)
        os.chdir(path)
    os.mkdir("Images")