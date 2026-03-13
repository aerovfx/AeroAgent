# 7 -Connect your n8n MCP Server to Various Hosts Claude, Cursor, n8n, Windsurf translated

---

In this video, we will connect our MCB server of course with different clients.

We will connect it natively in an add-in, so we will create a client in an add-in and connect it.

We will also connect it to Cloud Desktop and we will connect it to Cursor.

You should understand that we can connect this MCB server in every single MCB client.

And of course, you can use Lovable, you can use Windsurf, you can use whatever you want.

Now the first thing that we do is of course, to come to our MCB server inside of an add-in.

And of course, you need to make sure that this thing is active.

And remember, as soon as you are in this hosted application,

you need to make sure that you do not show basically this URL, the production URL to other people.

Because if you do this, other people can access your MCB server.

This is really important. I will delete the server after this course is finished.

As soon as you want to talk to other clients, you need to create a config file.

And I have already created a config file, but first let's just connect this natively in an add-in.

So how can we do this? We can either create a new workflow,

but to make this a little bit cleaner, I just want to work inside of this workflow.

But this is not necessary. You can also create another workflow and talk to this workflow if you want to.

So the first thing that we do is right here, I use an AI agent, for example, and I press on it.

Only the AI agent of course, I need a trigger.

And I want to work with a chat trigger.

So we press on chat trigger and we need to connect this chat trigger on this AI agent.

It's now important that you understand that you can use different triggers in one workflow.

So you see we have one MCB trigger and one chat trigger,

but you cannot do this include another chat trigger here.

Because if you press on chat trigger, this thing will not get included.

But because one trigger is just the MCB server trigger, we can absolutely use a different trigger,

for example, the chat trigger.

Now we need to connect the AI model.

So we press on it and for the purpose of this tutorial, we simply use this OpenAI model

because I do think they work great.

If you have not connected this, please do this.

You can simply press here, create new credentials,

and here you need to insert your OpenAI API key.

Remember, you can come to OpenAI Playground, you press on it,

you already solve this in detail, then you simply come on dashboard,

API keys, create new key, you give it a generic name, create key, copy,

you come back into an add-in and you paste your API key here.

So just insert it, save, boom, then you are connected.

As soon as you are connected, you can use different AI models of course.

To make this really easy and simple and cheap, we use GPT 40 mini.

You already saw an open router that this is a model that a lot of people use.

And of course, if you do not want to work with the OpenAI API,

you can also delete this if you want and you can use a different model.

You can work with OpenRouter and here the same thing is true,

you need to create new credentials, throw the OpenRider API key in here.

Of course, I already have some credentials here, so I close it.

And here you can use all these different models that you want and you can also work with free models.

You will find for example, Gemini models that work completely for free.

This thing for example, Gemini 2.0 Flash Experimental Free works for free,

so you can work with whatever you want.

But I do think the OpenAI models are great, so I connect this OpenAI model with GPT 40 mini.

This is really cheap. Come on.

Then the next thing what we need to do is of course to create a client for the server.

So we press plus and we need to type in of course,

MC, let's just see, MCP client tool and you press on it.

And then you need the server send event endpoint.

And of course you get your server send event endpoint from this MCP server trigger.

You can simply press on it.

You can use the test URL if you are not active,

but because we are active and because we want to trigger this workflow later from outside,

we use the production URL and we copy this production URL.

Then you come to your MCP client and you insert your endpoint right here.

Authentification right now is none, don't worry, we will include authentication later.

And the tools to include, I just leave it at all, but you can also press on it,

go on the list and see for yourself if you just want to include Google Sheets or both Google

Sheets tools or the calculator. But like Adobe, I just want to use all right now.

So what we can do right now is we can add new context to Google Sheet and we can also see

what's in my context. It's really that easy.

And everything that you have to do is to simply press Open Chat and now you can talk

to your Google Sheets via MCP. I just want to ask for example to the mail of Arnie.

So what is the mail of Arnie from my leads?

And I send it out and most likely we will trigger our MCP server trigger and the server trigger

will tell me that the this right here is the mail from me and of course this is exactly right

because this is in my context. If you come back to an add-on, you see actually that you can not see

that our MCP server gets triggered in order to see this because we are in a production environment,

you need to come to executions. And in executions you see that basically everything should

go through. If you scroll out you see the MCP server trigger get executed and we use to the Google

Sheet tool and the Google Sheet tool was of course rate. To make this even better, you can name this

Google Sheet tools a little bit better. You can press on it and you call it for example Google Sheets

Rate, rename and this right here would be for example Google Sheets a Pant. This is important as soon as

you start to build bigger workflows and as soon as you need to make a system prompt but if you

work with smaller applications remember the best system prompt is no system prompt just give a

naming and as soon as your application starts to hallucinate you can come on these AI agents,

you press add options, you use a system message and here you can type in exactly what your

application should do remember the basics of prompt engineering but if it's not needed we just

leave it how it is. So you see we can read our tools and you can also see what we did right here.

Of course we started with the AI agent then we send the data request to open AI the input was

what is the mail from my leads then the output is just this JSON format you can see the JSON

format right here exactly then you can come to the MCP client and the client translates everything.

The client gets this input so it was the query tool the name was Google Sheets 1 the description

read update and write data to Google Sheets and so on and then the output was of course the response

in text and we get everything back and lastly our AI model structures are nice good answer for us

and basically the email address of Arnie is this right here so you see the MCP client and the MCP

server communicate really really great I simply type in what is the mail of Arnie from my leads

and because the output gets automatically structured from our MCP server into this perfect JSON format

the AI code is perfectly structured so we send it out and then we get everything back that we need

boom there we have it let's just see if I can add new leads for example add this to leads

Sarah Sarah at Sarah.com and then a random phone number I don't tell Chatsypt right now that

Sarah is the name or Sarah is the email or this is the phone number I think Chatsypt is smart enough

to figure this out automatically I just sent this out and with a relatively good high probability

we will call the MCP client you see it and MCP server will do all our work and it tells me the

lead Sarah has been successfully added name Sarah email Sarah at Sarah.com and the phone is this

right here and if I come into my Google sheets you can see that we have Sarah included right now

so it worked perfectly and lastly I just want to make one little test list every lead of me and then

I should get back from my MCP server like all these four names the others are just four but you get

the concept the name is Arnie male and telephone the name is Paul male and phone check male and

phone Sarah male and phone boom there we have it and right now it's of course really practical that we

can also communicate with other MCP clients and in order to do this we need to have a config file

and I will show you exactly how we can make this config file actually I already have created a

config file with Chatsypt and Chatsypt does a great way in explaining what we do of course we use

Chasing and it's the same structure as you already know we communicate with our MCP server it's of

course an add-on the command here is npx the arguments is dash y we use super get way and then you

need to include your n8n MCP trigger URL this is important this is dynamic you need to change this

later and then we close our brackets and then Chatsypt explains us every line step by step

MCP server this is the root key that holds all MCP server configurations think of it like a dictionary

where each key is a server name then n8n this defines one specific MCP server config named n8n it's

basically our n8n based MCP server of course we can also work with Python or cursor and so on but

for this server we work with n8n then the command is npx you already understand this we work with

no chs here tells the system to use npx command line tool to run the MCP client npx is used to

execute no chs packages without globally installing them you already understand this then the arguments

the arguments is of course once again the npx command and we use dash y dash y simply auto confirms

prompting during the execution dash y stands for yes to all prompts so that every prompt gets

executed and then sonner got away this is the name of the no chs package that we are executing

via npx in this context it's likely it's not likely it is see a like client wrapper of the MCP

trigger and then this is of course just a placeholder that you need to include so basically our code

looks exactly like this and where I have this placeholder you need to include your server trigger so

let's just delete this actually throw it aside then we come to the MCP server trigger we come on

the production URL we need to copy this until you see that we communicate with sse so with the server

send event so please just copy it insert it exactly here then save this file up then you can copy

this whole code and we can include this code in every client that you want first we come to cursor

on cursor we come of course once again so file preferences cursor settings this is basically where

we are right now then we come to mcb and we need to add a new global mcb server of course we

delete our old save your mcb server and we will include our n8n mcb server and we save it by

control less or you can also press file and save and then you can come back to cursor settings for

example or also to new chats or whatever you want and you see right now we have an n8n connected

but right now we have no tools available because we need most likely to press here refresh and boom

there we have it google sheets google sheets calculator so basically we have right now all of our

things and maybe you ask yourself why we call this once again google sheets google sheets and

calculator and not google sheets read google sheets append because I have forgotten to press save

so right now we press save and you will see that we can also update these by simply pressing

with refresh right here and boom now we have google sheets append google sheets read and the calculator

so right now we can call our mcb server for example what is 888 times 777 use mcb because I want to see

if we can also use our calculator do you see everything should work so I press run tool and our

calculator tells me that this is the answer and if I come into n8n on executions the newest execution

is this thing right here and you basically see that we used the calculator for this calculation now

let's just see if I can add new leads right here actually let's just do it this way so that we can

see it even clearer add him do leads Jamie his mail is Jamie at jme.com and the phone so remember

I say I tell phone and in my sheets it's telephone so I do think that also this thing is smart enough

to do this and the phone is a random number now I send it out cursor will ask me once again for

permission if everything is right so I press run tool and then our new lead should appear here in

Google sheets and boom there we are and now let's just ask for the lead that we have added previously

via n again so for example what is the phone of Sarah I send it out run tool phone of Sarah is this

number and of course it's exactly that number now let's just connect this with cloud desktop so we

open up cloud desktop of course we come on file settings developer edit config file on this cloud

desktop config file we open this up I have included our web search mcp so we can delete this you can

also insert new ones I insert my n8n mcp server and I save this and you see we communicate always

with the server sent event so boom there we have it we can close this down then of course we need

to restart cloud so quit I want to open cloud once again I make it a tiny bit smaller so that we

can see it a bit better then we can press on this thing down here and you also see it here we have

an 8n and we can do Google sheet the pen Google sheet rate and the calculator is excluded but of

course you can include it if you want but we do not really need it but I want to talk to my leads for

example so let's just add a lead one last time so that you understand that everything works in

conjunction add to leads codey the number s this right here and the mail codey at codey.com and I

send it out we will allow this always so that we can communicate every single time with our mcp

server right now and boom codey is added to my google sheets to my lead list I hope you understand

the power if we create a server for ourselves via nn it's really easy we can connect a lot of

different tools the server is easy to maintain we can communicate via sse via the server sent

event and we can connect every single client that we want see of course in the next video as soon

as we start to make this bigger as soon as we start to make this even more awesome