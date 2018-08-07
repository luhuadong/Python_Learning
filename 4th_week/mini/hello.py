import sys

from django.conf import settings


# 这些设置通常会包含在 settings.py 文件

settings.configure(
    DEBUG=True,
    SECRET_KEY='thisisthesecretkey',
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)


from django.conf.urls import url
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse


# 通常会放在应用程序内的 views.py 文件

def index(request):
    return HttpResponse('Hello World')


# 路由，通常放在根目录中的 urls.py 文件

urlpatterns = (
    url(r'^$', index),
)


application = get_wsgi_application()

# 典型的 Django 项目带有一个 manage.py 文件

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

