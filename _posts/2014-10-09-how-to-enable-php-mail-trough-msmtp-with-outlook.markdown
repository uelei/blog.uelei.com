---
layout: post
title: "How to enable php mail() trough msmtp with outlook"
date: "2014-10-09"
categories: php
tags:
- outlook
- php
- mail
- msmtp
---

To be able to send email trought mail() function in php without set the complete smtp server you can use msmtp, first you need to install **msmtp**

{% gist ccffa4b8db0a6595fe46 %}

create a config file

{% gist 8e1dc89357a282299cf0 %}

with the follow lines

{% gist 29d115d8d37d3c03c4cf %}

create a log file **/var/log/msmtp.log**, set permissions

{% gist 2b8eaa1499a258278f6b %}

comment the lines on **/etc/php5/apache2/php.ini**

{% gist 9ece64af30cd183b7526 %}

if everything is working fine you are ok, if you have any problems you can try

{% gist 07e97d3f60536e766b04 %}

and sent it with

{% gist cae344afc217bbabe225 %}

[source](https://www.digitalocean.com/community/tutorials/how-to-use-gmail-or-yahoo-with-php-mail-function)
