---
layout: post
title: "Backup incremental com duplicity"
date: 2014-09-27
categories: linux
tags:
- backup
- duplicity
---

primeiro para instalar no debian/ubuntu

{% gist a4c1838962b1cf1294d1 %}

uso

{% gist 5f1c02152bc3e70f5020  %}

[wiki do projeto](http://duplicity.nongnu.org/duplicity.1.html)

para backup pode ser usado

**scp://user@server//diretorio **
**FTP_PASSWORD=[senha] duplicity [origem] ** **ftp://user@ftp_server.com/backup_directory**
**s3-http://**
**file:///diretorio**

* para visualizar data dos backups

**duplicity collection-status file:///**

* listar os arquivos atuais

**duplicity list-current-files file:///**

* verificar o backup

**duplicity verify origem backup**

* finalmente restore dos dados

**duplicity [backup] [destino]**

************************************************

Pode ser feito o backup para S3 da Amazon, instale os seguintes pacotes

{% gist eb97a54d93d0fd3b4e62 %}

e depois

{% gist 3ed2e4356f625ba4077e %}

exelente script de backup nesse [site](http://thomassileo.com/blog/2012/07/19/ubuntu-slash-debian-encrypted-incremental-backups-with-duplicity-on-amazon-s3/) e meu fork no  [gist](https://gist.github.com/uelei/e591e65476755f30968a) 
