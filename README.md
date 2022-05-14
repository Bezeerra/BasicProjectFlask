
para o pip voltar a funcionar
python -c "import pip.__main__"
python -m pip install --upgrade --force-reinstall pip

CTRL+SHIFT+V tem como visualizar o readme.md

- \sql
- connect root@localhost:3306
- show databases;
- USE database;
- show tables;
- describe <table>

- INSET INTO pet VALUES ('','')
- SELECT name FROM pet WHERE conditions... AND .. OR
- SELECT * FROM pet -> selecionar tudo

- SELECT * FROM pet WHERE especies = 'Homem';
- SELECT name, especies FROM pet
- SELECT name, birth FROM pet ORDER BY birth DESC;



==========> in flask
<link rel="stylesheet" href="{{url_for('static', filename='style.css')}}">




# Chamada para o terminal flask
    - app.shell_context_processor()
    export FLASK_APP=main.py

