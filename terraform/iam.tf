#Queue IAM resources

data "template_file" "unused_sg_queue_inline_policy_file" {
  template = file("${path.module}/policies/unused_sg_queue_policy.json") 

  vars  = {
    lambda = aws_lambda_function.sg_reporter_lambda.arn
    queue = aws_sqs_queue.reported_unused_sg_queue.arn
  }
}


resource "aws_sqs_queue_policy" "permit_lambda_put_messages" {
  queue_url = aws_sqs_queue.reported_unused_sg_queue.id
  policy = data.template_file.unused_sg_queue_inline_policy_file.rendered
}

#SG Reporter Lambda IAM resources

data "template_file" "sg_reporter_iam_inline_policy_file" {
  template = file("${path.module}/policies/sg_reporter_inline_policy.json") 

  vars  = {
    queue = aws_sqs_queue.reported_unused_sg_queue.arn
    account = var.AWS_ACCOUNT_NUMBER
  }
}

resource "aws_iam_role" "sg_reporter_iam_role" {
  name = "SGReporterLambdaRole"
  assume_role_policy = file("${path.module}/policies/sg_reporter_assume_role_policy.json")
}

resource "aws_iam_role_policy" "sg_reporter_iam_inline_policy" {
  name = "SGReporterLambdaPolicy"
  role = aws_iam_role.sg_reporter_iam_role.id
  policy = data.template_file.sg_reporter_iam_inline_policy_file.rendered

}

#SG Cleaner Lambda IAM resources

data "template_file" "sg_cleaner_iam_inline_policy_file" {
  template = file("${path.module}/policies/sg_cleaner_inline_policy.json") 
  
  vars  = {
      queue = aws_sqs_queue.reported_unused_sg_queue.arn
      account = var.AWS_ACCOUNT_NUMBER
  }
}

resource "aws_iam_role" "sg_cleaner_iam_role" {
  name = "SGCleanerLambdaRole"
  assume_role_policy = file("${path.module}/policies/sg_cleaner_assume_role_policy.json")
}

resource "aws_iam_role_policy" "sg_cleaner_iam_inline_policy" {
  name = "SGCleanerLambdaPolicy"
  role = aws_iam_role.sg_cleaner_iam_role.id
  policy = data.template_file.sg_cleaner_iam_inline_policy_file.rendered

}


