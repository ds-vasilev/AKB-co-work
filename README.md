# rss_reader_tests
Selenium python rss reader tests

Our test app https://berpress.github.io/react-shop/

How to start

Use python 3.8 + Create and activate virtual environments

```angular2html
python3 -m venv env
source env/bin/activate
```
pre-commit https://pre-commit.com/
```angular2html
pip install pre-commit
pre-commit install
```


Список багов:
- "Erorr, check network" при регистрции через одинаковые имена-пароли
- грамматическая ошибка во всплывашке "Erorr, check network"
- регистрация через кирилические домены не работает 
- ломается верстка при появлении большого красного аллерта на странице регистрации при попытке ввода невалидных данных