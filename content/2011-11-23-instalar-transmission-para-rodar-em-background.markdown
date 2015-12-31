---
layout: post
title: "Instalar Transmission para rodar em background"
date: 2011-11-23
categories: linux
tags:
- linux
- transmission
- torrent
- debian
- ubuntu
---
![transmission](/assets/images/post/2011-11-23-instalar-transmission-para-rodar-em-background/transmission_logo.jpeg)

Para instalar o transmission para rodar em background, vc deve instalar o transmission-daemon

{% gist feca03d13a79c77f7e0c %}

O serviço é iniciado automaticamente, mas devemos configurar algumas coisas para poder controla-lo corretamente. Vamos parar o transmission.

{% gist e758419249604579fa47 %}

Vamos editar as configurações, o arquivo padrão fica em **/var/lib/transmission-daemon/info/settings/json** para editar novamente vamos usar o sudo .

{% gist 6a01718a4f4e8b20cd00 %}

temos que alterar as seguintes linhas

{% gist 4a4966502e9c8853a32e %}

alterando o rpc-whitelist para '''*.*.*.*''' ele aceita conecções externas.Agora inicie o transmission novamente .

{% gist f583f20ae669a357cceb %}

Agora vc pode de qualquer lugar controlar o transmission, somente digite o ip do computador e a porta 9091  http://IP:9091 ou http://localhost:9091 se tudo deu certo vc verá a seguinte tela !

![transmission_screen](/assets/images/post/2011-11-23-instalar-transmission-para-rodar-em-background/transmission_screeny.png)
