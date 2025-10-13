# Mural Digital (Django + SQLite)

Projeto de uma aplicação Django que exibe banners cadastrados pelo admin em um carrossel Bootstrap.
O projeto está otimizado para o navegado google chrome para android 10 visando reutilizar equipamento tvbox doados a instituição.

**Características**
- Django + SQLite
- App `mural` com model `Banner` (imagem opcional)
- Armazenamento em disco local via `MEDIA_ROOT`
- Página pública simples com carrossel Bootstrap exibindo os banners (imagens em full HD)

**Requisitos**
- Python 3.9+
- Djanto 5.2+

**Como usar**
1. Crie e ative um virtualenv.
2. `pip install -r requirements.txt`
3. `python manage.py migrate`
4. `python manage.py createsuperuser` (crie usuário admin)
5. `python manage.py runserver`
6. Acesse o admin em `http://127.0.0.1:8000/admin/` e cadastre banners.
7. A página pública ficará em `http://127.0.0.1:8000/`

**Observações**
- As imagens devem ter resolução Full HD (1920x1080) para melhor resultado.
- Formatos permitidos: jpg, jpeg, png, gif (imagens).
- Altere o env_sample renomeando para '.env' e modifique com as suas variáveis de produção.
