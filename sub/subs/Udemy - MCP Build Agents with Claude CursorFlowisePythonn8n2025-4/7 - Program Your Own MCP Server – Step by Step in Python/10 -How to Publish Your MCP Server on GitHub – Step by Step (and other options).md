# 10 -How to Publish Your MCP Server on GitHub – Step by Step (and other options) translated

---

There are a lot of different ways how you can publish your MCB server.

You can upload this to GitHub.

If you program with TypeScript, you can also upload this to NPM.

If you work with Python, you can also upload it to PEP.

You can simply throw everything on GitHub and let people download your server.

And if you have a streamable HDDB server, you can also host it and run it of course in

a virtual machine and pay for it.

So that other people can just access it.

It is with a want to give a little bit more clarity.

In order to make this clearer, let's just go on this MCB server from Airbnb.

If you scroll down, we have already used the server you know that we can simply add NPX

with our arguments dash Y and then the server for example into an add-in into call or desktop

in wherever you want.

So in an add-in, we just added these three commands and we also used the ignore robots.dxt.

What these things are doing is that we run over NPX all the code in the background without

installing everything locally.

So our server will simply spin up on our machine and everything will work.

And how does Airbnb do this?

They just upload it to their code and everything on NPM home.

If you Google NPM home, you can simply come on this and then if you just copy this name

for example exactly that one and you throw it on NPM and you send it out, you will find

exactly the server and if you press on it, here you can see the same thing as on GitHub.

So as soon as you type in this NPX command, your NoteBakage Manager will do the heavy lifting

in the background and run the code that is here included.

So if you have a server in TypeScript or whatever, you can also upload it into NPM and use

the NPX command in order to run this.

If you have a Python server, you can also come to PyPy and upload your stuff right here

and as the command we would use PIP for example.

If you do have a server that works locally like we have right now, because I have used

right now our old server that just uses the STDIO communication.

We can simply upload like every single file on GitHub and right now are readme that the

people need to clone our GitHub repo and then run everything locally.

And that's what we will do in this video.

And if you want to run your server on a virtual machine, you will also have the option to

host it on for example Cloudflare, but here you need to be cautious, you need to make

out the notifications and so on.

So the first thing that we are doing is to simply push all of this to GitHub.

But if we come to our readme, our readme is right now not perfect because we have made

some updates in our server and the readme got no updates.

So before you publish such stuff on GitHub, you need to make sure that your server is first

of all running and it should have a good documentation how people can use it.

Also remember, yes, we do have the prompt.md included, but the resource is on our local

machine. So we also need to write this in the readme if people want to use resources.

They should simply add these resources for themselves basically.

So what I am doing right now is I come here to Cloud.

I use for example Cloud for Sonnet and I tell something like this.

Take a look at the server and update the readme.

I want to publish this on GitHub and people need to understand exactly how to use it.

And then I send it out.

I do think that this thing will right now read the server and then update our readme.

It reads a lot.

Now it has a good understanding and we will remake our readme so that we have also the resources

included and everything because until now we did not have this included.

What I am doing in the meantime because this takes a bit of time.

I just come to GitHub so simply press on it.

I hope that you have an account on GitHub.

Then be pressing you in order to create a new repository.

We give it a name.

I just call it MCP example.

By the way, you can also work with my example.

Just download my GitHub server if you want.

This can be public, but if you want to do it for yourself,

you can also leave it on private if you just want to test.

I don't want to use any description.

We could also start with a readme,

but I just want to press create repository.

Now we can either start by creating a new file or uploading an existing file.

And we will upload an existing file.

Of course, if you work with Git, you can also do all of this in the terminal,

but I just want to make it easy.

So we press on this thing right here.

And here we can simply drag and drop all the stuff in it.

Let's just see where we are on our readme.

I just press on the readme, MCP multidool server,

except I do think this is fine.

Comprehensive, yes, this is also fine.

Seems to be fine.

Seems to be fine.

Yeah, I do think the readme makes a lot of sense.

I'd just accept everything and then we take once again a closer look.

So it's right now, I MCP multidool server.

A comprehensive model context protocol server

with fast MCP that provides calculator tools,

documentary sources and prompt templates.

This server demonstrates multi-plamsep capabilities,

including tools, resources and prompts in a single implementation.

The features, we have the calculator tool that can do some basic stuff.

Then we have a documentary source, we have the TypeScript SDK,

the GIFS access to this thing right here,

the dynamic file reading and error handling.

Then we have the prompt template that can summarize a meeting

until we have the quick start how to use this.

So clone this repository with this thing right here.

Then you need to install the dependencies.

Test the server.

Yeah, I do think all of this is fine.

The readme seems to be good, at least at first glance.

Then the chase for the cloud desktop config file looks something like this.

Seems to be perfect.

Path to your server directories of no longer my thing is included.

Then you can run the server with this command.

Of course, also this is perfect.

Then testing the individual components,

calculator tool, all of this works.

Then the resource and the prompt templates.

Customization is also possible.

So I do think all of this makes sense.

So let's just assume that this thing is right right now.

I just close it down.

I make this thing small.

I come into my MCB server.

And what we are doing right now is we can not throw the whole file in here,

but we need to copy this file's right here exactly like this.

And we throw all of these files in here.

Then all of these files will get uploaded.

And as soon as this thing is uploaded,

we can simply press commit changes.

Processing your files and boom, there is our server.

And here you see that we have the whole documentation included.

How all of this is working, how people can use this.

What's expected and so on.

How to use it in for example,

cloud desktop, how to use it on different machines and a lot more.

So this is just a really easy and basic server.

And people can use this in order to build their own stuff.

But if you have made something special,

of course, they can use it exactly like this.

People can just copy this GitHub repo

and then they can run with this.

And of course, we have also the server.py people can click in it,

see the code for themselves.

And if they like it, of course, they can simply download everything

on their computer, on the templates.

They have also the prompt.d,

so they can play with this prompt if they want.

So basically what people have is they can download our server,

install everything locally and can run with it.

What people can not do is simply typing in the config file and run with it

because we have not uploaded this to npm or pip.

To be honest, this is also not really needed.

We have not as streamable HDDB server.

I worked here with our local server,

but people can still run with it.

If you have on the other hand,

a streamable HDDB server or a SSEN point,

of course, you can also upload it to npm or to pip.

It depends on what programming language you are using.

And then people can access your server with a really easy file.

The file would look something like this here

from the Airbnb server.

They would use npx if your server is in DIPEScript

with the arguments-y.

And then a link, for example, either to this thing here

or you can also include your get-tub link here.

And then the command npx will do all the heavy lifting

so they don't have to copy your get-tub repo.

Same thing is true if you upload to pip.

You can also work with the pip command here.

But with it, the easy way.

People can simply clone our repo and run with it.

And if you use streamable HDDB or the server send

a vent, of course, you can also run this onto a virtual machine

and people can access your server without installing it locally.

And in the next video, I want to talk bravely about that.