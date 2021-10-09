# Para contribuir com o projeto.

1. Criar um diretório dentro do seu workspace para conter o projeto
2. Criar um python virtualenv para poder trabalhar com o projeto com o comando
~~~
    python3.8 -m venv env.emprestimos
~~~
3. A estrutura do projeto deve ficar parecida com a demonstrada abaixo
~~~

    |__ emprestimos
        |__env.emprestimos
        |__ src

~~~
4. Dentro da pasta src, que devemos criar, iremos clonar o projeto git

~~~
    git clone git@github.com:jdcarvalho/controle-emprestimos.git
~~~

5. Ative o ambiente e instale os requisitos de código

~~~
    source ./env.emprestimos/bin/activate
    cd src/emprestimos
    pip install -r requirements.txt
~~~

6. Devemos criar as migrations e migrar o projeto com os comandos especificados abaixo

~~~
    ./manage.py makemigrations
    ./manage.py migrate    
~~~

7. Devemos então coletar o estáticos o projeto

~~~
    ./manage.py collectstatic
~~~

8. Crie sua própria branche (Seguimos git flow) ou faça um fork para aplicar um pull request
