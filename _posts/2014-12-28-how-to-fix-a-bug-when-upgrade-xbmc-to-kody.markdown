---
layout: post
title: "How to fix a bug when upgrade xbmc to kody"
date: "2014-12-28"
tags: kody xbmc fix
categories: hack
---
![kodi](/assets/images/post/2014-12-28-how-to-fix-a-bug-when-upgrade-xbmc-to-kody/kodi.png)

I recently upgrade my xbmc but when i started just a login screen show up. I found the fix in [http://forum.kodi.tv/showthread.php?tid=207214&pid=1821898#pid1821898](http://forum.kodi.tv/showthread.php?tid=207214&pid=1821898#pid1821898)

update line 5 of the file /etc/lightdm/lighdm.conf

{% gist a654808c6804f0fa4935  %}

and restart
