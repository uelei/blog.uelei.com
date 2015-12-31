---
layout: post
title: "Configurando a saida de audio no linux com alsamixer"
date: 2012-04-10
categories: linux
tags:
- linux
- som
- alsamixer
---

configurando a saída de audio no linux alsamixer, se o audio no maximo ainda nao é o suficiente : vamos ajustar o alsamixer para explorar todo o potencial da placa, geralmente o linux rezerva 25% para nao “forçar” o amplificador de som ; no meu caso mesmo no maximo o volume estava quase inaudivel  (acabei de invertar essa palavra ) vamos ao que intereça !

primeiro como root execute :

{% gist 18e43e778bf28b1a7a22 %}

vc verá esta tela

![](/assets/images/post/2012-04-10-configurando-a-saida-de-audio-no-linux-com-alsamixer/alsamixer.png)

selecione o MASTER e aparte o direcional para cima até o maximo depois ESC
agora vamos gravar as mudanças, como root execute o seguinte comando :

{% gist 619ae9dc57ea3c8d835a %}

agora está tudo pronto é só usar.
