Installation
------------

Pip
^^^
Installing Python Bitbucket is simple with pip: ::

	pip install git+git@github.com:Alir3z4/python-bitbucket.git#egg=bitbucket

Get the Code & contribute
^^^^^^^^^^^^^^^^^^^^^^^^^
Python Bitbucket is hosted on GitHub, where the code is always available.

You can either clone the public repository: ::

	git clone git@github.com:Alir3z4/python-bitbucket.git

Download the tarball: ::

	curl -OL https://github.com/Alir3z4/python-bitbucket/tarball/master

Or, download the zipball: ::

	curl -OL https://github.com/Alir3z4/python-bitbucket/zipball/master

Test
^^^^
Run public tests::

	site-packages$> python -m bitbucket.tests.public

Run private tests. Require **USERNAME** and **PASSWORD** or **USERNAME**, **CONSUMER_KEY** and **CONSUMER_SECRET** in *bitbucket/tests/private/settings.py*::

	site-packages$> python -m bitbucket.tests.private
