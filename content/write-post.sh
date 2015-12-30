#!/bin/sh
#Usage: ./write-post.sh <post title in quotes>

T=$(date +"%Y-%m-%d %H:%M")
slug=$(date +"log_%Y-%m-%d_%H-%M")

echo "Title: $1
Tags:
Date: $T
Category: Log
Slug: $slug
Author:
Summary:" > $slug.md
vim $slug.md
