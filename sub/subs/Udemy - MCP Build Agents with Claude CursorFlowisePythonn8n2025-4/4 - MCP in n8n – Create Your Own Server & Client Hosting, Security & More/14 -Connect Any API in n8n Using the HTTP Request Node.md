# 14 -Connect Any API in n8n Using the HTTP Request Node translated

---

This video I want to show you how we can integrate everything LAPI that we want.

Generally speaking, NADN already offers such a gigantic library of pre-builder tools of pre-builder nodes.

But sometimes it can happen that a node is no longer up to date, is no longer maintained,

or it's strict just not there for you.

And if you have an API on the other hand that you can call, you can call this API via an HDDB request.

You already know an MCB server resource of perfect just as a wrapper around an API call.

And most of the time if we use a tool we simply do this.

And if we already have a pre-build tool, it's of course really perfect because it's easy.

You already saw this. We can simply press plus and then include the stuff that we want.

If you want to have for example the Brave Search API right now it's not there,

but I do think NADN is working on actively include the Brave Search API.

If we search for the weather API right now we do not have it for example.

If we search for Vlax for example we do not have it.

If we search for GPT1 I do think that OpenAI has released this right now,

but if not I also want to show you how we can integrate this later via HDDB request nodes.

Generally speaking you can connect to ever-resing API even if it's not there.

I do think we have a double node right now.

This double node is a community node.

You should also be a little bit cautious with this community nodes because everybody can

build this community nodes out. Normally this after defined inside of NADN it's

already verified by NADN, but you can sometimes not trust community nodes.

Let's just put it this way. That's why I want to show you in this video how we can connect

ever-resing API if you do not find the right tool. I have to tell you it's totally possible

that you do find this tool as soon as you see this course. Always look first if you find the

node that you want to include and include it if it's there. If it's not there you can include

it via HDDB request and that's exactly what we want to do right now.

We have found out that we do not have any weather API. So we will include a weather API.

Maybe a weather API is practical for you. This is just for the sake of the tutorial.

So that you understand how you can call ever-resing API. Later we will do more API calls to more

different APIs. We will also include maybe a search tool right now that is not necessarily

include at the RONDIA community node. You should just understand that you can include ever-resing

API via HDDB request. So the first thing is of course you press plus and you search for the HDDB

request tool. As soon as this is included of course we need to configure this tool. First let's

just toss this calculator because we do not really need it and let's make a configuration on this HDDB

request node. The request is get. You already see it and now we can press on it and here you also see

that later if we add options we can include a little bit of code but I promise this will be easier

than you think. The first thing that we want to do is to rename this. Let's just call it HDDB

request or maybe weather HDDB request. So we will rename it that we call this tool immediately

the right way. Makes an HDDB request and returns the response data of the weather API for example.

Then the MFET 99% of the time you want to have either get if you want to get information here

or you want to have post if you want to send information. Delete is like only in some specific

use cases if you want to delete an email or something else but normally just get or post with

these two methods you can basically connect to everything that you want. Then you always find a

new URL that you need to include. If you have IBI key you need to do this via this authentication

and then we can send to the parameters that are important for our API call and we also have this

option to import a curl so if we find a curl we will simply import it you will also see how we

can import a curl inside this video. So you will be covered after this video to set up every single

API call that you want. In this first example we want to have a get request because we want to get

the weather data. Then the URL we will include it before we include this URL I have to tell you

that at some web pages it's also enough to just include this URL without any other things. If you

just want to scrape some HTML content you can just simply make a get request to the URL without any

authentication and you get the HTML. If you actually Google weather API you find a lot of different

services. One service that I really like is this free weather API because we can test it completely

for free. I do think you get premium features for like one or two weeks, 100% for free and then you

get a lot of free basic requests so make an account here on Blogger'selfin. As soon as you are logged

in in your account you will get something like this. Most of the time you will get like a pro

plan for free in the first weeks or so and then you will switch automatically into the free plan and

you get of course also a lot of calls completely for free. You also get your API key right here but

before we will use this API key I want to show you how we can set this things up. You can simply

scroll on the left side press on this API explorer. Here we come to the documentation so docs and

here you can see what you can do on this API. You get the real time weather you get a 14 day forecast,

you get the historical weather, you get basically a lot of cool features here everything that is weather

related basically and then if you scroll down you also see how you can get started you just need to

sign up and so on. We already did this. Then you need of course your API key always and then you see

how you can structure your request. If you just want to have the current weather you will make a

request so the API method to this URL. If you want to have a forecast you need to do it at the

URL. If you want historical data you need to do it at the URL and the base URL is of course always

this thing here. So of course what we should do is to simply copy this base URL as soon as this is

copied we come back into an add-in and insert the base URL here. So we will get the information from

this base URL and of course I can also fix my dipoles it's of course weather this way excuse me

so weather rename. What I want to include is of course the current weather so we have this

base URL now we come back and after this base URL we need to include the URL for the current weather

and it's of course this right here and I want to have it in JSON because and it then always

communicates with JSON also XML would work eventually but I want to work with JSON so we copy also

this we come back to an add-in and after our base URL we also insert of course the current dot

JSON boom and there we are we are perfect this structure for our API call but API also tells us

that we need to have key parameters and we need to insert our API key so we come back of course

we want to send out headers and on this headers we can define everything here below

and the name of this parameter is of course key just you can see it here and after that is the value

and the value is of course your API key so you can basically come back to this weather API right here

yeah I have to log in once again excuse me so my account here I get my API key so I copy the API

and then we insert the API key down here as value when there we are so we have our base URL we have

the exact URL that we want to call we have our authentication and of course we need to send out

parameters this is important so we also accept the parameters that we want to send out and if we

come back of course into our console here we come back once again on this API explorer and here

you see that we dock via HTTP in chase the parameter and value if you come back into this documentation

you also see what you can and probably should include so the request parameters you always have

a parameter it's of course key this is required we already included this and we have also

included the API key then we have the next parameter it's also required and here we need to give of

course the location where we want to have the weather from and then for example the days this is

only required if we want to make a forecast for example so you can set this up however you want

but we will do it relatively easy this is just for the sake of this tutorial so we include just

the stuff that we need to include so required is of course the parameter Q and on Q we need to

give the location with the value so we come back the parameter is Q and the value is let's just

roll here with London because we assume that we are living in London or this application is

specifically built for London so I include London here but of course you can also change your

parameters you can pass you us zip code UK boss code Canada boss locate IP addresses latitude or

longitude or a city name you need to test this out for yourself what works for your location

and as soon as this is included I do think that we can simply press execute step to test this

things out and boom you see you get your data back from this API if you come to table you get it

in table format if you come to chase and you get it into chase format table is for us perfect because

we have the location is of course London the region is the city of London it's in united kingdom

we have latitude and longitude we have the time zone the local time then the temperature in Celsius

in Fahrenheit we have light rain what else in London we have also the wind we have basically

every single thing that is important for a weather API if you come back on this documentation from

the weather API and we scroll down just a tiny bit you see these are all the parameters that we

get back so everything was perfect our API call works so right now our MCP server also has access

to a weather API you just need to press safe then you open the chat for example and you can ask

how is the weather in London right now and remember we have also structured our AI agent with

assistant prompt that it understands what time it is right now so we should get everything back

just perfectly fine temperature is 15.4 grad Celsius we have light rain and this is the wind

so I do think this works really fine and if you come on executions let's just see we have basically

made a HTTP get request to this weather API and of course I don't have to tell you if you come back

into cursor and you reload this thing we will also get our weather info right here weather HD

to be a request and the same thing is of course also true for a cloud you need to restart cloud

and then you can ask everything about the weather from ever-easingly client that you want

and this is basically how you can set up ever-easingly API call that you want let's just make it bigger

with an example where we can import a curl for example because this is also sometimes really really

practical so let's just include doubly this is an internet search tool that a lot of people love

because this is specifically made for LLMS I do think an event will include this over time but if

it's nothing clue that you can do this also here we will make a get request and we will simply

import a curl because we need to set up some chasing data but I promised this is easy and later

we will also make calls to models that can generate pictures as soon as we start to talk about special

workflows so we simply come on tably here you need to make an account with do whatever it's necessary

I just log in because I already have an account here we are immediately on this overview and you

see that we also get an API key here we always need to disable the APIs keys but a good starting point

is always the documentation so we press on the documentation and you also see that we have

basically a tably mcp so I want to open and dis up because I do think the mcp of tably is new

and we also open up this documentation let's just come to this mcp because I have never

found this yeah you can also use this via gettub this is maybe for a later video because we can

also include gettub servers to an add-in and maybe if you want to program your own server you can

also set it up with a tably mcp nice to know this was also new for me so they will always include

new stuff here also I learn all the time for right now we want to make our own mcp server because

we already have this gigantic one so we come of course to the API and here we come to the API

reference until you do see a little bit of code but I promised this is a lot easier than you think

and here on this tably search you see the following execute a search query using tably search

and here's also interesting that you need to send out a post request in order to search information

and on the right side you see how you can set all of your information up you can do it in

byte and in JavaScript in bhb in go or in Java if you develop your own servers in like a programming

language you can simply import this stuff here but what we want to do is we need to set up of course

this chase format and we can simply import our code it's really that easy we can simply copy all

of this code then we can come back into an add-in of course we need to have a new httb request tool

on this httb request tool we call this for example web search makes httb request and returns the data

of the search query and then everything that we have to do is to simply press import curl

here you can simply copy all of the stuff that you have included and then we import it and boom

we have automatically set up our whole node the method is post exactly as you can see right here

the URL is of course the tably.com search exactly as you see here then we will send of course

and on the header we have our authorization and we send the value with pair and the token exactly

as you see here everything that we have to include is of course the token later but first let me just

scroll down you do not have to do anything because at the last part here we have the body content

type it's chasing and we use the chasing below and here is the rest of the chasing this time the

query is static we need to change this later to dynamic this chasing query is who is Leo messys

or we will simply send out a search query that always asks this question but later we want to

include here a dynamic variable so that we can ask questions that we want to ask basically so

let's just come back of course to this API and include our API key for that we come back here

and we simply copy this API key we come back to an add-in we scroll up here and on this token

so where this token is we can simply delete this and insert our token and boom now we can simply press

execute step we do get an error let's just actually test it again boom once again a error and

we also find here a error logs let's just see what could be not right status 442 but request I do

think this is because it expects that we give for example the country we do not have the country

here the time range we can also include the time range but I do think it's actually the country

so what we could do is either delete country entirely or give a country like the us or europe

or whatever I just want to delete it completely delete also this last comma I save it and then we

press test step once again let's just see testing twice make sense boom we have one item let's just

show this data because actually we get a lot of data and the data is the query who is Leo Messi

we have no follow-up question of course Leo not Messi is and so on so I do think this totally works

we have stuff from Wikipedia we have yeah like we have a lot of search stuff here from Leo Messi

but the only thing that we cannot do right now is of course to ask questions about other stuff

because our query needs to be dynamically used from the AI so this is really important right now

I do think that our web search tool works but what we need to have is right now a dynamic query

so actually we could ask chatch ebd or we could ask this AI here in order to set up our API call

for our dynamic question what I want to do is I simply copy all of this and then we ask chatch ebd

to format this in a way so that the query will get decided from the AI let's just use

over and we ask something like this I have this API call to tably it searches the web but I want

that it searches a dynamic query from the AI then we include for example our chaser structure

and maybe also the link to this documentation and then chatch ebd can do a lot for us here is docs

let's just see if chatch ebd can solve this and if not we will solve it ourselves in the meantime

while chatch ebd is thinking with the in this documentation so it's a string that is required

and here is just the example included so I do think we can simply add it also this query inside

of the chase format let's just see what chatch ebd uses here as query is only user's query

but it actually messes up a lot of other stuff so we simply yeah let's just try this query equals

maybe the AI is smart enough for itself to decide so we open this up so instant of who is Leo

messy we include query and I only need the ones so query is query we can delete this part right now

we have no syntax and now we can simply ask let's just actually save the workflow and ask for

example what are the news from apple search the web we trigger the client client should trigger

the server and then we see if we get an answer back or not first I got one or two errors but right

now it simply works and I want to tell you what the error was if we simply come back to this note

here I just show you exactly what I needed to do so first import curl as always just import it

then of course on this token insert a token just like we did so we copy a token we've

wrote within here then on this chase also here the same thing as with it so simply delete this here

inside I also typed in query exactly ever a single thing that with it but the only thing that I

did in order to fix my error was here to let the AI decide this different parameters and today

AI decided simply the parameter query for us so we simply need to press on this button and then

our API calls work everything that we have to do is to press save and right now we have the

devily search include the tier so let's just reload this and actually ask something else

so right now we simply want to test this right here what are the news from tesla today maybe

search the web and we see if this is working or not here are the latest highlights about tesla

the stock is slumping as Elon ramps up attacks on trump's big beautiful bill and so on

some senior tesla executes were reported and so on then something about self-driving I do think this

is great let's just come on executions our newest execution both of course a call to our web

search tool and the web search tool told us exactly this from Yahoo Finance then from tesla

news and so on so you see basically we had a good research result here everything seems to work

but I have to tell you this tool so devily sometimes it's not perfect I personally would love

that and then we'll include this but I do think they will include this so sometimes this htp

request notes can also be a little bit difficult to set up because they will or can make some

mistakes from time to time don't worry later we will dive in in more reliable notes but I do

think you do not have to include this devily search at least not with an htp request but in general

you can set up everything lp i call that you want right now with this simple tips you can simply go

always on the documentation of the API you make a call like you saw with the weather API it's either

a get or post on the URL maybe you need to give a little bit more specifics on the URL then you

need to always send the parameters that you want to send and maybe insert an API key and the same

thing was true of course also for our second API call this time it was post to tably and we

imported our call and then we needed to mess a little bit with this chase but right now it works

and I'll see you of course in the next video right now you know how to set up everything

lp i call if you do not find a note but always make sure first to check if you've already

find a note because sometimes we spend a lot of time in order to configure API calls and maybe

you can just do something like this you can come here and use instant dessert API for example and

here we have an official integration or the elastic search so basically you will always find options

here inside of nade and if you do not find an option make an API call