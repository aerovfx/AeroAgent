# 6 -Create MCP Server in n8n and Use the Google Cloud Console translated

---

In this video we will create our first MCP server and we will do it as easy as possible in an ADN.

It is a no-code or low-code environment so you can absolutely do this.

And I have to tell you we will communicate via SSE so the server sent the event.

And this is also really really great if you want to communicate with instances that are hosted.

So right now I also need to warn you.

If you are in the plan of an ADN, this instance will be hosted in the web.

And other people can access it if they see your URL.

So you need to be cautious.

If you work locally with no choice and if you have installed everything locally,

you do not have to worry about data security because the server will only run on your local machine.

But if you work in the cloud with an ADN plan, of course other people can use your server if you expose it.

So please stay cautious. I also want to show you how you can connect some tools.

In my case I will connect for example a Google Docs so that we can include

a pen, throw, and get-row or whatever.

And then we can communicate or integrate to this also in different clients and we can work in

conjunction with all our relevant links in the next video.

So this will be really really practical. Remember you need to be cautious.

If your server is hosted, of course we will cover security also in this section how you can

integrate out the realization. And if you work locally, no problem.

The first thing that we do is of course we add our var steps so we press plus.

And it's of course the MCB server trigger. It's really that easy.

And then it already makes our SSE so our server sent the end point.

And the authentication right now is at none. So this is right now also the dangerous thing.

If you want to make this really really safe, you need to do this without identification like I said

more on that later. On this MCB trigger you can connect whatever you want but we will start really

easy. You can also connect a code tool if you want to insert

special JavaScript or Python code if you are a developer.

If you want to call a API that is not included, you can use the HTTP request tool.

We will do this later. You can use different vector databases for example Pinecon,

Postgres, Quadrant, and so on. The simple vector store super base and a lot more.

And you can also use all these pre-configured tools like AirTable if you work a lot with AirTable.

All the services from AWS. You can basically connect whatever you want to

desemst the servers with just a few clicks but like I told you we will do it relatively simple.

In this workflow we simply connect three easy tools and later we will make this bigger.

The first tool that we will include is for example a calculator because this is the easiest one.

You can just press on it and boom there you have it. And now we will include the Google Sheets.

If you include Google Sheets you actually have to follow a few steps.

So we simply press Google Sheets here, the Google Sheets tool.

And as soon as Google Sheets appears here you need to press on it and now you need to connect your

account. If you are in the hosted version of an add-in, you can connect your account really,

really easy. You can simply press create new credentials and then you can sign in with Google.

But it always depends on where you are hosted. If you are working locally for the first time,

you need to connect Google Sheets in the Google Cloud Console.

I also have a hosted instance on Hostinger and here you also need to do basically something

really, really similar. If we include for example the MCP server trigger node and be pressed plus

right here, use for example Google Sheets. Here we can also connect new credentials and here you

have something like this. So if you work locally you need to connect this yourself. If you work for

example with Hostinger I will show you the hosting later because self hosting is a lot cheaper.

You need to connect this yourself and I want to show you how you can connect this if you work

locally or even if you host it like on Hostinger or whatever because on an add-in it's really that easy.

You just have to press right here, sign in with Google and right now I want to show you how you can

connect this if you work locally or with whatever. You can connect Google really, really easy.

Everything that you have to do is to open up this documentation and please follow me along.

This are a few clicks that you have to do but you can totally do this. First you need to come to

the Google Cloud account so you can simply open up this link and then you need to come to the console.

Of course you need to make an account if you don't have an account. What you need to do next is to

create a new project. So you will press here in this corner and you press create new project

and I simply call it MCP course and then we press create. I don't include any location here.

So we create this and as soon as this is created we will go into this project and in this project you

can add every single Google service that you want. You can connect Gmail, you can connect whatever you

want. You simply have to select this project. Then of course you are here, you're working in MCP

course. Then you come into the left corner. You need to come to APIs and services and you come to

library and on library you need to search whatever you want to include. For us it's right now of course

the Google Sheets API. So you press on the Google Sheets API. You also press right here. Then you

press enable and as soon as this is enabled you need to go on. So we come on Oof.com.sense

screen on the left corner and then we press get started. Here we need to give our app a name.

Let's just call it MCP course. We need to connect our email. I just used this one right here.

Then we press next. The audience, this is important. I simply use external so that everybody can access

this. This is also perfect or better for us right now also for testing. Then we press next.

Then we need to give context information of the developer. In my case it's of course me. So we press

next. Then we need to agree here and we press continue and create. Then under metrics you get

create Oof client and you need to press on it. The client type it's a web application. We can skip

this thing but authorize to redirect your rel. This is important. So you need to press add URL

and you can find your URL of course in an add-in. So you can press on it and you see right here

Oof redirect your rel. You can simply press on this and it will get copied to your clipboard.

Then you come back and we need to insert this down here and then you can press create and this can

take up to five minutes until it's working. So you press create and then you have a little bit of

patience most of the time it's really fast. Then you also get this right here the client ID.

This is a number that I will not show you. You have to copy this number. Then you have to come

back to an add-in and on an add-in you find this right here grand type. Most likely if you work

locally you will just have this client credentials and on client credentials you get your client ID

and the access to open URL and the client's secret. The authentication is either header or body.

For us it's header right now so you can simply insert the stuff down here.

So the client ID we have already copied this so we will insert it down here. Just copy paste it,

boom and then you are done. Next we come back to Google we press here okay and what we need to

have is an API key. So you press here on edit and you also find the client's secret down here.

So your copy is client's secret. You come back into an add-in and here on client's secret you will

simply include your client's secret down here. So the leads the old one include the new one.

Lastly we have this access to open URL and here you need to be cautious. It is not always required.

If it's required you need to type in this right here. HDDBS, OAuth2, google apis.com,

slash token and then you can simply press safe and boom if this thing is green you are connected

successfully. So congratulations you have connected Google Sheets. As soon as Google Sheets is

connected of course you need to type in what you want to have. The tool description is automatically

the resource is sheet within a document you can always press on it and see for yourself what

you want to do. I want to let's just say a pentrose first. Then I want to chose from a list. I

just used this leads list. On this leads list I just have a Google Sheets with some generic names

so Arnie, Paul and check always with name, mail and telephone you can also call this phone if you

want or phone number and then we can use this sheet and from list you can press on it. We use

the table one and we can map each column manually but I do think that name, mail and phone the AI

should decide what thing comes in what field. So you press let the AI decide. So what we can do

right now is we can trigger this empty piece server from every single client and insert new leads here

but sometimes it can be also cool like if you say you work in cloud desktop and you were pent

new leads but then you later working cursor and you want to search for your leads. So of course what

we will do next is to press plus once again let me just see. Then we append once again the Google Sheets

tool but this time we use of course get rows and not the pent rows. We will use once again the same

leads list and from list we use once again the same table and you can combine filters if you want.

So right now we are connected what we can do is we can absurd new stuff in our Google Sheets and

we can get stuff from our Google Sheets. This was basically the configuration of our server. Remember

we have a sse endpoint and we can connect to this endpoint from wherever you want. Everything that

you have to do in order so that this is working is to send this from inactive to active and you need

to press got it. This is really really important if you work locally if you work in the nn plan.

If you work in a cell false that instance of hosting it's always the same game. Please just connect

to your Google service the Google service that you want. Google is just an example you can connect

to ever a single tool that you want and later we will connect more. Then you need to send this

to active and now we can trigger the server from every endpoint that we want and in the next video

we will do exactly this we will include this mcp server in different mcp hosts or clients. See you

of course in the next one.