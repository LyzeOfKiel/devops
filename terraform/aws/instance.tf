resource "aws_instance" "app_python" {
  ami                    = var.vm_ami
  instance_type          = var.vm_type
  vpc_security_group_ids = [aws_security_group.allow_http.id, aws_security_group.allow_ssh.id]
  subnet_id              = aws_subnet.subnet1.id
  key_name               = aws_key_pair.master-key.key_name

  tags = {
    Name = "server"
  }
}

resource "aws_key_pair" "master-key" {
  key_name   = "ansible"
  public_key = file("./keys/id_ed25519.pub")
}