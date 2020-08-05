---
layout: post
title: "Terraform gcloud kubernetes first steps"
date: "2020-08-03"
categories:
- kubernetes
- gcloud
- terraform
---

before start you need gcloud setup and terraform setup as well you can follow my 2020 setup

1- install google provider 

First we need to install google provider on terraform if you didnt do it yet !
create a file `provider.tf`


```yaml

provider "google" {
  credentials = file("./credentials/serviceaccount.json")
  project     = "demo"
  region      = "us-east1"
}

```

now run `terraform init`, gonna output something like 

```

* provider.google: version = "~> 3.32"

```

2- create a cluster kubernets

create a file as you wish (all .tf from the folder is gonna be loaded ), I used gkecluster.tf

```tf

resource "google_container_cluster" "gke-cluster" {
  name               = "uelei-gke-cluster"
  network            = "default"
  location           = "us-east1-b"
  initial_node_count = 1

  provisioner "local-exec" {
    command = "gcloud container clusters get-credentials ${google_container_cluster.gke-cluster.name} --zone  ${google_container_cluster.gke-cluster.zone} --project [PROJECT_ID]"
  }
}

```

ps. local-exec is only for export kubectl credentials, you can do it manualy after `terraform apply`


now run `terraform apply`, and answer `yes` when prompted, all the magic is goona work ! 


Done !! 

## extras 

You can also set a node pool with your disired machines 


```tf

resource "google_container_node_pool" "gke-cluster-nodepool" {
  name = "gke-cluster-node-pool"
  location = google_container_cluster.gke-cluster.location
  cluster = google_container_cluster.gke-cluster.name
  node_count = 2

  node_config {
    preemptible = true
    machine_type = "e2-micro"

    metadata = {
      disable-legacy-endpoints = "true"
    }

    oauth_scopes = [
      "https://www.googleapis.com/auth/logging.write",
      "https://www.googleapis.com/auth/monitoring",
      "https://www.googleapis.com/auth/devstorage.read_only"
    ]
  }
}

```

also add 

`remove_default_node_pool = true` to your google_container options 

thats it ! 