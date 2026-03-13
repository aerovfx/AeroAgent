# 3 -Install Flowise locally with Node.js and Update It translated

---

In this video we will install Flowwise locally because we want to build agents visually.

With the Model Context protocol included, if you scroll down of course you can generally see how it works.

You can simply type in this in your Node.js command prompt. Before you do this,

of course you need to have Node.js installed. If you are here in this course,

I hope that you have already installed Node.js if not, I don't know what you are doing until now.

So the Node.js command prompt should be here and remember you have also installed NVM.

And if you type in NVM list, you need to make sure that the user version that works great with Flowwise.

The version 21.16.0 is a really reliable version that always works for me with Flowwise.

The newest version sometimes makes some problems. So make sure to use this version.

You can also try it with the newest version. But if you get some problems, of course you know how to fix it.

Just type in NVM install and then the version that you want like I told you 20.16.0 is great.

And then of course NVM use in order to use this version.

So make sure that you have a version that works. But before we install it, I want to show you once again

some things because like we have a lot of options in order to use Flowwise.

If you scroll down a tiny bit, of course you see that you can also include PDF, CSV, XML, HTML,

you have the option to loop over items and you have also the option to include human in the loop.

Basically you can do a lot of great things with Flowwise. You can also call the API endpoint if you

want. And Flowwise is completely 100% open source. Of course you can also deploy it to the cloud.

You can self-host it. They are production ready to scale. So if you host it, you are also able to

sell your applications and more. If you come down to pricing, you see that you can also use the plan

from Flowwise directly and you can also start completely for free. So if you just want to follow

some tutorials, you can also press get started right here. You can create two flows and assistance

completely for free. You get 100 predictions a month, 5 megabyte of storage, evaluations and

metrics, custom and better chatbot branding and the community support. So basically you can

simply start for free even if you don't want to install this thing locally. Then of course,

if you want to use a little bit more. You can use the 35$ a month plan. This is the host version

from Flowwise itself. The greatest thing at least how I see it is that you don't have to make your

updates yourself. You can simply click here and then you are ready to start and you have always

the newest version included. You get everything that you have from the free plan and limited flows

10,000 predictions a month, 1 megabyte of storage and of course also the community support.

The only thing that I don't like that much is the pricing here. It's a little bit expensive.

We can do self hosting and later we will also talk about the self hosting. And then of course you can

use a pro plan or then the price plan. Basically I do think that self hosting makes a bit more sense if

you want to have a lot of access here. Generally speaking, a great tool so let's just come to their

get-tap page because this is 100% open source if you press on get-tap. You can also scroll down

until the last thing and you see that they have a Apache license version 2.0. So 100% open source.

Basically, an add-in is also open source but it has a special license and Flowwise on the other

hand is 100% open source. And also a lot of people are using Flowwise and more and more people

come in because it's a great application. If we come up here you generally see how you can use

it and install it in NoChS of course we will do this click by click and later you can open it up

on this URL. If you are a Docker guy there's also the detailed Docker installation you can simply

start with a Docker image and use this command. If you are a developer of course you have also

here some options and you can simply follow these commands step by step. And the last thing that I

want to show you is that you are able to self host your instances. If you press on others then you

see that you have a lot of options. If you are already working with AWS Azure Digital Ocean,

Alibaba Cloud or whatever you can also host the tier. Later in this series I want to show you how

you can deploy this to render because I also think that the render is a great option but you can

simply see for yourself what's the right thing for you. So what we want to do right now in this video

is that we want to install this thing locally with NoChS remember use NVM to make sure that you

have the right node version installed it should be at least right now higher than this version 20.16.0

works great for me like at all you. And later in this video I also want to show you how we can make

updates inside the flow wise. So the first thing that you need is this NoChS command prompt.

So you press on this and this thing will get opened up. As soon as you do this the first time whatsoever

you need this line right here NPM install G flow wise. So you type in NPM install dash G flow wise

and then you will send this out and you can also delete this if you do not want to write any

single thing that in here you can simply copy this thing you go back right here you insert it

and you need to send this out and then the computer will do its thing. Flow wise will get installed

locally on your machine and this will take you it depends on your machine sometimes two minutes

on some machines it can take up to 10 minutes every single thing that you need to do is just to

insert this line and then send it out. Now I have already installed flow wise. So you send this out

and come on I do it again I send it out and then flow wise will get installed normally I already

have installed flow wise. So I want to show you life how all of this is working. So I will install

flow wise again right now. So right now something like this will happen and this takes a little bit of

time I see you as soon as this is installed and here you see it and even my flow wise instance took

a little bit of an update because flow wise is a really really nice tool that gets updates all

the time. So this branches they get updated all the time and now I will show you how we can start

flow wise it's the next line npx flow wise start you can type it in and if you do not like to type

you copy this thing right here and you send it out down here you simply send it out and then

flow wise will get started on a local server so flow wise server is listening at 3000 and you can

open this server up either by typing it in or you guessed it right by copying it you can also just

open up this link in a new tap and then you are in flow wise. So here you see these are my chat

flows so the chat flows that I have already built then we can go into the agent flows in the market

place and so on. So you see this right now is flow wise and I want to show you something this thing

is hosted locally on this server if I close down note if I close this thing down this will no

longer work if I go on agent flows for example right now I can't find anything because this is

now closed down so you need to open up note command prompt in order that this is working. So we

have already installed flow wise you just need to do this once so now you just need to restart it

so we just need to copy this line so the installation you only do the installation once then you can

just npx flow wise start and you send this out and your instance will work so you see the starting

of flow wise is really really fast flow wise server is listening at 3000 so this thing will work

if I reload it so I really reload it bam and there we are once again in my flow wise interface

this is how you install flow wise and how you start flow wise so the installation you only do

this once and you need to start it every single time as you use it and your command prompt needs to

be open as soon as you want to do something in flow wise if you host it in the cloud you do not need

to have this open but I want to show you that later so this is how you can run flow wise and now I

want to show you how you can update flow wise without installing the whole back catch again so you

see right now flow wise is working everything is fine if I close it down it will no longer work of

course and now I want to show you how you can update your local instance of flow wise of course

you open up the note chs command prompt and the update line is not here but now I want to show you

what you need to type in in order to update your flow wise instance you simply type in npm update

dash g flow wise npm update dash g flow wise you can send this out and your flow wise

instant will get updated if an update is needed you can do this from time to time if you think your

flow wise is not up to date and every time they will also tell you on get up if there are new branches

if there were new updates this is really really that easy so you can update your flow wise

instance with this nice little line I think this will take a few seconds and then I'm ready to

rock once again and no surprise flow wise was already updated so of course everything works fine

and then I can of course restart flow wise once again with this line so no need for further

installations and px flow wise start I send this out I will get my server back my server will be of

once again this local server 3000 if I go on this if I reload it of course I am once again

in my flow wise instance that's how you can install flow wise and how you start flow wise

so in this video you have saw how you can install start and of course update flow wise you just

need to have these three lines if you need to install flow wise open your command prompt and

insert this right here npm install dash chief low wise if you want to start flow wise npx flow

wise start as soon as flow wise is installed once you can just start it every time just with this

line so you only need to install it once if you want to update flow wise you type in npm update

dash chief low wise so the same thing as here but not install but update as soon as your instance

is up to date you can once again start it with npx flow wise start and then you get your server so this

is always this low closed you can open this for example in a new tap and then your flow wise

instances here and in the next video I will show you how we can work with flow wise because now

we have a local server and of course how you can host this in the cloud maybe for clients I will

show you these at the end of this flow wise sections because I want that you use this locally as

soon as you start to develop with these things because locally is always the most secure