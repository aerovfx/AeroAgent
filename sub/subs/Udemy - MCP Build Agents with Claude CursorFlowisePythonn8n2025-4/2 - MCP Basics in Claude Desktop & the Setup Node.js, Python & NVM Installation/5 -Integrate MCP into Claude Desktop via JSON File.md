# 5 -Integrate MCP into Claude Desktop via JSON File translated

---

In this video we will integrate our first MCP server in Cloud Desktop.

Before we do this, I am once again in Cloud and you see right now I have excluded every single MCP server.

This should be exactly the same thing as you have right now if you never work with MCPs.

And if I do something like this, for example, write a poem and save it on my desktop.

Of course, this will absolutely not work.

Yes, Cloud will write me a poem but it can not save this stuff locally on my machine.

We simply open up this canvas here. Yeah, this canvas is great or anthropic calls, desarty facts.

You can copy these, you can publish these, you can do whatever.

But if we close this down, you see nothing is on my screen.

There is basically no new file included right now.

And right now I want to show you how we can use an MCP server that can do exactly this.

I close this down once again and I use a new chat.

Then we come into this documentation because in this documentation they have really clear instructions.

To add the file system MCP server, this is one of the easiest ways to integrate an MCP server.

And I do think we should start with this right here.

Because they already have a file system MCP server for Cloud Desktop.

And that's basically also the next thing.

So don't develop something that can use a local system because we already have a server.

Everything that we have to do is we can't scroll down.

Of course we need to go into this developer mode.

This will create a convict file and you already know it on Windows.

It's exactly in this path and it's called Cloud Desktop Convict.chase. Like at Olu.

If you are on my iOS, it will be called exactly the same way.

But it is saved in a different path.

And if you don't have this file, you need to create one.

And then we have the thing that we need to include.

If you are on mycoes or Linux, it's basically exactly this thing down here.

And if you are on Windows like me, it's exactly this code down here, this Chase Informat.

You can simply copy this and if you scroll down, then you see that you need to replace the username

with your username. So this thing you need to replace it.

And you also see this right here. If you are on Linux, we only use one slash right here.

And if you are on Windows, this is like a stupid bug.

We need to do two packs, lashes and they are also in the other direction than with Mac.

So in Mac you see it's this direction.

And Windows, it's that direction.

And we always need to use two on Windows just to escape it.

This is like as the stupid bug like come on. We just need to accept this.

How it is. We also need notch. Yes, you already noticed.

You can test this with this version. I hope you already did this.

And now let's just see how this is working.

So please just copy this file. You come into Cloud, you press on this button right here.

You come to file, then we go to settings, developer, edit config.

So you see this thing right now is empty also for me because I have deleted my old config file.

Then we come to this Cloud Desktop Config file.json and you see it's exactly in the path that the documentation tells us.

If you open this up, you see this right here.

We have 99.9% of the time this thing right here included a curly bracket.

And here are the biggest syntax errors. Some MCB servers.

Have this bracket already included and some have not.

And you need to take a closer look at this. I just want to show you this thing right here.

If you include your server here, you will have a syntax error.

Because we start with a curly bracket and this makes no sense.

So you need to delete this and then your syntax will be perfect.

You can delete everything once again. And you see that you have something like this.

Your cursor will go most likely inside of this bracket.

And if you include your server here, you will also have a syntax.

Because some servers do not have this bracket included.

And then you simply need to delete this two brackets boom and then you are fine once again.

The easiest thing is, if you have already a bracket included, just delete it first.

Include your server and this server has the bracket already included boom and then you have no syntax error.

If your server has no bracket, you need to include this curly bracket.

It's really that easy.

And the next thing that we need to do is of course, do give the right path.

So my name on this machine is Arnold. So Arnold.

So you need to type this in where they ask for your username.

And then we should be basically set.

So now you can save this. I do this with control S.

But you can also press on file and save.

And by the way, I have opened this stuff up with VS Code.

This should work like with nearly every single text editor 99.9% of the time you will have a text editor already included.

And if not later, we will install cursor.

So this right here is VS Code.

What you can or should do right now is to close this thing down.

Close also this thing down and that here.

And then you can come here and your MCP server will pop up.

But I hope you remember what we need to do first.

We need to restart it.

If we close, clothe down and reopen it, it will be not included.

Boom. There is nothing.

But as soon as you come here and close it down completely,

reopen it up once again.

This thing should get at least in theory,

include that if you do not have any syntax error.

And if we do have a syntax, we should come into this logs.

If you press right here right now,

we need to wait most of the time for you seconds.

And then our MCP server should pop up.

And there we are, file system.

And you can press on it and you see that you can do basically 11 different tasks.

If you press on it, you see that you can read file.

You can read multiple files. You can write files.

You can edit files. You can create a directory.

You can list the directories.

You can make a directory tree.

You can move files, search files, get file info,

and list aloud directories.

I will not show you every single thing right here,

but I want to show you some.

And if you do not like that,

clothe can read your files just excluded.

If you do not like that, clothe can basically edit your files

and delete important stuff just excluded.

You need to think for yourself what you need, what you want to include.

And now we ask the same question once again.

Write a poem and save it on my desktop in a new text file.

And I want to make clothe a bit smaller so that you can see how clothe is working.

So clothe is right now on my right side.

And then it should make a text file right here, I think.

Let's just send this out.

Clothe will also ask me if I want to give access to the MCP server or not.

So there you see it.

List aloud directories.

Then the response is this.

Then perfect, I can save this to your directory.

You already know this from this documentation first.

We always list the tools that we can do.

Then clothe sees that we can absolutely do this.

And now clothe ask me if I want to allow these ones or allow these always.

If I allow these always clothe will no longer ask me this in the future.

So I simply press on allow always.

You can also press decline and you should also read for yourself what's the request.

So the request is that on path see user desktop Arnold and so on.

Let's just open this up once again.

We want to create some content.

The content will be this thing down here.

And this thing will get saved on our local machine.

And you also see it right now on the left side.

We have a poem dot txt and you can press on these.

And then we have here the content that clothe tells me.

Let's just see if clothe can edit this file.

I have a file named poem dot txt on my desktop.

I want that you delete the content in it.

Let's just send this out.

And right now clothe should simply delete it everything.

And here you see them.

I've cleared all the content from poem dot txt.

Let's just press on it.

Boom.

And now it's empty.

We can also edit this file.

Right.

Our story about Fox in the file.

We will send out the request in this file of course.

And clothe will basically edit this file and include new content.

And boom.

It should be done.

Let's just open this thing up once again.

There we have this file and it's edited.

Of course we can do a lot more.

I just want to show you one or two things once again and you can test this out like for

yourself if you want.

You see that I have a lot of pictures right here and these pictures they are a mess.

I also have some pictures of my desktop right here.

I just want to do something like this.

Search every picture on my desktop, create a folder named Pictures and move them in the

folder.

If I send this out, clothe will basically find every single picture that I have.

And of course once again I need to allow this because this is a completely new task.

I want to allow this always because clothe will now search for PNGs.

It will search for JPEGs.

It will search for every file that can be a picture and then it will move them.

It will create a folder named Pictures, hopefully at least and then move these things in it.

First we search files and if you press on it, you see exactly what clothe is doing.

It searches right now for JPEGs.

Then it will search for PNGs.

It will also search for GIFs also dot BMP, Diff, WebP.

So everything that can be a picture will get founded.

Right now clothe has also created a folder that is named Pictures and it starts to move

this into this directory.

So you see this picture right now get moved into Pictures.

We list these things, we move it.

Yeah, I think this looks great.

Dot goes on and moves everything in this new folder.

You see it right here, move file, move file, move file, move file and my desktop starts

to get empty.

And right now I do think that clothe searches once again like I have some pictures here on

this desktop.

I already have three desktop here.

They all get turned right now moved into this directory named Pictures.

And boom, there we are done.

You can also ask what's in specific folders.

You can ask clothe to search everything like search every text file, search every other

file on your machine, do whatever you want.

We have one JPEG file, six PNGs and two WhatsApp images.

And the clothe also asks me if I want to call this build that because like I have stored

everything in German.

So clothe understand that I am speaking German.

But I think this is fine.

This is just so that you can see that we can access our whole machine.

So right now I can do a lot more, but I think you should test this for yourself.

You can, if you press on this, see what you can do.

You can read every file on your machine.

You can read multiple files.

You can write files.

You saw this.

We can edit files.

You also saw this.

We can create directories, list directories, make a directory.

Move files, search files, get file info.

And list allowed directories.

So basically you can do a lot with this MCB server and you know how to connect it.

You can also think of a really simple workflow to save some stuff locally on your machine.

If you always chat with different LLMC remember, you can also use this MCB server and plug it

in different hosts.

And then you can write and read stuff that you want to save.

I just want to show you this really quick.

Make a text file, call it memory, save this.

I like pizza.

Memory I like pizza and boom, there we are.

And boom I like pizza is saved in this memories.

I like pizza and we can add memories.

Safety is in my memory file.

I need to finish my course.

Then I can send it out.

Right now I have I like pizza and I need to finish my course.

So here are basically my memories and we can go on and on and on and on and you can ask

also in cloud desktop right now what's in your memories.

Of course this is not perfect to be do this better with a vector database later but the

coolest thing is to already know it that we can switch clients really easy.

You can come for example in cursor and with cursor you have access to the same memories.

I will not show you this right now because this is not the part where we talk about cursor

but you will understand this over this course like section by section this is really really

powerful.

One MCB server can connect to ever a single client and you can work in calm junction.

If you want to share for example different data sources with all of your alimps this

is the way to go.

One last time let's just come back to the documentation.

With it all of this we also restarted cloud our server works but if your server for whatever

reason will not work you have the troubleshooting guide you can open this up and you can see for

yourself.

Most of the time you have this one two three four five errors server not showing up in

cloud and most of the time it's just a syntax in this cloud desktop config file.

It should be in the right folder and if it makes still problems just look at this logs.

So basically come on it press right here you can come on developer open up this logs

and on this logs you should come to the latest logs so I have right now a lot of logs down

here.

You will have most likely just a view logs and on this logs you can see what's going on.

You can basically just copy some of these logs throw it into cloud and ask what's wrong.

That's the easiest way.

If the tool calling fails you can read for yourself basically this should work everything

that you need to make sure is include the developer mode make sure that you have your cloud

desktop config file in the right place use this command insert the right path to your machine

and then just ask cloud to edit some stuff and a really really big attention right now

because cloud can delete stuff from your machine it can edit stuff it can create new stuff

so don't do this unresponsibly if you delete stuff that you do not want to delete yeah this

can be a little bit problematical but this is just the downside this is just the nature

of the beast if you give an LLM access to your machine it can delete stuff you can also

eventually work in a virtual machine if you want to play with this a tiny bit but just

with responsibly also your main system like normally it should be safe so just try disout

it as you of course in the next video because right now you know how to include these MCP

servers and in the next video want to show you a really cool server that allows you to include

a lot of servers a lot faster without editing your config file every single time yourself

see you in the next one