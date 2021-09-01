variable "region" {
  description = "AWS Region"
  default     = "eu-central-1"
}

variable "vm_ami" {
  description = "VM AMI"
  default     = "ami-05f7491af5eef733a"
}

variable "vm_type" {
  description = "VM instance type"
  default     = "t2.micro"
}