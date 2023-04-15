```bash
# run pytest
pytest test.py

# run with allur report
pytest --alluredir=<path to report directory> test.py
pytest --alluredir=./allure-results

allure serve
# or
allure generate

```