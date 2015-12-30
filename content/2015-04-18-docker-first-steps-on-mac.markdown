---
layout: post
title: "Docker first steps on mac"
date: 2015-04-18
tags:
- boot2docker
- docker
---

first we need to install docker and boot2docker

i did using brew

{% gist da2e356f4ba117118f80 %}

{% gist ec6d3c9c32027d0409c7 %}

after we need to initiate boot2docker

{% gist 98b5b3bcfa66e3bf487a %}

and start the vm

{% gist 6b3db7cb93e2a14d9652 %}

the vm is up but you cannot use **docker ps**, you gonna need use the follow command to make things work.

{% gist 97ed38bda0d3034879a2 %}

now you can run your docker.

to know boot2docker ip address cmd this

{% gist 6bc443cd8cb84d28ed7c %}
