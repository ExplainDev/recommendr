# kommandr-ML
Machine Learning Service of Kommandr

This API service recommends a k number of programs similar to another program  you pass as a query parameter

### Prerequisites
- Docker

## Installation

### Download the source code
```bash
git clone git@github.com:kommandr/kommandr-ML.git
```

### Build docker image
```bash
docker build -t api-recommendr .
```

### Run docker container
```bash
docker run --rm -it --name api-recommendr -p 7070:7070 --network backend_default api-recommendr
```

## Usage
Parameters:
- program: the program name
- platformid: the platformId
  - 1: Generic, a program is usually installed and used in multiple OS's
  - 2: Linux
  - 3: macOS
  - 4: Windows
- k: return up to k programs
- 

### Show up to 10 programs similar to 'git commit'
```bash
$ curl -X GET 'http://192.168.99.100:7070/recommendations?program=rmdir&platformid=1&k=5'
{
  "recommendations": [
    {
      "cliName": "mkdir", 
      "shortDescription": "Creates a directory."
    }, 
    {
      "cliName": "popd", 
      "shortDescription": "Changes the current directory to the directory stored by the `pushd` command."
    }, 
    {
      "cliName": "popd", 
      "shortDescription": "Remove a directory placed on the directory stack by the `pushd` command."
    }, 
    {
      "cliName": "popd", 
      "shortDescription": "Remove a directory placed on the directory stack via the pushd shell built-in."
    }, 
    {
      "cliName": "ls", 
      "shortDescription": "List directory contents."
    }
  ]
}
```
### Show up to 5 programs similar to 'halt' 
```bash
$ curl -X GET 'http://192.168.99.100:7070/recommendations?program=halt&platformid=1&k=5'
{
  "recommendations": [
    {
      "cliName": "reboot", 
      "shortDescription": "Reboot the system."
    }, 
    {
      "cliName": "shutdown", 
      "shortDescription": "Shutdown and reboot the system."
    }, 
    {
      "cliName": "shutdown", 
      "shortDescription": "Shutdown and reboot the system."
    }, 
    {
      "cliName": "kexec", 
      "shortDescription": "Directly reboot into a new kernel."
    }, 
    {
      "cliName": "systemsetup", 
      "shortDescription": "Configure System Preferences machine settings."
    }
  ]
}
```

