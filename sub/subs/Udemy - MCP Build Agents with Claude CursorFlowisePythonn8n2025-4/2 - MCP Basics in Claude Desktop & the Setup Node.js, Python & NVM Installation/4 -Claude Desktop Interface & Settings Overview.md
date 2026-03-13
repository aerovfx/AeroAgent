# 4 -Claude Desktop Interface & Settings Overview translated

---

Cloud desktop is installed and this video wants to give you a brief overview of the interface

also of the developer mode because we need to include some things in order to work with MCBs.

This will be a general walkthrough if you are already familiar with Cloud desktop. You can also skip this,

but I think you will find some things here even if you know Cloud already.

Now Cloud is installed. The first thing that you should do is of course to press on Cloud and then

this thing will get opened up. Later we need to do a few restarts in this application. Every time

as soon as we connect an MCB. Right now I do think I have an MCB connected to the SIDS blender.

I will show you this step by step how it works, but first I want to show you how you can restart

Cloud. Because if you close it down completely it is still open on this sidebar down here. If you press

on these something like this thing will pop up so you can still dock with Cloud, so this thing is not

completely closed. If you want to restart you need to restart always down here you need to press

quit. This is the most important tip as soon as you insert a new MCB server you always need to

do a restart. Now let's just open Cloud back up once again and take a closer look at the interface.

If you are already familiar with chatch ebd like this is really really similar. You can simply

type in your prompt right here in this prompt bar. You can press plus in order to observe stuff so

you can upload the file. You can add from GitHub you can add from Google Drive. Here you see the

stuff from blender this is an MCB. I will show you how you can include this and you can use a project

if you want. If you do have some projects I will show you how you can set this project up. If

you are in the free tier it is possible that you do not have these projects but this is also

no problem. You do not have to have a subscription in order to work with MCBs in Cloud Desktop.

Then the next button is this right here. Here you can use different styles for example the normal

style or formal and you can also press create and edit styles if you want to be far. Cast them

style and so on. These are just some simple basic settings. You can include the web search you can

connect with Google Drive with Gmail or with the calendar for example. I do also think these are

just paid features but we can connect with these features also via an MCB so you do not have to

pay for Cloud like I told you. Then you can of course write, learn, generate code or talk about

life stuff with Cloud. These are just some tips from UnTropic and you can connect apps. So these

are the apps that you can connect. It is totally possible that you also can connect for free. I do

think that you can connect for example to GitHub for free. Then here you chose your model. Right now we

have Cloud Opus 4 and Cloud Sonnet 4. These are the strongest models at least at the time as I am

recording this course. You can also use some older models and it's also possibly they do have

just a limited amount of usage if you are in this free tier. Then the next things are all on the left

side. In the left corner down here is your name and you can press on it. Here is personal. So you see

I am on the pro plan and if you press on settings for example this thing will pop up. You have a profile

with an A-man so on. You can also type in if you are in finance or sales or something like this and

Cloud will adjust the tiny bit. You can set a system prompt with this person or preferences. I will

not dive into this right now. You already know it and the feature preview is for example

analyzes tool I like to include this. Then we have the appearance. So do you like the bright mode or

do you like the dark mode or system. I like this style. Let's just put it this way. You can also use

different text if you want. Then the account you can log out or contact support if you want. If you

come on to privacy you can read this privacy data for yourself and if you do not want that cloud

knows your location you can simply exclude it. Then if you come to billing you can simply manage your

account and on these integrations you can connect once again some apps. Nothing of this is really

necessary for MCP. If we come on the left side once again you can press here in order to create a new

chat and you start from scratch. The chats that you are created are saved right here. For example

this is a chat that I had where I talked with Cloud and Blender was connected and if you press new

chat you will always have a new chat. If you come on these chats this thing will open up and you see

I have right now 101 active chats here. The next thing is projects so you can press some projects.

Here you can search through these projects if you already have projects and you can also press

create new projects you can give it a name like MCP, give a description if you want and press

create project. In this project you can also set a system prompt. So set project instructions you

can press on these and you can give Cloud some context of course. Then you can also upload PDFs

and other documents like for example documentation or code examples or whatever you can simply upload

stuff in order to give Cloud context for these projects. These projects are really really cool

like if you want to develop something if you want to write a book you can make a project for example.

Now we come once again back on Cloud here and we come in the left upper corner. Here we do have file,

edit, view, developer and help and I want to start down here with help. You can open up this

documentation, check for updates, submit feedback and get some more information on about. The most

important thing that I want to tell you right now is if you never ever used Cloud Desktop until now

here will be a button that is called developer mode and you need to activate it. I need to stress

this out you need to activate the developer mode so that you can do the stuff that we will do

over the next videos so please just activate it. Then also this thing will open up the developer mode

and here we have the MCP log files and you can press on these and then the MCP log files will get

opened up. These things are later practical for debugging for example. So you need to activate

first the developer mode on help then you will get this right here and then Cloud will also write

some logs for you. Then you have view and here on view you simply get some shortcuts on edit. You

have basically the same thing here are some shortcuts for undo, redo, cut, copy, paste, select all

and find and then we have file. This is also cool because on file we need to do a lot later we have

new conversation we have settings we have close and we have exit and the settings we will need

the settings later. Here we have general this will be always active even if you do nothing

include the developer mode. You can run Cloud as soon as you start your system I like to include this

because I always want to open up Cloud. Here some more configurations and the important part for us

will be later this developer section because on this developer section we can edit this config

and on this config we have basically everything that we need then most important thing for us will

later be this Cloud desktop config file. You need to have this file if you do not have this include

the right here you need to make a file that is called exactly in this way. Cloud underscore desktop

underscore config dot chasen 99.9% of the time this file will be included automatically and we need to

come in this file later and in this file we will include this mcp servers. This mcp servers we can

include is via a really really simple chase format we always start with a curly bracket then we

type in the mcp servers most of the time it's called blender in this way then the command to the

command in this example is uvx on most of the other servers we will have npx npx works in node js

uvx is a python by catch manager just like pip maybe you know pip install and so on it's just a

python by catch manager then we have some arguments right here for this blender mcp and then we simply

close this brackets once again and we need to make sure that we have good syntax so we do not have

any errors but don't worry we will take a closer look in the next video how we can set this up in

the correct way in this video for me it's just important that you need to understand that you should

press in the left upper corner on help and you need to activate the developer mode so that you can

come on the settings on file on this developer mode and on edit config you need to have this

clot desktop config file dot chasen and then you are ready to rock and before I forget it the last

buttons are down here here is your name and you can press on it here you have personal i am in

the pro plan personally like i told you you do not have to use a plan here you also have settings

and if you press on it you are on these settings once again you already know the settings then you

have their languages i use for this course english so united states normally i do use german because

my main language is german i live in italy i also speak italyen but for this course like i told

you i will use english then we have got help if you want to get some help then you can also press

on view all plans and if you press on it you see that you basically have a pro plan this thing

costs you 15 bucks a month and you also have the max plan the max plan gives you 5 to 20 x more

usage than the pro plan you are like heavily limited on the free plan a little bit less limited on

the pro plan and you will have most of the stuff on this max plan but it is also a bit expensive with

90 bucks a month and here you can always read for yourself what you get i would also assume that

this thing's changed over time you have also the team and enterprise plans and you can simply

contact the sales team if you want to have a specific plan so it always depends on what you want to

do i do think that cloud also offers a 200 bucks a month subscription but right now at this

second it's not included here maybe you have to contact cloud here or on tropic then you can also

press on learn more if you want to have some documentation don't worry you are covered and you

can log out that's basically it about this interface so basically this was just a brave walkthrough

to call out desktop you should know all this basics from this client because we will work with

this client in this course a lot like at all you like not specific prompt engineering and so on

just a basic overview so that you know what you can do see you of course in the next video as soon

as we connect our first time to be server-verse