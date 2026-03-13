# 3 -Capturing Images using Camera in Android

---

after choosing images from gallery the next thing is capturing images using

camera inside of our application. So now we are going to start implementing that

part. So basically inside of our application we want that when user click

on that button then the gallery will be opened and he can select the image and

we have implemented that part and now we want that when user long press on this

button then the camera will be opened and he can capture an image and once he

will gonna capture the image the captured image will be displayed here

inside this image view and to do that the first thing is adding an own long

click listener on our button. So here we are going to use this BTN and we are

going to call this set own long click listener. So there you can see this own

long click listener so simply select it and it will be added and then this own

long click listener will gonna return a boolean variable so we are going to

return true here and that's it. So now whenever you will gonna long click on

this button then this block will be executed and here we can write the code

for opening the camera and capturing the image. So how we are going to do that

thing? So to achieve that or to launch the camera activity where user can

capture the image the process is similar to choosing images although there are

some differences and we are also going to handle them. So the first step of

doing this thing is registering for an activity result. So similar to our

choosing images we are going to call this register for activity result method

here and after that inside this method we are going to specify the contract or

the type of activity and to do that we are going to use this activity result

contracts and now we are going to specify the type equal to take picture.

So as for now we want to capture images using camera so here the type will be

take picture and after that we are going to add the callback here which will be

executed once user have captured that image but now inside this callback we

are not going to get the URI of the captured image and there is a specific

reason for it and we are also going to handle it. But for now after calling this

method similar to our choosing images we are going to assign the result to a

variable so here we are going to create this variable and name it take picture

and after that we are going to assign the result to it and then inside this

onClickListener we are going to use this take picture for launching the camera

activity. So here we are going to call this take picture dot launch method and

then inside this method we are going to specify a parameter and that parameter

is actually the URI of the image. So what does that mean? So it means that if we

want to launch the camera activity from our application so that we can capture

an image then during launching that activity we need to specify or pass the

URI where the captured image will be stored. So basically inside this launch

method we are going to pass a URI variable and then inside that URI

variable the captured image will be stored. So here we are going to firstly

declare a URI variable above. So below this button let's declare a lateIntUri

variable and we are going to name this variable as imageUri. So I will gonna

rename it imageUri and after that the data type of this variable is URI. So

simply import this class and now inside this launch method we are going to pass

this imageUri and that's it. So now when the user will gonna long click on

this method we are going to call this takePicture.launch method and pass

this imageUri and upon click on this launch method the camera will be visible

here and once user will gonna capture the image inside that activity the

captured image will be stored inside this imageUri variable and after that

inside this callback we can show that captured image to the user on screen and

to do that we can use the code which is present here so you can simply copy this

code and then put it inside this register for activity result but here we

are going to use our imageUri variable so simply select it and then also

pass it here and that's it. So now when the camera activity will be launched user

will gonna capture the image and once he will gonna capture the image this

callback will be executed and we are going to show the captured image inside

our imageView but here the process of launching that camera activity and then

capturing that image is not that simple we have to do some additional steps as

well and the first step is we need to firstly initialize this imageUri

variable so basically while launching this activity when we are passing this

imageUri this Uri is pointing to the location where the captured image will

be stored but for now we have simply declared this imageUri variable and we

did not initialize it but now we are going to initialize this imageUri

variable and then pass it here and once we are going to pass it then the camera

activity will gonna store our captured image at that particular location where

this imageUri is pointing. So now to initialize this imageUri variable we are

going to create a function here and we are going to name this function create

imageUri and after that in the body of this function we are going to

initialize our Uri variable. So now inside this method to initialize our Uri

we are firstly going to create a file object and this file object will be for

storing the image which will be captured so as the captured image is actually an

image file so to store that image file we need a file object so here we are

going to declare an object and we are going to name it image and after that

the data type of this object is file and now inside this files constructor we are

going to pass the directory where that file will be created and then the name

of the file so to specify the directory we are going to use application context

dot files directory and then we pass the name of the file to camera photo dot png

similarly if you want you can select a different name here so now after

creating this file object we need to get the Uri for that file and then we need

to return that Uri so basically to initialize our imageUri variable we are

going to call this create imageUri method inside our own create so here

above our take picture we are going to initialize our imageUri variable and to

do that we are going to call this create imageUri method so this method

should return an object of type Uri and now inside this method we are going to

return a Uri object and to do that we are going to use a class here called

file provider so basically file provider is subclass of content provider and in

Android content provider is used to transfer data between two applications

securely and in our case we want to capture images using the camera

application and then we want to get that captured image inside our application so

basically the data will be transferred from camera application to our

application and we are going to do that using a subclass of content provider

called file provider so here to get the Uri we are going to use get Uri for file

method of this file provider so simply add this method here and then inside

this method we are going to pass few parameters and the first one is the

application context so simply pass our application context and after that it

has added two other things so the second thing which we are going to pass is the

authority and this is actually a unique string and in our case we are going to

pass the package name of our application which is com.example and then we are

going to check our package name which is com.example.imagepicker1 so we are

going to pass imagepicker1 here and after that add this file provider so

this is a unique string which we need to pass in the authority and then the third

thing is the file object for which we want to get the Uri so this method will

gonna return that Uri and we are going to assign that Uri to our image Uri

variable so now when inside the stake picture dot launch method we are going

to pass this Uri it is actually pointing to this file object which we created and

now when the camera application will gonna capture the image it will gonna

store that captured image on a location which is specified by this image Uri so

now here at this point if we will try to run our application and then long

press we will get some error and there is a specific reason for it and we are

going to cover it inside our next lecture but for now let's simply run our

application and test the behavior so there you can see when I try to install

our application it is not launching and the reason for this thing is inside our

application we are registering for this activity result where the type of

activities take picture but inside our application we have to add some code

inside our Android manifest so that we can get the data from camera application

inside our application and we are going to do that inside our next lecture but

for now we have completed the code for capturing images using camera so now we

have to do some configurations and then we are going to test our application