# 7 -Connecting Flowise to n8n Use HTTP Request & cURL Import translated

---

In one of our previous videos inside of the Langchains section or the Flowwise section,

we have connected, in Flowwise, on an AI agent and MCP server that we have created inside of Niden,

and we used the SuperGET Way MCP to simply connect it with our SSE endpoint.

And maybe you ask yourself, is it possible to do with vice versa?

Is it possible to create a workflow inside of Niden?

And then call Flowwise with the model context protocol.

And I have to tell you, it's not really possible.

You already know it.

In Flowwise, you cannot really create MCP servers,

but still you can create workflow.

So you can create this workflow, you can also come back.

And maybe create one of these other workflows,

maybe you want to use a workflow from version 1,

maybe you want to use a chat flow,

maybe you want to use a dual agent, it does not really matter.

If you can also use a dual agent that has times the observer include that,

like at all, it does not really matter.

In this video, I want to give you an example,

how you can connect one of your agents from Flowwise to Niden.

It will be relatively easy, and we will start from scratch in Niden,

and connect already existing workflow from Flowwise.

Maybe you have something working in Flowwise,

and you want to connect it with Niden.

And also here, you can work over a few edges.

If you have inside of Flowwise,

a workflow that connects with a lot of different MCPs,

and maybe also with a superget with MCP that triggers your Python servers,

your Niden servers, even,

then you can still integrate it inside of your Niden workflows.

So let's just start from scratch in Niden.

Sometimes it can happen that you build out, for example, a chatbot or an application

or a workflow or whatever in Flowwise, because it's easy,

it's fast, it's production ready, no time whatsoever.

But then you build out something in Niden,

and maybe you think for yourself, it would be cool

to use the same workflow as in Flowwise.

And instead of rebuilding the same exact workflow,

you can simply trigger this workflow out from Niden.

In this way, I want to show you how.

And of course, we do it from scratch in Niden,

but in Flowwise, because we have already

built a lot of stuff, we will simply use this workflow.

I have this connected composer,

you're right now, because I do not want to send any mails here,

but what we do have is like the Bray search API,

the current date and time calculator, the Windows buffer memory,

the open router with Cloud 3.7 Sonnet as chat mode.

We also have a retriever with a document store,

so we have the red technology included,

and we can also save stuff locally on our own machine.

So basically, we have a nice agent here.

Something that can eventually make mistakes is, of course,

the right file tool, because I want to write files locally

on our own machine, for example, to this path.

But I am, to be honest, not 100% sure if I can do this,

because I am, of course, in the hosted version on render.

So this can make mistakes to save it locally.

Normally, we need to work with a local instance

if I want to write files locally.

But let's just test this out, maybe it works,

but I would assume that this doesn't work.

So first of all, let's just test this agent out.

I simply want to make one test to see

if the Bray search API works.

And for the reason we do something really simple,

what is the Bitcoin price?

For example, and this thing will know what's the Bitcoin price,

most likely it's roughly at 100K,

at least the last time that I have checked.

And the thing tells me that it's roughly 100K.

It depends on what exchange it sees.

For example, 101K and a bit more on Coinbase and so on.

And if I come into trading view and search for the Bitcoin price,

we are like roughly at 100 at 1K.

So you see, we have up to date information

be used to Bray search API,

and we made a lot of API requests in order to get our Bitcoin price.

Then as soon as we come into an end,

and let's just create a really simple AI agent.

But of course, this can also be a big agent

that you have already in production and you want to include

like flow wise as a tool.

You can think it this way.

First of all, of course, we can connect a simple chat model.

I just use chatGPT4 or Mini.

This can be really easy.

You can also make here a agent that works really cheap

with thorough Mini.

And as soon as you want to do complicated stuff,

you can call flow wise with a more expensive model

with Cloud3.7 Somnit or whatever you want.

First of all, let's just save this and ask here,

OpenJet, what is the Bitcoin price?

Of course, this thing will not know.

It will hallucinate or will tell us

that it does not have any current price information.

And now I want to show you how we can access this flow wise

instance so that we can access the internet,

but we can also access our whole rack application

and every single tool we can trigger this workflow.

The coolest thing is that we can simply press on tools.

And what we need to do is right here

to use the HTTP request tool.

And of course, you can simply do this yourself.

You can send the get method, you can use the URL.

You can basically type in all the stuff here,

but the easiest thing is you can come into flow wise.

You can press on this interior, you have a curl command.

So you can come to this curl command,

you can copy this curl command, we can come back to an add-in,

then you press import curl.

And here you can simply insert this curl command.

And there we have it.

So you see the curl to this flow wise instance, of course.

It's a post request.

Then we always have a question,

so this is just an example.

This you see it, this is a chase format.

And then we simply press import.

This thing is imported right now.

So we send a post request to this URL.

Authentification is none.

We only send the body, the body is chasing.

Then we have the specific body with name and value.

And basically that's it.

So let's just simply test this thing out.

First of all, let's just save it.

Open chat once again.

And I want to ask the same question,

but most likely this thing will not know

that it needs to trigger this flow wise tool.

So let's just reload it for all this in.

I do not think that we will use it.

We don't have the Bitcoin price,

and I want to show you why.

If we press on this note,

you see basically that we sent out this question.

And here you see that we have as the question,

hey, how are you?

Because this down here is the value.

And of course, we don't like to have this value.

So let's just come to mapping.

And we always want to have the chat input.

So we come to expression.

We delete this thing down here.

And before I win the chat input.

And basically there we are.

So right now we can trigger flow wise.

So let's just save it once again.

And we want to re-ask once again the same question.

So that we can map these things correctly.

So what is the Bitcoin price?

I will assume that we call right now flow wise once again.

And we will get the right answer at least, hopefully so.

And boom, there we have it.

So you see it, we have the same answer.

On CoinMarketCap it's this thing here.

On Coinbase it's this price here.

So we are at roughly 101K.

And of course you can ask whatever you want.

I just want to ask one last thing.

Current date and time.

Just so that you can see that everything works,

you can also send emails with these things

if you include Composer,

you just like in one of the previous videos.

The only thing that I would not really recommend you is

to write to your local file because this is a complete mess to be honest.

I had to mess with this a little bit.

What is current date and time?

So last test, we call our tool.

And the tool gives me of course the current date and time back.

So all of it seems to work perfect.

In that manner it's really the easy.

Everything that you have to do is to come to your hosted instance of Anidan

and your hosted instance of flow wise.

And if you have a application into flow wise that you want to use for example over Anidan,

you can simply call it via an HDDB request node.

You can simply import this as a curl and then you can talk to it.

Of course this cannot be only an AIA agent node.

You can also make normal workflows.

You can make a workflow that is practical for you in Anidan

and call a flow wise workflow.