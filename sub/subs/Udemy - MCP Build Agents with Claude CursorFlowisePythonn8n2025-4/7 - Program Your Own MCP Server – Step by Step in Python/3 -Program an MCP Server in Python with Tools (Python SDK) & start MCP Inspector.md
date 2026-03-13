# 3 -Program an MCP Server in Python with Tools (Python SDK) & start MCP Inspector translated

---

In this way, do we program our own first MCB server with the PIDNES SDK?

Of course, if you are a JavaScript developer, you can also use the TypeScript SDK.

You can work with whatever you want.

And I just want to make a really, really simple,

engineering explanation.

We will build a server that uses of course a tool.

We will later include also resources and we will include prompt templates.

So our server can do all three things that the model context protocol supports.

But we will keep it really easy.

So in this video, we will start with the basic functionalities of our server.

We will create it like a dole in Python.

You can add more tools.

You can add less tools.

You can add other tools.

You can do whatever you want.

The first thing that we should probably do is that we come, of course,

to the documentation.

So you should come to model context protocol.io.

And of course, something that we need is the SDK that you want to work with.

It's either the Python SDK or the TypeScript SDK.

If you are a special developer like in C sharp or whatever,

you can also work with other SDKs.

But I would strongly recommend you to start out with the Python SDK.

And if you are a JavaScript developer,

you can also use the TypeScript SDK.

So you should also open up the model context protocol,

Python SDK on GitHub, because we will need it later.

Then the next thing that I want to show you is that we will program,

of course, like it's not 1999.

We will program with LLMs.

And here you can see building MCP with LLMs.

So you can press on it and we will get the good documentation for it.

Also, we will use Clot, but we will use Clot over cursor.

You already know cursor.

First, we need to prepare the documentation.

Before starting, gather the necessary documentation to help Clot understand MCP.

And they have something really, really nicely here.

They have a whole LLMs.txt file.

So you can simply open this up here.

This is basically the whole documentation.

Everything is in markdown.

And here, like everything is included that you need to have.

If you simply index this file,

you have like a lot of context.

And Clot and cursor will help you build out your application really easy and fast.

So open this up.

Then we should navigate either to the TypeScript SDK or to the Biden SDK.

Of course, we have already opened it up.

We use the Biden SDK.

Then we should copy the readme files and eventually also other relevant information

from the documentation.

And we need to paste all of this documentation into Clot.

We will use cursor like a dodo.

So we close this down.

We come on my desktop.

On my desktop, I have cursor.

Before we open up cursor, we should make a new file.

I always like to do this like manually on my PC

because it makes it easier to work with.

And we call this MCP server course, for example.

Then we open up cursor.

As soon as cursor is opened up, we should come to file, open folder.

And I open up the folder that we have created.

The next thing is that we need to add context.

So simply press on add context.

And we want to add documentation.

So we press on it.

You see that I have already some documentation included.

But I just want to start over again.

And we will include every documentation that we need.

So we simply press add new log.

And here we need to give the link.

The first link that we give is of course all of this file.

So we want to give the full LLM text here.

So we click on it, we copy it.

We insert it here.

And then you can send it out.

Right now you need to give a name.

I want to call this, for example, MCP, LLM, full.

And we press confirm.

Right now this thing is added.

And you find it in indexing and documentation.

Here you see everything that I have added.

And also MCP, LLM, full is included.

And if you actually come on this book, you can click on it.

And you see that we have one page indexed.

But in this page, there's a lot of information.

And Claude can simply pull all of this information

as soon as we start coding.

I want to add a little bit more documentation

because the other documentation told us to.

So we simply press add context.

Once again, documentation.

We scroll down, add new docs.

And the next documentation should come

basically from the Python SDK.

And here we can either copy the readme

or the stuff that is relevant for our documentation.

So we come to the Python SDK.

And if you come on the readme,

here we basically have a lot of things that we can include.

So this thing understands that we need to work with you.

We and we need to install the MCP CLI.

We have a quick start or so that we need to use the vast MCP.

This is how we can define tools.

And so on.

Then the core concepts, everything for the resources.

How to define tools.

How to define prompts.

How to define images.

How to give context.

Authentification if we want to include authentication.

How to make a Claude desktop integration.

How to do direct execution.

How to use streamable HTTP report.

So I do think that we have everything that we want.

I just want to see for a brief moment

if we also get, for example, the STDIO communication.

But I do think that we get it.

And also the SSE endpoint configurations.

Yeah, I do think like this is more than enough for us.

So we simply copy this readme, we copy this.

And we also insert it right here.

We send it out.

And we call it once again, python SDK, MCP, readme.

We press confirm.

Right now also this thing is indexed.

And if you press on it, here we have 13 pages.

And you can basically see for yourself what get at it.

But I do think that we have everything included right now.

And the next thing is that we need to write a prompt.

Also in the documentation, they tell us that we need to describe our server.

So once you provided the documentation,

clearly describe to cloud what kind of server you want to build.

Be specific about what resources the server should expose,

what tools it will provide, and any prompts it should offer.

And what external system it needs to interact with.

So we need to make a prompt that is really, really specific.

And here we also get a small example.

Build an MCP server that connects to my company's bossgres SQL database.

Expose tables schemes as resources provide tools for running.

Read only SQL queries.

Include prompts for data analysis tasks.

I do think this prompt is a little bit too big.

And I would not recommend you to work with such a prompt template.

If you scroll down and read a little bit further,

they tell us start with the core functionality first.

Then iterate to add more features.

That's also the stuff that I would recommend.

I would recommend you to start with tools and then add, for example,

prompts and resources step by step.

Next, ask cloud to explain any parts of the code you don't understand.

You can also do this in the first prompt.

Then request modifications or improvements is needed.

We will need this if the server doesn't work.

And lastly, have cloud help you test the server and handle edge cases.

So you need to work with the element not against the LLM.

Cloud can help you, of course, with everything, basically.

Then the best practice is,

break down compresurvers into smaller pieces like we will do.

Test everything, keep security in mind,

document your code well for future maintenance,

and follow MCB protocol specifications carefully.

And of course, the last steps we should test everything,

for example, with the MCB inspector.

And the last steps, we need to review everything we should test it with MCB inspector.

We should connect it eventually to cloud,

and then iterate based on real usage and feedback.

So let's just start with a simple prompt.

And like I told you, we will not do it every single thing in one prompt.

We should not do this basically with a zero-shot prompt.

We should do this slowly.

We close down the cursor settings.

We are in this folder, so in this MCB server course.

And now we need to start with a prompt like this.

I want to create a MCB server from that,

then we type in add.

And here we can add documentation.

So you press on docs,

and we use the MCB LLM full.

Use that, then once again, add.

We want to use the PytNSDK,

so the documentation.

PytNSDK MCB read me.

The server should have one tool, a calculator.

And then I include a little bit more context,

so I include this right here.

Write that detail to read me with every single step included,

so that we can simply follow the readme.

Installation of UV, PytN, etc.

Every step should be documented,

including how to verify that the version works,

assume that I have already created and opened a folder.

The server should run in a virtual environment.

The MCB CLI package should also be installed using UV.

This is just a little bit of tweaking, fine-tuning the prompt.

I have found out that it works a little bit better.

If you want to do it even better,

you can give right now in this prompt once again,

a little bit of examples with the short prompting.

But I just want to run with this,

if it works, it works.

If it doesn't work,

we start once again and fine-tune our prompt,

or we simply work with cloud in conjunction.

Now you need to press on the model that you want to use.

You can either use an auto model,

you can use the maximum if you have the planning included.

I just want to run with cloud for Sonnet,

and we send it out.

And right now, cloud inside of cursor will do all the heavy lifting for me.

It thinks for a tiny bit,

then it searches the MCB PytN SDK,

and I want to press continue,

so this is allowed.

It will index everything that it needs.

Once again, continue.

Now it can create the server,

so you see we create the server.py and boom.

We have our first file, this is the server.py,

and at least at the first glance, it looks somehow okay.

We have a lot of things with the calculator we have at,

subtract, multiply, divide, power, square root,

and so on.

Right now it's creating the rate me.

Boom, there's the rate me,

and it seems that we have most of the stuff included

that we want to include.

So let's just take a look.

We start with from MCB server,

fast MCB, import fast MCB.

This is the library that we absolutely need.

We also need the math library, this is right.

Then we need to create the MCB server,

and we use once again the fast MCB,

and we call it calculator server.

This is okay.

Then we use the final MCB tool,

and the tool is the add tool.

So we can simply add two numbers together.

This is the description that description needs to be always

really, really precise,

so that our server knows when to call this tool.

And it returns, for example, 1 plus b.

Then we define the next tool.

The next tool is the subtract tool.

This is the function, and this is the description once again,

and this is what it returns.

Then the next tool is multiply, same thing.

Next tool, divide.

Same thing.

Next tool is power, same thing.

Next tool is square root.

Here once again, the description.

We also have a if function,

if it cannot calculate the square root,

then the next tool with the same concept,

and now the last tool with the same concept.

And lastly, if name equals main MCB run.

So this is a really, really easy and same preserve,

I do think that this server should work.

I just want to accept this file.

What I am not 100% satisfied is that we don't have, for example,

SSEN points included.

We don't have HTTP included.

STDIO is also not specifically included.

So I do think we will communicate via STDIO

because it's the default function from MCB.

But this is a great starting point.

Now we come into the rate me.

And the rate me, let's just accept it.

Let's just see what we need to do.

So MCB, calculate our server,

add multiple context protocol server

that provides calculator and so on.

This seems to be fine.

Then the prerequisites.

Here's everything included.

For Windows, download Python 3.10.

We already did this.

Then we need to verify our installation

with, for example, Python-dashversion.

Let's just actually follow this rate me.

You can either do this here in the terminal,

so you can simply open up a terminal.

And now you can type in the stuff that you want to type in.

For example, we should check the byte conversion.

This thing tells us that we need to check.

So Python-dashversion, we send it out.

Boom, we have a byte conversion that should work.

We don't have a Mac.

Then step two, we need to have UV installed.

This is the command for UV.

Or we can install it via pip.

For Mac, we install it with Brue,

for Linux and so on.

And now we need to verify if we have UV installed.

Because I have already installed this,

I would guess that this is fine.

So I send it out.

And boom, UV is installed.

Step three, restart terminal.

I have already installed everything,

so I don't have to restart.

Then we need to make our project set up.

The directory is fine because we are inside this folder,

so this is okay.

Our UV project, we need to initialize this.

Because we are already in this directory,

we can also do this, UV, in it.

And we add a point.

And we can send it out.

Initialize project, you see,

MCP server course, at exactly this thing right here.

So we have initialized everything.

Then we need to create a virtual environment

with UV, VNV.

So we copy this and insert it.

And boom, we could also verify this.

I already done this.

This was basically stupid.

This was not needed because we already see

adult VNV right here.

Then we need to activate our environment with this command.

Everything should work.

The Python version is okay.

Yeah, this is a detailed explanation.

Now we need to install the MCP SDK.

This is important.

So we need to have UV at MCP CLI.

So we copy also this and throw it down here and send it out.

This thing will get right now installed.

Everything should be installed right now.

And basically also our MCP inspector should be installed right now.

We don't need to verify the installation.

Everything seems to be fine.

We should see packages like this included.

Yes, we do have them.

Verify the installation.

We don't really need to do this.

Then create the server file.

We have already done this.

So attention, we already have the server.

Don't buy here included.

And in this server, yes, everything here is included.

All these tools are included from our calculator.

And we don't need to verify it.

Now we need to test the server with the MCP inspector.

So we need to run this command.

UV run MCPDevserver.py.

This is basically the last thing that we need to do.

If I copy this, then we insert this thing down here.

And we send it out.

This thing should basically spin out our server.

It should open up our server if everything seems to work fine.

Right now it's loading.

And I do think that this thing works fine.

And if I type in Y to proceed, it will spin out.

So I type in Y and I send it.

We also should open up our model context protocol in Spector.

This thing is loading so everything seems to work just fine.

Starting MCP in Spector.

Proxy server listening on board 6, 2, 7, 7.

And MCP's vector is up and running at exactly the ZURL.

So you could basically just copy the ZURL or just press follow link.

It gets opened up right here.

Let me pull this aside here.

And right now let's just see connect to MCP server to start inspecting.

So we press connect.

We communicate via STDIO, the command is UV.

The arguments should be this right here our server.py.

So everything seems to work fine.

So let's just press connect and see if we are connected.

And boom, there we are connected.

Everything seems to work fine.

So server is up and running and in the next video we take a closer look into the MCP in Spector.

We need to talk about debugging.

We need to see if our server is working or not.

Because in this video you have learned how you can code up a basic server.

Everything that you have to do is to simply give cursor a lot of documentation.

Before you do this, make sure that you open up a new folder.

Inside of this folder you give documentation, you write a prompt

and you should include the stuff that you want to include.

We have included just tools.

And it got basically a calculator but the calculator needs to use a lot of different tools.

And that's what we have included.

We have include the add function, the divide function, the subtract function and a lot more

with all of these different tools.

And I see you all for in the next video.

In the next video we take a closer look to see if our server is working or not

or if we need to debug it.

And then we will add prompts and resources.