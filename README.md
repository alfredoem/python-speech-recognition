# Speech Recognition

Run computer commands by voice 

#### Running with Docker

```
make build
make start
```

#### Running Locally
#### System Requirements
* Python3
* Pip3
* Python Audio
* Python Virtual env

#### Local Installation
```
sudo apt-get install python3-pyaudio
```

#### Application Installation
```
make init
source env/bin/activate
make install
```

#### Commands
Computer read an audio
```
make read
```

Computer listen and run a command (usr bin program) by voice
```
make run
```


#### Exit Virtual env
```
deactivate
```


