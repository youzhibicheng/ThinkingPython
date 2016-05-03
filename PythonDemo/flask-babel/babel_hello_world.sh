pybabel extract -F babel.cfg -o messages.pot .
pybabel init -i messages.pot -d translations -l zh_Hans_CN
pybabel compile -d translations

¸üĞÂ·­Òë
pybabel update -i messages.pot -d translations
pybabel compile -d translations