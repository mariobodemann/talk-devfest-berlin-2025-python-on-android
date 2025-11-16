# Python on Android

## How to Integrate Python Libraries in Your Android Apps

### Mario Bodemann

----------

# (Disclaimer |: `Mario Bodemann`)

* (not test relevant)
* Android Developer Advocate @ Yubico
  * builder of security usbc yubikeys
* Ask me sbout fido 2 / WebAuthn / Android Developement & building things
* uses python alongside Kotlin (#noHate)

----------

# (Disclaimer ][: `deckdown`)

* shenanigans
* running code :mind-blown:
* https://github.com/mariobodemann/deckdown

``` bash
head -n 5 talk.md
```

----------

# Python

![](python.png)

---------

# Python: Hello World

``` python
def hello(name):
  print(f"Hello World, {name}!")

hello(input('What is your name? '))
```

----------

# Python: Hello Data

``` python
# something something numpy
```
----------

# Python: Hello Mario

``` python
fraktur -m rainbow -b round -f caps -- Hello World!
```

----------

# Python: Hello Mario 2.0

``` python
fraktur -f all -- Hello World!
```

--------

# Python on Android

![](python-on-android.png)

--------

# {{MOTIVATE}}

* `fraktur` on Android?
  * kotlin
  * best practize

--------

# termux

* android app
* runs a terminal
* can install open source tools
* python is oss

``` bash
pkg install termux-gui python

python -c 'print("hello")'
```

-----------

# termux-gui

* control Android via cli

``` bash
pkg install termux-gui
```

-------

# termux-gui in python

* control termux-gui from python

``` python
subprocess.run(["termux-dialog","-t","hello"])
```

--------

# termux-gui: frakturize

``` python
import subprocess
p=subprocess.run(["fraktur","-f","all"],capture_output=True)
opts = ",".join(p.stdout.decode().splitlines())
p = subprocess.run(["termux-dialog","sheet","-t","Frakturize?","-v",f"{opts}"],capture_output=True)
import json
t=json.loads(p.stdout)
subprocess.run(["termux-clipboard-set",t["text"]])
```

-------

# {{Or integrate in `fraktur`?}}

-------

# {{Or tool from ole?}}

--------

# {{flask(?)}}

``` python
# PSEUDO
flask.run:
    post(json_body: str | None = None) -> list[str]:
        body = json(json_body)
        response = subprocess.run(['python3', 'frakture', '...'])
        print(f"in: {body}\nout: {response}\n")
        return response
```

``` kotlin
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

```

--------

# {{CKLOQUOAI}}

--------


