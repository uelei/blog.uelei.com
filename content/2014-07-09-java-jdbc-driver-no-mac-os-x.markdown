---
layout: post
title: "Java JDBC driver no Mac OS X"
date: 2014-07-09
categories: java
tags:
- mac
- java
- mysql
- jdbc
- java
- driver
---

Ao complilar codigo usando o eclipse no mac usando as bibliotecas java.sql o eclipse retorna erro ! E não é possivel adicionar ao classPatch, mas é facilmente contornado.

Primeiro faça o download do conector no site [http://dev.mysql.com/downloads/connector/j/5.1.html](http://dev.mysql.com/downloads/connector/j/5.1.html)

depois descompacte e copie o arquivo **mysql-connector-java-5.x.x-bin.jar** para o diretorio
**/Library/Java/Extensions/**

pronto tudo vai funcionar corretamente.

[fonte](http://gumho.blogspot.com.br/2009/10/mysql-jdbc-and-mac-os-x.html)
