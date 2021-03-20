data "archive_file" "cleaner_code" {
    type = "zip"
    output_path = "${path.module}/sg_lambda_cleaner.zip"
    source_dir = "../cleaner"
  }

resource "aws_lambda_event_source_mapping" "event_source_mapping" {
  event_source_arn = aws_sqs_queue.reported_unused_sg_queue.arn
  enabled          = true
  function_name    = aws_lambda_function.sg_cleaner_lambda.arn
  batch_size       = 1
}

resource "aws_lambda_function" "sg_cleaner_lambda" {
  filename      = "${path.module}/sg_lambda_cleaner.zip"
  function_name = "sg_cleaner"
  handler       = "main.main"
  role = aws_iam_role.sg_cleaner_iam_role.arn
  source_code_hash = data.archive_file.cleaner_code.output_base64sha256


  runtime = "python3.8"
  
  tags = local.common_tags

  environment {
    variables = {
      "SG_COLLECTORS" = var.SG_COLLECTORS
      "RULE_GROUPS_ID_DENYLIST" = var.RULE_GROUPS_ID_DENYLIST
    }
  }
}
