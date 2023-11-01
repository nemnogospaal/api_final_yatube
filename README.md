# Описание
<h2>Проект представляет собой финальную версию API для проекта Yatube.</h2>
<h3>С помощью api_yatube можно запрашивать, а также добавлять данные о постах, комментариях, группах и подписках проекта Yatube.</h3>
<h3>Добавлена система аутентификации</h3>

**Как запустить проект:**
Клонировать репозиторий и перейти в него в командной строке:

```git clone https://github.com/nemnogospaal/api_final_yatube.git```

```cd api_final_yatube```

Cоздать и активировать виртуальное окружение:

```python3 -m venv env```

```source env/bin/activate```

Установить зависимости из файла requirements.txt:

```python3 -m pip install --upgrade pip```

```pip install -r requirements.txt```

Выполнить миграции:

```python3 manage.py migrate```

Запустить проект:

```python3 manage.py runserver```

**Примеры запросов**

Получить список всех постов (GET):

```http://127.0.0.1:8000/api/v1/posts/```

Получить конкретный пост (GET):

```http://127.0.0.1:8000/api/v1/posts/1/```

Получить список подписок (GET):

```http://127.0.0.1:8000/api/v1/follow/```

Создать пост (POST):

```http://127.0.0.1:8000/api/v1/posts/```

