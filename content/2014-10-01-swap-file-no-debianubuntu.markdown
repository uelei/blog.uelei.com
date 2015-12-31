---
layout: post
title: "Swap file no debian/ubuntu"
date: 2014-10-01
categories: linux
tags:
- linux
- debian
- ubuntu
- swap
- memory
---

Para habilitar um arquivo de swap para o debian/ubuntu, primeiro devemos criar um arquivo imagem

{% gist 3ce560ca309de2c3b8e9 %}

depois transforme esse arquivo em imagem tipo **swap**

{% gist df1de3fdb0f21c91000c %}

e finalmente ative essa imagem

{% gist 560f3e5f2a1fabbe93d8 %}

Já está funcionando, mas para carregar automaticamente apos o boot temos que incluir no arquivo **/etc/fstab**

{% gist 904ca7e44a064c837de8 %}
