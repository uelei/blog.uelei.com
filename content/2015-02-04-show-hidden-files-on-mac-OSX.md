---
layout: post
title:  "Show hidden files on mac"
categories: mac
date: 2015-02-04 12:00
tags: mac hidden files
---

To show hidden files on Mac, just run the follow command on terminal

    #!bash
    defaults write com.apple.finder AppleShowAllFiles true && killall Dock

[gist](https://gist.github.com/uelei/c91d41e2360a802bdf54)

![hidden_files](/assets/images/post/2015-02-04-show-hidden-files-on-mac-OSX/hidden_files.jpg)
