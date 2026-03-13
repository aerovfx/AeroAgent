# 9 -Add Tools to Your MCP Server & Use Zapier for Free in Claude translated

---

This video want to show you basically a special workflow because we can use this APR MCB also in

Cloud Desktop completely for free. Yeah, I don't know if this is the purpose of Cloud Desktop,

but yeah, we have the possibilities of why don't just we do it. First of all, you already know it,

we have this MCB server and what we can do is press plus on the server and we can add new tools.

You already know it, you can basically also connect various apps out from an add-on,

but the APR offers more apps and you can integrate them a lot easier. So what we do right now is

something a bit special with that in MCB and we want to connect the MCB client tool. Why do we

connect a client tool? I will show you. We can basically connect the MCB client, like this client

or cursor or also Cloud Desktop. The client will communicate with this server. This server will

communicate with this client and this last client can communicate one last time with another MCB

server and the server that it will communicate will be the SSE and point of Saber. Yes, I know this

is cool. What we have to do is to simply type in Saber, Saber MCB server. We come to the Saber MCB

servers, we press get started. And here we can connect a new server or create a new server. We need

to select a client, but the client should be other right now and we create the server.

And right now on configure we can add the tools that we want. I just want to make a generic example

with Google Sheets once again. I want to use get many spreadsheet rows so I can get up until

1,500 rows and I connect it. Then once again add tool, once again Google Sheet. Then we want to have

the Create Spreadsheet column. What we also want to include is for example the Google Calendar. I want

to have find event but also find multiple events and create detailed event. And lastly I want to have

Gmail included. I want to have find mail and once again on Gmail send the email. Of course you can

go on, you can include whatever you want, but I do think these are enough tools for right now.

This is just for the purpose that you can see how this is working. What we do right now is we can

come on connect and on connect we have the server URL and this is everything that we need.

So you can simply copy the URL, we come back into an add-on and on these MCB servers we have the

MCB client and on the client we give the SSC endpoint so we can simply copy this from ZB or in it.

And as soon as this is included of course we can talk to our ZB or MCB tool because we communicate

with SSC. On this MCB client of course you can also give it a name. Let's just call it MCB client

one. Yeah it's maybe not perfect. We call it ZB and we press Rename. Also here you can give

authentication if you want to make it even more safe. And now we test this out. Add this to my

calendar meeting with my dog at 5 pm today. You say beer MCB for example. I send it out and my MCB

client right now gets not triggered so this is also a great example to show you that sometimes

a system prompt can help. Let's just go on to the system prompt and we add something like this.

If I ask things about mail and calendar at events, get events always trigger the MCB client for

example. And now let's just test this once again. So I copied this. I reloaded. Always press safe.

Maybe it also did not work because I have forgotten to press safe. It could be also the case that

this was the problem. So at this few words in the system prompt they can help sometimes.

And once again an error and I purposely don't cut this thing out because sometimes we run

in errors. Let's just come on executions and see what the problem was. The problem is in the MCB

server. It is a problem in ZB. So let's just actually come to ZB and see how done by him and I do

think that I know it. It's not streamable HTTP of course. It's server sent event. Please make

this things always the right way. So right now our server URL is this. I copied it as URL once

again. I come back into an add-in on editor on ZB. I have deleted this old URL and I will include

my new one and I will not show you this. And this is right now with the server sent event and

point. So right now I do think this should work. So safe. Maybe the system prompt was not the problem.

Maybe the problem was that I am damp. This is of course server sent event and not streamable HTTP.

Add this to calendar meeting with my dog today at 5 pm. I send it out. Client gets triggered.

It will trigger most likely our server. The server will trigger our next client and the next client

will trigger our server inside of ZB. And this takes a little bit of time sometimes. And then you

see the event meeting with my dog has been successfully added to your calendar at 5 pm. And if I

come to ZB here on the history you can basically see. So this thing gets executed. And the coolest

thing right now is of course that you can access once again ZB here out from a client that is normally

a paid feature. So you have saved 90 bucks a month congratulations. If you come back into clothe

and if you press on your MCB servers you have an add-in and this thing is not included of course

because you need to restart clothe. I do think that they should make a refresh button. But

let's just take it how is this. We simply re-open up clothe. Asks the once again we press on it.

Let's just wait until an add-in comes through. Boom an add-in. Right now you see we have 11 things

that we can control. So we have Google Sheets get many. We will find two demos and we will find

basically everything that you want. If you do not want to use Google Sheets from SAPER of course

you can also exclude it because we have some redundant stuff right here. So Google Sheets we could

exclude it because we have Google Sheets already included basically in our normal tool here.

But the rest should be fine. So you could actually also do something like this in Cloud Desktop.

List my leads. Then we have my leads and next let's just say send a mail to Arnie. Also search

my calendar and tell him when I am free for example. I send it out and right now we need to do two

actions. So first it will search my calendar to see if I am available today or not. Always allow.

Next it asks me if I want to send my mail also always allow. It also finds some other events

like a live call tomorrow and so on. It crafts the mail. It also finds that it needs to send the

mail to this mail because we have the mail right here. And it has sent it the mail successfully.

And by the way if you ask yourself why do I not have the event of walking my dog or meeting with

my dog on my calendar. I just want to show you this in SAPER I have some this also just a few seconds

ago. Date and time was 2023. Why was this date and time 2023? Because our model inside of NADN

we have triggered this from NADN. The GPT for a mini model thinks that it is basically 2023

because this was its training knowledge cut off. So of course you should include either date and time

for example in the system prompt you can do something like this date and time. Then you can open up

two curly brackets and you type in now and you can close your curly brackets. Most likely it also

works better if you come on expression and make it big so that this thing can help you if you are

not familiar with this. So do curly brackets and then you can type in now and then you have date and

time included so that this thing knows exactly when to put stuff in your calendar. So this is also a

great explanation how you should use a system prompt if you're running to such errors. Then

training knowledge cut off is this right here and that's why in this mail it told me that I am

basically always available but of course today I have a meeting with my dog. But the mail of course

will send it out hey Arnie hope you are doing well I wanted to reach out and share my available

time for coming days. Here's when I'm free for example June 5th 6th and 11th so basically everything

is fine. I have just excluded the stuff where I have a life call and something with materials. So

everything works perfect. Congratulations you have connected Zapier to call out desktop completely

for free and you can connect every single thing that you want inside of this anadense server really

easy. You can come to Zapier connect new tools you can connect new tools into anadense and do a lot

more and over the next videos I want to show you even more even cooler use cases. We can work with

vector databases and do a lot more. See you in the next one. And of course the server also works once

again in cursor. I hope that I don't have to tell you this. If you come to cursor reload we have right

now all the tools included.