# Deploy on AWS EC2 with docker

### 1. Create EC2 instance with ubuntu OS Image on [AWS Console](https://aws.amazon.com/console/)
![aws-os-image](./screenshots/4.png?raw=true)
### 2. Make sure you tic _"Allow HTTP traffic from the internet"_ in the network setting
![aws-network-settings](./screenshots/5.png?raw=true)
### 3. log in to your AWS Ubuntu Linux with either local SSH or [Putty](https://putty.org/) or use directly log in to AWS Dashboard and use the Web console
### 4. Update Ubuntu Package List
As you got the access to your Ubuntu Instance, run the system update command first. This is necessary to install security and version updates for packages including refreshing of APT index cache.
`sudo apt update && sudo apt upgrade -y`
### 5. Add Docker’s package repository
Although Ubuntu’s default system repository and Snap both offer Docker packages to easily install, however, it is better to go with the official repository. Because you will have future updates from time to time for Docker on your system.  Now, on your terminal screen follows the given commands.
#### a) Install Common required packages or tools:
`sudo apt install ca-certificates curl gnupg lsb-release`
#### b) Add Docker’s GPG key:
`sudo mkdir -p /etc/apt/keyrings`

`curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg`
#### c) Add the official repository:
`echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null`
#### d) Run the system update again:
`sudo apt update`

### 6. Install Docker CE on AWS Ec2 Ubuntu

	`sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin`
### 7. Check the Version & Status
As the installation is done successfully, let’s check the version of Docker and whether its background service is running properly without any error or not.
#### For Version details:
`docker -v`
#### To get the service status:
`systemctl status docker`
### 8. Copy local files to server
* Connect to server storage with Filezilla or any SFTP tool with generated `.pem` key file.
* Create a new folder and required code files/folders inside newly created folder.
### 9. Build Docker Image
* cd into the project folder and run following command: `sudo docker build -t imageclassi:0.0.1 .`
### 10. Run Flask API in container
Run the following command to build & run the Container from Docker Image: `sudo docker run --name classi_flask_app -d -p 8188:8188 xxxxxxxxx`

**Note: `xxxxxxxxx` is the Image ID of `imageclassi` Image**
### 11. Verify the API working.
* Visit _http://server.ip.address:8188_ to verify deployment of API.
* Visit _http://server.ip.address:8188/classification_ to start using the API for Prediction.