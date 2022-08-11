resource "aws_s3_bucket" "test_bucket" {
  bucket = "tf-test-bucket"
  acl    = "private"

  tags = {
    Name = "tf-test-bucket"
  }
}
