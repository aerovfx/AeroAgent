# 7 -Flowise AI Agents V2 with MCP translated

---

In this video I wanted to talk about the agent flows and more specifically the agent flows version 2.

Now in FlowWise we have version 1 and version 2 and version 2 is a little bit of the newer technology.

If you do not have this button of course you need to update your FlowWise instance.

If you work locally you already know how to do it and if you are a cloud host that you should also

be able to update your FlowWise instance. And I have to tell you everything from version 1 still works.

So you can press that new on version 1 and do every single thing with this normal workflows from version 1.

But now first let's just come on version 2 and see how this thing is looking because I do think this is great.

But still also version 1 works great. So you can press that new and then you are in an interface just like this.

This looks relatively similar to an add-on. On the left side you have still this plus button and you can

include a few different notes. We will take a look at every single note in this video. We will make an

overview of what these notes can do and we will create our workflow. Before we do this I want to show

you this button right here. This is basically the AI button. So you can simply press on this button and

here you can type in what you want to create. It's really that easy. And you also get some examples.

Generate response to user queries and send it to Slack. So if you press on these basically the AI

from FlowWise will generate our workflow. Everything that you have to do is to use a chat model.

Let's just say you want to work with the OpenAI model so you can simply press on it. You can also

use OpenRouter. You can use whatever. You need to connect of course to your credentials from OpenAI.

I just want to press on this FlowWise MCP credentials that I have created. And of course it will also

take a close a look at the model context protocol because the model context protocol is included in

this version too. Then you give the model name the temperature. If you want to include streaming

the max. The Oconsensor one but I just leave it at the default settings here. But you can take

a closer look if you want to make something special here. Then we press generate and basically right

now FlowWise will do its work. We'll do all the heavy lifting and then we have our workflow that

is finished. We just have to connect to maybe I keys and you see this is also relatively fast.

As soon as your workflow is created you can simply take a closer look what's included. We always

start with a start note. So if you press on it you see you can start either with chat input or of

course with a form input. Then you have the generate response and here we can simply connect an AI

model, use whatever you want and connect your credentials. You can also give an input message so

a system prompt and maybe also some structure or output if you want and then we use the send to

Slack. If you press on these basically you see that we use the Slack MCP. So here we use a tool

and it works over the model context protocol. So we can send messages to Slack thanks to the

inclusion of the model context protocol. Of course here you need to connect your credentials to Slack

but first I have to tell you that I don't really love this tool. Sometimes it can make mistakes

so what I am recommending you to do is to play with this a little bit and if it will not work of course

we would start from scratch so you can simply delete this. The thing that you always need in order

to start the workflow is of course the start note. So let's just take a closer look at these.

If you press on it here you can see that you can use this chat input or of form input. If you use

of form input of course it needs to give this form a title. For example please fill this out. Then

the description do you have a job for example. Then the form input types you can press on it.

It can be string number boolean or options. If you use options you can give a label and the

variable name and if you use string you can still give label and name and of course you can add

once again some input types and also here you can use string with label and variable name. So let's

just use option for example or actually let's just do it this way the form description. Job check

king then the form input type. We use here options. Then the label let's just make it also a question.

Do you have a job for example. Then the variable name let's just call it job and then add options.

So option one would be of course. Yes. Add option two would be of course. No. So yes this is a stupid

example. I just want to show you how this forms work generally speaking. If you press safe right now

of course we gifted the name. Let's just call it V2 test. We save it and if you press right now here

you see that you get this form input. Please fill this out. Job checking do you have a job. You can

press on it. Yes or no. And if you have a job you can simply submit it and boom there we are.

And then of course later you could trigger right now your workflow for people that do have a job

if you publish this application for example and the other route but for example talk to people that

don't have a job. And in order to do that you would press plus for example and use the second one

for example a condition with the zip files. You can simply connect this and then you can use

as the condition value one yes and value two no and then you can simply split out two different

ways. In one way you would use an LLM that talks specifically to people that have a job and in

the other way you would talk to people that don't have a job. Like I said this is just an explanation.

Let's just take a closer look at every single note so that you understand what's going on.

Like I told you we always start with the start note. So this is the first note and normally we use

this chat input. And if you use this chat input and you save you have this chat right here. So you

can chat normally without this form data. And if you type stuff in of course right now you will

not get nothing back because we do not have nothing included. Then the next thing that most of the time

is needed is an agent. And if you include this agent of course you can connect this agent to your

chat trigger. If you press on this agent of course you can use a mod let's just use this open AI

mod because they are great. Then the parameters if you press on them you need to include credentials.

Let's just use once again flow wise mcb here. Then the model temperature and so on all the

things that you already know you can simply leave them as they are. Then you can include messages

if you press on plus you can give a role. So this should be for example the system message.

And here you can integrate the system prompt. And if you are lazy and you want that the AI

from flow wise is writing your system prompt you can press right here. Diping what you want to have

let's just say summarize that document and if you press on generate the AI from flow wise will

generate your system prompt specifically for summarizing a document for example. Then if you press

apply of course you will have your system prompt included and it's all included in markdowns you see

it with this hashtags with examples and so on. So if you want to work with a system prompt this

is the way to go right now I don't really need a system prompt for this simple explanation.

So we could also just delete this and press safe. Then you can connect to tools. Then here you do

have a lot of tools that you can connect. If you press plus you can press right here and you see

you can connect the brave search API a calculator chat flow the code interpreter compose a yo in order

to send mails you can do basically the same thing as with the tool agent in flow wise you can really

include a lot of different things. Current date and time. The custom tool the extra search the Google

custom search the brave search mcp the custom mcp and get up mcp both classical thinking like I

think that you do get the point you can include whatever you want here. For the Z key of this simple

tutorial let's just include a calculator you can give parameters but for the calculator most

likely not and then you can use require human inputs so if you activate this this is basically human

in the loop you as a human need to accept if the calculator can get called or not I just leave it

that off because I think it's fine if we use a calculator then you can include knowledge so document

stores you already know how to include document stores so you can simply press on them you can

press on the document store that you want to include and simply insert them right here here you

can connect every single vector database that you want and then of course you need to describe the

knowledge so you would simply type in use this tool when I ask questions about xyz this is just a

quick overview because generally speaking you already understand all of this and of course you can

add more than just one document store and if you want to include vector embeddings that is

basically the same thing you can also connect here you can type in the document store that you want

to use so if you don't have made your document store inside the flow wise maybe you already have

a vector database in bindcon or boss grass you can simply click on it if the embeddings model

all the credentials and connect it but right now I do not want to do this then you can include

memory if you want if you press on the enable memory here you have something like a windows

buffer memory so this thing will simply know about what stuff you are talking then the memory type

would be for example all messages and then you can also type in here return response as either

user message or assistant message I just leave it as user message so we basically have set up a

really really simple agent that just has a calculator as a tool and if you press save right now we

can chat with this thing if I type in here right now we process the flow and this flow answers to me

hello how can I assist you today so you see this thing is working and it's working great

and if I ask questions where we need to use a calculator we will use the calculator what is 99

times nine let's just say we send it out and then we will use most likely the calculator boom

there we have it but on this agent you already know this is really really big you can include a lot

of different tools and you can do a lot of cool things actually let's just come on plus once again

because I want to show you the things that we can include right here let's just go over every single

node like relatively fast you already know the agent and you also know the condition remember you

can simply connect to the condition and type in the values that you want to have and then simply

answer on two different paths then we have the condition agent utilize an agent to split flows

based on dynamic conditions this is relatively similar but here you do have a y included

so you can analyze your questions and then split it out relatively similar today fells note but

here you have a y included to split stuff out if you start for example with our own forms of

mission and here people are typing longer texting you can use the condition agent in order to figure

out what these people are telling you and then make different classifications right here next we

have the custom function so this is basically the same thing as you already know this is just the

custom tool so here you can include some chabas crypt code and then you are basically ready to rock

and you can also update flow state if you want if you simply press right here you can give key and

value so the custom tool this is the same thing as you already know then you can press plus once again

you can also use direct reply let's just make an example for the direct reply

we just would assume that we have a condition node first and on this condition node we have a

direct reply if people have for example a chop if we use for example a start node and on this

start node it's our own forms of mission and if people have a chop we would directly reply like

this is not for you because we only talk to people that need a chop and then you can simply use

this direct reply interior you can hard code your messaging and this message will get

send it to people but on the other hand you can use the second route and I want to take the chance

to show you here this tool node because of course you can connect here this tool node and this

tool node can also be everything that you want and if you press on it this can be of course a normal

tool but for our example this could be for example once again this like MCP so you would connect

like for example and the people that don't have a chop here you would then surround like for

example and people that have a chop simply get the direct reply this is just a stupid example now

let's just go on because besides this direct reply we have execute flow what you can do with this

notice you can execute other workflows let's just say that you have this agent and after this

agent you want to trigger another workflow from flow wise you can totally do this by simply

connecting your credentials select the flow that you want to trigger here are all the flows

included that you already have and you can communicate with this flows it's really easy then you can

give them both and some variables and you already the rock maybe you already have for example a workflow

that includes rack and you don't want to include rack here once again and if there comes specific

questions you can execute your other workflow then we have the HDDB request node and here we can do

the same thing as in an add-in if you are still familiar with an add-in what you can do is basically

you can use a get or post-meffat even put delete or patch and you can connect to every single API

that you want if you already played a little bit with an add-in I am sure that you can set this

things up it's relatively easy to use so you can basically just set up HDDB requests with this tool

besides the HDDB request you have human in the loop and here you can simply do the same thing as

you saw right here you can you can require human input in order to use different tools so let's just

say you have once again this start node and after this start node you always want that you as a human

want to check if the workflow gets executed you can work here with fixed or dynamic and you can use

for example an LLM to summarize different stuff and then you will get the question if you want to

execute this so human input is really nice if you have specific workflows next we have iteration

and here you can work with n integrations if you throw this on here I have to tell you that this

is a node that I personally don't use ever but you can play with it if you want you can always give

an array input this is also a node that was at least for me buggy from time to time so I do not

want to dive deeper in this node I will talk about this node as soon as this node is fixed a little

bit more then you have your normal LLM node with this normal LLM node it's basically similar to

one agent but without any tools so this is a simple LLM node of course you can talk for example first

to the agent then do an LLM node you can also use this LLM nodes to analyze different stuff from

your agents if you want then you have loop and loop is also an interesting node you can loop

basically back to different parts of your workflow let's just say you want to loop back twice to

this agent so if you connect this basically if you have a question this thing will make sure that

the agent works twice over your input then you have this retriever here you can basically just

retrieve knowledge bases with document stores and so on this is always the same things as you see

right here under these tools so this is just a retriever tool as you already know from all your

other workflows you already know the start node then you have the sticking out and on this sticking

out you can simply write stuff let's just say you want to write here calculate the agent because

this is an agent with a calculator you can simply organize your workflows a tiny bit better

and you can press plus once again and then you see the tools and I already talked about you with

the tools this is also the same thing as in the agent you can use all these different tools

right here also here if you want to make for example workflows that are a little bit different

let's just delete this we do have for example a start node after the start node we could use for

example the condition agent if we throw this condition agent on it we can type in in this chat

then analyze the question make two different outputs in one agent we would use for example

some kind of tool and in this other route we would use for example a big agent and this big agent

can ask and serve some questions maybe also with tools attached and so on so you can basically

build chat flows really really easy with the version two or flow wise it can do basically the same

as you can do on chat flows if you press that new with this tool agent here you can connect

basically also the same things and if you work on agent flows in version one you can also basically

do the same things but this version two makes it a little bit easier a little bit more organized

to work with so I will recommend you to check the diversion two out you already got a lot of

different examples over this course so we will not go over every single example here this is just

a nicely lab date you can also work with version two