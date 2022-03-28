                                                  Hello! I'm Burak.

# About me

* 💼 Senior DevOps Engineer at [Intertech](https://www.intertech.com.tr/)
* ❤️ I love writing automation scripts and building infrastructures
* 💬 For contacting me [Linkedin](https://www.linkedin.com/in/burak-aydin-9a392065/)

# Project Description
This project is used to create a virtual machine, install Prometheus with Grafana on Azure Cloud and monitor current temperature in Tallinn/Estonia.

# Pre-requisites
[Terraform](https://www.terraform.io/) installed on your system   
[Az Cli](https://docs.microsoft.com/tr-tr/cli/azure/install-azure-cli-windows?tabs=azure-cli) installed on your system

# Nice to have
It's nice to have an azure storage for storing tfstate if you would like to store it first of all you should create Azure Storage Account
[Azure Storage](https://docs.microsoft.com/en-us/azure/developer/terraform/store-state-in-azure-storage?tabs=powershell)
If you don't want to use azure storage you can delete or comment out backend tf.

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

# Secrets
Secrets are stored in github Repositry secrets

     - TF_ARM_CLIENT_ID  //Azure Client ID
     - TF_ARM_CLIENT_SECRET  //Azure Clint Secret
     - TF_ARM_SUBSCRIPTION_ID  //Azure Subscription ID  
     - TF_ARM_TENANT_ID  //Azure Tenant ID
     - AUTH_PASSWORD  //Prometheus Password
     - VM_IP  //Virtual Machine IP
     - VM_KEY  //Virtual Machine private key
     - VM_USER //Virtual Machine user


## Building the Terraform-based infrastructure
*First off all you need login azure portal via azure cli*  
"az login"
*initialize terraform Azure modules*  
"terraform init"   
*plan and save the infra changes into tfplan file*  
"terraform plan -out tfplan"  
*apply the plan*  
"terraform apply tfplan"    
*delete the infra*  
"terraform destroy"

## Acces Temperature in Grafana
You need to get Public IP of VM from terraform apply output (there is an outputs.tf file on repo)  
"terraform output vm_ip"

From web browser VM IP:3000 login Grafana with default password (admin:admin) you can change the password after login.
There is a predefined Dashboard called as Weather in Estonia(Tallinn) (weatherestonia.json)
Weather is currently based 

## Github Actions
For automate the flow, github actions is used.
There are four workflows for terraform plan and apply.   
[Terraform Plan](https://github.com/Je0pardy/cloudformazure/actions/workflows/terraform-plan.yml) runs when a PR created to master branch   
[Terraform Apply](https://github.com/Je0pardy/cloudformazure/actions/workflows/terraform-apply.yml) runs when a PR merged to master or a commit pushed.  
[Terreform Destroy](https://github.com/Je0pardy/cloudformazure/actions/workflows/terraform-destroy.yaml) Destroys whole infrastructure with manual trigger    
[Deploy Weather Project](https://github.com/Je0pardy/cloudformazure/actions/workflows/output.yml) Deploys python code and copies custom dashboard to grafana with manual trigger


## Resources ##

| Name | Type |
|------|------|
| [Terraform Registry](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs) | resource |
| [terraform templates](https://github.com/HoussemDellai/terraform-course) | resource |
| [weather api](https://openweathermap.org/api/one-call-api) | resource |
| [prometheus and grana docker-compose repo](https://github.com/stefanprodan/dockprom.git) | resource |
