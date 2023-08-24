# ip_lookup

For ip_lookup with some Public or Private API 

## Guides/Tips/Docs..etc?

* [ipwhois](https://github.com/hong539/ipwhois)
* HTTP/1.1
* HTTP/2
* HTTP/3
* check protocol
    * [http2.pro/api/v1](https://http2.pro/api/v1)
    * [How to check http protocol version in chrome?](https://www.sudshekhar.com/blog/http-protocol-check-in-chrome)
* [Internet_geolocation](https://en.wikipedia.org/wiki/Internet_geolocation)
* [flask](https://flask.palletsprojects.com/en/2.3.x/deploying/#deploying-to-production)
* WSGI server
    * [Gunicorn](https://flask.palletsprojects.com/en/2.3.x/deploying/gunicorn/)
    * uWSGI
    * mod_wsgi
* load_test
    * [locust](https://locust.io/)

```shell
#請問Chrome的開發者工具（DevTools）/Network介面顯示的protocol
#出現h3或h2表示哪些資訊?

#在 Chrome 的開發者工具（DevTools）中的 Network 頁面，
#如果出現 h2 或 h3，表示該請求使用的是 HTTP/2 或 HTTP/3 協議，
#而不是 HTTP/1.1 協議。HTTP/2 和 HTTP/3 都是新一代的網路協議，相較於 HTTP/1.1 具有更好的效能和安全性。
#其中，HTTP/2 支援流、多路徑、優先級、壓縮等功能，
#而 HTTP/3 則是基於 QUIC 協議，使用 UDP 傳輸，並且使用 TLS1.3 加密。
```

## Prerequisites

* [Setting up your python-dev-environment](https://github.com/hong539/setup_dev_environment/tree/main/programing_languages/python)
* python version >= 3.8.15

## qucik start

```shell
#simple install packages
pip install requests
pip install ipwhois
pip install hyper
pip install httpx
pip install httpx[http2]

python src/*.py

#if using python virtual environments
pipenv shell
pipenv install requests
pipenv install ipwhois
pipenv install hyper
pipenv install httpx
pipenv install httpx[http2]

python src/*.py

#install packages from Pipfile
#--dev — Install both develop and default package categories from Pipfile.
pipenv install --dev

#Test with flask
flask --app main run
```

## Important!!!

== We're Using GitHub Under Protest ==

This project is currently hosted on GitHub.  This is not ideal; GitHub is a
proprietary, trade-secret system that is not Free and Open Souce Software
(FOSS).  We are deeply concerned about using a proprietary system like GitHub
to develop our FOSS project.  We have an
[open {bug ticket, mailing list thread, etc.} ](INSERT_LINK) where the
project contributors are actively discussing how we can move away from GitHub
in the long term.  We urge you to read about the
[Give up GitHub](https://GiveUpGitHub.org) campaign from
[the Software Freedom Conservancy](https://sfconservancy.org) to understand
some of the reasons why GitHub is not a good place to host FOSS projects.

If you are a contributor who personally has already quit using GitHub, please
[check this resource](INSERT_LINK) for how to send us contributions without
using GitHub directly.

Any use of this project's code by GitHub Copilot, past or present, is done
without our permission.  We do not consent to GitHub's use of this project's
code in Copilot.

![Logo of the GiveUpGitHub campaign](https://sfconservancy.org/img/GiveUpGitHub.png)