This project is used to create a virtual machine, install and configure Prometheus with Grafana on Azure Cloud.

# Pre-requisites
[Terraform](https://www.terraform.io/) installed on your system 


* An accessible Azure bucket to store Terraform state (specified in backend.tf).
* A Terraform variables file customized for  assessment environment, for example:

- resource_group_name         = "my_terraform_rg"
- resource_group_location     = "West Europe"
- virtual_network_name        = "vnetprod019"
- subnet_name                 = "subnet019"
- public_ip_name              = "publicip019"
- network_security_group_name = "nsgprod019" 
- network_interface_name      = "nicprod019"
- linux_virtual_machine_name  = "linuxvm019"

# Building the Terraform-based infrastructure


## Resources ##

| Name | Type |
|------|------|
| [terraform templates](https://github.com/HoussemDellai/terraform-course) | resource |
| [weather api](https://openweathermap.org/api/one-call-api) | resource |
