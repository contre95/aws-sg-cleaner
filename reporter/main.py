from presenters.AWSLambda.handler import lambda_handler
from presenters.AWSLambda.handler import lambda_handler


def main(event=None, context=None):
    lambda_handler(event, context)

if __name__ == "__main__":
    main()
