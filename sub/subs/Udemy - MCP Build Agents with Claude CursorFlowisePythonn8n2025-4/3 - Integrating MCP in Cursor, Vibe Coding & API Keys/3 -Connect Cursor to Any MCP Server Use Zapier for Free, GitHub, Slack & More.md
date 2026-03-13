# 3 -Connect Cursor to Any MCP Server Use Zapier for Free, GitHub, Slack & More translated

---

In this video I want to show you how we can connect every single MCB server also in cursor.

And it's really easy.

And I want to show you the SAP RampsyB server.

Because in cursor we can connect this for free.

So you basically should not do this in Cloud Desktop.

Or you do it with the workaround that I will show you later.

The first thing is of course simply Google, SAP RampsyB servers.

And you can come on SAP RampsyB AI in action.

You press on this and you press get started.

You will be in this interface once again and you simply press new MCB server.

You need to use your right client for assets of course.

Cursor right now it is made that cursor MCB server is the name.

Let's just call it course.

And then we create the server.

As soon as this is created you press add tools.

And you can include whatever you want.

I want to include Gmail.

You can include every single Gmail tool under the sun.

What I want to include is just two for example, send email.

This is enough for me.

Then I press plus once again.

I want to include Google sheets.

I want to decorate spreadsheet tool.

And then I can press plus once again.

You can basically include whatever you want.

You can include Google Docs on Google Docs.

Let's just say I want to have everything.

So I include every single thing and I press on it.

Of course you need to connect your account if you are not connected.

I do it with Google right now.

I have given my access and I want to add all Google Doc tools.

And right now you see we have a lot of things included.

But this is not all.

You can go on however you want.

You can even include confluence.

You can include vector databases and a lot more.

But I do think vector databases is better to include via and then

because it's a lot easier to manage our vector databases

if we do this in our own server later.

So let's just close it.

I do think this is enough.

We can do everything in Google Docs.

We can make or create spreadsheets.

We can also send mails.

I can also include like get mails to see what's in my mails.

This is not really the point of this video.

I want to show you how you can connect this.

So you can simply come to connect.

And here you see basically the cool thing.

You have this config file and you can simply copy this config file

and include it of course into your application.

It's really that easy.

And here you see this, create your MCP server URL like a password.

It can be used to run tools attached to the server and access your data.

So please, please, please stay cautious.

You should never ever show this URL to other people.

If I would show you this, for example,

you can access my Zapier account and you can do everything on my behalf.

You can send mails in my name and do everything that you want.

Don't worry, I will delete the server as soon as this is done.

This is just for you, please stay cautious.

Then we come into cursor.

We already have this project, but what we want to do is of course to create a new one.

I have created a new file that I call it MCP course test 2.

We come back into cursor once again.

We come on file, open folder and I open the second folder.

So it's MCP course test 2 and it's of course completely empty.

You can chat here.

You can create code.

You can do whatever you want.

But first let's just include our MCP server.

For that we come on file, preferences, cursor settings, MCP as you know,

add new global MCP server.

Here I have an an MCP server included the runs via the npx command-o with a server send event.

Let's just delete this, include my Zapier MCP server.

And here you see at least a part of my API key.

I will not show you the whole API key.

Please make sure that nobody sees your entire API key.

Of course we start as always with a curly bracket.

Then we have MCP server, a curly bracket once again.

It's from Zapier.

Then we have the URL and the URL does everything for us.

So we do not have to include npx or whatever it's really that easy.

You can simply save this by control S or you can also press here file and save if you

want.

Then you can come back to cursor settings or whatever you want.

And here you see that Zapier is already connected and as soon as this thing is green it will

work.

If you want to exclude it you can press on it and the server will no longer work.

If this is not green or sometimes it takes a bit, it can take like 1 or 2 minutes until

all of this is loading up.

You can press here to refresh.

So you do not have to restart cursor.

Normally it should be enough to simply press refresh right here and then you should get

your tools.

And here you see every single tool that is added.

So you have add tools, edit tools, Gmail sent, Google sheet with create spreadsheets and

so on.

Everything is here included and you also see the server link.

So this is basically my mcb server of Zapier.

And right now we can trigger this out from cursor.

So let's just test this out actually.

Create a Google sheet, call it mcbcours with three columns, call them mcbcours and

test and let's end it out.

And then you see basically cursor has planned everything and right now cursor ask me if

I want to run this tool.

Cursor will ask me actually every single time as soon as I want to run a mcb tool.

You can do a workaround.

You can go into YOLO mode with cursor but I will not do this and I also think that this

can be dangerous.

YOLO mode in cursor is a little bit special.

Let's just call it this way because it will edit your whole code base and if you have

a big code base this can mess up everything.

It will run every single tool without asking you for permission.

So I would not recommend you necessarily to use the YOLO mode.

And of course you should always read what cursor tells you before you press run tools.

I create a Google sheet called mcbcours with the columns you specified.

As you mentioned three columns but only provided two names, mcbcours and test.

I create it with these two columns for now.

You can easily add more columns later if needed.

So you see you should be also clear with your instructions.

A simply told cursor three columns call them mcbcours and test and cursor thinks that mcbcours

is just one element but previously I had in mind that I want to have mcb, then another

row course and then another row test.

So yeah this was basically just on me, cursor was most likely smarter than me.

So let's just press run tool and I do think that we will create a Google sheet that it

will be called mcbcours and we will have our two or three columns or whatever.

Boom perfect there it's done and we also get a URL so let's just press on this URL.

I will open it, it opens up actually on this folder and you see that I have mcbcours.

Here we have mcbcours and that's so just two columns I should have told cursor maybe

a little bit better that I want to have three columns but this was just on me,

this just see that cursor basically has access to my Google sheets and that was the point here

and I can close this down and now I can send mails for example.

Send a mails to my mails address basically and tell him great mcbcours I believe of

I've started writing and I send it out.

Cursor will basically plan its action, it will ask me for permission I run the tool

and boom in no time whatsoever I have send it my mails.

So let's just come into my mails to actually see if I get this subject great mcbcours 5 star

rating with this message and an email id.

In my mails I have of course exactly this great mcbcours 5 star rating hey there

I just watched your course on mcb and so on leaving 5 star rating best regards of course I

haven't told cursor to sign off with Arnie or with whatever but I do think that you get the point

and right now I want to show you also something cool.

You are in cursor right now we can do all of these things that are included here but if you come

back to say beer and you come to history you can basically see everything that happened

over the mcb server we have created a spreadsheet and we have send a mails and if we come on configure

you can just add tools right now it's really that easy you press right here let's just say you

want to add the google calendar and I just want to for example find event and once again on the

calendar create detailed event so I just want to access also my calendar I come back into cursor

I do think that I need to reload this so that we get our new tools so let's just reload this

refresh it boom we have the google calendar find event and we have the google calendar create

detailed event and you can also see here on the parameters exactly what you can do here the

instructions or lay the color summary location attendees event type calendar visibility description

and so on so let's just test it out create event in my calendar for this date it's basically tomorrow

on 5 pm I need to work on my mcb course remind me of that and I send it out planning next moves

I create the event in your calendar round tool because I need to give permission of course

and boom there we are and you get also the event link and if I press on it open you see that I

have these right now on my calendar work on mcb course and I also got an error just look at this

I told cursor to create the event for this date and cursor actually added tune fifth

so this can also be a little bit problematical you always need to double check cursor can

eventually always make mistakes and you need to keep this in mind maybe I also wasn't that clear

with my instruction but generally speaking if you mean something if you have a diaper or whatever

cursor can make mistakes check my calendar when do I need to work on my mcb course run tool based

on your calendar you have one mcb course work sessions scheduled it's basically on tune fifth

2025 and it's on 12 am cursor is right this is exactly the time and date that is included in my

calendar the only error was as soon as I have created this event this could be on me because I

wasn't clear enough with my instructions I do think that I was like somehow clear I just leave

this purposely in this course I do not want to mislead you l alms can and will make mistakes and

you need to be aware of these and of course the same thing is true if you want to connect everything

lather server you can do it exactly as in cloud desktop everything that you have to do is to simply

include this into this mcb dot chasen so you simply come on file preferences cursor settings

you come on mcb and you add a new global mcb you can simply add it to this config file of course

you can include more than just one server just make sure that you don't mess up your syntax

you basically need to include your new server somewhere right here if you have any problems of course

you can also ask chatchapity for syntax or you can ask cursor for syntax it should be really easy

you can include whatever is server you want you can include how many servers as you want you can

also make this save your mcb server a lot bigger you can include even more tools but I need to tell

you as soon as you add like something between 20 or 30 tools it can be a mess maybe then you

need to come into your system prompt of cursor remember it's of course once again on preferences

cursor settings and on rules and you need to give a really really nailed down system prompt

if you have chasen tools everything works without a system prompt if you have 20 it can be like a

bit hard and if you have more than 30 tools you need to make a really really detailed and nailed

down system prompt because if you do not do this cursor will mess up it will call false tools

it can be problematical I just want to include this you should not use too much tools you should

not use too much servers if you use like a gazillion servers and no system prompt it will mess up

if you include a few servers and the servers start to mess up it the tool calling is not perfect

just try to improve it with a better system prompt and if it still messes up

throw some servers out of the window that you do not need this is important for me

generally speaking in this video I just wanted to show you how you can include

global mcb servers inside of cursor it's really easy you just come to your cursor settings

so on preferences and you add a new global mcb server you can connect save here but you can also

connect everything you get up server later as soon as we develop our own servers you can include

right now at this minute you can only include servers that do tool calling you can not include

prompt templates and resources I am sure cursor will fix this I am sure cursor will also include

all the other cool mcb servers also the servers that we will program and later over the course

we will also include the servers that we are programming but generally speaking this is how you

can connect to every single mcb server and also make no mistakes you can connect one single

mcb server to cursor and to cloud desktop and to every single other tool and if you have

included for example a database you can access your database from every single lm and the lm

will have context what you are doing in other lm interfaces this is really really powerful

that's why we needed to include this video and I do think this is everything that you need to

know about including basic easy mcb servers in cursor remember you can use save here for free

so just try this out and I'll see you of course in the next video