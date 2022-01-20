import os
import shutil

root_dir = os.path.join('./', 'my_project')
templates_dir = os.path.join(root_dir, 'templates')
for root, dirs, files in os.walk(root_dir):
    if os.path.split(root)[1] == 'templates' and root != templates_dir:
        try:
            shutil.copytree(os.path.join(root, dirs[0]), os.path.join(templates_dir, dirs[0]))
        except FileExistsError:
            print(f'файлы из каталога {root} уже были скопированы')
