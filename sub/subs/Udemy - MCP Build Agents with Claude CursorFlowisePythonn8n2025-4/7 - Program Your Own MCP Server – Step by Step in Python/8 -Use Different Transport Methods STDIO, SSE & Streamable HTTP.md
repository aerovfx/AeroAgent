# 8 -Use Different Transport Methods STDIO, SSE & Streamable HTTP translated

---

Until now we have our server running with the STDIO command.

And of course, you can also make this into SSEN points,

so you can also work with the server send event.

Maybe you want to publish the server and give other people access.

Before you do this, of course, always make sure to save your progress before you mess something up.

I want to show you like a quick example how you could integrate also the server send event as communication.

If we come into our code,

we have here nothing included the docs specifically about the communication.

If you scroll down, basically you see mcb.run.

And here you can simply include one line and then you have a streamable HDDB.

And I want to show you what this line is.

You type in transport equals, you also see the auto completion.

Then you open up a quotient mark.

And this time you can type in either SSCE, STDIO or streamable HDDB.

Now I have this auto completion already included because I have done this a few times.

If you never done this, just type this stuff in.

Transport equals streamable HDDB.

Or you can also use the server send event.

But we will talk about the server send event in a minute,

a little bit more detail because the server send event alone can get deleted.

So the streamable HDDB is great.

By the way, if you come into the brightness decay,

you can come into SRC, mcb.

Here you can come into the server.

Then you come in the fast mcb.

And in fast mcb, you come under server.py.

And here you can also find the transports.

If we scroll down here or actually let's just type in run,

then you will find everything.

Here you can basically see it.

As the transport, you can simply use either STDIO,

SSCE or the streamable HDDB.

And by default, you work over STDIO.

So if you include nothing, you will work over STDIO.

We have right now included the streamable HDDB.

So we will communicate over the streamable HDDB.

This is really cool.

And now I want to show you something else.

If we come into the model context protocol inspector once again,

we are here in STDIO and I want to restart it, connect, boom.

You see, we are connected.

List resources.

This thing still works.

List prompts.

Clear.

This thing still works.

Now why is this working?

This thing works because the mcb inspector always spins up a STDIO for you.

So this is really cool.

Of course, now you need to test the HDDB.

So this streamable HDDB.

And if you press on it, I do think that this thing right now will not work.

Reconnect, for example, connect.

This thing is not working.

Why is this not working?

Because this is not the right URL.

This is also somehow like not perfectly made.

I wish they would make this a little bit easier, a little bit better.

But we need to take this how it is.

So how do you get access to your streamable HDDB?

Because you have here the streamable HDDB included.

What we need to do is we need to find, of course, our endpoint.

If you come into your terminal and add a new terminal,

of course you can simply spin up your server once again.

You can also disconnect to the server and reconnect once again,

but I am already connected and I do know where this server sits.

This server sits on this URL.

So you can do streamable HDDB.

And you need to use this URL, at least on Windows.

It is HDDB.

Double point and this do backslashes.

Then it's zero, zero, zero, zero, zero.

Double point, eight thousand.

This should be the board where you can access your server.

And this right now will still not work.

If you press connect, boom, nothing works.

But what you need to type in next in order that this is working is

forward slash mcp.

And right now you see HDDB with this URL is connected.

And you can press list prompts, clear prompts, tools, list tools, clear tools,

resources, list resources, clear resources.

So yes, I know this is a little bit stupid, but of course we need to work with the stuff that we have.

So this is the easiest way how you can include the streamable HDDB.

But of course you can do more and you can also switch between different transport ways.

So let's just delete it and I want to show you something on GitHub.

I have found a really great GitHub repo and in this GitHub repo,

this guy right here has some great insights for us.

Because if you scroll down into the code, everything that he has done is

he used SinkDefMain and the transport equals to SSC, so the server sent event.

And then he simply uses an EFELS function.

So if the transport equals the server sent event, we simply use the server sent event.

And else we run it via the STDIO.

So this is a really, really simple thing that you can integrate if you want to create here something

that can use both. So one of the simplest things that you could do is to copy for example this code,

then throw it into cursor and tell cursor that you want to implement this for yourself.

If we come back into cursor, make sure to save everything up.

Tell cursor something like this.

I want the possibility that my server can also communicate via SSC.

Use this code as an example how to implement it and then update my server.

Then be throwing this few lines here and we send it out.

Now boom, we will get our edits and I do think this should work after our implementations.

So you see we have some things that we implement here.

So let's just simply accept them, accept accept.

I do think this seems to be fine except and if we scroll down also here,

this is the most important things here, accept and accept.

So I do think this is fine.

And as soon as these things are added, you should be set and you should also be able to communicate

with the server sent event. And of course you should always take a look at the original documentation.

If you scroll down, you see that the basic communication is of course always standard input

output so STDIO and you always get the Python examples.

Then we have streamable HTTP. They also show you exactly how it works and also here you get

the Python example. It's basically relatively easy to use.

You can also give this documentation to cursor to code up your server.

And lastly if you scroll down the server sent event, I do think that this can depreciate over time,

at least that's what they are telling us. So SSE as stand alone transportation is depreciated

as of protocol version, this right here. It has been replaced by streamable HTTP,

which incorporates SSE as an optional streaming mechanism.

For backwards, compatibility information, see the backwards compatibility section below.

So you basically see you can no longer use the server sent event as a stand alone transport.

So you need to use the streamable HTTP. And with the streamable HTTP you can also communicate

with the server sent event. And you also get some Python examples here for your server.

It's basically relatively easy to include. You can always give this documentation to cursor

if you want to fix your server at any bit. I have to tell you right now,

I am personally not the guy that the program is a lot of SSE endpoints to make this things public.

I do think this is a lot easier and maybe also more productive if you do this via Niden.

Because you can include a lot of tools really fast and really easy.

And also the hosting within Niden is really fast and really easy. But nonetheless you can totally

do this. You can communicate with the server sent event, you can also include the streamable HTTP

if you really want to. In the next video I want to talk briefly about what things you can still

include. So yes, you can make your server bigger and bigger over time.