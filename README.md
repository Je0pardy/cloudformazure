This project is used to create a virtual machine, install and configure Prometheus with Grafana on Azure Cloud.

# Pre-requisites
[Terraform](https://www.terraform.io/) installed on your system 

# Nice to have
[Azure Storage](https://docs.microsoft.com/en-us/azure/developer/terraform/store-state-in-azure-storage?tabs=powershell) For backend.tf (it's commented out on repo)

* An accessible Azure bucket to store Terraform state (specified in backend.tf).

# Variables
* A Terraform variables file customized for  assessment environment, for example:

  - resource_group_name         = "my_terraform_rg"
  - resource_group_location     = "West Europe"
  - virtual_network_name        = "vnetprod019"
  - subnet_name                 = "subnet019"
  - public_ip_name              = "publicip019"
  - network_security_group_name = "nsgprod019" 
  - network_interface_name      = "nicprod019"
  - linux_virtual_machine_name  = "linuxvm019"

## Building the Terraform-based infrastructure
*initialize terraform Azure modules*  
terraform init  
*plan and save the infra changes into tfplan file*  
terraform plan -out tfplan  
*apply the plan*  
terraform apply tfplan  
*delete the infra*  
terraform destroy  

## Resources ##

| Name | Type |
|------|------|
| [Terraform Registry](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs) | resource |
| [terraform templates](https://github.com/HoussemDellai/terraform-course) | resource |
| [weather api](https://openweathermap.org/api/one-call-api) | resource |
| [prometheus and grana docker-compose repo](https://github.com/stefanprodan/dockprom.git) | resource |
