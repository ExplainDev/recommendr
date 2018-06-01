# kommandr-ML
Machine Learning Service of Kommandr

This API service recommends a k number of programs similar to another program  you pass as a query parameter

### Prerequisites
- Docker

## Installation

### Download the source code
`git clone git@github.com:kommandr/kommandr-ML.git`

### Build docker image
`docker build -t api-recommendr .`

### Run docker container
`docker run --rm -it --name api-recommendr -p 7070:7070 --network kommandrapi_default api-recommendr`

## Usage
Examples

### Show up to 10 programs similar to 'git commit'
```
$ curl -X GET 'http://localhost:7070/recommendations?program=git%20commit&k=10'
{
  "git bisect": "Use binary search to find the commit that introduced a bug.\nGit automatically jumps back and forth in the commit graph to progressively narrow down the faulty commit.",
  "git blame": "Show commit hash and last author on each line of a file.",
  "git clone": "Clone an existing repository.",
  "git gc": "Optimise the local repository by cleaning unnecessary files.",
  "git pull": "Fetch branch from a remote repository and merge it to local repository.",
  "git rm": "Remove files from repository index and local filesystem.",
  "hg add": "Adds specified files to the staging area for the next commit in Mercurial.",
  "hg commit": "Commit all staged or specified files to the repository.",
  "hg init": "Create a new repository in the specified directory.",
  "hg pull": "Pull changes from a specified repository to the local repository."
}
```
### Show up to 5 programs similar to 'halt' 
```
$ curl -X GET 'http://127.0.0.1:7070/recommendations?program=halt&k=5'
{
  "kexec": "Directly reboot into a new kernel.",
  "reboot": "Reboot the system.",
  "shutdown": "Shutdown and reboot the system.",
  "systemsetup": "Configure System Preferences machine settings."
}
```
