# 15 -Self-Host n8n Make Your MCP Server Accessible from Anywhere – Even for Others translated

---

If you want to host your application so that you can have access from everywhere,

not just from your computer or if you want to host this application for other people,

so that other people can call your MCP server.

With for example a cloud desktop config file or with other AI agents that they are building

inside of an ADN or in cursor, win, serve, whatever.

Of course you have a lot of different options.

You can either work with the cloud version of ADN itself and you see right now here I am

on the cloud version of an ADN. You also have the possibility to use hosting her and hosting her

is at least how I see it, one of the things that I really love. Besides that we have also the

possibility to use render, render results on option that is relatively good. Personally I have to tell

you I do like the hosting our version a bit more because we get more access and it's also a bit

cheaper but nonetheless I want to show you everything. If you come for example on an ADN.io,

you can come on this documentation and you can come on self-host and ADN. Before we come on

self-host and ADN I want to show you the pricing from ADN itself. Of course you can start completely

for free for two weeks. If you just use a startup plan but after the startup plan is finished so

after two weeks they will contact you and you need to give your credit card information.

So if you want to start for free just for a tiny bit without local installation and you need to work

in the cloud so that you can see if this is working for you you can absolutely work with the startup

plan for free. But then they will build you 20 euros a month. If you are building annually,

if you are building monthly it actually gets a bit more expensive if it are 24 bucks a month

and you just have four active workflows. But this is the least hassle it goes like really really

fast and like I told you if we come on self-host and ADN you will find a lot of different options

that you can use. Of course if you understand Docker you can do it with Docker and you can also

host these on your own servers and do a lot more. We also can use ADN we already did this so this

is just for the local stuff. Here the detailed explanation of Docker and then you also have server

setups and here they show you digital ocean, Heroku, the Hetzner Cloud AWS Azure or Azure, the Google

Cloud Platform and also once again Docker Compose. So you see you have a lot of different options.

Hetzner Cloud is besides hosting are also one of the tools that I really like. But then this video

I want to show you how we can do this click-by-click inside of Render because I also think Render

is somehow great and I also want to include hosting her so that you can decide for yourself what's

the right plan for you. I personally have to tell you that I use also this cloud version because I

got basically a yearly plan. So I am in this cloud plan. This is fine especially for tutorials

it's great because we do not need to make any updates and so on. But mainly I do work with my

hosting or plan. So my favorite is hosting her but nonetheless also want to show you click-by-click

help to do it on Render so that you can decide it yourself and all these other options they are

click-by-click explained also on the documentation of an ADN. I just want to show you everything so that

you can decide for yourself and I also need to tell you that I do have a special code for hosting

her. No I'm not defeated from them. I just got a code to create a YouTube video I already done this

but nonetheless I just want to include this code. Maybe you can save something if you really want to

if you are deciding to for hosting her but I am completely unbiased. I do not have any advantage

in saying this. I just want to tell you what I am using. I like the normal plan from ADN because

we can also start for free so you can basically just click on it, follow the course along do it for

two weeks for free and then simply decide for yourself if you want to host it but I also want to

show you how you can do self hosting and you can absolutely do self hosting completely for free

but the only downside is if you do self hosting for free your instance will spin down as soon as

the server disconnects and this can happen from time to time so your workflows will not be saved.

This is of course a gigantic downside. If you want to self-host it forever you can also do it.

Here you need to pay I think like seven bucks a month but don't worry like you can start with

all of this for free and then you need to decide for yourself if you want to host this applications

forever you need to pay a little bit but of course you can sell this applications and you can

have them online for you forever and you can access them with your phone over the telegram over

WhatsApp over whatever so I think it's absolutely worth to try this out because like trying is

completely for free you can host them just like at all you in an add-in for free for two weeks

and also in render.com forever for free but in render they will spin down your workflows after

the server restarts so the first thing that I like to do is to simply google an add-in you can press

on this first link and here you see that you can simply press get started for free and if you press

on this you can simply log yourself in with your email address with a password and so on and then you

can test this thing out completely for free without the credit card for two weeks and after two

weeks they will ask you if you want to pay if you want to do one upgrade but I like to do the most

or at least I find it really really practical that way is to use render because on render.com we

can self host either completely for free with spinning down our instances from time to time or we can

simply pay seven bucks a month and I think like seven bucks is really really fair for a self-hosted

instance one of the downsides of render is that you do not get a lot of disk space so you see for

example that a few an add-in installations have failed in deploying and this only happens because render

does not offer a great bandwidth hosting around the other side offers a broader bandwidth so I

would really recommend you to stick to the end of this video so that you can see everything how you

can host it and also how you can use hosting are if you want to be serious about this if you want

to create a lot of automations and if you want to host them for a long time I do think that hosting

are is the best option but still I want to show you render because on render you can start at least

for free even if your instances can spin down and even if your deployment can fail from time to time

because the bandwidth is not that broad before we do this I need to make something clear once again

if you simply come on to this website and press get started for free you can follow along with this

course completely for free because you get access two weeks completely for free if you come over to

render.com you can simply make yourself an account here this will be relatively vast to simply

connect yourself with Google you click get started for free and then you come to your dashboard

here you see that I have already a lot of instances most likely this thing will be completely

empty for you so you can simply create something you can scroll up and press add new in the right

corner so press on these and we want to have a web service and here you need to connect the

RugeTap profile if you do not have a GitHub profile we need to make a GitHub profile right now you simply

Google GitHub you press on the webpage and then you press either sign in or sign up of course it

depends if you have a profile or not you can simply make yourself an account with an email address

I just press sign in because I already have an account as soon as you are here in GitHub you need to

search for an add-in so you go here on search and then you search for add-in and normally the first

instance should be the right one yes it's this right here that has a lot of stars now you are in

this GitHub project with your GitHub profile this is important what you want to do right now is to press

or press on these right here and then create new fork you see I already have a fork but if you

do not have one you press on create a new fork here you just need to click okay like I said I

already have a fork so I can simply press on my fork then it will look something like this so

basically everything that you have is an add-in in your GitHub profile this is important and by the

way while we are here right now I want to show you how we can make updates to this GitHub profile

you can simply press on synchronize forage and update branch so you know it an add-in will make

updates all the time and you simply can press on synchronize forage and update branch and then

this thing will be completely up to date all the long this is really fast this is really easy

you can do this from time to time as soon as you have this forked in your GitHub profile and as

soon as you are up to date you can come back to render and here on render you need to go to get

provider most likely you have not connected your GitHub profile and that's why you would need to press

here and connect your GitHub profile as soon as you are connected you will see some instances that

you can connect in my example this is right now of course my add-in instance and now we simply press

connect and and then here you see the source code and it was of course updated two minutes ago so

this is perfect you can give it a name if you want and it n3 is perfect for me then the project is

optional so I don't do it the language is not the branch is master you can leave it here or also

use Frankfurt like this doesn't really matter the root directory is just optional and because we use

the language node we have of course automatically the build commands the build commands are of course

pnpm install and pnpm run start so this is basically working right now and then you see this right

here the instance type you can either use a free plan or you can use the starter plan like I told

you if you use the free plan if you press on it you already see it upgrade to enable more features

free instances spin down after periods of inactivity they do not support ssh access scaling one of

chops or persistent disks select any paid instance type to enable this features so basically you can

use this you can self-host for free but all of your workflows will get deleted over time this can

help me soon as a server spins down or this can also help me just randomly like this is not the

most secure stuff generally speaking what you can do right now is to simply use the free plan and

you can also upgrade your plan later if you want and just to follow this tutorial you can also press

here get started for free so you already know it so chose for yourself what you want to do this is

the easiest way the fastest way two weeks for free this thing is forever for free but will spin down

and if you want to sell this applications just think about if you want to have this plan for 20

euros a month or 20 dollars a month roughly or if you want to have this starter plan for seven bucks

a month generally speaking this is cheaper but here you need to do a few more clicks if you just

want to follow for free here you can simply press on this then you scroll down and everything that

you have to do is to simply press deploy web service because this is so easy I just want to show

you how you will do it in the starter plan because in the starter plan you have a lot of things that

you can include and that you also should include you basically can scroll down and here you have

then also the advanced stuff with discs and so on and right now I want to show you how we can do

this so if you want to pay for this now just use this and you also need to give the credit card

of course then we can scroll down and we want to go on to advanced and on the advanced we want to press

add the disc so that we can have a persistent disc this is really really important this

size can be just one gigabyte this is more than big enough and here we need to give the mount path

and if you press on it like for me it's nearly instant or automatically because I have already made

a few of them you see we can use something like this so it's basically slash OPT slash render slash dot

but not flow wise in this example it's of course an 8n then the size as one gigabyte like I told you

and then the rest down here is completely fine but what's not fine is the right here the variables

we need to have some variables so environment variables we need to type this in we can simply press on

these and you see right here that we need to type in everything big so let's just take big letters

what we want to type in is an 8n underscore editor underscore URL the fastest way to get this

value would probably be if you would scroll down and press deploy web service then you get

in your projects this thing's running and you can copy simply this thing right here you can come

back and copy this value here in this would be basically the fastest thing then we need to add a

new environment variable so please just make one for free first and then you go on with this

once again after it we need of course an 8n underscore host and that's basically once again the same

URL but this time without the HTTP so basically something like this then we want to have the

an 8n port excuse me of course with an underscore and it's 4 4 3 then add new an 8n underscore

protocol and that's of course HTTPS and now the last one I promise at new an 8n underscore user

underscore folder and that's basically the same value as we have here on the mount path on our

disk so we can copy this and for within here as value and everything that you have to do right now

is to simply scroll down and press deploy web service but first of all you need to remember do you

want to have it for free or do you want to have the starter package if you insert your credit card

you'll starter include this things down here and then you press deploy web service then you need

to pay I just want to press deploy web service I have used the free one for this tutorial it's

just for the sake of this tutorial because I have already some paid ones so here you see your free

instance will spin down within activity and so on but if you use it with the paid plan this will

look completely similar and right now this thing will take a little bit until we can start it

and as soon as this is deployed you can simply go on to this web page on to this URL and then you

can launch your instance and remember every time that you want to do updates just come to your

guitar profile and press here synchronize fork and then you are basically ready to rock with your

updates so let's just wait until this thing is completely done after a while you will find this

right here build successful deploying and so on and then you need to wait just for a little bit

and then as soon as everything is done you will find your project also here and you can press on

your projects and from here on you can either upgrade your instance later but if you just want to

test you simply press on this link right here and then you are basically in an event and your

instance will be completely empty if your deployment fails or if you want to get serious and want to

deploy a lot of projects to the cloud like I told you the thing that I use at least right now

is hosting her and I do think that I will stick with this plan because I really think this is

a great plan everything that you have to do is to come to hosting her.com slash vbs slash

anything hosting and they have everything pre-installed for you so this is actually also a lot

easier than render so you can press chose your plan and on the plan I love the kvm2 plan and on the

kvm2 plan we get two CPU cores 8 gigabyte of RAM and 100 gigabyte of NVM disk space this is actually

a lot more than in render you already know it and the pricing is really compelling it's actually

a lot cheaper than on render if we want to use this thing on render we need to pay more so if you

want to do it serious I would strongly recommend this plan right here and then we can press on chose

on plan and then the only downside is that you only get this pricing if you use it for 24 months

if you use it for just one month actually it gets a little bit more expensive but still just

$9 a month at least right now and in comparison with render we have for the 7 bucks a month only

0.1 CPU and 500 megabyte so it's actually a lot less so the thing like a dolly that I love to do is

to use this 24 month plan right here and if you use a coupon here you can actually use Arnie

like a dolly I am sponsored but I just want to be transparent what I am doing and if you use also

you get actually once again 10% off so I do think this is the cheapest way it's under six bucks a

month and you can scale it infinitely you have a lot of space for your instance so I do think this

is the best option if you want to do this for a long time if you want to make projects for clients

but keep in mind you need to pay this upfront but then you are set for two whole years just think

for yourself what you want to do as soon as you press here okay you will be in a dashboard that

looks something like this and here we can go on we have to set up our KVM 2 so we go on we go on here

then we need to use the region that is the nearest to your clients for me it's Germany and we have

also a really small latency here we go on this thing is free so we got a one then we need to give

a password we go on and then we are basically done of course if you do not like an add-on or want

to hold something else you can simply change this by pressing here but for me or for us is an

add-on of course fine so we go on and then we are basically done if you press on vps you can give

some additional info what you want to do and you go on then we have this thing right here running

and you can access your replication by actually just copying this link you coming on your browser

you type in an add-on dot then you type in this stuff that you have copied and you send it out

of course here you need to give your email and so on and you go on you can give additional

info but you don't have to the wise keep it here you actually get a license key and if you get this

you can simply send this key for yourself and activate it because you get some additional tools

that are not available every time as soon as you have your key you can come down in the left

corner press on settings until you can verify your key so simply type it in and activate it and

then of course you are once again in an add-on you can come to your overview can start from scratch

and then you are in the interface that you already know you already know that an add-on makes updates

all the time right now we are on this version and I want to show you how you can make updates

over hosting her you can actually come back to hosting her so on the start side you can press on

this button right here then you come to your browser terminal and this thing will open up don't

be scared it's really easy you just have to type in three lines and you can actually find

these lines in the documentation from hosting her you can pull the latest version by Docker compose

pull so you can simply type in Docker compose pull and you send it out as soon as this is done

we do Docker compose down to spin down our old instance so Docker compose down and we send it out

and as soon as this thing is done we come back once again to see in the documentation

that we start the container by Docker compose up dash D so we type in Docker compose up dash D

and we send it out and right now everything is once again completely up to date and it will work

as soon as you open up your application good job you have done everything right and then we can

start building in a cloud version so in this video you have learned a lot of options how you can

host your anad and services you want to host them first of all for accessing anad and from everywhere

you can access it from other computers you can access it from your phone you can also use the

telegram trigger notes and do a lot more the fastest and easiest way is to start with the free

plan of anad and just press start and you can test this for free this is perfect for the tutorials

in this course if you want to do self hosting what I like to do is to use render if you just want to

test use the free plan but your instances will spin down most likely every day if you want to

self host it forever you need to pay either the seven bucks to render or you can pay roughly 20

bucks to anad and then anad and makes it a lot easier and if you want to be really serious if you

want to host a lot of applications for clients and do this for a longer time I would actually

recommend you to doing the same thing as me and use this plan from hosting her because you get

the most out of your money you can build a lot and you get a lot so basically you have unlimited

options so please choose your weapon wisely have fun with the self hosting and use anad and plan

if you just want to follow with this tutorial.