# -*- coding: utf-8 -*-
import sys
import subprocess
import os
from click import style, echo

is_windows = sys.platform == 'win32'
is_cygwin = sys.platform == 'cygwin'
is_linux = 'linux' in sys.platform
is_mac = sys.platform == 'darwin'

class Platform(object):
    @staticmethod
    def is_windows():
        return sys.platform == 'win32'

    @staticmethod
    def is_linux():
        return 'linux' in sys.platform

    @staticmethod
    def is_mac():
        return sys.platform == 'darwin'

    @staticmethod
    def is_cygwin():
        return sys.platform == 'cygwin'

  
def start(command):
    if(Platform.is_windows()):
        call("cmd /c start {}".format(command))
    elif(Platform.is_mac()):
        call("open {}".format(command))
    elif(Platform.is_linux()):
        call("xdg-open {}".format(command))
    elif(Platform.is_cygwin()):
        call("cygstart {}".format(command))
    else:
        raise Exception("Unknown platform")

def open_url(url, exitOnError=True):
    try:
        start(url)
    except:
        print_error("Sorry, don't know how to open a browser on your platform, please use the url below to create a pull request")
        print_info(url)
        if(exitOnError):
            exit()

def call(command, exitOnError=True):
    print_verbose('Exec [{}]'.format(command))
    if(subprocess.call(command)):
        print_error("Error happened when running [{}]".format(command))
        if(exitOnError):
            exit()

def popen(command):
    print_verbose('Exec [{}]'.format(command))
    return os.popen(command).read().strip()

def colored_decorator(color):
    def decorator(func):
        def wrapper(output):
            #return colored(func(output), color)
            return style(func(output), fg=color)
        return wrapper
    return decorator

@colored_decorator('cyan')
def verbose(output):
    return output

@colored_decorator('green')
def info(output):
    return output

@colored_decorator('red')
def error(output):
    return output

@colored_decorator('yellow')
def warning(output):
    return output

def print_verbose(output):
    echo(verbose(output))

def print_info(output):
    echo(info(output))

def print_error(output):
    echo(error(output))
