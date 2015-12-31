---
layout: post
title: Instalando Lazarus 0.9.30.rc2 no MacOSX Lion
date: 2011-10-27
categories: dev
tags: mac,pascal,lazarus,ide
type: post
published: true
---

Escreva uma vez. Compile em qualquer lugar !

![Lazarus](/static/images/post/2011-10-27-instalando-lazarus-0-9-30-rc2-no-macosx-lion/lazarus.jpg)

**Lazarus** é um ambiente de desenvolvimento integrado desenvolvido para o compilador [Free Pascal](http://pt.wikipedia.org/wiki/Free_Pascal).O software objetiva ser compatível com o Delphi e, ao mesmo tempo, suportar diversas arquiteturas e sistemas operacionais.Free Pascal é um compilador de [Object Pascal](http://pt.wikipedia.org/wiki/Object_Pascal) que roda em Linux, Windows, OS/2, Mac OS tradicional, Mac OS X, ARM, BSD, BeOS, DOS e mais. Ele foi desenhado para compilar código com a sintaxe do Delphi ou dos dialetos Pascal do Macintosh e gerar executáveis para diferentes plataformas a partir de um mesmo código-fonte. (fonte [wikipedia](http://pt.wikipedia.org/wiki/Lazarus)) Eu estava com saudade do Delphi ai resolvi esperimentar gostei bastante !

Primeiros passos :

* instalar o Xcode da apple (pode ser pela appstore ) [aqui](http://itunes.apple.com/br/app/xcode/id448457090?mt=12) 1.68 GB
* Download dos arquivos lazarus :
  * Ide Lazarus [aqui](http://sourceforge.net/projects/lazarus/files/Lazarus%20Mac%20OS%20X%20i386/Lazarus%200.9.30.2RC2/lazarus-0.9.30.2RC2-i386-macosx.dmg/download) 121.3 MB
  * Compilador fpc [aqui](http://http//sourceforge.net/projects/lazarus/files/Lazarus%20Mac%20OS%20X%20i386/Lazarus%200.9.30.2RC2/fpc-2.4.4.intel-macosx.dmg/download) 76 MB
  * Sources para o fpc [aqui](http://sourceforge.net/projects/lazarus/files/Lazarus%20Mac%20OS%20X%20i386/Lazarus%200.9.30.2RC2/fpcsrc-2.4.4.intel-macosx.dmg/download) 59.3 MB



Comece instalando o Xcode
Depois instale o compilador fpc(dentro do dmg instale primeiro o **fpc-xcode-2.4.0.pkg**) depois o **fpc-2.4.4.intel-macosx.pkg** e finalmente instale os sources do fpc

Pronto Lazarus instalado e funcionando !! Pode Começar a brincar !!

**PS.** instale tb o ZEOSLIB (conector com banco de dados ) neste link um [tutorial](http://professorcarlos.blogspot.com/2010/03/lazarus-conectando-postgresql-com.html) muito bom !!