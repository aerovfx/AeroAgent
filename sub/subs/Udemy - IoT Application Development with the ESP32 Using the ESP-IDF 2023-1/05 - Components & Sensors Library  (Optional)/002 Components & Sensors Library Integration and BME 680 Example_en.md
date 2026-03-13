# 002 Components & Sensors Library Integration and BME 680 Example en

---

So here I have a blank specified project and we'll start off by cloning the ESP off sensor and Components

Library into the project folder right here.

So let's go to the project folder.

And right click.

Then go to get Bashir.

Now let's grab the Clone Command.

So just copy this line.

And then paste it into get bash.

And just let it finish.

And now we can close it and let's check out the project folder.

And there's a component we've cloned.

All right, so let's go back and check the ID.

Then let's right click on the project folder and go down to refresh.

And other components is visible here as well.

All right.

So now we need to include this component into the project build by adjusting the top level.

See Make List file, which is this one right here.

So let's open it.

And you need to add this line to the file and you could put it just underneath the first include statement

here as I have.

So I'll just give you a moment to type it.

And then we're including the additional component as shown in the how to use section that we saw in

the previous lesson.

And what we're doing is quite similar to the instructions.

We're just including this part here in the quotations, which is our path to the make list file to include

the components folder.

And once you've done that, you've successfully integrated the library into the project.

But to see how to work with the examples included in this library, let's continue by going to the resource

files I provided for this lesson and we're going to drop those files into the main folder here.

So within the resource files, what I've given you is the BMS 680 sensor dot C file, which is based

on the main dot C provided from the library.

And the BM 680 header filed just contains a function prototype so that we can run the example from our

main dot C and the C make list file includes our source files into the build and will replace our existing

file here with it.

And the k config project build file contains configuration defines and was also taken from the example

in this file.

We'll also replace our existing file here.

And we'll also have an updated main.

And this is the task common header file, which we'll update throughout the course to include all free

auto's tasks, definition information like the stack size priority and the core idea of the ESP 32 that

the task should run on.

So just know that we'll make use of this file as we progress in the course, not just the current lesson.

All right, so now let's select all of these files and we can drag them over to the main folder.

And then choose copy files OC.

And then select overwrite all.

And now let's check out the main quake list file here.

And there we have two source files listed that we need to build into the project main dot C and the

beam CCD sensor dot C.

And first, let's take a look at our main C file.

In our main Dead Sea.

We have an include for the BM 60 sensor header file and including that gives us access to the beam 680

task start function, which starts the example task.

So let's check out this header file.

And there we have the function prototype which replaces what was in App Main from the example.

So let's go ahead and take a look.

So we have this function definition here for the BM 680 test start, which is what we are calling from

main see.

And here the beam 680 test task is created using the x task create Penta Core API which takes our definitions

provided by the task common header file.

And those definitions are for the beam 680 task stack size the task priority.

And the core ID that the task should run on.

So let's take a look at those.

And there we have the stack size priority and core ID given by the example.

So I've kept all these values the same as what was provided by the example.

So let's go back.

And now let's check out the BMV 63 autos task, which is the function specified here.

So again, this is from the example provided by the library, and I won't go into too much detail here

because this isn't our code.

But you can see that they've done some initialization for eye to see communication.

And then they've initialized the sensor and then they've set the sampling rates for temperature, humidity

and pressure and then set the air filter size for temperature and pressure.

Then they've changed the heater profile and set the ambient temperature.

Then they get the measurement duration.

And in the wild one loop, the measurement cycle is triggered with the reference to the sensor settings

that were previously applied.

So that gives you a general idea of how this works.

The sensor is triggered based on those settings and that we have a delay until the measurement results

are available and then we get the results from this values instance.

Of the BM 60 values.

TYPEDEF So here we access values for the temperature, humidity, pressure and gas resistance and those

are all accessible via the typedef here.

And the floating point sensor values are all here in the BMB 680 head of file from the library that

we've integrated.

So let's go back.

And I'll just show you the other slight modifications I've made to this file, and that's at the top

of the file.

And there we have an included far ahead of file for our function prototype.

And then we also have the task common to access our free auto definitions.

And then we have these config example I to see definitions and this one is for the sensor address.

And then we have another here for the serial data line.

And this one is for the serial clock.

And these come from the K config project build file.

So we'll go ahead and open that because this file enables us to set various options from the sdhc config.

So let's see how this works.

Now I'll open this with the C C++ editor.

And this config file provides us with this example configuration menu option.

And when we build the project using this config file, the SDK config will then contain the menu configuration

items that we see here.

And this menu contains a choice for the example I to see address and the options for that.

And there's also the example I to see master serial clock and serial data as well.

So let's build the project and then we can view the config by going to project.

Then go to build all.

And this may take a moment.

So I'll go ahead and speed up the video now.

And once it's done, let's open the SDK config.

So just double click on that.

And the example configuration is right here.

Where we have the BM 60 I to see address options.

And we had the GPIO numbers for the serial clock and the serial data as well.

So that's how the SDHC config and the CÉ config project build file work together.

And I've already made the connections to the BMS 680 sensor based on the settings here.

So now I'll go ahead and flash to my dev kit by going to launch and run mode.

And again, I'll speed up the video.

Now that that's done, we can open a monitor and view those printf statements from the while loop.

Here we can open a terminal.

And there we have the values printed at the duration, determined by the wild loop.

Okay.

So that's all for this one.

And now that you know how to integrate the ESP lib, you now have an abundance of sensors and other

components at your disposal.

And I really hope you found this useful.

And I'll see you in the next lesson.