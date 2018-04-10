# Lab session #5: Enhancing your web app using additional cloud services

## Task 5.1: Use Amazon Simple Notification Service in your web app

The deployed app works as expected as shown in the following screenshots.

Signing up throught the deployed up:
![Singing up Screenshot](img/cc5_1signup.png)

Record appears on DynamoDB:
![DynamoDB Record Screenshot](img/cc5_1Dynamo.png)

SNS arrives at e-mail:
![SNS Screenshot](img/cc5_1SNSemail.png)

However we faced some challenges during this task:
* While working with PyCharm IDE we had to define the environment variables WITHIN the IDE (configuration problem).
* Initially, we did not commit locally before deploying our app in EB, so technically we were constanlty deploying the same old version of the app without SNS.
* Although we updated the software configuration as indicated in the assignment description, our environment variable SIGNUP_TOPIC was not being recognised. We had to update the eb environment through the bash.

## Task 5.2: Create a new option to retrieve the list of leads

The deployed app includes now an Admin Search feature and a changed navigation menu as shown in the following screenshots.

The Admin Search feature in the deployed app:
![Admin Search Feature](img/adminSearch.png)

The Results page for a specific search:
![Results of Admin Search](img/results.png)

However, we faced one challenge during this task:
* The current policy attached to the role did not include permission to scan the DynamoDB table. We had to add this permission throught the IAM Management Console (See figure below).

![IAM Console](img/scanAction.png)

## Task 5.3: Improve the web app transfer of information (optional)

## Task 5.4: Deliver static content using a Content Delivery Network

Our S3 bucket containing the static content looks like this:
![S3](img/S3.png)

Our CloudFront CDN console looks like this:
![CDN](img/CDN.png)

Finally our deployed app utilizing the CDN looks like this in Google Chrome (note that the static content is delivered through the CDN):
![App with CDN](img/app_cdn.png)

Overall, we spent approximately 6 hours for this lab. The difficulties we experienced are described in each seperate section.