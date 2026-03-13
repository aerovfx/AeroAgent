# 6 -Pinecone Vector Database in Tool Agents for RAG (with SQLite Record Manager) translated

---

In the last video you saw that we can build this tool agent and on this tool agent we can connect like nearly ever-racing LAPI.

The last thing that we should eventually connect is of course a vector database.

And for that reason we will connect bindcomb as a vector database, bindcomb works outside the flow wise,

you can store your data forever on bindcomb and call it as a tool.

This will be really really cool.

The only downside right now is that it's not really an MCB,

but nonetheless I want to show you how we can build a rec application inside the flow wise

because rec applications are always really really great.

Of course with some workarounds we can also include rec with an MCB server.

You can make something for example in an add-in and then connect it with the supergetway MCB

later in this course we will do this in the special workflows.

But first I want to show you how we can build a rec application inside the flow wise

because this is also always a really really great thing to include.

You can of course use the simple dual agent, include some normal MCPs

and include the vector database directly with the normal dual calling.

The first thing that I want to show you is of course that we can also copy this workflows.

So as soon as you have a workflow here we can copy this workflow and insert it for example

into a new one, make it a little bit clearer and then we can work with it.

And I also need to tell you that we need to make something like two workflows in order to work with this thing.

Of course we have our standard workflow but we need a second workflow in order to observe the data

in a bind convex to database. So the first thing that I would like you to do is to simply

copy this workflow. For that you can simply press here on settings and you can press duplicate

chat flow. Then you are of course in a new canvas with an untitled chat flow.

It's really that easy. And here you can give it for example a new name so as soon as you save this

up we can give it a name. Let's just say tool agent with rack and we save it.

Then I want to delete some stuff that we do not need. I don't want to have for example

our custom tool because I don't want to have access to perplexity. Windows Buffer memory is okay.

Calculator is okay. The Brave Search API is also okay. Current date and time is also okay.

We boot not to really need it. We can write stuff on our local machines. Also this is fine.

And also compose a yo. We can just leave it. But always think about if you really need these tools.

This is just an example. You can also delete some tools. And of course at the end of this video

you can also just copy my workflow. So right now save this once again because we cannot use

this vector store. You already saw that we used some vector stores down here like this in memory

vector store. Of course this is the easiest one. You can simply connect your embeddings,

your documents and so on. But the important stuff is here that this thing will get deleted over time.

It needs to get absurd that over and over and over again. And if you want to build out something

like for the real world where your stuff gets stored in a vector database forever you will not work

with this stuff here. We want to work for example with bindcom. So let's just delete it save it.

And now we build out our second workflow so that we can insert our bindcom vector database right here.

For that we come back and we come to document stores here. I really love this one. Of course we can

also go to chat flows and create a new chat flow in order to absurd stuff to bindcom. But I love

the document store from here because here we have a lot more flexibility. We can also connect

both Crest and a lot more if you want to manage your chunks. This makes it really easy and really

fast. As soon as you are in document stores you simply press add new. And you can give it a name

and a description. Be press add. Then we can press on this. And now you need to have document

loaders. So you press plus and now you can decide for yourself what you want to use. Do you want to

have data from air table an API loader apfy website content crawler if you use this for example

of course you need api keys and a lot more if you already work with apfy you can of course do this

but this is a paid feature and I don't want to show you the paid features so once again press plus

you can use once again the brave search api confluence csv files a normal file loader get tap get book

chase files and a lot more what I want to use is yeah let's just actually do two different things

I want to have a pdf file so I press on pdf file and I upload the pdf file let's just make a generic

example once again with this cld prompting so upload file and I use the cld prompting and I have

uploaded it right now here then the usage is one document per page we can also include additional

metadata if you want and of course we can use a specific text splitter we come back to metadata in a

minute let's just use a text splitter so we press on it for this pdf file a recursive character text

splitter is perfect then we use the chunk size and overlap actually for this file the chunk size

with 1000 is fine and an overlap of 200 is also fine and we don't need any customs operations

what we want to do is to press process right now this will take a minute or so then you can refresh

these and as soon as this is refreshed you can come on this once again so you can simply press on it

you see these are 17 chunks with 13,000 characters so if you press on it you can also see how

these characters or how these chunks are looking and if you scroll down here you see every single

chunk and on this chunk is also this here and here we can add a little bit more metadata if we

want so let's just come back once again now we press on these options and on these options we press

preview and process and then you are once again in the same interfaces previously and also here you

can press preview chunks and you see that you get the preview of 20 chunks actually we only have 17

because this document it's not that big and this document look completely like this so here you

see everything that you need and if you want to include metadata of course you can totally do this

and this metadata will be somewhere here so you have a little bit more clarity later if you want

to absurd for example of UPDFs or text files or whatever so actually let's just come to metadata

be press plus and let's just say PDF, C-O-D and be press okay and if you want to add a value of course

you can totally do this so actually let's just add this here and let's just say C-O-D so this

is about the chain of draft prompting and be press okay also here and now let's just see first of

all these are our old metadata so you do not see from what document this chunk comes from but now

I press preview once again and now you can see that we have of course the metadata it's from the C-O-D

and also the content is C-O-D and if you press also here you can see every single time that you

have on this metadata included from what document this chunks came from and of course then we press

process so that you can observe everything you can reload it and then this 17 chunks will get

them better the sooner we embed them but before we embed them I can press add document loader once

again and I can upload different files this could be more PDFs this could be a CSV file this could be

once again whatever you like additionally I want to train on this document this is a prompt

engineering guide a comprehensive guide for AI and so on so you see basically this is a whole

document and it's structured in markdown it shows the most powerful prompting techniques like

fuchsia prompting and so on with examples and a lot more so you have basically a lot of good

information in it and because this is a normal text file I just want to use this text file by the

way you can also use plain text and copy paste your text in it but I already have this text file so

we simply use this text file I press on it then of course I upload it it's this prompting text

then we can also give additional metadata you already know it so we simply press plus

and this right now is prompting paper let's just call it this okay and the value this time is

let's just say prompting and okay then we come down the text blitter this time I want to have a

different text blitter because this is a markdown text so we use markdown text splitter so that we

get the most out of it this file is also not too big so let's just use chunks like I think 500 is

enough with an overlap of just 100 this should be completely fine let's just press on preview

chunks here we have 20 chunks as preview and we have everything split that perfectly and you see

that it comes from the prompting papers or we have our metadata and we just want to press process

once again and of course you can go on you can upload even more stuff if you simply press add

document loader you can add whatever document you like this could also be an entire book if you

want because this thing on bindcon has a lot of space but in order to make it fast come on I think

we are set and the coolest stuff here is that you can manage your records really really easy you can

always come to options let's just say this PDF is no longer up to date you can come to options you

can preview and process this thing and if it's no longer up to date you can simply change it upload

another PDF or whatever and if you want to delete the whole thing you can simply delete it so you

can manage your chunks really really easy especially if they come from different documents this is

the easiest way you can you see for example 20 different sources and always manage them really really

right now let's just say that you are ready to rock you can press on more options and then you can

view and edit all chunks if you are still not happy so you can come here in and see all the chunks

that you have here absurd that right now only in flow wise we need to absurd them right now in a

vector database but what we want to do is absurd all chunks because we want to have all chunks here

and here we have three different steps we have them beddings we have the vector store and lastly

a record manager so first we need an embedding model and you already know that you can use every

embedding model that you like some people like your llama because it's free but for this tutorial

we simply use the open i embeddings we press on them then we need to give the credentials then

embedding model we use the text embeddings free small because they are cheap strip strip new lines

we don't need this and also here batch size timeout and so on we do not need this and the dimensions

all of this is automatically because we use the text embeddings free small so actually the

embeddings are set the next thing that we need is a backdoor store so we press on it and here you

can see for yourself what you like like I told you if you work with both creases is also fine

but what I want to do is to use bind cone because I like bind cone the most if bind cone is completely

new for you we will make new credentials in order to do that you simply google bind cone and you

press on the first link as soon as you are in bind cone you need to sign up here with your google

account with whatever you want and I can simply press login then you will be in a web page that

looks something like this most likely this will be empty for you of course but you just have to

press create an index then we can give this index a name for this thing let's just call it prompting

but of course make sure to write it at all in small lowercase letters then we need to use the

embeddings models and here it's important that you use the same embeddings models as previously

and we had of course the open AI text embeddings free small so we press on them this is really

important it will not work if you use here different models because if we come down here the

dimensions are always automatically set and also the max input tokens and a lot more so basically

make sure that you use the same embeddings model if you use for example the text embeddings free

large you see that that dimensions change and this will not match with your absurded chunks so

use the same as you used in low wise so we simply connect this text embeddings free small and then

we press create index then our index is of course created this will be really ready for us and the

next thing that you need is of course an API key so you simply press on API key you can create a

new API key and we give it a name and we press create key we can simply copy this key come back

into low wise and here of course we will create new credentials we press on it create new bind

cone we delete this old key insert a new one and we press add now we are connected and now we need

our bind cone index and in order to find your index we come back to bind cone of course once again

and you press on database index and you press on prompting so this is basically the index from

previous and you can simply copy this name I would always recommend you to copy this name so that you

don't have any typos in it so you can simply copy this stuff come back into low wise and give

the index name then a bind cone name space this is also important so you want to create something

and here our name space will get created and you can also manage your name spaces later you can

delete different names spaces and do a lot more so let's just give it a name and we call it for

example rack course or actually let's just call it prompting because this stuff is about prompting

so that you are a little bit more organized file upload bind cone text and so on all of this

stuff is not really important if you want to add metadata once again you can do this but this

is not that important you can also use a different top k if you want but the top k of four works for

me fine but you can go up until 20 if you really like then the search type is of course always the

similarity search but you can also try with max marginal relevance but the similarity is more

accurate then the vetch k is 20 and the lambda is 0.5 don't mess with this stuff the default settings

are always great here the next thing would be the record manager and we'll come back to this thing

what we want to do is right now to absurd so we press on this button and then our 37 chunks will

get absurd and you can also test the retrieval so if you press test on retrieval you can simply

enter a query and see if bind cone gets the stuff back that you want so let's just ask what is

COD for example and then we will get some chunks back so here you see four different chunks

they will be most likely from our COD prompting paper and if you press on it you can also see it

here that they come from the metadata COD and I would guess that every single chunk comes here from

COD COD also this is from COD and also this is from COD let's just ask something else few short prompting

we got once again these documents and now you see that this chunk comes from the prompting paper

and I would guess that there are also some chunks in the COD document about prompting so let's

just see if we find something and there we have it so this is from the COD paper because also here

we have for example the few short prompting included so we can also search every single chunk that

is relevant so you see one chunk comes from our markdown text file and some other chunks come from

the POD paper so this seems to work perfect and also here you can mess with this stuff if you want

if you come up with the top K let's just say to eight and we will press once again and see if you

get more data back now you see that you got eight chunks back but always remember this stuff will

get more expensive if you go up with this top K more and more and more you will get more and more

and more chunks and this costs you more and more and more tokens so make sure that this thing is

relevant for me atop K your 4 is here perfect because I think this is more than enough so we get

4 chunks back every time as soon as we send stuff out okay this was 7 actually I want to have 4

and now we are set once again and it's also really fast if you come to bind cone right now you will

see that this vector database is no longer empty you see that here we have 37 chunks included and

all of these chunks are in a namespace that is called prompting so this is perfect and if you come

on browser you also find here some documents and you can search through them manually if you want

and also here you can go up with the stop K so that you see more documents here but this is just

10 different things that you can see in the namespace of prompting what we want to do actually right

now is press save configurations we come back here to document stores you see this is right now

absurd that it's ready to use so what we can do is to come back to chat flows with scroll down

we want to have the tool agent with rack of course because right now we can include direct

technology here and how we can do this we press plus of course with scroll down we want to have

tools we want to add the retriever tool and we need to connect the retriever tool of course

on our tool agent so retriever tool on our tool agent and actually this gets a little bit

big right now so there we are then of course we give this retriever tool a name and a tool

description let's just call it prompting and a tool description use this tool on questions

about prompting and c o d and what we want to have next is of course a retriever you can see it

always here it's always nice stuff that is a red you need to connect stuff so we press plus

we scroll down as retriever we actually want to have a vector store so a vector database and of

course the vector database comes from pine cone because we have trained here stuff from pine cone

so we can connect this pinecon vector database with our retriever tool and if you do this of course

you need to connect and batting credentials and so on but right now I want to show you a trick

that works a lot faster let's just actually delete pine cone once again if you press plus once

again and you come down to your vector stores we can use the documents or vector you can simply

throw it in here connect it to your retriever and then something cool will happen if you press here

you will find wreck core test this is the stuff that we have created previously so boom there we are

right now everything is connected because we simply want to retrieve the documents that we have

created previously in our pinecon vector database and right now our wreck application is basically done

so let's just save it and now we can ask questions about c o d and about prompting and about

whatever stuff that you have uploaded here so actually let's just come on it and I want to test

something out first let's just test of course our retriever tool what is c o d prompting and I

would guess that this tool uses of course our vector database and gives us everything back that we

need and here we have everything and by the way you can also always press here and then everything is

big so that you can read it a little bit better and you can also see that we used the tool that is

called prompting so you press on it and you see that this is the stuff that we got back from our

vector database we got three items the tool is prompting then put this c o d prompting and this

is the tool output so you basically see that we get everything back that we need and this thing of

course tells me what chain of draft prompting is and it will give me exactly the information from

the paper so basically we can also see these exact numbers we have already covered these numbers

a few times but we can totally do this and if I ask right now for example what are three good

prompting techniques I would guess that we will also search the other stuff and right now we get

our data back and I would guess that we use not only the c o d paper but also the mark thumb format

that we have uploaded so if we come on prompting you see this query got sended out to bankone

most effective prompting techniques for rel alams and this is the output that we get and here is not

only the chain of draft included but also the chain of thought prompting the chain of draft is of

course also included then the react reasoning and act prompting and you see everything gets

described perfectly because this is the stuff that we have uploaded so here we also have the chain

of thought prompting for example we've also some examples so this seems to work perfect and now

let's just actually see how you can manage your vectors or a little bit more effective we can simply

come back here we come to document loaders come to records test until you can for example absurd

new chunks or manage all of your chunks if we come back to this prompting stuff here you see that

37 records are added and if you are right here we can simply press once again add document loader

let's just make it easy you want to include plain text and on this text we include for example

something like this this right now is text it's also marked down but this text is stored

in a Microsoft word document so this is not a normal text file but what we can do is right now

to copy all of this division prompting techniques and here results some special stuff about different

lenses and about different lighting and so on so this is special stuff about prompting for

the fusion models so you can simply copy all of this data and as soon as this data is copied let's

just wait there we are as soon as this data is copied you can come back to flow wise we insert this

text here we scroll down actually we add some metadata first let's just say diffusion prompting

okay the fusion also here and okay then we need once again a text splitter and because this stuff

is also marked down we want to have the marked down text splitter so that the text gets splitted

a little bit more accurate the chunk size this is also really small so 500 chunks with an overlap of

100 this is completely fine overlap of 50 I think would also work for these you can press on

preview chunk once again and then you see that we get of course the characters perfectly split that

all in all we have 21 chunks so actually let's just process this chunks and then we can reload them

and right now you see that we have once again 21 chunks so right now we have once again this

37 chunks here but then of course we can simply absurd this chunks once again and we do not have to

absurd all of these chunks we can just include the chunks that come from this marked down text

splitter so we can press on it and we press on absurd chunks also here everything is set so you

can simply press absurd and now this few chunks got absurd that you can also test the retrieval but I

think this is fine and if you come back into pine cone let's just wait for a minute this chunks

should get added and there they are so we have right now 58 chunks included so right now you can

also ask stuff about diffusion prompting and if you come back to your document stores once again come

on right course or whatever and let's just assume that you no longer like the diffusion prompting

of course you can simply delete this stuff or let's just actually do something different let's just

actually say that you do not want to have no longer the chain of draft prompting in it you can

press on options delete and delete all of it now we have our normal prompting guide and we have

also the diffusion prompting guide then we come back here to pine cone right now you see 58 chunks

are added then we come on namespace and we simply go on and delete this namespace by typing in prompting

delete namespace now this namespace is empty once again we come back to flow wise and of course

right now we can simply absurd the chunks that we have here so we come on options absurd or chunks

we press absurd once again and now I will test that we add something like 30 or 40 chunks you see

it 41 chunks actually you can test the retrieval but actually I think the retrieval is fine so let's

just come back to chat flows once again then we come down to this two-legend with the rack we press

safe of course because right now our pine convex to databases 41 chunks and also the diffusion

prompting is included so we come back to flow wise and now let's just ask basically clear this

make it big and we ask how does prompting for diffusion models work make up example with lenses

of course we will use once again our vector database and we will get our information back

here we get also the example and you see it also let's just wait until this is done so there we are

we have a prompt that we can also copy if we want we have the detailed explanation that we should

include subject modifiers composition extra details and so on so this is exactly the stuff that we

get out from our vector database and if you press on prompting you see that we send out of course

this prompt and this is right now of course the chunks that we get back here and we have also here

everything included from our studio photo and so on this is really really nice this is how you

can manage your vector database with ease and this stuff will get stored here how long you want

the last thing that I want to show you inside of your document store is of course if you press on

absurd once again so absurd or chunks for example you can also use a record manager and this makes

it really really easy to manage all of your chunks so if you press on the lecture record manager

you can use my SQL record manager you can use boss class record manager but what I like the most

is the SQL light record manager because this thing makes it really really easy you can simply press

on this things you can give a table name and some additional configurations but normally you don't

have to include anything if you want to you can include also a cleanup and so on but the easiest

thing is if you simply include this thing right here and the coolest feature of this thing is if

you have some chunks included inside of your vector database and you want to absurd it this thing is

smart enough to figure out that this chunks are already included this means as soon as this record

manager is included and let's just say on your document stores this two files are completely the same

you will not add new chunks to your buying come back to database but on the other hand if you come

for example to this text file and in this chunks new stuff gets included let's just say you make a

small update to this chunks the new updates will get included because your record manager will be

smart enough to figure out that these are new chunks so you will only insert a new chunks and don't

fill your vector database with unnecessary data also for this record manager I will guess that we

get some mcp servers over time but for right now like at old you for this video we do not really

need an mcp server this was just normal tool calling normal vector databases and so on we don't

have to use the model context protocol for every single workflow sometimes the normal function

calling works just fine but nonetheless later I want to show you some special workflows just

remember use a record manager if you need to manage your chunks like all the time if you need to

make updates to your chunks and you don't want to fill your vector database with unnecessary fluff

with the same tokens over and over and over again because this thing will be smart enough to figure

out that your tokens are already included so basically right now you have a red application

you can also delete stuff like write files or the brave search API or whatever but generally

speaking this agent should still work you can delete stuff for yourself later if you really want

and what I want to do is to press once again export chat flow so that you can use this chat flow

in this manner this was a really really cool video you are able to build a powerful

replication and you can manage it with this document stores in no time whatsoever you can update it

you can delete chunks you can delete namespaces you can include new chunks all the time you have a

really really flexible solution and you can also give the tool agent whatever tools you want

basically you can build out everything that you want see you in the next one