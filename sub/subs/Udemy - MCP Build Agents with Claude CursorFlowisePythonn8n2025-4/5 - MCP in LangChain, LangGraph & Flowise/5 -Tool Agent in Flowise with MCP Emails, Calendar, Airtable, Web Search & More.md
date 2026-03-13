# 5 -Tool Agent in Flowise with MCP Emails, Calendar, Airtable, Web Search & More translated

---

In this video we talk about the dual agent and I will split this video in two separate videos.

In this video we will talk about the basics so everything that you can do with this dual agent,

I want to give you a broad overview and in the next video we will build a

Reciplication with our dual agent because all in all the dual agent can be readily, readily big.

In some stuff you have to write a little bit of JavaScript code. We can also use

ChatGbD for it. We can use different libraries and connect them. We will include a lot of

different tools and I will also show you the exact differences between these tools and the

model context protocol inside of low wise because here we do have some special things and I will

also show you a really really powerful tool. Compose IO with Compose IO you can connect every single

API that you want Google Calendar Gmail Amazon Gera Firecrawl even YouTube and a lot more one API

key and you can connect every single API that you want. So stay tuned also for Compose IO

this dual agent is gigantic and you can do whatever you want with it. Right now we are in Chat

flows so no agent flows yet and we simply press add new then we are once again in this canvas and

you already know it you can save it and then we call it for example dual agent test course or whatever

you want. We press save then we press plus we come under the Lang chain library and of course

right now we need to use agents and on these agents you know that we have a lot of different agents.

We have for example the air table agent and if you throw this on it you can also connect air table

but you can also do this with this dual agent so we will not use the air table agent. We could

use auto-gen baby agi these are two tools that I no longer like that much because I think they are

a little bit too old they don't get a lot of updates but then we have the conversational agent.

This is somehow great you can also play with this stuff a little bit you can simply make

conversations with these and you can add memory to it this is also self-explanatory so I will not

cover this thing here the CSV agent. The open air assistant this thing will also go offline in

2026 then we have the react agent also this stuff is a little bit buggy from time to time with

this react agent and the thing that I like the most is the dual agent because you can do

most of it with this dual agent. Now let's just build actually the simplest dual agent that we can

build. We simply press plus and we start with a chat model and here is important that you need to

have a dual calling chat model so you can press plus here now of course we need to use the chat

and what can you use you can use AWS as your chat down tropic so also the cloud models work

you can absolutely connect the cloud models with this dual agent and insert your API keys but I

want to delete this because I want to show you actually something that is a lot cooler than the

un-tropic note. You have Baidu you have everything here just like you know you can also use

hugging face and so on the chat low clay eye model mistrell you can use whatever you like but I

want to show you the thing that I also like the most so I really love the dual agent and I also

love open router what is open router let's just first connect it you know it we need to connect it

with this dual calling chat model open router is this web page here 7.9 trillion tokens get generated

every single month they have two million globally users 50 active providers and over 300 models now

what you can do here you can simply press on models and connect every single API that you want

you can connect some coin models if you like and they have most of the time also some three APIs

before we can talk about these models of course first you need to make an account so if you come

back on this web page you have to press most likely in the upper right corner anterior you need to

login just login with google or whatever you want then you need to come to credits anterior you

need to add some credits it should be at least five dollars at least how I know it but trust me

this thing is cheap and especially if you use cheap models I like open router for three models the

open AI models are used and mostly over the open AI API but also here you can use the open AI models

as soon as you have some balance on open router trust me five dollars it's really inexpensive and

you can work with this forever if you use especially for models as soon as this thing is done you can

simply come to the documentation and read for yourself everything that you want so here you get

everything that you want you can also train a right application to learn something about this

but the next thing is that you can come on ranking and on ranking you always see what models get used

most on open router and little spoiler the models that get used most are also most of the time

really smart models anterior see top today so today cloud 3.7 sonnet got used a lot

chamonipe 2.0 flash got used a lot 2.0 flash preview got used a lot the 3d psik version got used a lot

there's also some llama models a 3d psik are one version open AI 4.0 mini open AI 4.1 and so on

and you can always see how this stuff behaves you can come on top this week and see for yourself

what's on top on this week you can come to trending and see for example that google chamonipe 2.0

pro experimental is right now on top on this trending models and you can basically reason for

yourself what model you can use then of course you can come to chat and on this chat you can make

some comparison about this flagship models if you press on flagship models you can compare for

example cloud 3.7 sonnet against GPT 4.1 against chamonipe 2.5 pro against groc 3 beta you can

simply throw in your message here and then see for yourself what output you like the most and then

lastly you can come on models anterior you find every single model under the sun that you want

and you can also filter through it so the input modalities do you want to have text image or

then the context length do you need for example a model that has a gigantic context window of let's

just say 1 million token you will find the chamonipe models but of course you can also go down and

you can filter through this however you want then of course the prompting price do you want to have

for example only three models and then you will find for example a quen model this is our

relatively new model and you can use this for free you find a lot of three models so just search

for the models that you want to use and I am sure you will find something that works great for you

but right now for me pricing is not that important then you can come down to the series you can

search for GPT cloud chamonipe and if you press on more you find groc nova mistral deep seek and a lot

more then you can also search through categories so roleplay programming marketing whatever you want

then the supported parameters do you want to have that the model has tool calling you press on it

and then you find the models that have tool calling included you want to control the

temperature the top p the top k the main p the top a and so on for us it's mostly important that we

have tool calling and maybe also top k and here you find for example llama for maverick but you don't

have to play like with ever a single model under the sun as soon as you have something that you like

to use you can simply roll with it and you can always come back to open router reload this models once

again so that you get a fresh interface what I want to use right now is cloud 3.7 sonnet for

example and if you simply type in cloth we find here cloth 3.7 sonnet I also work with cloth

for a lot but I have to tell you I do not know why but if we use the model context protocol sometimes

3.7 works at least in my normal tests a little bit better than cloth 4 you can basically test

for yourself in theory cloth 4 sonnet should be better but I have to tell you I just want to roll

with 3.7 for right now and if you press on these you can always see what you get out of this

and the easiest thing to use this apis to actually press on these things once again then you come to

keys create a key we give this a name let's just say rack of course you can give it a limit if you

want then we press create we have our api key we copy the key we come back into flow wise

and here we give the credential so create new here we insert the api key we press add and then we

need to give a model name of course and of course to find the model names in open router so you come

back to models you type in for example cloth 3.7 sonnet and you can always copy the name of this

model right here we will come back to flow wise and insert the model name right here and boom

there we are so right now our api agent model is connected and we have a model that has dual calling

included we absolutely need this for this agent next we need memory for this model so we press plus

we come down to memory and we use let's just say the buffer window memory and we connect this

buffer window memory and I want that this thing remembers like for five messages about what

stuff we are talking so we have our model we have some memory and right now we need tools so let's

just connect our first tool and we want to do something really really easy right now and then we

will add more and more tools I want to show you what you can do with this tool agent so we can

come down to tools and let's just use the calculator so that this stuff is working so we connect this

thing here and now we can save this up and we can see if this thing is working or not so we type

in A for example and right now our dual agent should talk back to us and here works right now cloth 3.7

sonnet in the background and if I ask what is 77 times 77 times 5 for example we can send this out

and right now we will most likely use of course the calculator anterior see it I've solved this

math problem for you using the calculator tool the result equals to this thing right here and if

you press on it you see that we did function calling to the calculator so this thing absolutely works

of course you can add chat prompt templates to this dual agent you can add input moderations

and you can also press on additional barometers and you can give us system prompt here and you can

also enable streaming more on the system message later because as long as this thing is reliable we

do not necessarily need to add a system prompt so if we call this tool is reliable we do not need it

and cloth 3.7 sonnet is really reliable in calling these tools if we add here arch-agantic system

prompt without needing it we just make our API calls more expensive and now I want to show you

what this windows buffer memory that actually does if we come back to one here press safe

and now let's just delete this once again so clear and I say hey my name is Arnie what is 77

times 2 I like that you are nice and now I ask what is your name I don't have a name and so on

but now I ask what is my name right now this thing does not know my name even if it told me

right here that my name is Arnie and also here I told it that my name is Arnie so here it knows

my name because it is in this memory only for one message it told my name back and then it starts

to forget my name and if I go up here for example to 20 so let's just go up to 20 save this once again

this thing will remember my name hey my name is Arnie now I ask some random questions that you do

not have to read so right now I got through a few questions and now I can ask what is my name

and it still remembers that my name is Arnie because it remembers it for 20 messages so for this

thing is the buffer memory needed and now let's just actually talk once again about the tools

because you can do a lot first let's just add some internet access I want to ask something like

this what is the bitcoin price today and the model will tell me most likely that it has not

a really an answer for me because it has of course no internet access I don't have access to real time

bitcoin price and so on we should check it ourselves on stuff like coinbase, buy an answer or crack

but then on the other hand if we press plus we can come back down to tools and let's just add for

example the brave search API we can connect the brave search API also to this tool then we need to

connect our credentials if you don't have any credentials of course google the brave search API key

as you know then you can press on it you can sign up or login it depends if you have an account

you will be in an interface that looks something like this and you get 2000 queries completely for free

you can come on API keys and here you can simply create an API key you can call it mcbe if you want

so just press add API key copy the key and insert it in flow wise just like you know and now I press

save and I ask once again for example what is the bitcoin price today let's just actually delete

this chat so that it has no information that it does not have information for the internet

so let's just send this out right now we will call a tool and then we will get the bitcoin price

and boom there we have our answer I help you find the current bitcoin price let me search the

information for you based on the search result to the bitcoin price is 95,103 US dollars and if I

come to trading view we see 94,500 and something but of course this is a little bit different on what

exchange we are checking so here you have for example a lot of different exchanges on coinbase for

example the price is also 94.75 free and so on it always depends on what exchange this thing is

but generally speaking it has the right answer for us and if you press here on brave search you can

see that we have called an API the brave search API with this tool and we got the answer back here

with a lot of information and our red alarm makes a summary so we do function calling to the brave

search API so right now we have this basic workflow and now it's a great time to see the difference

between the brave search API and the brave mcb so if you press on plus once again and if you come

down to mcb you already know that we have the brave search mcb and if you include it this note looks

relatively similar you can simply connect it to this tools but then something interesting happens

you cannot only connect your credentials but you will also have the available actions just like

it should be in an mcb server so you can simply connect your credentials I use this desk credentials

and then the available actions as soon as you save this things up and reload it here this is

important this actions will occur and you see that you have the brave local search and also the brave

web search so what's the difference here if you use a search query it will automatically use the

right tool for you if you want to search for example for local businesses and places the brave

local search will get automatically used because this thing is smart and if you want to do a normal

web search the brave web search will get automatically used here on this normal brave search API you do

not have any chance to use specific things so if you want to include the local search just include

the local search and if you want to include both just click on both and if you use tools that can

include like 10 different things you can make 10 different API calls with one single tool this is

generally speaking a lot more powerful so if you use for example the normal brave search API you

have only one API call setup and not specifically for an LLM and if you use the brave search mcb you have

two things connected two different API calls and they will get translated completely automatically

for you if we put the lead for example the brave search API right now and we save this thing up

right now I can ask stuff about local search and also about the normal web search so if I open this

up and I ask something like about a local business the brave local search will get executed and if I

ask once again what's the Bitcoin price the normal web search will get executed this is generally

speaking the big difference with mcb inside of low wise of course you have a lot more mcb's you have

this custom mcb tool and if you include this you see that here you can include different things

you can simply include code snippets just like you know the command would be npx then the arguments

dash y then the model context protocol that you want to use and the path that you want to

give access to this is a example for the file system mcb but I have to tell you something normally

this should work perfectly but low wise has a little bit of problems with this npx commands at

least right now at this minute I am sure they will fix this if you press plus once again and you come

down you see that you can connect also the get up mcb the boss grass sql mcb sequential thinking

slack and also the super get where mcb so you can simply play with this mcb's just like with the

brave search mcb and one thing that is also really powerful is this thing right here because here

you can connect to ss en points so the server sentiment as you already know in this video we will

make it simple I want to delete these two things right now because we will come back later to

these two things we will simply leave it with the brave search mcb by the way you don't have to

use this mcb you can also come back and use the normal brave search tool if you want to play with

the tool first so let's just include once again the tool for example and delete mcb and we connect it

and then we will work later with these mcb's a little bit more details so that we don't have too

much in one single video so let's just go on with some tools once again we press plus once again

we can come down to tools and see what we have we have the cheerio web scraper so this thing can

scrape web pages for us you already know this and if you add it you can simply connect it to this

tool agent you can press on additional parameters if you want and give a tool description if you like

and then you can scrape web pages is really that easy next we have the chain tool if we want to

chain a few agents together we have the chat flow tool we have the code interpreter if you use the

code interpreter you can give the credentials you can simply google them and then you can run

Python code in a sandbox environment so similar to the stuff the chat GPT is doing and you can make

for example some charts and do whatever you want it's really that easy you can always just connect

such a tool there you are you can give credentials and then this tool will get called and will be

executed I'm sure there will be added new tools all the time so if you want to add this

code interpreter and if you want to run Python code in a sandbox environment you can use this

code interpreter but then if you scroll down once again you can use for example compose IO I want to

show you this at the end of this video because this is a really great tool then you have current time

and date you can simply include it there there is no big deal you can simply throw it on tools

save what time and date is today and the thing simply knows time and date and uses this time and

date tool of course you can make custom tools I want to talk about this custom tools later in more

detail because here we need to add a little bit of chava script code so this will be for later

because right now we do not want to code but remember you can absolutely add custom tools then you

have the access search the google custom search the open i api toolkit you have rate files request

get so you can execute hddb get requests you can access hddb both requests you have the retriever

tool for the vector database more than that in the next video here some other apis in order to call

the internet you have a striped agent in beta I don't like this because financial transactions for

agents yeah maybe we are not there yet the tabilly api web browser wolveramalva and write files

so you see mostly stuff for internet search tools but also stuff like write files so we can also

include this thing here at tools and give here for example a path to our local machine I just give

a path to this thing right here so I copy the path of this folder I included this is my pdf path

I can press safe and now I can ask something like this for example what are the news about tesla

today save it on my machine if I send it out we should use two different tools first we should

search the web with the brave search api and then we should write a file on my local machine and

there we are so you see we used the brave search api in order to get information about tesla

and then we used the right file tool in order to write the news on my local machine here are the

news and you can also see that this stuff got executed so everything works perfect even if we do

not use a system prompt and actually if I come to this folder and open it up you see that I no

longer have only this pdf but I have also tesla news from today and here are the latest tesla

news from april 29 2025 this is the date of today and some news now let's just talk about composer

yo if we throw in composer yo this is a tool that you can also add to your tool agent and composer

yo can actually do most of the things that you can think of you need here connect credentials

you need the app name the office status and the action to use you can google compose a yo come to

this link you can sign in or sign up this is actually for free and then you are in app.composeio.deaf

slash dashboard here on getting started you get the stuff that you can start in python but we

do not use any python here we can do this really really simple you can press for example on all apps

and see what you want to connect with flow wise let's just say you want to connect to gmail or google

calendar or notion or google sheets or a slack or super base or perplexity or twitter or whatever

you want to connect let's just make a generic example with the google calendar you can press on it

set up google calendar I am already connected in this app but if you are not you can simply press

OAuth 2 and save and then you can simply go on and try to connect with your calendar

of course you need to give your google account and go on and then you are connected and as soon as

this thing is integrated you can actually close it down then you can come to api keys you can scroll

down and you need to have the organization api keys and you can copy this api key then we come

back to flow wise you can use your credentials here I actually will create new ones we delete this old

insert and you won't impress at then of course we press save and now you can go to the app name

you can press on it and see for yourself that you can connect nearly every single thing that you

want you can connect it over you can connect the finity air table or so over here amazon a baller

and a lot more so you can basically connect with every api you want as long as you give access

over composer you but what we use is of course the google calendar so let's just type in google

it's the google calendar then the calendar of course you have connected this previously so of course

on all apps you have give access to right here then you need to reload this once again you press on

this OAuth and this is of course connected and then the action to use you can also reload this once

again you can press on it until you do see some really interesting stuff you don't have just one

thing included but you have a lot of things included google calendar create event delete event duplicate

find event and so on so this is completely the same thing as an mcp server you can connect to

one single api and you can set up everything lapi call that you want this is powerful so compose

are you with basically the same thing as the sape or mcp server or at least really similar and let's

just say google calendar create an event so create an event in google calendar you can press on it

and now actually we can create events in my calendar it's really that easy let's just press save

here and make a event in my calendar so create an event in my calendar for tomorrow at 6 pm

I want to go shopping and I send it out actually this tool asks me a few things before it can do it

so let's just start first primary calendar second EU Berlin time third I want a pc fort only me

and there we are so you can see my agent also used the current date and time in order to see what

date and time we have then it used the google calendar create event in order to create an event into

my calendar and it tells me that it has created an event shopping for pc Wednesday april 30th

2025 6 to 8 pm European Berlin timezone and so on so actually let's just check my calendar if this

is true or not and now if I come in my calendar but actually we can see that at 6 pm we have shopping

for my pc so this is completely perfect so long story short with this compose io2 you can connect

every single API that you want and it's of course I think the easiest way to connect a lot of

different APIs to this dual agent you can simply come to compose a yo then you activate the API

that you want to trigger out of your application and you can talk to it over this interface and here

you can also add new stuff so let's just press on it google calendar get let's just fetch stuff

in my calendar you can also ask questions now about your calendar so actually let's just ask

what is tomorrow on my calendar search the main id so let me check what's on your calendar for

tomorrow first it used the current date and time then the google calendar get and it's

searched in this calendar event of course and it find also shopping for pc and of course at this

time zone so this is completely perfect all of this is working and you can really connect whatever

you want you can simply add a new compose io tool so if you press on plus once again

throw in compose io once again connect it give once again your credentials rack course

then the app name like whatever you want and you can give access to every single API that you want

and sooner or later you need to tell this thing in the system prompt at what point it has to

use what compose io tool so this is i think one of the most powerful things that you can do you can

interact with youtube you can interact with fire crawl with figma with this court with reddit you

can interact with whatever you like please don't sleep on this tool this tool is really great

and the last thing that i want to show you just briefly because it actually does nearly the same

thing that then compose a yo but here you can do it with custom code is of course this custom tool

so actually let's just throw it in i have also shown it previously on this custom tool you can

select this tools and here you see that i have basically a lot of different tools so i have also

here a sent mail tool i have add air table i have some stock information tools and a lot more

add context i have a make webhook slack air table and so on and if you simply press on one of

these things here so this add air table you can also come here and see how you can make this tools

you simply give a tool name a description then you give an input schema and then you need to write

a little bit of chava script code but because i have told you that we will do a little bit of

coding later we will not do it right now i actually just want to give you a quick tip how you can

use this custom tools so right now i want to delete this tool once again and save this chat flow

then if we come back right now come to the market place and here research on type for tool

you can see that you can basically search for yourself so let's just say you want to have access

to perplexity AI search you can simply press on it then you can press on use this template and

here is actually this code already included so use template add right now this is add add then you

can see for yourself if you come to tools you will see that perplexity AI search is already

added here and if you come back to chat flows scroll down to the dual agent test course press plus

once again add on tools your custom tool you can connect it press on it scroll down and use the

perplexity AI search you can edit it and see for yourself how this tool is working so perplexity AI

search useful when conducting research using perplexity AI online model then we always send the query

the query is a string query for research and here you can basically see that this code is working

and everything that you have to edit here is on your API key you need to put your API key here

from perplexity and then you have perplexity successfully connected to flow wise so you see these

are really really powerful workflows and you can do whatever you want with it and remember as soon

as your replication breaks you can come of course into the system prompt and tell AI agent on what

tools it has access but for me right now it did not broke down so you can absolutely use this

tool this tool works without any problems so what I do of course is to press right here export chat

flow and you can also use this workflow for you everything that you have to do is of course to

connect your API keys for example to compose a yo if you want to use perplexity also connect per

plexity you can also use this custom tool and basically that is everything that you need to know about

this tool agent if you want to use every single thing that you can use except rack because rack

is the theme for the next video so see you of course in the next one and in this video you saw

basically that you can ever think that you want to do with the tool agent inside of flow wise

you need to connect the chat model it should have function calling on open router you can find

every single model under the sun that you want just check what works for you you can also use

free models you can connect the buffer memory a calculator different web search tools

current date and time write files in order to write files to your disk you can also connect

to read file if you want you can connect custom tools but what I like most is the compose IO tool

because it's the easiest one you just need to include one simple API key from here you throw it in

then you can come on all apps and connect every single app under the sun that you want to connect

with your application so don't sleep on it have fun you can build out whatever you want with this tool

this tool agent is powerful