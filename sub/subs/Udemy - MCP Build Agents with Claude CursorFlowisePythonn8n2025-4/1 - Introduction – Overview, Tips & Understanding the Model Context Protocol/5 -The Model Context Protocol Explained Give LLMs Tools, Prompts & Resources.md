# 5 -The Model Context Protocol Explained Give LLMs Tools, Prompts & Resources translated

---

What is the model context protocol and how does it work?

Yes, I know. This is a theoretical video, but we need to understand this.

The model context protocol comes from Antropic.

The company that has created Claude, so an I-cell LLM.

And it was introduced on November 25th, 2024.

And in the first few days, it got like a small spike, but not that much traction.

But later it started to go somehow viral, everybody uses the model context protocol right now.

If you come on this webpage, you see that we have over 15,000 different MCP servers.

And this is important, because if nobody uses the model context protocol,

it's no longer valuable.

The model context protocol is similar than a USB-C port for the PC.

With the model context protocol, we can give Antropic and LLM tools, resources and prompt templates.

And you need to understand that there's something like a network effect.

The model context protocol is only available if a lot of people are using it.

Just like with WhatsApp, everybody's on WhatsApp, that's why WhatsApp is valuable.

I secure basically does the same thing, but it's no longer that valuable.

But it seems that the model context protocol is here to stay,

and that's why we need to understand it.

Let's take one step back in order to understand all of this.

An LLM like ChatchyPD, or even Claude, is not that smart.

LLM on itself can only generate text,

summarize text, generate code, translate stuff and so on.

If an LLM needs to do special stuff, it needs to call tools.

For example, we can call an API to create images.

We can call the web search tool.

We can call the research here in ChatchyPD.

We can call a Biden Interpreter.

So if an LLM on itself is not smart enough, it can call tools to complete the task.

Yes, we have some models that are multi-model,

but most of the time as soon as an LLM needs to do specific things,

it will do the so-called function calling, it will call a tool for help.

And as soon as we call these tools,

we make most of the time simply a HDDB request to an API.

Think of an LLM like this.

The LLM is somehow like the new computer,

and a computer is only valuable as soon as we install some tools,

a bit of software.

On a computer we have a disk, a hard drive, a file system where we can save stuff.

And the same thing is true for an LLM.

We can have extra databases within beddings where we can save stuff.

On a computer, we install the software 1.0 tools.

And the same thing is true for the LLM.

We can do function calling to a calculator,

to Biden Interpreter, to the terminal, to whatever.

Then we have the peripheral devices.

This means an LLM can do function calling to video models

so we can create videos if we do function calling.

And we can also get videos, analyze videos, and so on.

And we can also talk on LLM and generate audio.

Of course, we can also do web browsing within LLM.

And LLM can also talk to other LLMs.

If we make these things bigger and let LLM talk to a lot of different tools and other LLMs,

we have a AI agent.

And right now in 2025, this thing also got an update.

This is let's just call it a new LLM.

In an LLM, we can throw in voice, text, and vision.

And we can get back voice, text, and vision.

Thanks to the tools it can use.

And one of the tools can also be the model context protocol.

And with the model context protocol, we can combine all of the tools.

And of course, the new LLMs can also reason

with the test time computer chain of thought.

And the context window gets bigger and bigger.

This means that LLM on itself can only generate mainly text.

It will split out your text in the so-called tokens.

It will make a calculation in the neural net

and will give you the most likely tokens back.

This is a simple explanation, I know.

But thanks to function calling, we can do all of this.

And how all of this works exactly.

Where's the place for the model context protocol?

We should come in this whiteboard.

We have basically said that an LLM on itself

is not even that smart.

But if an LLM is not smart enough, it can do function calling to an API.

If an LLM for example doesn't know stuff, it can search the web.

An API usually communicates via HTTP.

And on HTTP we can have GET.

We can have POST.

We can have DELETE.

And a lot more.

If we call for example the Gmail API,

BI HTTP.

We can get mails.

We can read mails.

We can label mails.

We can send mails.

We can do a lot of stuff.

And forever a single one of these things,

we need to make a different HTTP request.

Because these APIs, they are not specifically made for an LLM.

If you call an internet API,

the web browsing can be for example a local search

or a global search or whatever.

And the API is not structured for an LLM

to know automatically what you want to do.

And now comes the model context protocol into play.

Some people call the model context protocol

the USB-C port for LLMs.

Now what do I mean by that?

Let's just make it this way.

Here stands your PC for example.

And your PC has of course a USB-C port.

And on this USB-C port you can connect a lot of different things.

You can connect a mouse.

You can connect a desktop.

You can connect a hard drive.

You can connect even power.

You can connect whatever you want with a USB-C port.

Before the USB-C port was invented,

every single one of these let's just call them tools

needed a different connection to this PC.

And right now thanks to this connection,

you can use just the USB-C port to connect all of it.

And the coolest thing is also your mouse and monitor

doesn't care on what PC you plug it in.

You can switch really fast and really easy.

Your heart disc doesn't care where you plug it in.

You can switch it really fast

and you can connect every single one of these tools

with just one standard.

And I do think that you know where I am going.

The PC in our equation is the LLMs.

The USB-C port is the model context protocol.

And the things that we plug in can be tools

like for example different APIs,

resources like picture, text and so on

or prompt templates that have dynamic variables included.

And the tool that you want to connect

doesn't care on what LLMs you connect it.

The resource doesn't care

and also the prompt template doesn't care.

As soon as the MCP server is set up once,

you can connect to every single LLM.

And as soon as an API for example, get an update

everything gets handled automatically.

With the model context protocol,

we have always a host,

so some sort of host.

For example, cloud desktop,

it can also be cursor,

lovable windsurf,

and anything whatever you want.

This host needs to have a client.

This client is most of the time automatically included in the host.

So if we do not need to worry about this client,

yes, we will talk later just a tiny bit also about the client.

But in most cases, the client is automatically included in the host.

And this client can communicate with a lot of different things.

It can communicate with APIs,

with resources and with prompt templates.

And this thing only works so good

because we have an additional layer of abstraction.

We call the MCP server an additional layer of abstraction.

So the host with the client can connect to the server

and the server can connect to APIs, resources, and prompt templates.

So this additional layer of abstraction can be a wrapper around an API.

You can include resources and you can include prompts.

And as soon as one server with this additional layer of abstraction is set up,

it doesn't care on what host you connect it.

And one of the coolest parts as soon as these API integrations are set up,

the server can decide automatically

what API call you want to make.

Because MCP server, unlike an API,

is specifically made for an LLM.

So generally speaking, we could skip MCP server

and connect to APIs with normal function calling.

We communicate always with ChaseNear

and these APIs, they are simply not specifically made for these LLMs.

This means at the end of the day that the communication between a host

through different APIs with function calling can be amassed sometimes.

And the model context protocol makes it a lot better.

This means at the end of the day that an AI application can dock to web APIs databases.

For example, GitHub servers, productivity app, terminals, WhatsApp,

prompt templates, resources, and a lot more.

Via the model context protocol and also only one server can include

every single one of these tools and you can switch your AI application immediately

as soon as the server's setup.

You can make your cloud desktop into an AI agent

that can use every single tool that you want.

Here for example, I have connected an add-in with vector databases and some different tools.

You can also include prompt templates and resources

and you can also connect the same things to for example cursor, wind surf,

or whatever you want.

Besides that we have a list function and the list function will make everything more concise.

So you don't have to specify every single API calls because

the MCP server makes or translates your API calls specifically for the LLM.

We can basically say that MCPs and APIs they have a lot of similarities but also some differences.

On both, the MCP server but also on APIs and API calls

we always have a client server connection.

We always work with some sort of abstraction.

We always want to get something back or send something out also with a normal API call.

And also APIs want to simplify integrations and now the differences.

The model context protocol is purposely built for LLMs.

For LLMs to communicate with other stuff.

And the APIs are of course general purpose.

This means the communication works a lot better with the model context protocol

because it translates our API calls.

And of course as soon as we have made one server we can connect to a very single client.

Besides that we have dynamic self discovery.

If we come back to this example, you know that you can connect via HTTP requests to Google.

And if you connect with HTTP to Google, you need to set up,

get, send, delete, label and everything manually.

In everything, maybe I call you can nuts which hosts.

And if you do this over the model context protocol,

you can send on this model context protocol.

The command list and it can list everything that it can do.

And it will do dynamic self discovery and we'll understand what function you want to call.

And besides that if you use one of these gazillion pre-builder MCPs servers,

you don't have to worry if API requests change over time.

Because superbase will make updates to their MCPs server all the time, you see an hour ago.

So you don't have to worry if something in the API changes.

You just connect to the MCPs server and your LLMs always up to date with the newest stuff from

superbase. And lastly, standardization of interface.

Every single one of the MCPs servers work completely the same.

We have a simple config file and we can connect this config file always the same.

On the other hand, if you need to set up API calls, you need to set everything

LAPI call differently. This is a mess.

So this is the new standardized communication between LLMs and tools,

but not only tools also prompts and resources.

Some people call the model context protocol simply a wrapper around an API.

And yes, you can also basically say this.

If you connect to different APIs, it's a wrapper around some APIs.

But of course you can also do more and it makes it a lot easier to communicate with the APIs.

Long story short, another LLM on its own is relatively dumb.

It works with tokens and it will calculate the next most likely token for you.

The next most likely token is most of the time text code maybe also a picture of work with

multi-modality. But most of the time as soon as you want to do something we need to call tools.

And we call this function calling. And function calling works over HDDB requests.

And HDDB requests connect to APIs. And APIs are not specifically made for LLMs.

We communicate via JSON. And in every single application that you want to build,

you have to set up new API calls. Because you have no clear standard to communicate.

And the model context protocol changed everything. You can create one MCB server.

You can connect a lot of different APIs. The communication will work perfectly because this is

purposely built for LLMs. And then you can switch client and you don't have to worry about the

stuff that works here. So the model context protocol is the new standardized way for

an LLM to communicate with APIs, resources and prompt templates. And we will use the model

context protocol extensively over this course. And the model context protocol gets more and more

valuable if more and more people using it. And you see that right now everybody starts to use the

model context protocol. I would not be surprised if nearly every single big tech company would have

at some point an MCB server for their services. Most of them also have it right now.

I know this was a lot for right now, but I promise you you will understand this step-by-step

over this course. And I'll see you of course in the next video.