---
layout: post
title: "Mac file server no ubuntu 10.04"
date: 2011-11-28
categories: linux mac
tags:
- linux
- mac
- avahi
- server
- ubuntu
---

![](/assets/images/post/2011-11-28-mac-file-server-no-ubuntu-1004/ubuntu_mac_feature_thumb.jpg)

Transformar seu ubuntu/debian em um servidor de arquivos para Mac, assim vc pode facilmente fazer backups em rede (usando o time machine) ou simplimente compartilhar arquivos **mac-linux**
**primeiro devemos instalar o netatalk**

{% gist be7afdf2a7c2dcf025c2 %}

editar as configurações no arquivo **/etc/default/netatalk**

{% gist 4a22abc6d1e12fdc3f40 %}

deixe ele com as seguintes configurações

{% gist 3812d9977ce34994cc40 %}

edite e descomente a ultima linha do arquivo **/etc/netatalk/afpd.conf**

{% gist 86aaaa2cb46eb0cf0b83 %}

e ultima linha deve ficar assim

{% gist f75296ef3edd9e73a088 %}

agora vamos reiniciar o netatalk

{% gist 0a64041d0bb0a3187900 %}

![](/assets/images/post/2011-11-28-mac-file-server-no-ubuntu-1004/bonjour97.png)

**Instalar o avahi**

{% gist da438192f44d1d56d395 %}

editar o arquivo **/etc/nsswitch.conf**

{% gist cb54359bfa0923e54fc2 %}

deixando assim

{% gist 50e9d40582b544712b9f %}

agora vamos criar o arquivo **/etc/avahi/services/afpd.service**

{% gist d93060b94f0c63c10792 %}

com o seguinte conteudo

{% gist a08ac5704548fa48810a %}

e finalmente reiniciar o avahi

{% gist aa0ac1bf1d42efa5511e %}

agora é só testar

( fontes [completo](http://www.kremalicious.com/2008/06/ubuntu-as-mac-file-server-and-time-machine-volume/),[outra](http://www.cognitivecombine.com/2009/12/diy-ubuntu-nas-with-afp-smb-dlna-and-itunes/))
