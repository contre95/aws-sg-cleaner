data "archive_file" "reporter_code" {
    type = "zip"
    output_path = "${path.module}/sg_lambda_reporter.zip"
    source_dir = "../reporter"
  }

resource "aws_lambda_function" "sg_reporter_lambda" {
  filename      = "${path.module}/sg_lambda_reporter.zip"
  function_name = "sg_reporter"
  handler       = "main.main"
  role = aws_iam_role.sg_reporter_iam_role.arn
  source_code_hash = data.archive_file.reporter_code.output_base64sha256

  runtime = "python3.8"
  
  tags = local.common_tags

  environment {
    variables = {
      "SG_COLLECTORS" = var.SG_COLLECTORS
      "SQS_URL" = var.SQS_URL
    }
  }
}


# Lambda trigger

resource "aws_cloudwatch_event_rule" "every_day" {
  name                = "every-one-day"
  description         = "Fires every one day"
  schedule_expression = "rate(1 day)"
}

resource "aws_cloudwatch_event_target" "check_foo_every_one_minute" {
  rule      = aws_cloudwatch_event_rule.every_day.name
  target_id = "lambda"
  arn       = aws_lambda_function.sg_reporter_lambda.arn
}

resource "aws_lambda_permission" "allow_cloudwatch_to_call_lambda" {
  statement_id  = "AllowExecutionFromCloudWatch"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.sg_reporter_lambda.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.every_day.arn
}
