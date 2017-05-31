#!/usr/bin/env python

import docker
import sys, requests, json

def get_header (repo, tag):
    login_template = "https://auth.docker.io/token?service=registry.docker.io&scope=repository:{repository}:pull"
    get_manifest_template = "https://index.docker.io/v2/{repository}/manifests/{tag}"

    response = requests.get(login_template.format(repository=repo), json=True)
    response_json = response.json()
    token = response_json["token"]
    response = requests.get(
        get_manifest_template.format(repository=repo, tag=tag),
        headers={"Authorization": "Bearer {}".format(token), "Accept": "application/vnd.docker.distribution.manifest.v2+json"},
        json=True
    )
    manifest = response.json()
    # print response.headers
    if not response.status_code == requests.codes.ok:
        return False
    return response.headers['Docker-Content-Digest']

def main():
  client = docker.from_env()
  containers = client.containers.list(filters={'status':'running'})

  print "CONTAINER ID\t", "TAG\t", "UP TO DATE?\t"
  for cont in containers:
    _id  = cont.attrs['Id'][:12]
    try:
      name, tag = cont.attrs['Config']['Image'].split(':')
    except ValueError:
      tag = "latest"
      name = cont.attrs['Config']['Image']
    finally:
      image_local = name + ":" + tag
      image = client.images.get(image_local)
      if image.attrs['RepoDigests'] == []:
          pass
      else:
          image_digest = image.attrs['RepoDigests'][0].split('@')[1]
          repo = "library/" + name
          header = get_header(repo, 'latest')

          if image_digest == header:
              ret = "TRUE"
          else:
              ret ="FALSE"
          print _id+"\t", tag+"\t", ret+"\t"

if __name__ == "__main__":
  sys.exit(main())
