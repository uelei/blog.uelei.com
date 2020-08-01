---
layout: post
title: "Multiple gcloud accounts"
date: "2020-08-01"
categories:
- dev
- gcloud
---

Setup more than one account on gcloud , thanks to google this is a peace of cake


```shell

$ gcloud config configurations create config-name
Created [demo-config].
Activated [demo-config].

$ gcloud config set project my-project-id
Updated property [core/project].

$ gcloud config set account my-account@example.com
Updated property [core/account].

$ gcloud config set compute/region us-east1
Updated property [compute/region].

$ gcloud config set compute/zone us-east1-b
Updated property [compute/zone].

```
after that you need to login

```shell

gcloud auth login

```

Done you create a new config  `config-name`


Now to swith between accounts 
just run 

```shell

gcloud config configurations activate config-name

```
