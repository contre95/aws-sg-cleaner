resource "aws_sqs_queue" "reported_unused_sg_queue" {
  name                      = var.QUEUE_NAME
  max_message_size          = 262144 #max size 256k
  message_retention_seconds = 86400 # one day
  visibility_timeout_seconds = 2700  # aws recommends - set the source queue's visibility timeout to at least 6 times the lambda function timeout 
  #redrive_policy            = "{\"deadLetterTargetArn\":\"${aws_sqs_queue.posted_patches_notificacion_queue_deadletter.arn}\",\"maxReceiveCount\":10}"

  tags = local.common_tags
}
