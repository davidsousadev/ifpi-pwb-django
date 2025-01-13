# **IFPI - PWB Django Tutorial**

Este repositório contém um tutorial passo a passo para a instalação e configuração de um projeto Django. [Site Oficial](https://www.djangoproject.com/)

---

## **1. Requisitos**

Antes de começar, certifique-se de ter os seguintes requisitos instalados:

- **Python 3.8+**
- **pip** (Python Package Installer)

---

## **2. Instalação do Ambiente Virtual**

Crie e ative um ambiente virtual para isolar as dependências do projeto:

```bash
# Criando o ambiente virtual
python3 -m venv venv-django

# Ativando o ambiente virtual
source venv-django/bin/activate
```

---

## **3. Instalando o Django**

Com o ambiente virtual ativo, instale o Django usando o pip:

```bash
# Instalando o Django
python3 -m pip install Django
```

Verifique se a instalação foi bem-sucedida:

```bash
# Verificando a versão do Django
python3 -m django --version
```

---

## **4. Criando o Projeto Django**

1. Crie um diretório para o projeto:

```bash
mkdir djangotutorial
```

2. Dentro do diretório, inicie um novo projeto Django chamado **mysite**:

```bash
django-admin startproject mysite djangotutorial
```

3. Acesse o diretório do projeto:

```bash
cd djangotutorial/
```

4. Execute o servidor de desenvolvimento:

```bash
python3 manage.py runserver
```

---

## **5. Criando um App Django**

Para criar um app chamado **polls**, execute o seguinte comando:

```bash
python3 manage.py startapp polls
```

Após criar o app, execute o servidor novamente:

```bash
python3 manage.py runserver
```

---

## **6. Executando Migrações**

Crie as migrações iniciais do banco de dados:

```bash
python3 manage.py migrate
```

Se houver alterações no modelo de dados do app **polls**, gere novas migrações:

```bash
python3 manage.py makemigrations polls
```

Aplique as migrações ao banco de dados:

```bash
python3 manage.py migrate
```

---

## **7. Acessando o Shell do Django**

Para interagir com o Django por meio de um shell interativo, use o comando:

```bash
python3 manage.py shell
```

---

## **8. Criando um Superusuário**

Para acessar o painel administrativo do Django, é necessário criar um superusuário:

```bash
python3 manage.py createsuperuser
```

Siga as instruções para definir o nome de usuário, e-mail e senha.

---

## **9. Testando o App**

Execute os testes automatizados para garantir que tudo está funcionando corretamente:

```bash
python3 manage.py test polls
```

---

## **10. Instalando o Debug Toolbar**

Para facilitar a depuração durante o desenvolvimento, instale o **Django Debug Toolbar**:

```bash
python3 -m pip install django-debug-toolbar
```

Verifique o caminho da instalação do Django, se necessário:

```bash
python3 -c "import django; print(django.__path__)"
```

