import socket
import subprocess
import os
#x = socket.gethostbyname(socket.gethostname())
#x = str(x) #http://192.168.1.42/
#os.system(f'python manage.py runserver {x}:5555')
print((f'cd .\siteProjet\ ; python manage.py runserver 5555'))
#os.system(f'python .\siteProjet\manage.py runserver 5555')
#Remove-Item C:\Users\ouesl\Desktop\devEnv\cours\django\sojen\siteProjet\competition\__pycache__\ -Recurse ; Remove-Item C:\Users\ouesl\Desktop\devEnv\cours\django\sojen\siteProjet\db.sqlite3  ; Remove-Item C:\Users\ouesl\Desktop\devEnv\cours\django\sojen\siteProjet\competition\migrations -Recurse ;
#python manage.py makemigrations competition  ; python  .\manage.py migrate
#python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')"
os.system(f'python manage.py runserver 5555')
