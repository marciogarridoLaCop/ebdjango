# Implantar uma aplicação Django no Elastic Beanstalk

## Pré-requisitos

Para usar qualquer serviço da AWS, incluindo o Elastic Beanstalk, você precisa ter uma conta e credenciais da AWS. 

Para seguir este tutorial, você deve ter todos os Pré-requisitos comuns para Python instalados, incluindo os seguintes pacotes:

    Python 3.7 ou posterior

    pip

    virtualenv

    awsebcli - https://docs.aws.amazon.com/pt_br/elasticbeanstalk/latest/dg/eb-clcd ..i3-install-advanced.html

Configurar um ambiente virtual Python e instalar o Django

Crie um ambiente virtual com virtualenv e use-o para instalar o Django e suas dependências. Usando um ambiente virtual, é possível saber exatamente de quais pacotes a aplicação precisa, para que eles sejam instalados nas instâncias do Amazon EC2 que executam a aplicação.

As etapas a seguir demonstram os comandos que você deve inserir para sistemas baseados em Unix e Windows, mostrados em guias separadas.

Para configurar o ambiente virtual

    Crie um ambiente virtual denominado eb-virt.

    virtualenv ~/eb-virt

Ative o ambiente virtual.

    source ~/eb-virt/bin/activate

Instale a versao do Django 

    pip install Django==3.2.16


Para gerar um aplicativo Django

    django-admin startproject ebdjango


Va para o diretorio do projeto 

    cd ebdjango

Teste se o servidor esta rodando 

    python manage.py runserver

Configurar a aplicação Django para o Elastic Beanstalk

Agora que você tem um site desenvolvido pelo Django em sua máquina local, você pode configurá-lo para implantação com o Elastic Beanstalk.

Por padrão, o Elastic Beanstalk procura um arquivo chamado application.py para iniciar sua aplicação. Como isso não existe no projeto Django que você criou, é necessário fazer alguns ajustes no ambiente do aplicativo. Também é necessário definir variáveis de ambiente para que os módulos do aplicativo possam ser carregados.

Como configurar seu site para o Elastic Beanstalk

Dentro da venv gere as dependencias.Execute pip freeze e salve a saída em um arquivo chamado requirements.txt.

    pip freeze > requirements.txt

Crie o diretorio para armazenar as configuracoes 
    mkdir .ebextensions

No diretório .ebextensions, adicione um arquivo de configuração chamado django.config com o texto a seguir.

    exemplo ~/ebdjango/.ebextensions/django.config

Dentro deste arquivo, copie as seguintes configuracoes 


option_settings:
  aws:elasticbeanstalk:container:python:
    WSGIPath: ebdjango.wsgi:application

Configuracao dos arquivos estáticos. No mesmo diretório, crie o arquivo de configuracao

    exemplo ~/ebdjango/.ebextensions/static-files.config


Dentro deste arquivo, copie as seguintes configuracoes

option_settings:
  aws:elasticbeanstalk:environment:proxy:staticfiles:
    /static: static

Abra o arquivo settings.py no diretório ebdjango. Localize a configuração ALLOWED_HOSTS e adicione o nome de domínio do aplicativo que você encontrou na etapa anterior ao valor da configuração. Se você não encontrar essa configuração no arquivo, adicione-a em uma nova linha.

    STATIC_URL = '/static/'
    STATIC_ROOT = 'static'

Gere o arquivo de configuracao de dados estaticos 

    python manage.py collectstatic


Inicialize o repositório da EB CLI com o comando eb init:

    eb init -p python-3.7 django-env-api

Crie um ambiente e implante o aplicativo nele com eb create.

    eb create django-env

Vefifique após o deploy o status de sua aplicacao



Environment details for: django-env
  
        Application name: django-env-api
        Region: us-east-1
        Deployed Version: app-221127_143837260353
        Environment ID: e-trpgxqywtp
        Platform: arn:aws:elasticbeanstalk:us-east-1::platform/Python 3.7 running on 64bit Amazon Linux 2/3.4.1
        Tier: WebServer-Standard-1.0
        CNAME: django-env-api-aws.eba-xmduvwi5.us-east-1.elasticbeanstalk.com
        Updated: 2022-11-27 17:39:59.261000+00:00
        Status: Ready
        Health: Green

Seu nome de domínio do ambiente é o valor da propriedade CNAME.

Abra o arquivo settings.py no diretório ebdjango. Localize a configuração ALLOWED_HOSTS e adicione o nome de domínio do aplicativo que você encontrou na etapa anterior ao valor da configuração. Se você não encontrar essa configuração no arquivo, adicione-a em uma nova linha.
    
    ...
    ALLOWED_HOSTS = ['django-env-api-aws.eba-xmduvwi5.us-east-1.elasticbeanstalk.com']


Salve o arquivo e, em seguida, implante o aplicativo executando eb deploy. Quando você executa eb deploy, a EB CLI empacota o conteúdo do diretório do projeto e implanta-o em seu ambiente.


    git commit -m 'sua versao' 
    eb deploy

Quando o processo de atualização do ambiente for concluído, abra o site com eb open.

    eb open

    Isso abre uma janela do navegador usando o nome de domínio criado para o seu aplicativo. Você deve ver o mesmo site Django que você criou e testou localmente.

Se o aplicativo não aparecer em execução ou se houver uma mensagem de erro, consulte Solução de erros de implantação para obter ajuda sobre como determinar a causa do erro.

Se a aplicação aparecer em execução, você implantou sua primeira aplicação Django com o Elastic Beanstalk.