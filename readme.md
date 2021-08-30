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
### add new language
```json
{
   "python":{
      "image_name":"python:3.9-slim-buster", //docker image name
      "extension":"py", // extension
      "is_executable":false
   },
   "java":{
      "image_name":"openjdk:8",
      "extension":"java",
      "is_executable":false
   },
   "go":{
      "image_name":"golang:1.17.0-buster",
      "extension":"go",
      "is_executable":false
   },
   "bash":{
      "image_name":"debian:buster-slim",
      "extension":"sh",
      "is_executable":true
   }
}
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