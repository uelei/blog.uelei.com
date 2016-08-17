---
layout: post
title: "Configurar date.timezone para fuso do brasil"
date: "2014-04-12"
categories: php
tags:
- php
- timezone
- linux
---

qualquer problema relacionado com fuso errado no php, geralmente é problema do **date.timezone** no arquivo **php.ini**.

o php.ini pode estar localizado no **/etc**,**/etc/php/** ou no **/etc/php5/** ou até em algum subdiretório

editar o arquivo **php.ini** e configurar a variavel date.timezone

{% gist d1d7e4bedafb1b1b9863 %}
