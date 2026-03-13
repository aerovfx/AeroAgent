# 16 -Connect Every MCP Server (GitHub or Python Servers) to n8n via Community Node translated

---

Until now we talked about the native integration of the model context protocol inside of Aneden.

And I have to tell you, this is a really really great integration.

So don't get me wrong, but I also have to tell you that this integration has some downsides.

You already know it.

IMCP tool should at least in theory be able to list all the actions out that one single server can do.

For example, if we want to connect with the Airbnb server, the Airbnb server should be able to list

every single action that it can do.

And this is absolutely not possible if you simply for also some tools on your normal

mcp integration inside of a native mcp server from aneden.

But we have IMCP tool from a developer that is inside the aneden community.

So we can install our external node.

And as soon as this node is installed, we can use actually a different backhatch to run different

servers. And we can also connect to get top servers.

Also, this was not possible with our native mcp integration inside of aneden.

And if we use this, we can list our tools and we can also call our tools.

So we can make simply one API call.

This API call will be perfectly structured.

It can list out all the tools and it can also execute all the tools with just one single API call.

This is the most powerful mcp possibility that we can include and we can also combine these two tools.

So basically we can also make a mcp server, the native integration, and then connect it with

the community node to have both words. In this video I want to show you everything.

The first thing is of course that we need to be on either our local host or on the aneden server

that we have hosted inside of hosting or at least in my case. Also render will work.

But rather you have your application hosted. It is important that you are in a self hosted one.

I would assume that also the aneden app will include these nodes over time.

This can take a tiny bit. Aneden actually does a really great job in order to integrate

also to the community nodes inside their native platform. They have already included a lot of

different tools. They have included for example a OCR tool browser flow and a lot more.

Also quadrant, scrape graph AI, 11 laps, desert API, and soon they will also include the brave search.

So basically they do a great job to include the newest developments from the open source community.

But at least at the time as I am recording this video, the community node of them cp server is

nothing included. So we need to install this node ourselves and this is also basically a great chance

to show you how you can do this. If it's already available as soon as you see this course,

of course you can simply skip the installation of the node. So what we are doing right now is

we are either on our local host if we simply want to test this out or we come onto our self hosted

version from hosting her at least that's where I am. And then we need to press on our name down here

and here we need to come to settings and in settings we will find these community nodes.

And here we can install basically a lot of different community nodes. You already see it?

And I then notes mcp I have already installed this in my local instance. Also my hosting are

instance if we come on settings community nodes. You will see that this thing is installed and

actually I can make an update here. And I want to show you how you can install here different nodes.

Basically you just press here install and then you can and then you can come on browse.

And here on browse you will find actually a lot of different packages. There are 1000

packages and I also have to tell you that you need to be cautious here because some nodes from

the community they can have malicious code because everybody can just make such a node and there

are like over 1000 and not every single one is controlled by the NADN team. But one node that

really works great and note that a lot of people are using is the NADN node with mcps. So this is

one thing that you absolutely can install this should work great at least for me it always works great.

So you can simply copy this name then you come into your NADN instance either the local one or

also hosting or if you want then you can include the package name so you include it here.

You press I understand the risks of installing this node and then you can install this node.

Because I have already done this basically I'm here and if I want to update this node we simply press

here on update update package and boom then we should basically be done. I will do the same thing

also for my hosting or instance so we simply press update update package and boom now I am up to

date with both of these nodes. As soon as the node is installed we can work with it and I want to show

you two really powerful workflows first to stand alone application and next of course so you can

even integrate this into an mcp server. So we come back on settings and we create simply a new workflow

then we give it a name let's just say community mcp course test then we press plus and I actually

want to start out with an AI agent we want to make this as simple as possible and we use a chat

trigger then we need to use a chat model I like to use once again an open AI model you can also run

with open router do whatever you like and now we need to connect tools and on this tools we will

connect to this community node and this will be really great so you can simply type in mcp right here

and then you see that you either have the mcp client tool this is the official integration

but as soon as you see this queue here you will have a community node this is the community

node that we have installed and if you press on these you will actually see that this gets

included automatically then we press plus once again and once again we should include our mcp

client tool here and this thing is right now a little bit different because on the second one

we can simply use not the list option but for example the execute tool and we can run our

tools so the first client will basically just list our tools and the second one can execute our

tools and you see that we can have here also get prompts list prompts list resource templates

list resources list tools and rate resources so with this community node we can actually do

every single thing that an mcp server can do we will make it really easy in this video we will

talk about tools because I do think that especially the Airbnb tool is really great for testing this

out so we have a list tool and we have an execute tool so we save it and right now we need to

configure this but we need to configure this the right way the first thing that we want to configure

is the mcp client with the list tool and I can also call this mcp list so our agent can call it a

little bit nicer then we need to create new credentials because I want to do this once again

from scratch so that you can see it then we can use different commands so we can either communicate

with STDIO we can communicate with the server send event and we can also communicate with the

HTTP streamable and now it's important that you understand what you want to do if you simply want

to work locally just use STDIO if you want to host your application later you should use the

server send event and the HTTP streamable then we need to include some commands and arguments and

lastly the environments so we basically can come for example to get up and we search also let's just

say also mcp servers on get up and we press on them and I just want to configure once again the

Airbnb tool because I do think this is a great tool so we simply search the Airbnb tool right here

and we press on this mcp server from the Airbnb tool this is a tool with a lot of stars a lot of

people love this tool but you can configure or exactly in this way every single server that you find

on get up and if you program a server and pipe you can also connect your server exactly the same way

inside of an event so this is really powerful you can do everything that you want with this tool

let's just scroll down here on get up and here you can see what we can do we have the Airbnb

search and we have the Airbnb listing details so we can basically do a lot and if we scroll down we

can also see how we can set this things up of course we need to have no JS this is no problem

because an add-on works with no JS so no problems here and here we can see what we need to add in our

cloud desktop config file and we also get basically all the arguments and commands that we need the

command is of course npx the arguments is dash y and then we get this urn and on this specific

server we also have something special because we need to ignore the robots dxt if somebody is here

that understands SEO like the robots dxt something like a side map you can also search for it if you

simply google n-edm and if you press on it and if you type in after an edm slash robots dot txt

it will be on a side map like this and on these robots you also find the side map with the

6ml and the side map basically lists you all the links so all the sub links and also on this

side map you can come for example to even more links this is just for SEO so that people can find

this web page like a lot better and for our mcp server we need to ignore this robots dot dxt

so what we need to have right now is of course the command it's nbx so we copy the command

we come back to an edm and we include the command right here it's npx then we come back to get

a book once again and we need all these arguments so we can basically copy just all of these arguments

then we can come back once again into an edm and we include these arguments here and here we

need to make sure that we don't have any syntax errors basically what we do not need is this

quotient marks so first we will delete all these quotient marks and then also the spaces we don't

need all of these spaces right here everything that we need is just a comma after every single argument

and one time the space bar and then we should be set or actually I also think that we do not really

need these commas here so basically it should be also fine exactly like this so the arguments are

dash y as you see right here the first argument is dash y this is simply i yes so you already know

it yes to ever reprom that we get then of course we have the URL from air bmb and this would be

the moment in most cases simply enough but the last argument that we also have is to ignore

the robots dot dxt so that we can simply get everything without like hamas and lastly we need to

include some environments and in this environment you need your API key but the air bmb server

is special they don't want to have an API key I personally don't know why they don't want to have

an API key but it is how it is if you use like other tools like the brave search and so on you

absolutely need an API key but air bmb does not need it so we can simply delete it and be press

and then boom you see this thing is green so we are connected with the air bmb server and you see

that we are connected right now with the air bmb server of course it's a different name because I

have already set this up and we communicate via stdio and I also have to tell you this is also not

problematic even if you publish your server because later I want to show you a great trick but for

testing this out stdio is perfect and later I want to show you how we can even leave this at

stdio and communicate on a publicly hosted server so the mcp list tool is configured actually let's

just test if this tool is working we delete the second one we press safe we press open chat

and right now I simply ask what can the mcp tool do and we should list everything that our mcp

server can do we have the air bmb search this allows you to search for air bmb listings with various

filters and so on and we have the air bmb listing details so we can simply search every single listing

that we want so basically this is what we can do now we can configure our next tool so we press

plus once again we have already included this previously but let's just do it again and what we

need to have right now is of course that we will connect once again to our same mcp setup here

we call this let's just say mcp execute rename the tool description is once again automatically

but this time we do not want to have list because we want to execute our tools and now this

thing is getting important we need to have the tool name and we need to give some parameters

actually let's just try to configure this so we want to start of course with an

anemic variable and we come to expression and make the speak to make it a little bit easier

so we start with two curly brackets and we get this auto completion what we want to have right

now is of course dollar sign then we want to have from AI and you see we have the auto completion

then we open up actually a normal bracket in this normal bracket we start with quotient marks

and we call it tool then we go outside of this quotient marks comma and actually we want to have

quotient marks once again and in this quotient marks let's just call this mcp tool to execute so

we give the name of course from the AI the AI gives dynamically every time the name with the tool

of them cp tool that we want to execute I do think this name should work because we get basically

everything back here if we come down here you see the mcp list tool first of all will list in

chasing what we can do and then the name will be let's just see and then the name will be

automatically updated here and then we need to come to parameters and here I want to do the same

thing I just want to make this big in expression with a lead this thing right here and once again we

start with two curly brackets and inside of these two curly brackets we start once again of course

with with dollar sign from AI we get our autocompletion we open up our normal bracket and we call it tool

underscore parameters and of course you need to put this into quotient marks then before we now

comma once again quotient marks I do think that we can leave this also empty let's just try this

out I need to figure this myself out let's just see because we do have three things so once again

new quotient marks the third quotient marks and here we call this Jason I do think this should work

if you have problems here you can also talk with chat ebd so let's just see what we are doing of

course the AI will decide here the tool because we have also told this right here from AI

then you see that we have the tool so the tool parameters then the mcp tool to execute will

basically come here I think and lastly we communicate with Jason I do think this should work so

actually let's just save it and now we can ask something so we reload it and now we see if this

is working and if you have problems with these just please run with my thing and use my thing in order

to train chat ebd so you can simply copy this throw it into chat ebd and ask chat ebd why does this work

and how can I make this work for a different ssn point for example so let's just see if this

is working before you can copy this from me where can I stay in New York for example on July 25th 2025

search a air bnb I sent it out first with list of course what the disserver can do then as soon as

we have our information our mcp execute tool will come and it will basically fail so we need to come

to debugging so let's just debug you see I leave this burp as they include it because sometimes

we will run into errors this thing tries now to call this tool over and over and over again so I

simply stop this tool then we come into this tool right here and let's just see where my problem is

first test I do think this should work basically but what can be false right here is tool barameat

errors so I want to have an s included and of course I also have come on a type in JSON it's of course

JSON this way so barameat errors and JSON should be fine and also this I do think also this is a

mess we need to close this bracket right here I think so actually let's just test this out once

again first safe reload throwing the same question we send it out we call them immediately the mcp

execute tool and boom right now it's working so you see this is perfect here are some air bnb

options available for you to stay in New York on July 2025 we basically have this right here

and that one and also this one and we get also the links that we can open up so let's just see

I do think this is fine we are on air bnb this is in German right now because like I speak

German so this finds German info for me but I do think this is completely fine this is completely

perfect close this down if we come for example into the AI agent we can also give a prompt that we

want to use the list tool always first and then execute tool for example add option system message

always use the list tool first and then execute we save it we close it and right now I do think

we have a functional mcp server actually let's just test this again I want to check this with

our location where I am living so that I understand if this thing is working correctly or not

so let's just close this down I search air bnb and Italy south tyro it should be near

brunac this is basically a city near by me I want to stay from let's just say August 15 to August 20

we send it out let's just see we call the list tool first this was also something that I have

included now the execute tool and now we should find the air bnb that is near by me let's just see if

this is working and boom romantic castl view price 150 euros per night roughly total for five nights

it's 700 euros good rating with a lot of reviews free cancellation and so on and this is the host

actually let's just open this up if this is really in boom neck romantic Schloss Blake actually I

know this this is of course in brunac in Italy yeah great job air bnb tool then the next one roughly

the same price a little bit cheaper because it's enough for let's just open this I don't know this

but it's also in boom neck in Italy I do think this also should work actually this thing I know

this thing I also know this thing and also this yes it's really great these are all things that I

personally know they are near by me so we are really really great our air bnb tool from anaden

works and it was relatively easy to set up we simply use the mcb list tool to list all the

available options that we can do with our mcb server and then we can execute our options we had

a little bit of a mess of course with this chase format because sometimes I'm damp I had a

type in chase and I have closed basically my bracket too soon but right now I do think that we are

ready to rock and now I want to show you how we can connect this to different hosts because also

this is possible so you can connect basically exactly this thing in every single host that you

want not only from anaden what you have to do is to simply copy this thing then of course what we

will do next is we can come in a new workflow but you can also stay here you press plus what we

want to do right now is we use an mcp server trigger and on this mcp server trigger we simply

connect these two tools so we simply include them from right here and we can connect these tools

right here and there we are we could also connect these tools right here but I do think this server

gets a little bit too big over time but of course you can totally do this and if you want to connect

this of course you can simply copy your production URL you would make it public got it then we come

into cloth we open up of course our settings developer edit config file and on our config file

basically everything is connected but of course we need to change the URL so we would delete the URL

and include that one and we save it then we would restart cloth and right now you see that we have

the anaden tool also included inside of cloth desktop so you can also call this tool from

cloth desktop if this fails for some reason it is most likely because you need to set up a ssen

point so of course everything that you have to do is to switch from stdio to sse and you basically

know how to do it you create new credentials and this time you use the same credentials but you

use the server send the vent and then you are basically done so in this video you have learned a lot

you have learned how you can use the community note and the community note is rarely really great

because you can connect basically ever a single server that you find on get up this is something that

is not natively included inside of anaden everything that you have to do is of course first of all to

install this community note and then you can use it you can use the list tool and you can use the

execute tool you can simply copy all the stuff that you find on get up and include it and you

can use a list and execute tool and call an entire mcb server without the needing of integrating

like a lot of different HTTP request calls as soon as we have for example gmail mcb officially

like on get up or on wherever we can simply connect to the stool our mcb server can list

everything that the google API can do and then can execute so this is a really great server and

this is a workaround so you can access ever a single get up server from anaden but you can also

make sscn points and if your application is hosted actually you can also give access to other people

this is a great way and i'll see you of course in the next video