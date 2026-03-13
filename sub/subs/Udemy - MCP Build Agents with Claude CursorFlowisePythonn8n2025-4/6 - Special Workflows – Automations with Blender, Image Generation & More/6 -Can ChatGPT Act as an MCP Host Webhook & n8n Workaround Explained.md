# 6 -Can ChatGPT Act as an MCP Host Webhook & n8n Workaround Explained translated

---

I got the question all the time. Can I use chatgbd as host for the model context protocol?

Generally speaking, I do think that they will include everything. Right now they have included

something. So we can basically use the model context protocol also with, for example, the

research. How all of this is working. First, if you come into the open a playground,

you already know that you can simply press plus you can include MCB server, and here you can

connect to the pre-programmed MCB servers or you add press new, and you can give the simple

URL, the label, and an API key. But of course, none of this works with these normal convict files.

So chatgbd or open a UI in general right now has not like every single thing perfectly set up

for this. If you want to work with chatgbd, you can press here on the right side, then you come

to set things. And on settings, generally speaking, you already have a lot of settings. You can

take a closer look for yourself. This is not the specific chatgbd course, but you have to come to

connectors and on these connectors, you can connect different things via the model context protocol.

Like box, Google Calendar, Hapspot, Gmail, and so on. I do think that here the model context protocol

will work in the background. Some people also get the button, add new connectors, and then you can

press on it and you can also try to include a URL to a model context protocol like the SAPIR URL.

But none of this is perfect. Unfortunately, you cannot just simply add a convict file and then

you are ready to rock and use chatgbd as a host for your MCB servers. But none or less, I want to

show you a workaround. Before I tell you the workaround, I need to tell you also that it's probably

not needed. I do think the sooner or later, also chatgbd and open a iBEL include this model

context protocol like RELA really easy. So maybe as soon as you see this course, this workaround

is no longer needed. So always keep an eye on the settings and here most likely the button

connectors will still be there. So you can simply browse for HC for yourself if you get something or not.

If you get nothing, of course you can create for example a GPT and then you can connect with this

GPT VR webhook. So what you can do is for example to come on GPT's, then you come on create.

And here you can give this finger name. I just call it test. Also here test. Then the instruction

calls are NA then workflow for example. And what we need to do right now is to press add actions.

And on these actions we have here a schema and we can include different things. What we want to

have is a blank template and we will use this blank template in order to call our NA then MCB

server. So we would simply copy this schema. Then we can open up for example a new chatgbd interface

with a new chat and we will tell something like this. I have this example. Then we include the example.

I need to call an a then workflow via a webhook. Here is the URL that I need to call with a HDDP

post request. And now we need to come into an add-in and build a workflow of course.

So we can for example into an add-in we create a workflow attention. This is right now not

time Cb server. We need to make a workaround. We press plus and what we want to use is we need to

use a webhook. On this webhook we need to come to this production URL but first let's just save it.

Maybe also publish it. As soon as this is public you can work for example with this production

URL. In order to test this out you can also make it not public and work for example with the test

the URL. The method right now is not get but post so we copy the URL then we come back into chatgbd

and we also insert the URL right here. And I also want to tell chatgbd maybe something like this.

I want to send out a prompt. Give me the code and send. Right now I have my schema. We will send a

bolster request to an add-in webhook and it is a prompt that we send. So you can also see it here

open a i3.1.0 info the title is add-in webhook trigger the description sends a prompt to an add-in

workflow and so on. Then we need to trigger the URL and the webhook is this test webhook.

Summarize and prompt to add-in webhook I do think this looks fine so we can simply copy these.

Then we come back to our gbd we delete everything and we include this thing right here and see if

this is working or not. This thing tells me that I don't have the post request inside of an add-in.

Let's just actually copy these. Throw it into chatgbd because I do not want to debug. Right now this

thing includes the operation ID copy. Include and boom right now this thing should work. So what we

want to do right now is to simply press create. This is only for me. This is important so you

cannot publish these or share this with other people. We press save view gbd. Now we come into our

webhook here and I press execute workflow and we wait for a trigger. Send this to an add-in test

I send it out. It asks me if I want to connect and I prompt this test so I confirm the message will

successfully send it and if I come back to an add-in boom there you see it we send that this thing

right now out. The next thing that we need to do is we need to add a ii agent. So we add this a

ii agent and on this agent of course we trigger with this thing right here. So this is important.

Here the prompt that we use comes from our webhook. So you need to press on this divine below and

then on the left side I need to search the test event that came through. Here is the prompt test.

This is an dynamic variable so I can simply include it right here and boom. Then we need to have

an ai model and for a ZikaFd tutorial we'll use gbd for our own mini and what we can do right now is

we can trigger from chatgbd this is a ii agent and this is a ii agent can also answer back for

example to chatgbd. If it should answer back we need to include once again our webhook. So

respond to webhook. This time we use the first incoming item but here on this first webhook we don't

want to respond immediately we need to respond using respond to webhook node. So this means that we

send the request to this webhook then our aia agent will simply work with the query and then the

response to webhook tool will answer back into chatgbd. So I hope this makes sense and how can we

connect right now our mcp server maybe you guessed it right with these tools so you can press on

tools and here of course we use our mcp clyentool and this clyentool we can connect this of course

to our mcp server. So if we come back on personal let's just save this. We can use of course this

gigantic workflow that we want to connect but in order to just make this really easy and really

I want to connect to this trigger just to see if we can trigger our workflow that generates

pictures. So I press on these then we come to this production URL. We copied a production URL

we need to make sure that this thing is public we come back on personal in our workflow

in this workflow on this mcp clyent we insert this thing down here and then we should be basically

ready. What we need to do right now is to press execute workflow in order to wait for our test

then we come back into chatch ept and I ask chatch ept create a pick of a office use an add-on for example

so that the alie doesn't work because I don't know if I have included the alie in this interface

of course this is not a practical workflow because we can already use the picture generation from

chatch ept but if you have for example a vector database and the vector database uses for example

a lot of different hosts you can also connect with chatch ept with such a workflow. Let's just come

into an add-on you see in an add-on our workflow works the a.i. agent calls the mcp clyent tool and

the client triggers of course the server the server will generate our picture and then the a.i.e agent

dogs backs to chatch ept so basically what we got is I at least I hope so if we come on personal

let's just save this on our mcp picture generation then on executions you see that an execution

came through we triggered a server the server triggers once again another workflow this other

workflow is the picture narrator mcp and here on executions you can see that execution came through

and inside of google drive boom there it is we have our picture of our office so this works

yeah I get it like these are some clicks but if you want to connect an mcp server to chatch ept

this is at least how I see it the only way how you can do it relatively nice and I also have to tell

you maybe this is not really necessary because I think the chatch ept will also include the mcp

server natively so that you can just add a config file at least I hope that they do it if they don't

do it you need to work with such a workaround everything that you have to do is to come to chatch ept

just as a quick summary come on gpt's create one here on these actions you use a blank template

and you need to connect such an agent that uses web hooks on this agent you can use a client this

client will talk to your server and then you are done if you already have for example a big mcp

server and you need to connect this to chatch ept because like you have some vector databases or

something similar included and you need to make sure that you can connect with this vector databases

because you want to work in conjunction with chatch ept with cloud with cursor with whatever host

you want then I do think that this could be a workflow that is relatively nice to use yes a

little bit painful to setup but like you see I do think in 10 minutes you can absolutely do it