resource "aws_dynamodb_table" "log_table" {
  name           = "log_table"
  billing_mode   = "PROVISIONED"
  read_capacity  = "30"
  write_capacity = "30"
  range_key      = "time"
  hash_key       = "type"


  attribute {
    name = "time"
    type = "S"
  }

  attribute {
    name = "type"
    type = "S"
  }

  ttl {
    enabled        = true
    attribute_name = "expiryPeriod"
  }
}

