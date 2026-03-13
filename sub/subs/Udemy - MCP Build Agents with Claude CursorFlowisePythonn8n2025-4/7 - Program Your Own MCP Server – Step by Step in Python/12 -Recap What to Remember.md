# 12 -Recap What to Remember translated

---

In this section we took a look at a lot of exciting stuff.

We started with an overview of the project,

and then we started immediately to code our power server.

We used cursor for coding with Cloud4Somnet as the work model.

The first thing that you should do is to index all the stuff that you need.

Use the complete text for the LLM

that the documentation specifically tells us,

and also link the PytN SDK maybe the readme.

You can also link more documentation if you want,

and then you need to write a prompt that is relatively specific.

And I do think you should make this small.

You should do it step by step.

Just start with some tools.

Don't tell like in one prompt every single thing that you want to include,

because if you make it too big, cursor will mess up,

and if cursor messes up,

and you don't understand coding that well,

you're like, you are not in a good place.

As soon as you have built that your server relatively easy,

you should simply start it with these commands.

And of course you can also make the readme with cursor

so that you can just follow the readme.

As soon as your server spins up,

you should open it of course with them the bin's vector.

Because the inspector works a lot faster

and a lot easier for debugging.

Just see if your tools are working and please use STDI over this.

After your server works,

you can create a config file for Cloud Desktop.

And also here, cursor can help you.

Always give a little bit of documentation,

maybe some example code, and then you are ready to rock.

As soon as everything works,

also in Cloud Desks,

the Ubisoft you should go on and include more stuff.

We started with a resource.

It's relatively easy.

Just give a path to a resource and tell cursor exactly what you want to create,

and then everything works automatically.

And the same thing is true for the prompt.

Download your prompt on your local machine,

give the path and tell cursor that you want to include a prompt template.

Always give a little bit of documentation or example code.

As soon as your whole server is robust and is running,

in the MCB Inspector, of course,

you should take a look at different transport ways.

The server sent event and especially the streamable HDDB.

You can include it with just a few lines.

You can also make it more robust and give a few options.

You saw all of it.

Of course, this is not all because you can include whatever you want.

You can include more tools.

You can include more resources.

You can include more prompts, but remember,

one of the biggest problems is

as soon as you include too much tools,

your MCB server will no longer work correctly.

The other lamps are not smart enough to decide if you give

like a gazillion different tools and prompts and templates.

So please,

like leave it a little bit on the smaller side.

Because a server that doesn't work for liable is a mess.

One of the other big failures is,

at least how I see it,

that people always build redundant stuff.

I do think there's not a lot of value

in adding a lot of different tools to a server.

First of all,

you can add tools a lot easier with an Aiden.

So I think you should do simply this.

But if you have special resources or prompt templates,

I do think this is the real value here,

because you can work, for example,

with Cloud Desktop really easy, really fast.

One of the other big problems is also the security.

And of course, we talk about the security

in the next section in detail.

This will be important.

Then you'll so click by click how you can publish your server

on GitHub.

And if you have used Streamable HDDB,

you can also host your server in a virtual machine.

You can use AWS Azure Cloud Flare Render, whatever you want.

You are just a view clicks away from hosting your server

in the cloud.

But I also have to tell you here,

maybe it's not really needed.

Maybe you don't have to give other people access to your server.

First of all, in an Aiden, it's easier.

It's also cheaper because with hosting

a weekend, spin unlimited servers.

And we can give also other big places

with just our server sent event file.

So yeah, decide for yourself.

But if you want to do it, of course, you can do it.

And you have problems, hit me up with a mail

and I'll be linked with another video where we do it.

Click by click.

I just want to save you some bucks here.

So in that manner, you have learned a lot

over this section.

And I have to tell you what learning is.

Learning is same circumstances, but different behavior.

Until now, maybe you did not know how to create

a three times a B server in Python.

Maybe also in TypeScript, whatever you want.

And you have only learned if you do.

You do not have to make something

that you want to host in the web.

But I would strongly recommend you to play with this a little bit.

You are in big, big, big advantage

as if you can create your own server in Python

or in TypeScript.

Because this is a skill,

and you should always learn new skills.

The model context protocol is something that is really cool

and you should be absolutely able to implement it.

This can also offer you new jobs.

If you can throw on your resume,

that you have built it out,

your own MCB server,

and it's public,

Reveil, Blomgettub,

you are in a good place.

And in that manner,

I also want to tell you what really good learners do,

of course, they learn together.

So if you could share this course,

does it really mean the work to me?

Maybe it also means the work to the other person.

And if the other person gets value out from this course,

they will describe the value to you

because you have told them.

Thank you for that and I'll see you, of course,

in the next section.

The next section is really important

because you should never, ever underestimate security.