---
layout: post
title: "Instalar e configurar minecraft server sem erro bad login"
date: 2011-12-16
categories: games
tags:
- minecraft
- server
---

![](/assets/images/post/2011-12-16-instalar-e-configurar-minecraft-server-sem-erro-bad-login/minecraft.jpg)

#Instalando no Windows

faça o download do aquivo [Minecraft_Server.exe](https://s3.amazonaws.com/MinecraftDownload/launcher/Minecraft_Server.exe) em http://www.minecraft.net/download, instale o arquivo e execute uma vez, se vc tentar se logar no server irá ver a seguinte tela

![](/assets/images/post/2011-12-16-instalar-e-configurar-minecraft-server-sem-erro-bad-login/bad_login.jpg)

Isso acontece porque vc deveria ter uma conta premium no [](http://www.minecraft.net), para funcionar sem essa conta devemos editar o arquivo **server.properties** com qualquer editor de textos e modificar a seguinte linha

{% gist 5ce2c6c0fefaa74e5257 %}

assim o servidor já vai estar funcionando

**ps.** talvez seja necessário abrir a porte **25565** do seu roteador

#Instalar no Linux ou MacOsX

fazer o download do arquivo [minecraft_server.jar](https://s3.amazonaws.com/MinecraftDownload/launcher/minecraft_server.jar?) em http://www.minecraft.net/download, executar o comando em um terminal

{% gist f5f2efd4f845d0d3e539 %}

se vc quiser usar somente em modo texto do servidor é só colocar **nogui** no final da linha de comando ficando assim

{% gist  3c298e952f5484a6e7da %}

**ps.** no MacOX é só clicar no arquivo jar ele mesmo efetua os ajustes de memoria

comando de servidor [aqui](http://minecraft.gamepedia.com/Server_commands?cookieSetup=true)
