#comandos para subir o ambiente hadoop-docker

$sudo apt-get update

$sudo apt install apt-transport-https ca-certificates curl software-properties-common

$curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

$echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

$sudo apt update

$sudo apt-cache policy docker-ce

$sudo apt-get install docker-ce make

$sudo systemctl status docker

$sudo apt-get upgrade

#Após criar os Dockerfile execute o comando abaixo

$sudo make build