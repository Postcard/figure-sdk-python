Figure SDK
---------

The official [Figure](https://figuredevices.com/) SDK for Python.

Role
----

The intention of this module is to provide developers a nice API to integrate their Python applications with Figure.

Installation
------------

Install the Figure SDK:

From Source:
```
https://github.com/postcard/figure-sdk-python
```

From git:
```
pip install git+https://github.com/postcard/figure-sdk-python.git
```

Documentation
------------

Please see [https://figuredevices.com/docs/api/?python](https://figuredevices.com/docs/api/?python) for the most up to
date documentation.

Platforms
---------

We also support [NodeJS SDK](https://github.com/postcard/figure-sdk-node).

Basic Usage
-----------

```python
>>> import figure
>>> figure.token = "yourtoken"
>>> figure.Portrait.get_all_public()
...
```

Support
-------

If you're having any problem, please [raise an issue](https://github.com/postcard/figure-sdk-python/issues/new).


License
-------

The project is licensed under the MIT license.
