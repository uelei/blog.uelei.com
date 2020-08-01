---
layout: post
title: "My development environment 2020"
date: "2020-07-12"
categories:
- dev
- wsl
- python
---

Recently I swith to Windows + wsl2, and it working pretty well for my python development, below my steps to setup "nearly perfect" windows + wsl2 setup.


---  
# Terminal 

On my ubuntu (wsl2 ) I use zsh + [oh-my-zsh](https://ohmyz.sh/#install) 

1- basics ubuntu packages git + zsh + some fonts

```shell

sudo apt install git zsh  fonts-firacode

```
maybe `fonts-powerline fonts-noto-color-emoji` too if you want

2- install oh my-zsh
```shell

sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

```

# Python

I use Pyenv to manage python versions, to install pyenv we need to install some dependencies

1- install dependencies
```shell

sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python-openssl

``` 

## pyenv
2- now install pyenv 

```shell

curl https://pyenv.run | bash

````

2.5 - after install pyenv we need to add to your .bashrc 

```shell
# WARNING: seems you still have not added 'pyenv' to the load path.
# Load pyenv automatically by adding
# the following to ~/.bashrc:  

export PATH="/home/uelei/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

```

3- now install some python to use (need to restart the terminal)

```shell

pyenv install 3.8.0
pyenv install 3.7.4

```

3.1- after set a default python 

```shell

pyenv global 3.8.0

```


## pipx 

Some aplications I like to use system wide so I use [pipx](https://github.com/pipxproject/pipx), to install use some python > 3.7 (as i define 3.8), its fine 

```shell

python -m pip install pipx
pipx ensurepath

```

if you want to install some global package 
```shell

pipx install youtube-dl

```


## poetry 

Now with pipx is easy to install poetry 

```shell

pipx install poetry

```
its done !


---

# Setup VcXrsv

Now I need to setup steps to work on windows and WSL2, to use GUI we need to install on windows [VcXsrv](https://sourceforge.net/projects/vcxsrv/) to act line a X11 remote for your Wsl distro, I make a small script to add to your bashrc to automaticly export correct IP and forward to X to that IP,

1- Install VcXsrv 

[https://sourceforge.net/projects/vcxsrv/](https://sourceforge.net/projects/vcxsrv/)

2- add follow script to bashrc , that script only will be executed if is called by wsl, so you can add to your bashrc fearless

```shell

if (( ${+WSL_DISTRO_NAME} )); then
        echo "exporting display for wsl"
        export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2; exit;}'):0.0
        export GPG_TTY=$(tty)
fi

```


# extras 

[spaceship theme](https://github.com/denysdovhan/spaceship-prompt) for zsh is beatyfull 

```shell 

git clone https://github.com/denysdovhan/spaceship-prompt.git "$ZSH_CUSTOM/themes/spaceship-prompt"


ln -s "$ZSH_CUSTOM/themes/spaceship-prompt/spaceship.zsh-theme" "$ZSH_CUSTOM/themes/spaceship.zsh-theme"

```
you need to change theme on `.zshrc` too ! 

Set `ZSH_THEME="spaceship"` in your `.zshrc`.


# gcloud 

https://cloud.google.com/sdk/docs/quickstart-debian-ubuntu

### Add the Cloud SDK distribution URI as a package source
```shell

echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
```
### Import the Google Cloud Platform public key
```shell
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -

```

### Update the package list and install the Cloud SDK
```shell

sudo apt-get update && sudo apt-get install google-cloud-sdk

```

```shell

gcloud init 

```


# kubectl 

```shell

https://kubernetes.io/docs/tasks/tools/install-kubectl/

curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/kubectl
kubectl version --client

```

# helm


https://helm.sh/docs/intro/install/

Always install the most update one ! 

```shell

curl https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash

```


# Terraform

1- Download the most update one and unpack it 
[https://www.terraform.io/downloads.html](https://www.terraform.io/downloads.html)


2- move to your `$PATH`

```shell

mv ~/Downloads/terraform /usr/local/bin/

```
