# 2 -Project Overview Python Code, Structure & GitHub Repository Explained translated

---

And this video will give you a quick overview of the projects that we will create over the next videos.

Don't worry if you do not understand it yet. We will do this slowly, we will do it step by step.

And you should basically build this with me. If it's too complex for you, you can also simply just

clone my GitHub repo. Because I also bubblyke all of this on GitHub and then you can simply copy my code,

manage my code a bit. Maybe you can use my code to throw it into cursor. But generally speaking,

this should be really easy. But of course, if you never ever coded before, I think you need to play

a little bit. I am right now here in cursor. And in cursor on the left side, we have these folders.

These folders will be on our local machine, especially on our desktop and we will create everything

step by step. The first file that is included here is its under templates. And here we do have a

prompt template. So we will also include a prompt template in our MCP server. This prompt can simply

make summaries of meetings and here we do include dynamic variables so that you can basically use

this tool inside of for example, Cloud Desktop. This prompt basically means that you can either list

your prompt, then press on your prompt. You can simply enter a meeting date, then the meeting title,

and of course the transcript. So here comes all your stuff in it. And then you can press get prompt,

and your whole prompt will get executed automatically. Right now I am here in the MCP inspector.

You can also list all the tools that we have included in our MCP server. Don't worry like we

will do this step by step and we will have everything also in Cloud Desktop so you can run your

prompt in Cloud Desktop, your resources in Cloud Desktop, and also your tools in Cloud Desktop.

So you are basically able to use all of this prompt in one click in for example, Cloud Desktop or

whatever host you prefer, and you can simply type in date, title, and a transcript and make a

nice summary of it. This is the prompt that we include. Then we have this gitignore, you can simply

gitignore it. We have the python version. I use 3.12 for this project. Then we have the Cloud Desktop

convict file. It will look something like this. We have the MCP server. I call it calculator server.

Don't worry, the server can do more than just a calculator. We have the command, it's UV.

The argument is dash, dash directory, and it points of course in my folder on my local machine.

We have run python server.py in order to run it. We use dot dnv and we use UV project environment.vnv

because we use a virtual environment right here. Then we have the main dotpy. Here is not a lot of

stuff included to be honest. Then we have the projects dot toml. This gets also created automatically.

Then we have the readme and the readme is big and it's important. This readme is right now at this

minute structured for GitHub. But as soon as we create this, this will be structured for you so that

you can follow this. But of course you can also follow it from GitHub if you want. We call this

MCP multi-dool server. A comprehensive model context protocol server built with fast MCP

that provides calculator tools, document resources, and prompt templates. This server demonstrates

multi-blmcp capabilities including tools, resources, and prompts in a single implementation.

We have some features. We have basically a calculator. The calculator can do additions,

subtraction, multiplication, and division. We have the advanced math with power, square root,

and factional calculations. Then we have the utility functions with percentage calculations.

And we have the error handling divided by zero protection for example, and so on.

Then we have the document resources. Here we use the type script as the chaos resource.

And you can access this resource. We have dynamic file reading included and some error handling.

So this is the resource that we include. And then we have the prompt template that you already

understand. Then we have the quick start in this documentation. So basically what you need,

you need Python and UV. Here how you can install it, basically you can clone my GitHub repo.

The dependencies that you need to install, where all of this is hosted on your local host,

then some dual descriptions, something about the type script SDK, because you need it in the

documentation. This is nothing included inside of our folders right here. The output structures.

Then of course the path to my specific file, you need to change this for you.

Then the prompt template path, this should basically just work also for everybody that simply

copied this thing. The required files, here you see it, you need to place the type script.d

in the path that you want to access it. And the prompt template is already included.

Then the cloud desktop integrations, here are just some examples for Windows and Mac,

how you can simply include this. And here's an example with my code. Then you can restart cloud

and this thing should work and this is the stuff that is included. You can run it with the

MCB Inspector of course, don't worry, we will take a closer look at these. And then you should

basically test it. And of course you can add new tools if you want, with just add MCB tool and

include the stuff that you need. You can also include new resources with add MCB resource and

you can add new prompts with add MCB prompt. Here's some stuff about error handling and basically

that's it. And once again for the debugging with the MCB Inspector, it's always this to start your

server. Lastly, some API references if you want to dive deeper in the stuff that I have used here.

So we have a really really big documentation here and they'll go to read me. Then we go into the

server.py. So let's just take a look at the code. First we import some libraries. We use of course

the vast MCB. Then we include math because we use a calculator. We include OS. We need of course our

file system paths with this library and we import also DICT but this is optional. Then we create our

MCB server with fast MCB and we call it at this minute calculator server. You can call it whatever

you want. This thing can do more than just calculating. Then we need to define the path for the

resource and the path for the prompt template. The resources on my local machine and the prompt

template is inside of our project. Then we use the MCB resources in order to access our resource file.

Then we use the MCB prompt in order to access our prompt. And the important thing is here always

this description. This description is always really really important under the resource MCB.

Provide access to the TypeScript SDK MCB documentation. This resource contains the information about

the TypeScript SDK for MCB. So you need to describe exactly what this thing is doing. If you don't do

this exactly, your server will not know when to use this resource or when to use especially a tool.

Then the meeting summary, basically the same structure with a good description, a prompt template

for generating meeting summaries with the arguments, so meeting date, title and the transcript,

and then what it should return, then how to read it and so on. This is just some basic code here.

Then the MCB tool. This is also important. You always write MCB tool for every single tool. Then we

define the function and lastly the description. This description is always important. Add two numbers

together. Simple but precise. We use this tool to add two numbers together. Then the next tool,

we use this tool to subtract numbers for example. Then the next tool, multiply two numbers together.

The next tool, divide the first number by the second number. We need to be clear with this

description. So you see we have a lot of tools included. This is just for the purpose of a tutorial

so that you see that we can include more tools. But every single tool can be also an API call,

whatever you want. And so it goes on. We add all of these tools. And lastly you see this right here.

This is the last tool. We calculate percentages. We make the description. And after the last tool,

you see if name equals main, we use MCB run. And here we use STDIO as communication. You can also

use another transport way. If you simply type in transport equals, for example,

stringy mobile HDDB, boom, there we are. You can also use the streamable HDDB with the server

sentiment. But for the sake of this testing tutorials, we work with this right here. First,

you will see how you can change all of this up. And lastly, you have UV lock.

This whole server will also be published on GitHub with the whole documentation. And everything

will be included right here on this GitHub repo that I will link for you. So you also find the

server.py. Everything that I have showed you is also here on GitHub. You can also clone this GitHub

repo if you want. If coding is new for you, this will be most likely really, really hard for you

right now. But I promise we will do it slowly. If you are already a coder, I don't think that this

is hard for you. You will do this in your sleep. So right now, I do think that we should start

coding. So I see, of course, in the next video, we will do it as easy as possible. We will do

mostly white coding with cursor because I do think it's not 99.99. See you in the next one.