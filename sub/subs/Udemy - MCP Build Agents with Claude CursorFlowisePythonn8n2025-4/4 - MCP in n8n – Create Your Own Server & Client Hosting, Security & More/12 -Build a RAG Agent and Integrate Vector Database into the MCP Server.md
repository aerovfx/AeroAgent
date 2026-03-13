# 12 -Build a RAG Agent and Integrate Vector Database into the MCP Server translated

---

In this video we will connect our vector database of course to our MCB server.

The first thing that we do is that we come into our canvas so we come on personal

deck. I can leave without saving in this workflow because I have already built it out this

from the previous video then we come to our MCB course. So this is basically just the server

with client and so on. Our basic workflow then we press plus of course to include new tools

and of course we need to include the pineconvector store and as soon as the pineconvector

store is included of course we need to press plus for an embedding model. We need to make sure

to use the same embedding model and it's of course text embedding free small right now

and then we can press of course on the pineconvector data store and here we need to use the things

that we want to have. So we have connected our pinecon account with our API key.

The operation mode is of course retrieve document because we want to search our vector database

then we need to give it a name and a description. Let's just call it TslA info or maybe TslA

financial info. We could also copy these and rename it so that we have it a little bit easier

later if we want to find this out so if you press on these we can also call it TslA financial info

and rename it. Then the description use this tool to get info about Tesla financials then the

pinecon index of course you need to press on it it was an add and a course Tesla or TslA

then this is the limit this is the so called top k if you increase the top k results you will get

back more chunks right now we get four chunks back and we hope that in these four chunks we will

include everything as we need it. We also include the metadata and here on options you need to use

a property so you press on it and we want to use a pinecon name space and it's of course the

pinecon name space that we have created here it is TslA and 8n so copy this and throw it in this

name space and then we should basically be ready to rock we should call this Tesla financial data

as soon as we trigger our MCP server let's just actually ask something about q4 so the thing that

we trained on the metadata to see if we even can get back this metadata I just want to ask for

example let's just see about total automotive revenues of q4 2024 and we should get back this

number I just copied this open chat we throw this in here how was total automotive revenues in q

of 2024 and right now we send it out of course what will happen here is that our AI agent

triggers the MCP client the MCP client will trigger the MCP server the server will search the

vector database and then we should get of course our answer back now let's just see Tesla still

out of automotive revenue in q4 of 2024 where 19.80 billion this figure includes automotive sales

and so on and basically if we come here you see it was 19.798 so we rounded a little bit but I

do think this is completely fine this works perfect let's just ask what was this performance 0

and we should get back that we got minus 8% how was total automotive revenue of q4 compared to the

previous year and we should get back minus 8% the year over year so Tesla actually did not

do that great in the year the automotive revenue declined by 8% so you see everything seems to

work perfect even if we have trained here on this metadata of course if we ask stuff about

the markdown data it should at least in theory work better this doesn't have always to be the case

but I do think most of the time it makes sense to make markdown and now I want to show you something

if we ask here for example and what was let's just say service and other revenue we have the

possibility that we get false information back and I want to tell you in a minute why so first of all

this thing will no longer know about what things exactly we are talking we get some information

back but not about a specific quarter but if we actually follow this jet flow here it should be

clear that I want to have services and other revenue of q4 in 2024 but why does this application

doesn't get this because we don't have any memory this is here special in the host of niden if

you work with cloud desktop or with cursor it will have this context but if you want to include

this context here you have to include the memory so you have to press plus and here we would use for

example a simple memory if we don't use the simple memory this thing will simply starts to forget

stuff and I want to make this clear once again if I delete this and I press open chat and I reload

this whole chat and I tell here hey my name is Arnie and I send it out this thing will greet me

back most likely it will of course not use the mcb server hey Arnie how can I assist you today and

if I ask right now what is my name this thing will not remember because we work over the API and the

API has not automatically included a persistent memory but we can include this persistent memory

remember this is just for this specific host so this is not really needed if you work with cloud

but in order to make this better we can simply connect this memory here and on this memory we use

let's just see we need to press on it the session key from previous note it's yeah this should work

then the context window length let's just say this thing should know for about 10 messages about

what stuff we are talking then we save it once again open chat then I reload it and I say once

again my name is Arnie hey Arnie and so on what is my name your name is Arnie so you see right now

this thing understands the context it understands for 10 messages about what stuff we are talking about

because we have this simple memory or buffer memory or however you want to call this this is

really important if you work with an add-on because sometimes you want to have a conversation with

your replication and if you want to have a conversation with your replication you need to include

this memory like I told you this is not really needed if you work with another host if you work with

cloud desktop for example of course it's not needed because in cloud desktop we already have this

conversation if we come back into cloud desktop and we press and we press on it we have an add-on

here and on an add-on we also have Tesla financial info right now so we can also search the vector

source from here so actually also let's just ask a question from here to simply see if this is

working total gross profit of q4 2024 what was total gross profit of TSLA in q4 of 2024 of course we

want to always allow this we want to always have access to our vector database and this thing tells

me that it was 4179 billion and it's of course let's just see 4179 billion so everything seems to

work just fine and if you come into cursor and we reload this of course we also have here the

Tesla financial info and you can ask the same thing now this is a really powerful concept if you have

a vector database with like your special data with data of your company with data that you need to

work with in different hosts in different application this is a real game changer because you can

insert all your knowledge that you need in every single client that you want as soon as you have

build it out one MCP server with one vector database you can include whatever knowledge you want and

you can access it from every host that you want later I will show you a special workflow where you

can add memories to a vector database so you can also absurd stuff from a chat throw it into a

vector database and then read it later as soon as you need it I do think with vector databases we

have a powerful powerful application if we include vector databases to our MCP server and I see

you of course in the next one