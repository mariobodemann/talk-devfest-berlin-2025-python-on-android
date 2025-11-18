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

# Python: Hello scipy/numpy

~~~ python
from scipy.signal import wiener
import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng()
img = rng.random((40, 40))

filtered_img = wiener(img, (5, 5))
f, (plot1, plot2) = plt.subplots(1, 2)

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

![](python-on-android.png)

~~~ bash
cd ~/Library/Android/sdk/emulator
./emulator -no-snapshot @Medium_Phone &
~~~

--------

# termux

* android app
* runs a terminal
* can install open source tools
* python is oss

--------

# termux-gui

* control Android via cli
* access ui
* read phone log
* create files

------

# DEMO: Termux in Android

~~~ pbcopy
termux-dialog -t hello
~~~

-------

# termux-gui in python

* control termux-gui from python
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
* ergo: **python Fraktur can interact with Android**

--------

# Termux: not native

* bridging from python to termux to android
* limited ui flexibility
* brittle (google says no?)
    * termux says no?

-------

# Termux Redux

## Android UI <--> Python WebServer

![](python-on-web-on-android.png)

-------

# Termux Redux

* Android UI
    * jetpack compose
    * retrofit

* Python Web
    * flask
    * fraktur

-------

~~~ python
import sys
sys.path += ['/Users/Mario.Bodemann/Projects/s9s']

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

------------

# Android Web Client

~~~ kotlin
@Serial
data class FraktureBody(
  val message: String? = null,
  val font: Font? = null,
  val mode: Mode? = null,
  val box: Box? = null,
)

interface FraktureService {
  @POST("/")
  suspend fun fraktureize(
    @Body body : FraktureBody? = null,
  ) : String
}

val service = Retrofit.build(..)
val text = service.fraktureize(
  FraktureBody(
    message = "Hello World",
    font = Font.Capitalize,
    box = Box.Round,
  )
)

// ...
Box {
  var message by remember {mutablestateOf<String?>(null)}
  var text = ...

  TextField(.., value=message)
  Text(text=text)
}

~~~

--------

# {{CKLOQUOAI}}

--------


