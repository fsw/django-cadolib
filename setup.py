# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='django-cadocms',
    version='0.1.0',
    description='Simple set of tiny usefull bits',
    author='Frank Wawrzak (CadoSolutions)',
    author_email='frank.wawrzak@cadosolutions.com',
    url='https://github.com/fsw/django-cadocms',
    download_url='git://github.com/fsw/django-cadocms.git',
    packages=['cadocms'],
    install_requires=[
        #'PIL==1.1.7',
        'Pillow >=2.1.0',
        'South==0.7.6',
        'Django==1.5.1',
        'django-configurations',
        'django-compressor==1.3',
        'django-imagekit >= 3.0.3',
        'django-mptt==0.5.5',
        'pilkit==1.1.4',
        'pysolr',
        'simplejson==2.3.2',
        'six==1.2.0',
        'python-dateutil==2.1',
        'flup',
        'pdfdocument==1.4',
        'reportlab==2.5',
        'openpyxl==1.6.1',
        'lxml==3.0',
        'django-debug-toolbar==0.9.4',
        #'django-versioning==0.7.3',
        'hamlpy==0.82.2',
        'html2text',
        #'django-tinymce',
        'django-filebrowser',
        'django-geoposition',
        'django-haystack==2.0.1-dev',
        'redis',
        'django-reversion',
        #'fsw-django-versioning>=0.7.3',
        'django-simple-captcha',
        'cssselect',
        'fabric',
        'django-rosetta',
        'django-modeltranslation',
        'Celery',
        'celery-haystack',
        'django-celery',
        'dnspython',
        'cssselect',
        'django-cache-machine',
        'python-memcached',
        'django-extensions',
        'bleach',
    ],
    dependency_links = [
        #'https://bitbucket.org/fsw_/django-versioning/get/master.tar.gz#egg=fsw-django-versioning-0.7.3',
        'http://github.com/SeanHayes/django-config-gen/tarball/master#egg=django-config-gen-1.0.0',
        'http://github.com/fsw/django-haystack/tarball/null-field#egg=django-haystack-2.0.1-dev',
        'http://github.com/fsw/pysolr/tarball/master#egg=pysolr-3.1.1',
    ],
)