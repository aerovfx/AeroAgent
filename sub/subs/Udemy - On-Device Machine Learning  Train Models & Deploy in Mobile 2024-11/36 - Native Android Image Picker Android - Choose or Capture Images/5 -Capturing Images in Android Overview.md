# 5 -Capturing Images in Android Overview

---

So, now after testing the application, let's quickly repeat the process so that everything

is clear for us.

So from our application we are launching camera application and inside that camera application

user is capturing the image.

And then we are getting that captured image inside our application and showing it to the

user on screen.

So to achieve that inside our application we have added a long click listener so that

whenever user is long clicking on this button we want to launch the camera.

And to do that we have created this take picture object and then we are launching our camera

application.

And while launching it we are passing the imiUri and it is indicating the location where

the captured image will be stored.

And we have created this imiUri variable above and then we initialized it inside this create

imiUri variable.

So basically while initializing this imiUri we specified the name of the image to which

this URI is pointing.

So now after passing this URI to our camera application when the camera application will

gonna capture the image it will gonna store that captured image on a location specified

by this imiUri variable.

And to give camera application the permission to write at that particular location which

this imiUri is indicating we have added some code inside our android manifest.

So here we have added a file provider and this file provider is indicating the location

inside our private space where camera application will gonna write the data.

So it is indicating the location in the private space and then we are specifying the folder

inside our private space using this path.xml file.

And then inside that particular folder the name of the file is specified using this file

object.

So hopefully you are getting the point that inside our private space at this particular

location inside this particular folder and in this particular file the captured image

will be stored.

And to achieve that we are using file provider and it is a subclass of content provider which

is used to pass data between different applications.

And in our case we want to pass the data from camera application to our application.

And that data is captured image.

So hopefully you get the idea or the complex concept behind capturing images using camera

and then displaying it inside our application in android.