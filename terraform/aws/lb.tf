# resource "aws_lb" "lb" {
#   name               = "LB"
#   internal           = false
#   load_balancer_type = "application"
#   subnets            = [aws_subnet.subnet1.id, aws_subnet.subnet2.id]

#   enable_deletion_protection = false

#   tags = {
#     Environment = "dev"
#   }
# }
