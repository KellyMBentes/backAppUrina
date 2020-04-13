# Equipe Blaschek
Estrutura back-end para o app Urina, utilizando django rest framework.

1 - Baixar mongoDB(com compass), PyCharm Professional e Python 3.8 
https://download.jetbrains.com/python/pycharm-professional-2019.3.4.exe 
https://www.mongodb.com/dr/fastdl.mongodb.org/win32/mongodb-win32-x86_64-2012plus-4.2.5-signed.msi/download 
https://www.python.org/ftp/python/3.8.2/python-3.8.2-amd64.exe

2 - Adicionar nas variáveis de ambiente(Path) o exe do mongoDB. 
Caminho default: C:\Program Files\MongoDB\Server\4.2\bin

3 - Criar uma pasta chamada data e dentro dela uma pasta no C:
Caminho: C:\data\db

4 - Abrir o mongoDB Compass e conectar sem fazer alteração

5 - Criar uma database chamada appUrina

6 - Logar com a conta iduff no PyCharm Professional

7 - Criar um projeto Django com nome appUrinaDjango e junto dele uma virtualenv com mesmo nome, e nela usar o Python.3.8.2

8 - Substituir os arquivos do projeto pelos do repositório

9 - Rodar o comando 'pip install requirements.txt' com a virtualenv(appUrinaDjango) ativada, para instalar todas dependências

10 - Realizar as migrações com python 'python manage.py migrate' e 'python manage.py makemigrations'

11 - Visualizar no Compass se as tabelas do django foram exibidas
