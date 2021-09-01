resource "aws_instance" "app_python" {
  ami                    = var.vm_ami
  instance_type          = var.vm_type
  vpc_security_group_ids = [aws_security_group.allow_http.id]
  subnet_id              = aws_subnet.subnet1.id

  tags = {
    Name = "server"
  }
}
