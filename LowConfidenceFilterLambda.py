import json


THRESHOLD = 0.80


def lambda_handler(event, context):
    
    # Parse the body attribute of the event JSON
    event_body = json.loads(event["body"])

    # Grab the inferences from the event body
    inferences = json.loads(event_body["inferences"])

    # Check if any values in our inferences are above THRESHOLD
    meets_threshold = any(x >= THRESHOLD for x in inferences)
    
    # If our threshold is met, pass our data back out of the
    # Step Function, else, end the Step Function with an error
    if meets_threshold:
        pass
    else:
        raise ValueError("THRESHOLD_CONFIDENCE_NOT_MET")

    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }