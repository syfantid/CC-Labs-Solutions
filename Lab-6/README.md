# Lab session #6: Interacting with users and services in the Cloud

### Task 6.1: How to provide your services through a REST API?

#### Q61a: Having domain_freq.json written as static content is not the best way to distribute it because different clients can invoke different parameters simultaneously? Can you use S3 to solve the problem? Write the changes in the code and explain your solution?

Yes, it is problematic to save the domain files as static content, because in reality they depend on the user's query. This mean that if 100 users perform 100 different queries, then 100 files will be created in our static folder and our site will be too heavy to load in the browser. However, if we use S3 all these files will be uploaded in S3 and the wep application will simply access them from there (no extra load). 

To achieve this the moment the user requests the domain frequencies a file is being created in S3 with a name representative of the user's query e.g. domain_freq_gmail_no.json (for domain gmail.com and preview access specified as no) or domain_freq.json (no parameters specified), etc. The file contains a JSON which reflects the current state of the Domain DynamoDB table (table in the form of (key,pair) or ([domain,preview access], frequency). For each user request a new file is being created because there might be insertions or updates in the table between different users' requests (even if the request is the same).

Thus, instead of rendering contents from a static file in the chart.html template, we now render contents from the S3 file. Of course our bucket has public read access.

Moreover, we chose not to distribute the domain files through CloudFront because their content is updated constantly and it would not be efficient to update the distributions for every user query.

Finally, to allow updates on the Domain table (e.g. after a new signup a domain count may need to increment) we needed to adjust our policy to allow UpdateItem action for DynamoDB.

#### Q61b: Once you have your solution implemented publish the changes to EB and try the new functionality in the cloud. Did you need to change anything, apart from the code, to make the web app work?

We added software configuration related to CloudFront and S3 bucket to EB (to be used for both map and chart rendering). A printscreen of the deployed app can be seen below.

Specifying domain name and preview (Same domain name, different preview parameter):
![yes](img/domprevyes.png)

![no](img/prevdomno.png)

No parameters:
![Chart](img/chart.png)

### Task 6.2: How to provide our service combined with third-party services?

#### Q62a: Now we are showing all the collected tweets on the map. Can you think of a way of restricting the tweets plotted using some constraints? For instance, the user could invoke http://127.0.0.1:8000/map?from=2018-02-01-05-20&to=2018-02-03-00-00. Implement that functionality or any other functionality that you think it could be interesting for the users. Change the code to implement the new feature and explain what you have done and show the results in the README.md file for this lab session.

Using a GET request we obtain the requested `from_date` and `to_date` from the URI. Then, in `models.py`, we convert these date strings to a datetime format and to a timestamp string, which is compared to the `created_at` field of each tweet (this field is also stored in a timestamp string format in DynamoDB). Only the tweets that fall within the specified range are returned. If no range is specified then all tweets are returned (full scan). The application supports both bounded and unbounded queries.

#### Q62b: Make the necessary changes to have geo_data.json distributed using S3, or the method you used for the above section. Publish your changes to EB and explain what changes have you made to have this new function working.

`geo_data.json` is not a static content file. It changes depending on the user's query. That's why we save multiple files in S3, whose names are representative of the queries they derive from. For instance, for a range between Tue, 17 Apr 2018 19:37:18 GMT (epoch timestamp: 1523993839) and  Wednesday, April 18, 2018 7:37:18 PM (epoch timestamp: 1523993931), the filename would be 1523993839-1523993931.json (See caption below). This way if a user requests the same date range the database will not be queried again, but the result will come from S3. This happens because the tweets that belong to a specific range are not changing. If the query is unbounded then we use the system's minimum and current timestamps. This process can be found in `view.py`. Note here that for every user request the application will first look for an equivalent file in S3 and if the file is not found it will query the database return the results and write a new file to S3 for the specific timeframe.

![json date files](img/mapss3.png)

For this bucket we consider that enabling CloudFront distribution would be more efficient, because the contents of the created files never change. 

To enable cross-domain access in CLoudFront, we attached a CORS configuration to the S3 bucket, because CORS enables a client web application that are loaded in one domain to interact with resources in a different domain (preventing Cross-Origin Resource Sharing related problems). After that  we enabled Header Forwarding in CloudFront distrubution that is associated with the our S3 bucket. By doing that, CloudFront now forwards all headers to our origin.

CORS Configuration: 
```xml
<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
<CORSRule>
    <AllowedOrigin>http://*</AllowedOrigin>
    <AllowedOrigin>https://*</AllowedOrigin>
    <AllowedMethod>GET</AllowedMethod>
    <MaxAgeSeconds>3000</MaxAgeSeconds>
    <AllowedHeader>*</AllowedHeader>
</CORSRule>
</CORSConfiguration>
```

![edit_behaviour_cloudfront](img/edit_behaviour_cloudFront.png)

Also, we attached the following Bucket Policy to our S3 Bucket to allow public access to objects, because declaring the bucket as public did not impose public read access to its objects.

```xml
{
    "Version": "2012-10-17",
    "Id": "Policy1523982566712",
    "Statement": [
        {
            "Sid": "Stmt1523982551046",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::map-jsons-dump/*"
        }
    ]
}
``` 
The deployed app can be seen in the screenshots below.

Bounded Query:
![bounded](img/map_from_to.png)

Unbounded Query:
![unbounded](img/map_to.png)

No parameters:
![no parameters](img/map.png)

In the following picture it is clearly shown how CloudFront is enabled for the static content S3 bucket containing the CSS and image files (eb-django-express-signup-423127002349.s3.amazonaws.com) and the maps' files bucket (map-jsons-dump.s3.amazonaws.com) but is disabled for the domain bucket (domain-bucket-43127002349.s3.amazonaws.com).

![cloudfront](img/cloudfront.png)

#### Q62c: How would you run TwitterListener.py in the cloud instead of locally? Try to implement your solution and explain what problems have you found and what solutions have you implemented.

Since `TwitterListener.py` is independent of our web application and just uses the same DynamoDB table we should not integrate it in the current application. It should run independently of it. Also, since it is not a Django application but simply a python script with limited dependencies, we do not need to run it through Elastic Beanstalk. 

What we did instead is that we connected through SSH to our EC2 instance and uploaded and executed the `TwitterListener.py` file there. Then it is possible to execute `TwitterListener.py` parallel to the application and stop it at anytime without stopping the application itself. The executed application on the EC2 instance can be seen below.

![listener](img/twitterlistener.png)

We also had to install the necesecary requirements (e.g. tweepy, boto, etc.) through `pip install -r requirements.txt`, in order to execute the python script. Given that Amazon's AMI Linux is slighlty different than Ubuntu we had some trouble figuring out how to set up e.g. install pip for Python 3.6 instead of 2.7 (default installation), but finally manage to overcome this difficulty by using the full path to the pip-3.6 executable instead of just the pip command. 

### Task 6.3: Advanced Analytics as a Service in the Cloud (optional task)

For this section, we collected tweets with images from specific user accounts. 'extended_entities' property of tweets was taken into account because if a tweet has picture, it is in 'extended_entities'. Inside 'extended_entities' only media with 'photo' type selected.
Then the images collected from tweets were sent to Google Cloud Vision through api for analysis. Every tweet was labelled with tags then these tags were converted into JSON. For storing tweets and related tag set we used DynamoDB. After succesfully saving 100 images into database, we used Plotly api to plot the data we have. Total score of tags for all images were calculated and showed in bar plot.

 ![DynamoDB](img/Twitter_DynamoDB.png)

Examples;
 
 @CNN:
 
 ![CNN](img/CNN.png)
 
 @EarthPix:
 
 ![EarthPix](img/EarthPix.png)

#### Q63: What problems have you found developing this section? How did you solve them?

When getting tweets from user timeline, we received index out of range error because in default, api.user_timeline() gets 20 tweets from user timeline. We have to add count=100 inside to get the last 100 tweets.
Also we had some issues with building JSON strings of valid JSON format. But after we searched online we found the solution.

#### Q64: How long have you been working on this session (including the optional part)? What have been the main difficulties you have faced and how have you solved them?
Approximately we spent 9 hours each for the whole lab 6 including optional part.
