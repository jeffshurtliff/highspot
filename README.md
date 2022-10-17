# Highspot Python SDK
A Python toolset for utilizing the Highspot API

## Installation
The package can be installed via pip using the syntax below.

```sh
pip install highspot --upgrade
```

You may also clone the repository and install from source using below.

```sh
git clone git://github.com/jeffshurtliff/highspot.git
cd highspot/
python setup.py install
```

## Usage
This section provides basic usage instructions for the package.

### Importing the package
Rather than importing the base package, it is recommended that you import the primary `Highspot` class using the syntax
below.

```python
from highspot import Highspot
```

### Initializing a Highspot object instance
The primary `Highspot` object serves many purposes, the most important being to establish a connection to the 
Highspot environment with which you intend to interact. As such, when initializing an instance of the `Highspot` 
object, you will need to pass it the API credentials it will use to authenticate so that the connection can be 
established.

#### Passing the information directly into the object
The API credentials can be passed directly into the `Highspot` object when initializing it, as
demonstrated in the example below.

```python
hs = Highspot(username='a1b2c3d4e5', password='abc123DEF456')
```

## License
[MIT License](https://github.com/jeffshurtliff/highspot/blob/master/LICENSE)

## Changelog
Refer to the [changelog](https://highspot.readthedocs.io/en/latest/changelog.html) for version change information.

## Reporting Issues
Issues can be reported within the [GitHub repository](https://github.com/jeffshurtliff/highspot/issues).

## Donations
If you would like to donate to this project then you can do so using 
[this PayPal link](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=XDZ8M6UV6EFK6&item_name=highspot&currency_code=USD).

## Disclaimer
This package is considered unofficial and is in no way endorsed or supported by 
[Highspot](https://www.highspot.com).
