# 001 Detailed Course Introduction en

---

Okay.

So let's continue with details of the course content.

The application we're creating will include the following features an extendable wireless local area

network application that supports device connection to the SB 32 access point in order to access in

FTP server.

And the FTP server will support over the firmware updates via a web page.

And connecting and disconnecting the ESP 32 with an external access point will display data on the web

page such as temperature and humidity sensor data local time using P as well as the ESB 30 two's own

SSD.

The over the year firmware update or OTA update mechanism allows the ISP 32 to update itself wirelessly

based on data received while the normal firmware is running.

In our case, we'll do this over Wi-Fi via a web page, and the Dash 22 sensor will be used for getting

the temperature and humidity data and will use non-volatile storage for saving and loading Wi-Fi credentials.

And we'll have an RG bleed and create different colors to indicate the application status.

S&P will be used for getting local time and additionally we'll have a button with interrupt and Semaphore

uses another method for disconnecting Wi-Fi and clearing credentials.

And once we have the wireless local area network up and running, well then configure the project so

that we can connect to a WSU T and go through the basic processes in a WC Iot core so that we can subscribe

and publish data to and from the WC dashboard and we'll view the published data from the ESP 32 using

the MQ T test client and the general steps that will take to accomplish this will include integrating

the ESP RWC LTE framework, which will include updating the project to include the framework into the

project build, which enables us to connect to a society will then go through a few processes in a WC

society core to get things going, like creating a thing and creating a policy which will need to be

attached to the thing and then generating the device, certificate, routes and keys.

And on the east side will embed the device certificate root, CAA and private key so that the ECP 32

can be authenticated with a W society.

And then we'll also update the source code so that we can publish data from the ESP 32 such as the temperature,

humidity and Wi-Fi received signal strength indicator or RSA say of the ISPs Wi-Fi connection so that

we can view this data from a WC Iot core using the empty test client.

And about the ESPN pdf, the ESPN pdf is express its official IOT Development Framework.

It's open source and freely available on GitHub.

It supports Windows, Mac and Linux and allows for development in C and C++.

It's production ready and has a well-defined release process and support policy, and each release undergoes

a rigorous Q&A process.

The ADF is feature rich and includes an Archos peripheral drivers networking stack and various protocol

implementations.

Additionally, the idea is version of the free Archos kernel is modified from multicore support and

will utilize both course of the ESP 32 in this course.

So let's talk about what you'll learn by taking this course.

You will learn how to create an extensible modular application using the SBA, PDF and free Archos will

program this application step by step, and I'll provide brief explanations of the SPF APIs that we'll

use.

And I must be clear that the focus of this course is not on theory or about the ESP 32 itself, as this

is a hands on programming project based course.

Additionally will utilize free artists and we'll have several free ARTAS tasks running within the application

and we'll employ message cues for test communication between and within the FTP server and wi fi application.

And we'll also have event groups in our state machine for the wi fi application and we'll also implement

a binary semaphore for our button task.

Now let's take a look at the programming languages used in this course.

The C programming language is predominantly used in this course, but we'll also write HTML JavaScript

and access to implement the web page.

I should also mention that while using the C language throughout the course, I am not going to slow

down and explain all of the aspects of the C language that we use.

The reason for this approach is to maintain focus on implementing the application itself, which allows

for a smoother, more efficient progression through the application code.

That being said, experience with C is helpful and or willingness to stop and research topics that you

do not understand.

So why take this course?

If you're working with the SB 32, then using the ESP IDF directly is the way to go for more serious

embedded software development.

Arduino for the ESP 32 is just a wrap around the IDF.

It works well for those that just want to get something running.

However, if you want to have a better understanding of what goes on under the hood of the ESP and if

you want to become a better programmer, then moving away from the Arduino is worth considering.

Also, the ESPN RDF is used in professional, commercial and industrial projects.

Additionally, project setup is easier than ever using the eclipse idea plug in.

Also I've selected commonly used components of the ESP ADF, which are often the basis of many Iot and

industrial Iot applications, which involve a wireless local area network which often includes connecting

to the internet, an HDB server, a web page for connecting and disconnecting the ISP and for OTA updates.

Additionally, not spending time on lectures about the ESP 32 and other highly general topics may be

beneficial to some.

There is plenty of information available directly from impressive about the ESP 32.

However, even though the focus is on physically programming this application, I'll try to fill the

gaps by briefly covering the ESP ADF components used.

I'll try to balance the South while maintaining focus on the application code because ultimately my

goal is to provide you with something that you can actually use, learn from and enjoy.

And yes, I do provide slides and code for all code changes implemented in each section of the course.

So you can always refer back to the links in the slides later as we're writing the code.

And you can always check your code by comparing yours with the resource files.

Okay.

So next, we'll take a look at the hardware and software requirements.