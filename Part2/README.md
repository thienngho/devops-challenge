## Usage

### Put check_tags.py into python:2.7.13-alpine
$ docker build . -t check_tags

### Launch check_tags.py with local docker socket
$ docker run -ti --rm -v /var/run/docker.sock:/var/run/docker.sock check_tags
