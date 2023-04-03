# create an ec2 and attach i am Role
# install packer using below commands
sudo yum install -y yum-utils

sudo yum-config-manager --add-repo https://rpm.releases.hashicorp.com/AmazonLinux/hashicorp.repo

sudo yum -y install packer

packer validate file name

packer build file name(apache.json)
