# Python on Android

## How to Integrate Python<br/>in Your Android Apps

### by Mario Bodemann

----------

# (Disclaimer |: _Mario Bodemann_)

* (not test relevant)
* Android Developer Advocate @ Yubico
  * builder of security usbc yubikeys
* Ask me sbout fido 2 / WebAuthn / Android Developement & building things
* uses python alongside Kotlin (#noHate)

----------

# (Disclaimer ][: _deckdown_)

* shenanigans
* running code :mind-blown:
* https://github.com/mariobodemann/deckdown

~~~ bash
grep '_deckdown_' -A5 talk.md
~~~

----------

![](python-logo.png)

---------

# Python: Hello World

* low WTF's per minute
* runs everywhere (Linux, Mac, Windows, Android)
  * we ignore iOS
* runtime compilation

~~~ python
def hello(name):
  print(f"Hello World, {name}!")

hello(input('What is your name? '))
~~~

-------------

# Python: Hello scipy

~~~ python
from scipy.signal import wiener
import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng()
img = rng.random((40, 40))

filtered_img = wiener(img, (5, 5))
f, (plot1, plot2) = plt.subplots(1, 2, label="🌭")
plot1.imshow(img)
plot2.imshow(filtered_img)
plt.show()
~~~

----------

# Python: How I Use It

~~~ bash
fraktur -m rainbow -b round -f caps -- Welcome!
~~~

~~~ bash
fraktur -f chess -- Hello World!
~~~

~~~ bash
fraktur -f slack -- New Release Available!
~~~

--------

# Python on Android

<center>
<img src="python-on-android.png" style="width:50%" />
</center>

--------

# Python on Android: Termux

* Termux is an Android app
  * https://termux.org
* runs a terminal
* can install open source tools
* python is oss

--------

# termux-gui

* plugin for termux
* access Android ui
  * clipboard, camera,
  * sms, calls, contacts

------

# DEMO: Termux in Android

~~~ bash
adb install f-droid.apk
~~~

~~~ f-droid
install termux
~~~

~~~ pbcopy
termux-dialog -t hello
~~~

-------

# termux-gui in python

* using _subprocess_ library
* calling termux-gui binaries

~~~ pbcopy
import subprocess

r = subprocess.run(
    ["termux-dialog", "-t", "hello"],
    capture_output=True
)

print(r.stdout.decode().splitlines())
~~~

--------

# termux-gui: frakturize

~~~ python
import sys
sys.path += ['/Users/Mario.Bodemann/Projects/s9s']
import fraktur

options = fraktur.generate(
    'Hello World', 
    font='all'
).splitlines()
print(options)
~~~

------

# Fraktur: show options to user

~~~ termux-python
proc = subprocess.run(
    [
        "termux-dialog", 
        "sheet", 
        "-t", "Frakturize?", 
        "-v", f"{options}"
    ],
    capture_output=True
)
~~~

---------

# frakturize: copy answer to clipboard

~~~ python
response = json.loads(
    proc.stdout
)

subprocess.run([
    "termux-clipboard-set", 
    response["text"]
])
~~~

# 🎉

-------

# Sub Summary

* termux with python
  * python can call Fraktur
  * python can call termux-gui
  * termux-gui can do Android
* ergo
  * **Python Fraktur can interact with Android**

--------

# Termux Redux

<center>
<img src="python-web-on-android.png" style="width:50%" /> 
</center>

-------

# Adding Native Android

* bridging from Python to Termux to Android
* limited ui flexibility
* brittle (google says no?)
  * termux says no?

-------

# Termux Redux

* Android UI
  * jetpack compose
  * retrofit
* Python Web
  * flask
  * fraktur

-------

# Termux Web: Flask 🧪

* simple 
* nice
* works

~~~ pbcopy
pip install flask
~~~

---------

# Import fraktur module

~~~ termux-python
import sys
sys.path += ['/data/data/com.termux/files/home/s9s']
~~~

-----

# Import flask and create server

~~~ termux-python
from flask import Flask
app = Flask('Fraktur.Server')
~~~

--------

# Set route (*POST "/" MESSAGE*)

~~~ termux-python
@app.post('/')
def hello():
  # NEXT  

app.run()
~~~

----------

# Call **fraktur** for server POST

~~~ termux-python
import fraktur
from flask import request

message = request.get_data().decode()

return fraktur.generate(
    message, 
    font='all'
).splitlines()
~~~

-----

# DEMO: *flask server on Android*

## (copy sample, create file)

~~~ { .termux-python .hidden }
import sys
sys.path += ['/data/data/com.termux/files/home/s9s']

from flask import Flask
app = Flask('Fraktur.Server')

@app.post('/')
def hello():
    import fraktur
    from flask import request

    message = request.get_data().decode()

    return fraktur.generate(
        message, 
        font='all'
    ).splitlines()
    
app.run()
~~~

--------

# Checking the Server

* test webserver
* should return list of messages
* but formated through _fraktur_

~~~ pbcopy
curl 127.0.0.1:5000 -d 'Hello WOrld 2.01' | jq
~~~

-------

![](pyweb-curl.png)

------------

# Android Web Client

* "default" Android App
  * MVVM
  * retrofit
  * kotlinx serialization
  * coroutines

-------

# Data Model

~~~ kotlin
interface PythonService {
    @POST("/")
    suspend fun getFraktures(
        @Body body: String
    ): List<String>
}
~~~

---------------

# Web Service

~~~ kotlin
class PythonBackend {
    private val service = Retrofit
        ./* setup */
        .create(PythonService::class.java)

    suspend fun requestFraktures(message: String) =
        service.getFraktures(message).map { 
            it.removeSurrounding("\"") 
        }
}
~~~

------------

# User Interface

* *Jetpack Compose*
  * *LazyColumn* for strings returned
* Android
  * *ClipboardManager* for clipboard access
  * *(Android)ViewModel* for cordination
* nothing too unsurprising

----------

# DEMO: Android calling Python Web

<center>
<img src="pyweb-android.png" style="width:80%" />
</center>

-------

# Sub Summary

good                        | improvements
----------------------------|---------
separation of work display  | android:usesCleartextTraffic="true" 👀
flexible                    | manual install of python dependencies
native                      | 
fast                        | user says "What?" 🧐  


--------

# Chaquopy

## Python Runtime Embedded in Android App

<center>
<img src="python-in-android.png" style="width:50%" /> 
</center>

-----

# Chaquopy

> https://chaquo.com/
{ style='font-size:98px' }

* embedding Python runtime in Android App 🤯
* Android -> Python **&&** Python -> Android 🤯
* *Wonderous 🤯*

--------

# Chakotay Dependencies

~~~ gradle
python = "16.1.0"
python = { id = "com.chaquo.python", version.ref = "python" }

plugins {
    // ... 
    alias(libs.plugins.python) apply false
}
~~~

---------

# Configuration

~~~ gradle
chaquopy {
    defaultConfig {
        pip {
            install("pystitch==1.0.0")
        }

        version = "3.13"
    }
}
~~~

-----------

# In Code Setup

~~~ kotlin
private val python: Python by lazy {
    if (!Python.isStarted()) {
        Python.start(AndroidPlatform(context))
    }

    Python.getInstance()
}
~~~

----------

# Usage in Kotlin

~~~ kotlin
suspend fun requestFraktures(
  message: String
): List<String> {
  val fraktur = python.getModule("fraktur")
  
  val result = fraktur.callAttr(
    "generate", 
    message, 
    "all"
  )

  val stringResult = result.toString()
  return stringResult.split("\n")
}
~~~

--------

# DEMO of embeded Python

<center>
<img src="embeded-python.png" style="width:75%" />
</center>

// THINK ABOUT WIENERS

-------

# Summary

* [Termux](https://termux.org)
  * unix like Terminal on the go
  * experiment with OSS software
  * install git!
* [WebServer](https://flask.palletsprojects.com/)
  * make your phone into a server
  * serve versuse surf. 🏄
* [Embedding](https://chaquo.com/)
  * make your app speak Python
  * use all^1 of your Python libraries
  * nice separation of work and design

-----------

# github.com/mariobodemann/<br/>talk-devfest-berlin-2025-python-on-android

# End

# QnA



