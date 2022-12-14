## Telegram Bot for watching the schedule of the Kyiv Polytechnic Institute
This is a bot for [Telegram](https://telegram.org/) written on [Aiogram](https://docs.aiogram.dev/en/latest/) framework.

List of libraries that were used in the project:
- [aiogram](https://docs.aiogram.dev/en/latest/)
- [sqlalchemy](https://docs.sqlalchemy.org/en/14/)
- [alembic](https://alembic.sqlalchemy.org/en/latest/)
- [aiohttp](https://docs.aiohttp.org/en/stable/)
- [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [lxml](https://lxml.de/)
- [loguru](https://loguru.readthedocs.io/en/stable/)
- [pytest](https://docs.pytest.org/en/6.2.x/)
- [pytest-asyncio](https://github.com/pytest-dev/pytest-asyncio)

First of all, you should create a database in PostgreSQL.
To start using the bot you should set the next **_environment variables_** in your system:
```
BOT_TOKEN = <your_bot_token>
DB_HOST = <postgresql_db_host>
DB_USER = <postgresql_db_user>
DB_PASSWORD = <postgresql_db_password>
DB_NAME = <postgresql_db_name>
MONGO_DB_HOST = <mongo_db_host>
MONGO_DB_NAME = <mongo_db_name>
MONGO_DB_PORT = <mongo_db_port>
```
To install all dependencies you should run the next command:
```bash
pip3 install -r requirements.txt
```

You need to change the directory to `src`. To start the bot you should run the next command:
```bash
python3 main.py
```
Also, you can use **docker-compose** for run the bot. For this, you should edit in the **_docker-compose.yml_** 
environment variable `BOT_TOKEN` and start the docker-compose:
```bash
docker-compose up -d
```
To get administrator rights, you need to send the bot command `/get_admin`. 
It works if in the database doesn`t exist users with administrator permissions.
> **Authors:** 
> - [Vladyslav Tsurkan](https://t.me/vladyslavtsurkan)
> - [Tetyana Savchenko](https://t.me/leasael)