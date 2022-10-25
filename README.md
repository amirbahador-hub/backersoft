# backersoft
![Tests](https://github.com/amirbahador-hub/backersoft/actions/workflows/tests.yml/badge.svg)   

https://bakersoft.de/en/ assessment

## RUN IN DEVELOPMENT MODE
Add ENV_NAME KEY to config/.env
```
ENV_NAME=dev
```
install dev requirements
```
pip install requirements_dev.txt
```


runserver
```bash
python manage.py runserver
```

## RUN TESTS
```bash
pytest . -rP
```

## Add dependencies

### Main requirements
add your dependency to requirements.in
```
pip-compile requirements.in --output-file=requirements.txt
```

### Development requirements
add your dependency to requirements_dev.in
```
pip-compile requirements_dev.in --output-file=requirements_dev.txt
```

