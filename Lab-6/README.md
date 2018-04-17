# Lab session #6: Interacting with users and services in the Cloud


## Q61a: Having domain_freq.json written as static content is not the best way to distribute it because different clients can invoke different parameters simultaneously? Can you use S3 to solve the problem? Write the changes in the code and explain your solution?

Yes S3 can be used to solve this problem.The problem is by default, CloudFront doesn't consider headers when caching objects in edge locations. If origin returns two objects and they differ only by the values in the request headers, CloudFront caches only one version of the object. 

To solve this issue, we first uploaded static contents into s3 bucket and created CloudFront distrubution of that bucket. To enable cross-domain acess in CLoudFront, we attached CORS configuration to static content bucket because CORS finds a way for client web applications that are loaded in one domain to interact with resources in a different domain. After that  we enabled Header Forwarding in CloudFront distrubution that's associated with the S3 bucket. By doing that we made CloudFront to forward all headers to our origin.

CORS Configuration: 
```xml
<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
<CORSRule>
    <AllowedOrigin>*</AllowedOrigin>
    <AllowedMethod>GET</AllowedMethod>
    <AllowedHeader>*</AllowedHeader>
</CORSRule>
</CORSConfiguration>
```
## Q61b: Once you have your solution implemented publish the changes to EB and try the new functionality in the cloud. Did you need to change anything, apart from the code, to make the web app work?

We added configuration related to CloudFront and S3 bucket to eb
