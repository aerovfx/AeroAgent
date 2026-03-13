# 4 -File Provider  Share Data Between Android Apps Securely

---

are getting some errors inside our application and the reason is we want to use file provider

inside our application and for that purpose we need to do some configurations.

But why we need to do these configurations for our application?

So to understand that let's understand the background working of our application.

So whenever we install an application inside an android device there is a space allocated

to that application and that space is called the private space of that application.

So in that private space the data of that application will be stored and no other application

can access the data stored in that application.

Like if we have installed our application on a device then a private space will be allocated

to our application.

And now as per our functionality we want to capture an image using camera application

and then we want to get that captured image inside our application.

So basically to achieve that what we are doing is creating a file in the private space of

our application and then we are passing URI of that file to our camera application and

camera application is writing the image on that particular URI.

So basically we are giving access to camera application inside our private space.

And to do this thing we need file provider or content provider.

As content provider is used to transfer data between two applications so in our case we

want to get captured image inside our application so we are using subclass of content provider

called file provider.

And now to tell camera application about that access that we are giving him access to store

captured image at that particular location we need to do some configurations inside our

android manifest file.

So now let's do that.

So we need to firstly open our android manifest file so here you can expand this folder and

open this android manifest file.

And then here before the closing of application tag add a provider tag.

And when we add a provider tag then we need to specify the name and the authority for

that provider.

Like here we are firstly going to add the name for this provider so here simply add

the name property first.

And then in the name of this provider we are going to pass our file provider class so here

when you will type file you can see the path of this class so simply add it.

And after that the second thing which we need to specify inside this provider is the authorities.

So simply add this android authority tag and here this authority will be a unique string.

And we have specified a similar authority while getting the URI.

So there you can see inside this get URI for file we specified this authority.

And now we need to specify the same authority inside our android manifest.

So here we are going to add our package name which is com.example.imagepicker1 and then

we are going to add this file provider.

So basically this authority is specifying the location inside our application private

space where camera application will gonna write the data.

And to specify that location we are passing the package name of our application and then

specifying this file provider.

And after that the third thing which we need to pass is a parameter called exported.

And we are going to pass the value false here.

And we are passing this parameter to let other applications know that this particular component

which we are adding inside our application is only for the camera application.

And we don't want other applications to access that component or access that location and

write anything there.

So only the application to which we are going to give permission can write on that particular

location which we specified using authority.

And after that the fourth parameter which we are going to pass is grantUriPermissions.

So as we pass URI to camera application using which camera application will gonna write

the data so we need to specify this grantUriPermissions to true.

And now we can close this provider tag.

And now inside this provider tag we need to add a metadata tag and then inside this metadata

tag we are going to specify the folder inside our private space where camera application

will gonna write the data.

So using this authority we are specifying the location inside our private space.

But now at that particular location we need to specify the folder name where camera application

will gonna write the data.

And to do that we are going to add this metadata tag.

So press enter and it will be added.

So here we are firstly specifying the name here which is fileProviderPath.

And then we are passing this resource parameter and here we are passing a file which is present

inside XML folder.

So basically in the XML folder of our application we need to create a file with the name paths.xml.

And then inside this paths file we need to specify the folder name.

And to create this path file you can simply click here create XML resource file.

And then you can specify the name paths here.

Now press ok.

And this file will be created.

And to check this file you can expand this res folder and now you can see there is an

XML folder.

And inside this XML folder there is this paths.xml.

And now inside this file we need to specify the folder name where we want camera application

to write that data.

So here to specify that folder name we are going to add a filePath tag.

So here add this filesPath.

And then we need to specify the name for the folder here and then the path for the folder.

So you can specify any name here like we are going to specify the folder name to camera

photos.

And after that you need to specify the path here.

So we are going to create this folder at the root directory.

So we are simply going to pass dot here.

And after doing that we are going to close this tag.

And that's it.

So after making this change you can simply install the application and our application

will gonna work correctly.

So it means that we will be able to capture images inside our application and display

them on screen to the user.

So now let's quickly install the application and test it.

And after that we are going to review the code that we have written.

So let's install our application.

So now the application is installed again.

So let's long press on this button.

And after that you can see something is launching and that is the device camera.

So this is the camera preview for Android emulator.

And if you are running this application on your real device then the real camera of your

device will be opened.

And here let's capture an image.

And then press this tick button.

And after that you can see the captured image is being displayed inside our application.

So it means that our application is working correctly.