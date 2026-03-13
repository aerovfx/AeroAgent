# 2 -Model Context Protocol (MCP) Official Documentation Overview translated

---

The first thing that I like to do with I want to learn something new is to take a clear look at

the documentation. Because this gives us always a holistic overview. And that's why I want to guide

you in this video through the whole documentation. We will do it relatively fast. And if you are

already an experienced developer, this will be like really clear and easy for you. If you are

a completely new developer that just wants to learn these things, it can happen that you do not

understand some things from this video. But don't worry, later over this course, we will do

ever-ristingly thing step by step. So don't worry if you do not understand something right now.

But I want to start with a quick fire of the documentation so that you get the holistic overview,

what we can do, what we will do, what can change eventually over time. And so that you always find

the right thing in the documentation if later, like in one or two or three years,

something changes in the documentation. So first we come to model context protocol.io.

And here you are on this introduction. If we start on the left upper corner, you see Python SDK.

If you press on this, you will land on GitHub. Python is basically a programming language.

It's also the most popular SDK in order to create servers and so on. And that's why we will work

mostly with Python. But if you are a JavaScript developer, of course, you can also work with TypeScript.

This simply builds on top of JavaScript. This is also a lot of stars. So you can also see it here.

Python is by far the most popular programming language in general and especially also for MCPs.

Here we have like 13,000 stars. Here we only have 7. Then you also have the Chabastikay,

the coldliness decay, the C sharp SDK and the Swift SDK. And the add is like smaller things like if

you are a special developer, you can also work with this SDK later as soon as we come to programming.

But I would really strongly recommend you to take a look at the Biden SDK. And like I said,

later of course we'll do it. Then we are on this introduction. So don't worry about this.

This comes like at the end of the course. And in this introduction,

it's simply tell us why we should use MCP. Of course, I already told you this.

There's a growing list of already build at MCPs. It's really flexible and it can run securely.

Here's some general architecture things. So we always have a host, a client and the server.

Then the local data source or a remote service. You already understand all of this basically.

And then we come to the quick start. Here we have the quick start for the server developers for the

client developers and also for cloud desktop users. Let's just take a look at the server developers.

They simply give you a step by step instruction how to build an MCP with better alerts.

They give you all the code. They show you how to do it. So it should be really, really clear.

They also tell us that we can integrate of course resources, tools and prompts. They have some

examples in Python, in Node and so on. Then exactly how we can build our servers with weather.py.

How to include helper functions, how to implement in dual execution. We can always start with at

mcp.tool to use this how to run the server as soon as everything is done. Here you also see

the transport way. It's STDIO. So standard input output and you can run it with uvrun weather.py.

And lastly you can test it in cloud desktop by simply importing this script.

So don't worry like we do all of this really, really step by step. Then about client developers.

I personally have to tell you I do not like to develop a client because most of the hosts already

have a client included. I can't think of a good use case why you should develop a client for yourself.

Maybe you have a special use case but even then just think about it. You can use the OpenEISDK.

You can use PyDandDek, you can use LangChain, LangRaf, even an Aiden. You can use cloud desktop,

cursor, you can use whatever you want as a host and the client is always integrated and that's

why I do not like to develop a client. So let's just skip it. We should not do unnecessary work.

That's one thing that I really want to stress out. We should not do unnecessary work. For example,

a lot of people show you how to develop a server and then they build a server that already exists.

This is rather than you should not do this. The next thing is how to use it in cloud desktop. We

will do this in the next video. Then they show you some example servers like the file system so you

can integrate some stuff that they show you here. This will be always servers that are safe.

So as long as you stick to this server, they are safe and they also have a link to the official

MCP server repository. Also, this thing should be safe. Then the example client. This is a cool list

and you should always take a look at this list because you see right here that we have a lot of

different clients and not every client can do everything. And this list will get updated all the

time. You already know MCPs can have resources. They can have prompts and they can have tools.

But right now at this minute, not every single client has access to all three of this.

If you scroll down a little bit, Agentec Flow has for example all three included.

Cloud Code has no resources. Cloud Desktop on the other hand has all three.

Cursor has only tools included and so on. You should take a look. This will change most likely

like from day to day because all these clients want to include everything. So resources prompt and

tools most clients should accept all of this. Then we have Discovery, Sampling and Roots.

And yeah, especially Sampling and Roots, not a lot of clients include this. So if you scroll down

like I think it's only one right now, only the fast agent. So we will also not focus that much

on these two things because I will include it as soon as we have some clients that let you use this.

And then they have a smaller FQ like what is MCP and so on. This is already covered. Then

they have some tutorials. You can also build an MCP server with a LMS. Of course we will also do this

like come on. It's not 99.99. We will do wipe coding. So basically they just tell you that you

should include a little bit of documentation. You should be also really clear. They show you some

example prompts how to build it. Then they tell you everything about debugging. Mostly we will use

the MCP Inspector because this is a great tool. But if we use for example Cloud Desktop and we

use a server that is already built from GitHub, we can simply take a look like at the server logins

and so on. It's relatively easy. You can simply take a look at the logs from Cloud Desktop.

Some people also like to use Chrome DevTools. We will not. And lastly some common issues. A lot of

time especially if we use already built servers, it's like the Cloud Desktop convict file. It's like

mostly dipos or syntax errors or something like this. I will show you the most important syntax errors

as soon as we include these things. Then they give you a small overview of the MCP Inspector.

As soon as we develop our own servers, we will use the tool. This has a really nice interface

and we can simply see for ourselves if the server works or not before we can include it into a client.

Then they tell us a little bit about the concepts. So the core architecture you already know it.

We have a host client and the server. It's all connected and so on. They give you some examples

in TypeScript and also in Python of course. Then they talk a little bit about the transport layers.

We have STDIO transport. So standard input output. It's ideal for local process. This is also the

fastest one, the default one. This works really really great if you work locally. If you want to

deploy something to the Cloud or if you want to use servers that are already on GitHub and you do

not download them, we need to use SSC, so server send the band. Also this works great. It's a tiny

bit slower. It has a little bit of latency. We always use JSON RPC to communicate with the servers.

And the message is structured like this. Don't worry if you do not understand JSON. This will be

easy later. And then the connection lifecycle. It looks something like this. The client sends initializer

request with protocol version and capabilities. Then the server responds with its protocol version

and capabilities. Then the client sends initialized notification as a acknowledgement.

And then the normal message exchange begins. You will see this in Cloud Desktop you need to accept

a view times. Then the message exchange and I don't think we need to go that deep right now.

I think this is fine. Then you see we have resources, prompts and tools, so the three things that we

can connect. If you press on resources, this is also something that not a lot of people talk about,

but we can include resources. And this can be file content, data-based records, API responses,

live system data, screen shots and dimmatures, log files and basically a lot more. We can

include it something like this in our code. Here's some examples. Then the resource types is of

course source code, configuration files, log files, JSON or XML data and plain text. And the

binary resources can be images, PDFs, audio files, video files or non-text formats. This is also

something that nobody really talks about. You can also include like audio files, video files and so on.

These resources can be everything that you want basically. And then some templates are you can

include it, we will do this later. Then the next thing is the prompts. We can also include prompt

templates. They accept dynamic arguments so you can later type in specific stuff and the prompt

will change. You can include context from resources, chain multiple interactions, guide specific workflows

and surface as UI elements. Like slash commands for example. Then they tell us a little bit about

the prompt structure. Right now it's really not that important. How to use them. Then also that

dynamic prompts. This will be something that we include later and a closer look at all of this

later. Just remember we can and will include the dynamic prompt templates and we can also string

a few prompts together. Then the next thing and the most important thing is tools. This is something

that everybody talks about and also in this tools we can include a lot. First we have this discovery

tool. This is really really cool. You will see this in an add-in in the community note later because

not a lot of clients include this discovery. You see here the discovery of this client.

Mostly it's like rats or not a lot of clients include this. It's basically a mess. But in an add-in

we will use it. It simply means that the tool can list what the endpoint can do. Then we have the

and the flexibility of course. The tool definition structure is relatively easy. Then how we can

implement these tools for example in Python. Some example tool bad turns. How we can integrate

APIs. Data processing and some best practices. This is basically always the same thing. So you need

to be clear. You should use detailed JSON schemes and so on. We will do all of this. Then we have

sampling of course. This is basically a human in the loop design. First the server sends a sampling

request to the client. Then the client reviews the requests and can modify it. Client samples from

an LLM. Client reviews the completion and client returns the result to the server. So yeah I think this

is a little bit unnecessary and we will not spend a lot of time with sampling. Maybe in some special

use cases this can make sense. If you work with payments or something like this but generally I

would not recommend you to work with payments. Then we have roots. Roots is also not included in

most clients. You can basically give access to different paths and so on if you want to. Then we

have the transport ways. Generally speaking we always use JSON RPC as the buyer format. The request

looks something like this and the response something like that. Once again they tell you a little

bit about the standard input output so as TDIO. You should use it when building command line tools

implementing local integrations, needing simple process communication and working with shell

scripts. Then we have the server sent event. It's basically just streaming with HDD boaster requests for

client to server communication and we should use it only server to client streaming is needed

working with restricted networks and implementing simple updates. Then a little bit of security

warnings. So SSE transports can be like in danger to DNS rebinding attacks. If not properly secured.

Of course we will take a closer look at these. You should always validate origin headers,

avoid binding servers at all network inference and implement proper out identification.

And this is at least how I see it the most important thing. Outentification if you use server sent

event this can save you like a lot of pain. And then some stuff that is in development so what's new

you can take a look here from time to time. They will make updates all the time because it's a

relatively new protocol. Then we have the roadmap. So what they will do next and lastly the

contributing. Like I said this is just a quick fire so that you can understand what we will dive into.

Of course we will do it really slow we will do it step by step. This is also not everything that

we will do in this course. We will do basically a lot more because we will also work with like

local tools with an add-on and flow wise before we develop our own servers in python because it's

a lot easier it's faster and like I told you we should not do relevant stuff. A lot of people

build out like complicated servers in python that they don't need. Later we will build servers in

python. We will make a few examples but I think we should always do the easiest things.

Most of the time the easiest thing is the best. If you have cloud desktop and are already pre-built

MCB server wronged tab just use it. If you do not have it maybe you can build it in a no-code

tool or connect it to a no-code tool. So we should do that and then if this is also not a possible

option then then we work with python for example because we should work efficiently. So long story

short this was over review this was a quick fire let's just dive straight into it. In the next

video we will work with cloud desktop before we can do it we need to install some things. See you

in the next one.