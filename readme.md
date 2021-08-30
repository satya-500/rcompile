**we are using python and docker to compile the program in real time.**

## Table of contents

- [Table of contents](https://github.com/satya-500/rcompile#table-of-contents)
- [Description](https://github.com/satya-500/rcompile#description)
- [Installation](https://github.com/satya-500/rcompile#installation)
 
 - [Start app locally](https://github.com/satya-500/rcompile#start-app-locally)

	- [backend](https://github.com/satya-500/rcompile#backend)
	- [frontend](https://github.com/satya-500/rcompile#frontend)

## Description

Create a form that will show a list of programming questions and compile real-time and show errors.


## Installation

#### install using pip3

```
$ cd backend
$ pip3 install -r requirements.txt
```


## Start app locally

### backend
```
$ python3 app.py
```

### frontend
you can use any server to serve static front end files.

nginx configuration
```bash
$ vim /etc/nginx/conf.d/test.conf 
```
```nginx
server {
    listen 80 default_server;

    server_name _;


    location / {
        root frontend-location;
        try_files  $uri $uri.html $uri/index.html index.html;
    }
}
```