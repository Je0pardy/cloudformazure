terraform {
  backend "azurerm" {
    resource_group_name  = "cloud-shell-storage-tfstate"
    storage_account_name = "buaydinsam"
    container_name       = "tfstate"
    key                  = "terraform.tfstate"
  }
}