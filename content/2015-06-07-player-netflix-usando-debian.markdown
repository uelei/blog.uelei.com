---
layout: post
title: "Player Netflix usando debian"
date: 2015-06-07
categories:
- Netflix
- debian
- oldpc
- linux
---

  Objetivo foi criar uma instalação linux leve para servir como player da netflix
como a [netflix](https://www.netflix.com) recentemente addicionou suporte ao google chrome
sem a nescessidade de instalação do silverlight da microsoft, resolvir usar uma
mini instalação do debian como base.

primeiro instale o debian sem nenhum pacote de preferencia, eu usei a net install e quando perguntou para instalar os pacotes só selecionei o **ssh-server**

![debian packages](/images/post/2015-06-07-player-netflix-usando-debian/debian install packages.png)


  Apos a instalacao devemos instalar os pacotes do xfce, mas so queremos os pacotes basicos, usamos o commando --no-install-recommends
vamos instalar tb o slim como gerenciador de login

[gist:id=ece4c21c9e04f3a23bf6]


  Apos a instalação do xfce vamos instalar o google chrome, execute um comando de cada vez

[gist:id=4d1e160d6627bf6055ca]


  Vamos configurar o slim para autologin editanto o arquivo **/etc/slim.conf** editar de acordo com seu usuario e autologin yes

[gist:id=31257e6edcbefcf13972]


  Agora reinicie e vamos adicionar o google para rodar automaticamente em tela cheia, no xfce temos que ir em Menu de Aplicativos > Configurações > Gerenciador de Configurações > Sessão e inicialização > inicio automatico de Aplicativos
adicionar o seguinte commando

[gist:id=1f75ff3d4b46c9c1c3a9]

no meu caso tb mudei as acessibilidade para usar o mouse pelo teclado em Menu de Aplicativos > Configurações > Acessibilidade > mouse > usar emulação de mouse


[](http://auriza.site40.net/notes/debian/xfce-minimal-installation/)
[](http://www.tecmint.com/install-google-chrome-in-debian-ubuntu-linux-mint/)
[](http://forum.xfce.org/viewtopic.php?id=7864)
[](http://www.linuxquestions.org/questions/debian-26/squeeze-slim-how-to-autologin-852573/)
[](http://www.techiecorner.com/1941/how-to-auto-start-chrome-in-full-screen-mode-f11-everytime/)
[](http://askubuntu.com/questions/234663/what-command-should-i-type-to-run-chrome-from-the-terminal)
[](http://docs.xfce.org/xfce/xfce4-settings/accessibility)
