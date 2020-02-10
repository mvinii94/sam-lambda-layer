import json
import logging
import requests

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    try:
        ip = requests.get("https://checkip.amazonaws.com/").text.replace("\n", "")
        logger.info("Requester IP: %s" % ip)
    except requests.RequestException as e:
        logging.error(e)
        raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            "location": ip
        }),
    }
