
# prj.name = test.py

## Links
#### selenium-old:
- [pypi selenium](https://pypi.org/project/selenium/)
- [selenium](https://www.selenium.dev/)
- [selenium documentation](https://www.selenium.dev/documentation/en/)
- [locating-hyperlinks-by-link-text](https://selenium-python.readthedocs.io/locating-elements.html#locating-hyperlinks-by-link-text)
- [ref_attributes](https://www.w3schools.com/tags/ref_attributes.asp)
- [scrollIntoView](https://developer.mozilla.org/ru/docs/Web/API/Element/scrollIntoView)

## start
    ```bash
    python -m venv .venv
    cd D:\devgit\pytest
    .\.venv\Scripts\activate  # win
    # OR
    source d:/devgit/pytest/.venv/Scripts/activate  # bash
    
    pip install -r requirements.txt
    ```
### Errors
- [.ps1 cannot be loaded because running scripts is disabled on this system.](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.2)

```powershell
Get-ExecutionPolicy
Get-ExecutionPolicy -List
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser # recomended
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser # not secure
```

### Linux
    ```bash
    sudo apt install virtualenv
    virtualenv -p python3 .venv
    source .venv/bin/activate
    ```

## end
`deactivate`

`edge://version/`

pip install rpaframework --no-dependencies

## keyword
xpath cheatsheet

# Pytest
    ```bash
    pytest --help
    pytest -v name.py
    pytest -s name.py
    pytest --log-level=LEVEL name.py
    ```

## Node via volta

```
node -v
node start.js
```
### lib
```
npm -v
npm install puppeteer
npm install puppeteer-video-recorder
```
```nodejs
const puppeteer = require('puppeteer');
```
### links
- [puppeteer-video-recorder](https://github.com/shaynet10/puppeteer-video-recorder)
- [deno](https://deno.land/manual)
- [cargo](https://doc.rust-lang.org/cargo/getting-started/installation.html)


## Robot
### installation
```
pip install --upgrade robotframework
robot --version
```

```
robot --help
robot tests.robot
robot QuickStart.rst
pybot -d results tests/name.robot
robot -d ../../.logs/robot tst.robot
```
### BROWSER
```
pip install robotframework-browser
rfbrowser init
```

### Setting default options and syslog file before running tests.
```
$ export ROBOT_OPTIONS="--outputdir results --suitestatlevel 2"
$ export ROBOT_SYSLOG_FILE=/tmp/syslog.txt
```

### Links
- [robotframework](https://robotframework.org/)
- [UserGuide](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html)
- [QuickStart](https://github.com/robotframework/QuickStartGuide/blob/master/QuickStart.rst)
- [lambdatest](https://www.lambdatest.com/support/docs/robot-with-selenium-running-robot-automation-scripts-on-lambdatest-selenium-grid/)
- [Selenium2Library](https://robotframework.org/Selenium2Library/Selenium2Library.html)
- [SeleniumLibrary](https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html)
- [docs](https://robocorp.com/docs/)
- [lambdatest](https://www.lambdatest.com/blog/robot-framework-tutorial/)
- [edureka](https://www.edureka.co/blog/robot-framework-tutorial/)
- [robocorp docs](https://robocorp.com/docs/courses/implementing-rpa-robots/process-definition-document)
- [libraries](https://robocorp.com/docs/libraries)
- [robocorp portal](https://robocorp.com/portal/)
- [robocorp locators](https://robocorp.com/docs/development-guide/browser/how-to-find-user-interface-elements-using-locators-in-web-applications)
- [robocorp security](https://robocorp.com/docs/development-guide/variables-and-secrets/vault)
- [for API](https://github.com/MarketSquare/robotframework-requests)
- [Element](https://developer.mozilla.org/en-US/docs/Web/API/Element)
- [robo + playwright](https://robocorp.com/docs/development-guide/browser/playwright)
- [web-store-order](https://robocorp.com/docs/development-guide/browser/web-store-order-robot)
- [robotframework-browser](https://github.com/MarketSquare/robotframework-browser#robotframework-browser)
- [CI playwright](https://github.com/microsoft/playwright-github-action)
- [ci playwright](https://playwright.dev/python/docs/ci/)
- [github-actions-integration](https://robocorp.com/docs/development-guide/integrations/github-actions-integration)
- [actions](https://github.com/features/actions)

#### libraries
- [robotframework-browser](https://robotframework-browser.org/)
- [BuiltIn](http://robotframework.org/robotframework/latest/libraries/BuiltIn.html)
- [SeleniumLibrary](https://github.com/robotframework/SeleniumLibrary)
- [SeleniumLibrary](https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html)
- [Locating](https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html#Locating%20elements)
- [RequestsLibrary](http://marketsquare.github.io/robotframework-requests/doc/RequestsLibrary.html)
- [rpaframework docs](https://rpaframework.org/)

#### Other
- [playwright](https://playwright.dev/python/docs/intro/)
- [playwright](https://playwright.dev/)
- [puppeteer](https://devdocs.io/puppeteer/)
- [cypress](https://www.cypress.io/)
- [qweb_workshop](https://github.com/qentinelqi/qweb_workshop)


## Webdrive
```
pip install webdrivermanager
webdrivermanager firefox chrome --linkpath /usr/local/bin
```

### links
-[driver_requirements](https://www.selenium.dev/documentation/en/webdriver/driver_requirements/)

## UI testing
### locator

console: $x("xpath")
ex.: 
    - $x("html/body/div/div/header/img")
    - $x("html/body/div/div/header/img[@alt='Логотип проекта Mesto']")
    - $x(".//img")

## API

```
pip install pyresttest

# Interactive Mode
pyresttest https://api.github.com examples/github_api_test.yaml --interactive true --print-bodies true

# Verbose Output
pyresttest https://api.github.com examples/github_api_test.yaml --log debug
```

- [postman](https://www.guru99.com/postman-tutorial.html)
- [api](https://www.guru99.com/api-testing.html)
- [tools](https://www.guru99.com/top-6-api-testing-tool.html)
- [pyresttest](https://github.com/svanoort/pyresttest)
- [api-integration-in-python](https://realpython.com/api-integration-in-python/)
- [requests](https://docs.python-requests.org/en/master/index.html)
- [requests](https://realpython.com/python-requests/)


## Errors
- [Raise an Exception](https://www.w3schools.com/python/gloss_python_raise.asp)


## Jenkins
```
java -jar jenkins.war
```

