This is a simple flask project made to explore how to host/show/download images which are generated using a lot of userdriven data without the need of encoding the data into an image URL.  
Critical code for Post found on [TiM](https://thisinterestsme.com/load-image-as-blob-jquery/)  
Jquery from Google, Jquery.redirect from [mgalante](https://github.com/mgalante/jquery.redirect)

# Preface
Python3 := Python3.x.x >= 3.7
pip3 := Python3 -m pip

# Setup
## Virtual Environment
```console
$ pip3 -m virtualenv venv
```

## Imports
1. __PIL__
    * `$ pip3 install pillow`
    * https://pillow.readthedocs.io/en/stable/installation
2. __flask__  
    * `$ pip3 install flask`
    * http://flask.pocoo.org/docs/1.1/installation/

## Hosting
```console
> Startup and Shutdown
$ source venv/bin/activate
$ python3 application.py
> 'At this point your server is running'
$ ^C
$ deactivate
```
