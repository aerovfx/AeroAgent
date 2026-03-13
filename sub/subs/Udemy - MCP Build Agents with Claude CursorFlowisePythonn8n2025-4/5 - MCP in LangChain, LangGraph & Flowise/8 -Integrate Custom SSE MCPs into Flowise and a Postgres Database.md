# 8 -Integrate Custom SSE MCPs into Flowise and a Postgres Database translated

---

In this video we need to take a closer look at the model context protocol inside the flowbys,

because you already know it can connect also our own MCP servers.

So right now we are once again in version 2, and I have to tell you right now at this minute

that we do have some limitations inside the flowbys. So let's just actually begin with adding an agent,

and we connect the start node with this agent. We come on this agent, and we select the model of course.

For the sake of this tutorial I just stick with this open AI model because they work great.

We connect credentials like the flowbys MCP and use the GPT for our own mini model because they are cheap.

We don't want to have any messages and now we come to tools and now we need to take a closer look

at the MCP tools and we leave human input as not required. You already know that you can connect

every MCP that you see right here like the Brave Search MCP and so on. And right now I want to come

immediately to the downside of the custom MCP tool. If you press on this custom MCP tool you can

press right here and you see if you make it big that you can include always the command

and the command should be at least in theory and px. And then we need to give the arguments

and in array we need to type in dash y to give yes to all of these things. Then we would include

for example the model context protocol server file system and then the path to allow files.

So basically we can include something really easy like this.

Command is npx then the arguments with the model context protocol and then it would give access

to my machine on the desktop for example. And I just have these two slashes because I am on a

Windows machine to escape it. But I have to tell you that npx does not work right now at this

minute in flow wise. I am sure they will include it. What works here is only note. So you can only

work with a server that you have created for example in typescript and you need to run it locally.

So I do think this note has a gigantic limitation right now and I have to tell you I do not use it

because this is only practically as soon as we can use the npx command and then we come on this

GitHub server search for every single server that we want and we can connect everything that we want.

So it would be of course really nice if we can connect like to every single thing from this

GitHub repo but right now it's simply not there. If you search for example to Airbnb and if you press

on it you always see like in 99% of the servers they use the npx command and the npx command does not

work. So I do think this integration has right now a lot of downsides and that's why I do not use

it so cancel it and I want to delete this right now but I want to show you the cool thing if you press

plus once again and we come right here on it like you can connect to the servers that are already

included simply throw your API in it you should be able to do this right now but what we can also do

is to use the supergetwmcp and this is a great tool and this also works really great and everything

that you have to do right here is to specify in the arguments dash dash sse and then in

quotient marks the thing that you want to talk with and because we have already created our own

sscn point inside of an adn we can connect to it so we simply type in dash dash sse for the server

send event then we open up this quotient marks and inside of this quotient marks we throw in

the mcp server that we have created for the sake of this tutorial I simply use this thing right here

and you know that we have here for example the http request to the weather API we have google sheets

read google sheet append we have the zp rmcp included test love and angel info prompting info and also

a web search tool with http request so you need to make sure that this thing is active then you come

to your mcp trigger you come on the production or value properties make sure that this thing is public

then you come back to flow wise once again and here inside of our quotient marks we throw in our

server then we press safe and as soon as this thing is saved up you need to reload it down here so

just press on it in your command prompt something like this will start and then you see that we get

the these objects included and then if you press on this right here you can include the things that

you want to include so add new actions to your mcp provider you can also add new tools then you can

also edit these tools and then you have your normal tools so gmail find event gmail sent event google

calendar delete event and so on this is just the stuff from our sapear server then we have the google

sheets append then we have the google sheets read we have the prompting info the test love

an angel in for the weather HD tp request and also the web search so you can simply connect to

every single thing that you want so you already have a vector database created inside of an

adn you can connect these vector databases to cloud desktop to an adn so to this agent you can

connect it to cursor and you are also able to connect it to flow wise with this simple mcp

integration so just press on the stuff that you want to include let's just say this prompting

info and boom then you are connected let's just wait a minute until we come through right now we

have it and of course you can add more tools you can connect to more than just one server let's just

say you want to have for example the web search from right here with the brave search mcp you can

press on it select the credentials that we already have created then you need to reload it and then

we will use for example the web search and also the local search and right now we have two mcps

included let's just save it and we ask something about the cud prompting what is the cud prompting

use mcp for example process flow let's just see what we get back we get our answer back and

answer is actually like relatively big let's just make this big to see what we get

you see process flow we use the start trigger node then we use the agent the agent used this prompting

info and it used of course the vector database from our mcp server and then we get our answer back

and here is every single thing about the chain of the raft included so this works completely

perfect and also these numbers are correct and if you come back into an adn for example let's just

come on executions you see that an execution comes through we use the mcp server trigger and it

searched this prompting information so you see we can connect with flow wise to our mcp server

relatively easy and it's really nice to build this stuff out in an adn because it simply works

and of course we can also use the mcp from brave so let's just save this up and ask for example

let's just delete this clear we open this once again what are the news from apple so this will not

trigger our local search this should be a general search a general web search we are processing

the flow this agent is loading we get the answer back also with a lot of links let's just make it

big as soon as this thing is done boom there we have it now we have all these links and you see

that we used the brave web search so not the local search but the web search and you see that

everything seems to work and this is basically how you can integrate mcp inside of this version 2

this also works completely the same with the two agent but I wanted to throw it in the agent

because this thing is great and now I want to show you one more thing because I got a question

how to integrate a vector database directly inside of these agents with the version 2 of course

we can do this and right now you have two options you can either use the vector embeddings right here

if you already have a vector database but I got the question how to integrate both graphs so we

will do this first save this then we come back we come and document stores this is really easy

then we both press add new we give it a name let's just call it v2 test we add we press on it

we need to have a document loader and you can use whatever you want for the sake of this tutorial

I want to embed once again a pdf so pdf file we need to upload it I have simply used this dog

of pdf this is just a pdf on dog training that is not in the training data of an llm these are

just some examples you can train on whatever you want then the usage one document per page is fine

additionally and metadata I don't use it you already know how to include this I just want to

make this quick we use a recursive character text splitter with a chunk size of 1000 and over

lap of 200 this is fine and we don't need any customs operations we can press preview chunks in

order to see if this is working yes this works fine so we press process boom right now we have it

here and now we need to observe this documents and we need to do it into both graphs so what we need

to do first is to press refresh then of course we want to observe or chunks we need to use an

embedding model you already know that I like the open AI embedding models so we use the open AI

models we simply connect to credentials that are working then we need to come to this vector stores

and this time we use postgres because postgres and superbays are two bucks to databases that a lot

of people really like so I just want to show you how this thing is working it's a little bit more

complex to set up then bindcomb so we press on postgres now we need credential host and the

database and also the port if you have already an account you can connect it but I want to create

something new so that you can see it how to do it click by click let's just call it postgres

v2 now we need the user and password in order to create our postgres database we need to come to

super base so simply google super base and press on the first link of course you need to sign up

by already have an account and then you can press start project I do think that you can create

two projects completely for free and this is just a test account with some projects so first I

want to delete a project and then we will make something from scratch after that you can simply

press new project you can give it a name like flow wise and you need to give it a password that

you will remember this is important because we need this password in a few minutes then you can use

a region you can also add security options if you want and some advanced configurations I just

leave it how it is and then we press create new project next you need to press connect and we

need all parameters so you can copy these and user is also basically the stuff that you need to

write here so just insert it and then you need the password and this is the password that you

have typed in previously so just type it in I hope you remember it and then you press add and boom

your credentials are connected next you need host and database so you come back and here you see host

so you can copy this host you came back to flow wise and insert the host next we need the database

so you press copy on this database it's it's just boss grass then you come back and you include

the database and lastly you need the port and the port is once again also here so just copy the port

come back to flow wise and insert it you can leave ssl at off if you work locally I do think you

have to toggle this on if you work in the hosted version and all the stuff down here you can just

leave it at the default settings you can increase the top cave you want to get more information back

but the default settings generally speaking work relatively great the last thing that we include

is once again a record manager you can simply press on it and we use once again of course the

boss grass record manager and here we need to connect to the same credentials that we have already

created so of course it's boss grass version 2 then the host you can simply copy the host from here

it's of course also the same database and of course also the same port so simply copy these files

and insert them right here and lastly we press absurd of course and we need to wait until our

things get embedded boom 33 edit documents and you can also test the retrieval if you want but I

just close this down for right now and I press absurd once again and then we should not

add any additional things so you see zero things got added and 33 documents gets skipped this is just

because we have our record manager this makes sure that we don't absurd unnecessary resident data

over and over again as soon as you update your chunks if you include new knowledge the new knowledge

will get included and the knowledge that is already in your database it will not get included so

everything is added everything is fine if you come back to documents stores of course you can press

on these and add new documents you already know this and if you come back to boss grass you can

close this thing down and if you come to table editor here is nothing because you do not have any

table included if you come to ask you L editor you also should have nothing but if you come on

database you will have your database included and here you see in a nice visual presentation what

you have included and of course you can also open this upright here and then you see basically

everything that got embedded and of course you can switch between these files and see for yourself

what you got embedded you also see the presentation of the vector so this is the vector representation

the metadata we don't have any like real metadata and then always the page content of course

and of course you can press on it and see the sentences for yourself this is just from this

dog training and you always have a roughly 1000 chunks in every single document right here so

this is really nice so on this database you can simply see for yourself if you like tables you can

also come on tables and see here the columns that you have included but generally speaking this

vector database should work now you have to come back to agent flows of course once again we use

v22 because this was the stupid name that I have given then you come on your agent then you can

scroll down then you need to insert of course the knowledge so at knowledge then we can use the

v2 test use this tool for data about dog training and we can also return this or stock

meant if we want but we don't have to and then you have basically connected also your vector

database let's just save it and ask something about dog training and let me just open up my dog

of PDF so that I can ask a question let's just ask about the three categories of dog trainers what

are the three categories of dog trainers we are processing our flow and here we got the answer

let's just make it back you can always click on this thing you see that we used the agent the agent

used the v2 test PDF of course with the squery to search like the right information from our PDF

and this thing tells me that we have the first category with food or toy rewards the second category

that uses harsher methods and the third category with a balanced approach if you come to our PDF

the first category is food or toy rewarded the second category is the old school yank and cranked

trainer and the third category is in the middle of the do so of course exactly our information and

I also included returns or documents and so we can see that we have basically searched our content

and we got everything back that we need so this is really really nice to see so you don't have to

use mcp in order to include a vector database also postgres with super base works really really great

and you can integrate it but the main takeaway is of course that you should use the super get

way mcp if you want to include other mcp servers inside the flow wise just use the servers that are

already included or the tools that are already included you can use still compose a yo in version

you can still use current date and time you can still use the normal web search tools but you can

use the mcp's that are already included just stick with brave search get up postgres sql if you

already work with sql here you don't have the possibility of a vector database that's why I wanted

to include it you can use slack hands on you can simply connect the API keys and then you are

the custom mcp make some problems because we don't support npx at least not right now we only

can work with note and here you need to program your server yourself in typescript but you can use

super get way and this is great because we have created a ssz endpoint inside of an adn and you

can connect to it so this is also a normal host for everything lmcp server that you create for

example inside of an adn because we make an ssz endpoint and you can connect all the other tools

as you like so this is really great this is version 2 of flow wise and this is how you can

use mcp's inside of flow wise have fun playing with this and feel free to make this workflows bigger

and i'll see you of course in the next one