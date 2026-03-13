# 5 -n8n Basics Triggers, Actions, Nodes, Models, MCP and More translated

---

Before we can create our MCP servers and our MCP clients, use the community notes and do a lot of

fancy stuff inside of an event and you need to understand the basics. Of course, if you are really

advanced, you can build stuff out that looks something like this. But you will be intimidated,

as soon as you see a workflow like this if you do not understand the basics. So we need to

understand the basics before we build out bigger workflows and before we can use the model context

protocol inside of an event. So you come back conversional and then you press create workflow

and then you are most likely into empty canvas and in this empty canvas you need a trigger.

So you can press on it and you can add whatever trigger you want. Let's just use this manual

trigger. Now first, how this chain really works. If we come back for example into this thing right here

so that we can paint a little bit like little children, in an event we always have like at minimum

two steps. We always have step one and step one is always a trigger and step two, step two is always

an action. Now what do I mean by this? A trigger can be whatever. It can be a chat trigger. It can

be a manual clicking. It can be a non-form submission. It even can be something from ads. So this

trigger can be whatever you want. It can be a mail. It can be a Google sheet. It can be whatever you

can think of. And as soon as this trigger occurs, some kind of action should occur.

So let's just say as soon as a mail comes in, an action should occur and the action could for

example be that you want to answer to this mail. Or most likely if you want to build the

rack applications, an action could be for example a Google trigger and let's just say Google

Drive as soon as you upload something into Google Drive. The action that you want to create should

be for example that the stuff from Google Drive will get stored automatically in a bind-con vector

database as action. And if we talk about the rack chat, but so this is for example for

absurding stuff in a vector database. If we talk about rack applications, we would for example

have of course a chat trigger. The chat trigger would for example trigger then the action

and the action would be for example an AI agent with rack. So you always need to have some sort

of trigger and some sort of action will occur. You also have the possibility to make your trigger

that is immediately a MCP server. So also MCP server can be a trigger. But then of course we need to

trigger this MCP servers either from an add-in with a client note or from outside with for example

cloud desktop cursor, wind serve, lovable or whatever. So if you use a trigger inside of an

add-in that is a MCP server where we need to trigger this trigger note from outside either from an add-in

or from a different host. And if you are here in add-in you see that you have for example this thing

as a trigger and if you press on it so test workflow you see that this trigger got right now executed.

So this thing will always get executed as soon as you click. But of course you have a lot more.

You have their own app events. And here you have a gigantic amount of things that you can include.

You can include air table. So you can for example trigger something as soon as a new air table event occurs.

If you work with AWS congratulations you can also trigger out from AWS. You can also trigger out

from box, from bubble. You can use a normal chat trigger so this chat trigger is really easy.

As soon as you type in something here you see you can simply trigger via chat

similarly than in low wise. You can trigger via click up.

Coin get go if you are a crypto guy. Depot. Draft Dropbox. You can use different email triggers.

You can use Facebook leads at the trigger or generally Facebook so everything on Facebook also

Instagram stuff. Get get tap, get lap. Google ads or Google analytics. The Google calendar could

also be a trigger. Google docs, Google Drive and Google sheets. These are triggers that I love.

We will work with Google Drive. And basically you see that you can trigger with nearly everything

that you can think of. And you can also trigger with different HTTP request notes more on that later.

You can also trigger with Shopify if you have an online store with super base with Stripe really with

whatever you want. Besides that you have a on-scatchered trigger. And if you press on on-scatchered,

of course you can schedule the triggers. Let's just say you want to have that every single hour

this thing gets executed. Or let's just say every single second this should get executed.

You can come down to one second and this trigger will trigger actually every single second

or every minute or every day. Every day at midnight or 1 a.m. or whatever you want.

If you use this for example you need to make sure that you come here on settings this is really important.

You press on settings and you need to make sure that you are on your right time zone. So if you

work with time triggers you need to make sure that you work with the right time zones.

Besides this scheduled trigger you can use more like you guessed it. What you can also use is on

webhook call. Now what the hell is this? It looks something like this and this on webhook call

is something really cool and we need to talk about this later because we can also

talk to this application via other applications. This is a webhook and we can include this webhook

for example into jcpd or into flowwise and we can trigger this action or this workflow that is

behind this trigger from other applications. This is a powerful, powerful trigger. You can

basically connect whatever you want. You can use a non-form submission. So people or you can simply

type in different stuff and then this thing gets triggered. You can also use when executed by another

workflow. This is also relatively cool. I want to give you a brief overview just as you know what

you are getting into. If we come to personal ones again you can see for example this workflow

and here we have for example this gmail tool and this gmail tool triggers the sub workflow

mails. So it's basically this workflow. So you can trigger from one agent this agent. This is a

sub agent that works behind this other agent. I know it's a little bit confusing. Right now don't

worry we will get into all of this. Let's just delete this thing right now once again. I just

want to give you a broad overview. Then of course on chat message so this is your simple chat trigger.

You already know it and lastly you also have other ways. You can use email trigger, error trigger,

mcp server trigger and it end and also the sse trigger. So you basically see you have a lot of

different triggers. Now once again let's just press at first step and we use for example the

own chat message. As soon as you have found the right note that you want to use. Of course you

can give this a name. Let's just say test and of course you should press save so that this thing

gets not deleted if you are not careful. Then besides this you have here the editor and the executions

and here on these executions you will always find the executions that you have made. Previously we

have executed like this tiny thing here but later as soon as you execute more and more and more

things of course you can monitor this here and if you come to the editor you can actually edit

this thing. And of course if you want to send this adactive you can press right here, press got it

and then this thing is active also for other people but for testing purpose you will always have

this ad inactive. Then the next thing as soon as you have a trigger of course an action needs to

occur right now with trigger via chat and something that you can use for example as an action is for

example an AI agent. If we simply press on AI agent I know this is really really simple right now.

You can see for yourself that we will trigger this AI agent with this chat so you can always see

the stuff that is right here in it. Source for prompt the user prompt it's the connected chat

trigger note. And the prompt user is this format that comes here through and we do not want to have

any specific output it's relatively easy to understand but every time as soon as something is

right and as soon as you see these red stars similarly then into flow wise you need to connect stuff

and of course you know it on the AI agent note you need to connect that chat model so you press

actually plus we will connect for example the open AI chat model you can also use open router or

whatever you simply connect your credentials from open AI so make your open AI API key I hope that

you understand how to do this you can simply use it and then you can use a model from the list I

just used GPT4 or Mini for this generic test and now our trigger is chat and our action is this AI

agent and this AI agent will do the stuff that we typing in of course in this thing here so if we

simply type in hey of course this AI agent will get triggered and it will simply talk back to us

just like an ordinary agent but you need to understand that you can also trigger this agent via mail

so as soon as if you get the mail for example an agent could go on with this workflow and lastly of

course you can also connect other stuff also here you can connect for example Gmail for example

send message so you can also send messages right here into Gmail you can also trigger via mail

an agent writes and then send messages you can also press on tools and on these tools you can

also connect like for example a Gmail tool and also here you can use the operation send and a lot

more so please this thing is really really gigantic you can do a lot and you also see memory can

use a simple memory for example and this will be a really really simple agent and on every single

note that you see here you can always zoom in and you can see for yourself that you can press play

on this first button you can press here in order to activate it or this activate it you can

delete it and you can also press on these three dots you can open it you can press test step you

can rename it you can deactivate it sometimes you can pin you can copy it you can tie the up your

workflow you can select all and you can clear your selection and you always see here the shortcuts

that you can use and this works basically on every single note you can also copy all of this for

example and then throw this once again down here the only thing that the did not work here is we

cannot use twice the same chat trigger and one single workflow but if you came in a new workflow of

course you can include all of this and now I want to show you what's going on under the hood if we

press open chat once again and I just type in hey for example you can see how your data flows to

different stuff if I close this down you can always press on this first note and here on the left

side you see what's happening so right now make chat publicly available I will talk about this

later but what was the output of this note the output was a session ID the action was sent message

and the chat input was hey and then you can also see here on the right side that it got into the

agent so you can press on this agent and also here you see on the left side the input in the

middle is the AI agent and on the right side the output so on the first note we have here basically

the input and the output if you go on we have the input we have the agent note and we have the

and you see what was basically the input to our agent the input was the prompt user message and

the prompt user message is right here chasen.chat input and you see here it's basically exactly this

chat input this is always a variable so basically this variable is just here for all then we can also

map this manually later and because I sent here hey of course the AI agent will talk back to me

and the output is right now of course hello how can I assist you today here on the left side on

this input you can also always come to table and you can also see this chates and format and it

then always communicates basically with a chates and format and in the middle ground you will always

find this note you can also come to settings and if you come up a parameter is most likely you will

find add options and you can add system messages just like you know and lastly on the right side you

find the output and also the output here you find the schema and you can map this schema later you will

find a table and you will find the chasen and basically and I then always communicates with this

chasen and if you press on locks you can also see exactly how this chasen was processed it's relatively

easy to understand as soon as you get it but I completely understand that maybe it's a little

bit much right now because we can always work with these things like however we want if you both

for example delete this chat flow here for a brief moment and you use for example another trigger

let's just say the on-form submission and on the on-form submission you can use for example the

form title and then the form description and then here you can also add a little bit of stuff with

the placeholders and so on and then you can press test step you see that you can add the and

on-form submission you can press submit and then this data also flows relatively similarly

on also this data needs to get processed for example into the AI agent so if you press test

workflow once again for example and we submit this this data will come through and right now it will

not work because here on these parameters we have the user prompt is chat input and if you come

to the schema right now we have this form mode so you will most likely press here on defined below

and here you can come to expression and throw this stuff right here in and if you press the step

right now we have the input and we have also the output and if you come on the output it looks like

you're testing the functionality and so on because this was of course just a test so you can simply

see for yourself how this data flows for right now it's not that important I will show you in every

single video how you can do this step by step but I want that you understand that you can map every

single data point here manually one last time I just want to delete this and I add once again the

on chat message and as soon as we have added the on chat message of course we need not only defined

this below we can for example connect chat trigger node and we have once again the input and if we

open this backup and type in hey of course our data will also flow once again perfectly through it

and if you come on executions you can always see the executions that got through and also the

executions that they did not get through you see here that we had for example an error because the

own forms of mission was not right and right now everything seems to work perfectly if we come

back once again in this editor you saw already that we can come to this message and we can also make

this chat publicly available and here we have the chat URL and the mode is for example a host that

chat without any outendification more on that of course later as soon as we host these applications

but if you want to use this as a standalone application you can totally do this and in order to

see how all of this is looking you can simply copy this URL and you will throw this for example in

I am to browser and right now it is not working and I have to tell you why it's not working

it's not working because this chat flow is right now inactive if you want to access this of course

it needs to be active so got it then you need to save this stuff it is saved up right now

then we come back once again then you can copy this chat URL once again and if you throw it in right now

you will have an interface that you can chat with and here you have like the welcome message my name

is not an answer one and of course you can make this a little bit nicer looking but we need to talk

about this later as soon as we talk about the hosting right now it makes no sense because

generally speaking in this video I just wanted to show you some basics here you need to remember

what we need to have in an add-in always we always need to have first a trigger and second an action

that needs to occur the trigger can be anything it can be Gmail Google Sheets chat input on forms

of mission every single app that you can think of and also the action can be basically whatever

you want you can map your stuff manually it can be an AI agent but also the action can be whatever

you want and these are right now just some basics you can also add tools memory and a lot more

and please don't be sad if you do not understand it yet this will make more sense over the next

video I promise and especially if we work with MCPs this MCP server trigger is a note that is

really really easy to work with because you can simply communicate to this note until you can

throw some tools on it on the other hand if you work for example with an AI agent and you

type in this agent and here on tools you can also add MCP if you type in MCP you see that we can

use the MCP client tool so this is how you can make a client and the other thing was of course

a MCP server so you can create MCP server and MCP clients in one workflow and these two things can

also communicate with each other our trigger would be a for example chat then the AI agent would

do the heavy lifting for us it will call the client and then the client could communicate with the

server but this server can also be connected to ever a single other client that you want that's

the beauty of an 8n and don't worry if you don't understand it yet as soon as we build out this

application it will get clearer and clearer with ever a single video but you need to have a nice

overview before you start with this tool