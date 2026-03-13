# 7 -Add Prompt Templates Using the modelcontextprotocol Python SDK translated

---

In this video we will include a prompt template inside of our MCB server.

Before we do this, I want to recommend you to save your things up.

Because we already have a server up and running that can use a lot of different tools for our calculator,

it can also use the resources. And that's why I do think it makes sense to make a small backup.

The easiest thing to make a backup is to simply close down cursor.

Then you copy this file from your server and do insert it once again on your desktop.

Boom! Right now you have a copy of these, so if you mess something up, you can always come back to this copy and work with this copy later.

So this is the easiest thing here to make a small little backup.

Let's just assume that you mess up something and you are not like the best one in coding to fix it immediately.

It's always nice to have a backup. So what we want to do right now is to include a prompt template.

If we come into this documentation, you see that we can include prompts of course.

And prompts are designed to be user controlled, meaning they are exposed from the server to clients

with the intention of the user being able to explicitly select them for use.

A small overview, they can and probably should, except dynamic arguments.

If not, it makes no sense. They should include context from resources.

You can chain multiple interactions if you want.

You can guide specific workflows and you can surface as UI elements, like slash commands.

The prompting structure should be something like this.

Clients can discover available prompts through prompt slash list.

On your endpoint it will look something like this.

Then they can of course use the prompts by prompt slash get.

You should include dynamic prompts at least that's the thing that we will do.

Because it's a lot nicer to have dynamic prompts and of course clients can use it.

So also you can use it.

And if you really want to dive deeper you can also include multi-step workflows.

I don't think if this is really necessary but you can play with it a little bit.

You can do it in Python or TypeScript.

We will work with Python because our server is already in Python.

And here of course you get a lot of examples.

The best practices, use clear descriptive prompt names,

provide detailed descriptions for prompts and arguments,

validate all required arguments, handle missing arguments gracefully,

consider versioning for prompt templates, change dynamic content when appropriate,

cache dynamic content when appropriate, implement error handling,

document expected argument formats, consider prompt compatibility,

and test prompts with various inputs.

Then some UI integrations.

We will simply use this in cloud desktop it will be really easy.

Servers can also notify clients about prompt changes if you host a server for example.

And lastly of course the security considerations you always need to read

is for yourself. I am absolutely not your lawyer.

If you just work locally like we do right now, no problem.

The first thing that we need is of course a prompt.

And you should be smart and write your own prompt so that you can specify the prompt

like really really nailed down for the stuff that you need.

You should think for yourself.

Whether the prompts that you are always using and what are the dynamic variables that you

want to exchange all the time.

To make it easy and simple I just run with an example that I have found on GitHub.

The example that I have found on GitHub is this MCP prompt templates.

This is a server that only has 10 stars so this has not a lot of love but I do think this is a

great server. You also have the server.py but we don't need the server.py.

Everything that we need is to be honest just the prompts from this file.

Leave him a little bit of love, give him a star if you want because I think his templates

are relatively good. You can press on this template.

Then you see that we have three different prompt templates here.

Meeting analyzes, meeting summary and webinar block.

And if you press for example on meeting analyzes you see that you get the template.tmd.

So this is a markdown file and you see how this thing is structured.

It's called meeting analyzes template and then the prompt basically starts.

You are an executive assistant working for a global infrastructure consultancy.

Your task is to analyze the following meeting transcript with exponential attention to detail

and organization skills. This is the role promptings of the start with our role.

Then the meeting information here is the date and the date is the first dynamic variable.

Every time as soon as you see two curly brackets this is a dynamic variable.

Then the title once again another dynamic variable and then the transcript once again another

dynamic variable and then the prompt goes on. Please provide a comprehensive analyzing using

the following structure and then it's just the structure how we would analyze basically this meeting.

So you see you can simply type in date title and the transcript from the meeting and then you get

an analyzes. If you come back you can see the same thing for the summary or also for our webinar

I just want to include the meeting summary. We come to this template because I do think this is

a nice structure. Here we basically have the same structure we start with our role.

Then we give the dynamic variables and then we tell in the prompt exactly what we want to do.

So I do think this is really nicely structured and what we do right now is we can simply copy

this URL or you can also of course download this and save it on your machine.

But let's just see if cursor is actually smart enough to do this for us.

I come in cursor and I tell cursor something like this. I want to include a prompt template

in my server. Use the info from at docs.mcb.vola.lem to implement it. Include this prompt and then I

send this out. So let's just see if this thing is actually smart enough to see how all of this

is working. I don't think that I like this. So we will not accept this. So reject actually.

This was not perfectly set up. Restore checkpoint. We need to do it a little bit different.

For example, here is a link to get up. Download the MD file and include it in the server.

Let's just see what we get right now. This is also why we make backups because if we have some

problems this is like really a mess. Right now it seems to be a little bit better. So you see we

should add basically our markdown file right here. So meeting summary.md and then the server.py

gets also some small updates. Let's just see. I do think this is right now a lot nicer.

So you see here on the left side we have these templates and on these templates we have meeting

summary and this is right now the prompt and this is exactly the prompt that we use. So we accept this

file. Then we need to come in the server.py. So here server.py and we have added a few lines.

To find the path to the resource file, accept template file path comes to

direct-renaing template meeting summary. Yes, it's fine. Then we scroll down. Then we need to use

mcp.resource and of course also this is not right. We need to use mcp.prompt and not mcp.resource.

But nonetheless let's just work with this just for a tiny bit and come later into the inspector

and see if we get these under resources and not under prompts. Small little spoiler I do think

that we get these under resources and not under prompts. But I want to leave this stuff

purposely in this video so that you see that LLM scan making mistakes especially if you do not

communicate clearly enough. Prompt meeting summary provides access to the meeting summary prompt

template. This resource contains and so on. This seems to be fine. If we come in the server.py

from gettap you basically see that here we use the server list prompts and the server get prompts.

This would be to be honest a better structure. But let's just run with this and see if this is

working or not. So we accept first it's not really a resource but let's just accept it and see

if this thing is working or not. I do think that the rest should be fine so we have accepted everything.

So right now we come into the MCB inspector and see if we have prompts included or not. Because I

do think this can make some mistakes. This is why we saved the stuff from previously. If we come

right here let's just say restart. Resources let's just clear it. List resources. Here you see

get typescript resources and get meeting summary template. So you see this can make basically also

some problems. If we come up prompts, list prompts, you see that we don't have any prompts here

included. So we have it here on resources and I don't think that this is the right thing to do.

Inside of cloud we have the meeting summary and you see it if you press on it like the dynamic

variables they do not work. So I don't think this is right. We need to rework with these. This is

why we do have MCB inspector. I do think we need to do it different. Cursor will mess this up.

So we do it the old way. We copy this file. We come to in our project. Here we can come into templates.

We delete everything from right here and here I want to include a new file. So new let's just call

it text file prompt.md for example. We open it and here we do include this meeting summary template.

And we save it. We close it. We copy the path. We come back into cursor. Here is the path to my prompt.

And now I send it out. Let's just see what we are doing. We update the server.py. Right now I do

think it looks a lot more promising. Here on the left side you can actually see that under templates

we have the prompt.md and on this prompt.md we have actually the real prompt. So the meeting

information with our dynamic variables seems to be perfect. Right now we also update the code.

So let's just actually see what we got here. In the server.py we have some updates. So we come to

server.py with start here import the dictand list except this is fine. Then the prompt template path.

This is fine. Yes. Then mcp list prompts. Then the mcp execute prompts. And this right here is one

last time a small little mess up. We do not really need mcp list and execute. We can simply do this

via mcp.prompt. But let's just work with this and fix it with one last iteration later. And then

the mcp tools are once again correct. I do think most of it seems to be fine but I'm not really sure

if we really need the list prompt and they get prompt. Let's just actually fix it. Just a tiny bit.

I do think that just add mcp prompt would be enough. Fix the server a bit. I do think

list and execute is not needed only the mcp.prompt should work. Take a look at the documentation for

the model context protocol and we send it out. This thing is optional. Let's just accept it. This is

fine. Then the list prompt we can delete it. And then only the mcp prompt. Yeah, I do think this

is promising. So accept arguments accept also here accept. I do think this looks promising right now.

Let's just come into the mcp inspector connect on resources. Let's just list them. Now we have

our typescript SDK once again. Then on prompts list prompts meeting summary and boom. And there we

have it. The meeting summary we can enter a meeting date. A random date. Then we can enter a

meeting title a random title. We can enter the transcript a random transcript model and

temperatures. We can even include a little bit more. Actually, I do think that our server is perfect.

Let's just come on tools to see if the tools are not missing right now. No, we have everything.

So what we want to do is to restart clot and test the prompt out. So quit clot restart clot.

Let's just test the calculator. What is 666 times 555. We send it out. Calculator is still fine.

TypeScript SDK is still fine. And now our meeting summary we have our dynamic prompt.

The meeting date. Let's just actually use a random date. 13th June 2025.

Title. Let's just call it Q2. Then a transcript. I just use a random one. I just made something

if with chatybd we start with the participants. Zera, Jake, Lena and so on. Then Zera tells some

things that Jake tells some things like and a lot more. So we can simply copy all of this.

Then we come into clot and we insert our transcript. Then the model. We do not really need to include

the model and also the temperature. We do not really need to include one because here simply

works clot. That's the. So let's just use a random model. Cloud, temperature, would be for example

0.7 at prompt. Let's just press on this prompt. Meeting summary template as an executive assistant

and so on. Meeting information date. Title. Then the transcript. Please provide a brief summary.

So the overview. What was the purpose key participants main topics covered and so on.

So actually let's just send this out. I do think this is completely fine. So we can close this

and we can simply send this out. Then you can make summaries of your meetings all day long.

And of course, especially if your meeting is longer, this could be really, really practical.

Q2 meeting summary of June 13th, 2025. The overview, the meeting purpose was quarterly.

Think to review Q1 achievements and Q2 projectories. The key participants are Sarah,

Jake, Lena and so on. So here you see Sarah, Jake, Lena and so on. And they talk about Q2 strategy.

This is basically the stuff that they are talking about. I'm convinced that Cloud made a good summary.

And this is basically everything that you need. It's really that easy. You can simply press

right now on your server. Use the meeting summary and you can simply type in the stuff that you need.

If you don't want to have modeling temperature, of course, you can also delete it from your server.

Let's just actually do this because these two things are not needed for our prompt template.

So if we come back into our file, modeling temperature, this is actually from the code and not really

from the prompt. So we can also delete these two things right here. But you can do as for example,

you can copy some lines if you don't really understand what you are doing, of course. Control,

K, we should delete model and temperate. Except so this should be fine. Then if we scroll down,

actually we have the arguments and also in the arguments we have model and temperature. So let's

just delete these two arguments. Of course, you can also do it with cursor if you are not familiar with

these. I just save it right now. Let's just come back into our model context protocol. That's

there. We restart it. So connect clear list. Be present. Boom. Enter meeting date, meeting

title and enter transcript. And if we restart cloud desktop quit open. Let's just see meeting

summary date, title, transcript. Boom. Our server works. Congratulations. You have included a prompt

template inside of your mcb server. I know it was a little bit messy. This is the thing with

wipe coding. This things can sometimes mess up. But of course, if you know just a little bit what

you are doing, you can fix it relatively fast. And if you don't know nothing, please do the

thing that I told you at the beginning of this video. Copy your file, throw it on your machine,

and then you can work with the old one if the new one gets completely messed up. But normally,

you should be able to fix it if you simply come back and restart once again with the code.

So basically everything that we had to do was to download this file, include it into our project,

and then tell cursor exactly what it needs to do. It needs to add the prompt and it should not

use the list and execute tool. It should just use the mcb.prom command and then all of it worked.

List and execute is only necessary if you include a lot of prompts. So you can mess with this yourself

if you want to include a lot of prompts. I do think that we have right now a really powerful server

that includes tools, prompts, and resources. And I see you of course in the next one.