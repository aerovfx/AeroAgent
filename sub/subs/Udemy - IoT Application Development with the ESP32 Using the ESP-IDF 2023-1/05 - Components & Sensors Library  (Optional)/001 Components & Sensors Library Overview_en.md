# 001 Components & Sensors Library Overview en

---

Hello and welcome to the SPF Components Library section.

And in this section I'll introduce the ESP IDF Components Library, which is a library with an abundance

of sensor drivers and drivers for other components that may come in handy in your future projects or

within this course, if you like.

And all of these components and sensor drivers will be at your disposal once we integrate this library

and I'll show you how to get started with it.

So our plan for the lesson includes an introduction to the library and I'll show you how to integrate

it.

And in the next lesson we'll actually do the integration and run an example.

But I should be clear that using this library is completely optional and not necessary to complete the

course.

So you can always come back to this lesson whenever you'd like, if you want to use it.

All right.

So we'll start with the brief introduction of the library to show you where to find the documentation

and examples.

And then we'll take a look at our project structure and where this library fits into it, which will

then lead us into reviewing the steps that will take for the integration, and that will segue us into

the demonstration for the next lesson.

So the components library contains an abundance of drivers for sensors and more.

In the first link here.

Takes you to the SB Lib Components GitHub page.

Here you'll find information to help you get started.

Links to documentation and frequently asked questions.

As well as descriptions for all of the components included in the list is quite extensive and the library

seems to be actively maintained with contributions made by the list of developers here.

All right.

And if we go back to the documentation.

And then follow the link.

And again, first we have how to use it.

Then they provided links for all of the available components.

For example, if we're looking for the BM 680, which is for temperature, humidity as well as pressure.

They provided in-depth information about the sensor as well as documentation about the implementation.

And much like the documentation provided for the SBA itself, they've provided example, usage scenarios

and details about the results.

Measurement settings and other useful information about the beam.

680.

As well as full source code documentation and this is really nicely done and is a great resource.

So now let's go back to the repository and I'll show you where to find the examples from the GitHub

page.

Go to the examples folder, then here you'll find examples for all components which you can use to get

started with.

Now let's take a look at the BMS 680 sensor example.

And there we have everything we need to know.

We see what it does, how to connect the eye, to see serial clock and serial data lines, and then

example code in the main folder.

In not see.

We can simply take this file.

And what I would do is just create a function based on App Main here and integrate it into the application.

All right.

So let's go back up to the main folder.

And what I'm going to do is I'm going to show you how these macros are defined and brought into the

application.

Okay.

So let's go to this k config project build file.

And they've provided this file for us which we can utilize in our project, and it enables access to

define these settings directly from the SDK config menu from the expressive ID and I'll show you how

that works in the next lesson when we integrate the library.

And so that we can visualize where this component fits into our project.

Here's our course project structure without the sensor library component.

And the library will take its place as part of our extra components.

And there are some steps that we'll need to take to achieve this.

And we'll integrate the library by cloning the repository.

And we have the Git Clone Command for that right here.

And we'll also adjust the top level see list, text file, which is the see make list file in the project

folder.

And we'll add this line to include the ESP ADF sensor library component.

Then we'll integrate an example and you can either use mine or choose one from the library itself and

we'll need to adjust the make list file within the main folder to include the example files.

Also, we'll add the K config project build file from the example into the main folder and I'll show

you how that works with the sdhc config.

And lastly, I'll walk you through a few adjustments that will need to make for the application files.

We'll adjust Main C and we'll add this tasks common header file as well, which will eventually add

to your course source files anyway.

So again, any lessons added to this section are completely optional and you can consider these as bonus

lessons as this section will not include step by step programming, since we're simply integrating the

library along with example code.

And the idea here is that you can either use my code directly based on these examples, or you can watch

the lesson to learn by example for inspiration for your own projects.

If you plan on using the library or you can skip these lessons entirely.

So I'll start with the BM 680, which will communicate with override to see.

And I also plan on adding one or two more examples to this section in the case that anyone finds it

useful.

All right.

So let's continue to the next lesson if you'd like to integrate the library.

Otherwise, I'll see you in the section after.