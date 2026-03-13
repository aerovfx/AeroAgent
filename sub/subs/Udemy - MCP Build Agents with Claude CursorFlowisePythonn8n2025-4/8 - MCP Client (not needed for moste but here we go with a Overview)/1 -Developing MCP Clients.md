# 1 -Developing MCP Clients translated

---

Let's talk about developing MCP clients, and mostly I want to convince you that it's not really

needed to develop a client for yourself. I do think that you should invest your resources wisely.

Everybody has just limited time and can do unlimited things. One of these unlimited things would

be for example to develop an MCP client, and I do think that your resources are not wisely

chose if you want to develop a client. Let me tell you why. So developing MCP clients,

here are just some things that I have written down that were in my mind. You can do it, but you

probably shouldn't. Every host you want to use will either have a client integrated,

will add one at some point, or can be connected with a simple workaround. That's basically one of

the biggest things. Most likely you want to use clients for an MCP servers that already exist.

You want to work in hosts like Cloud Desktop, Cursor, Windsor, whatever it is. Even if you work

with frameworks, the MCP client is still included. So this is I think the biggest point. All of

this hosts will include a client for themselves, so there's no need to develop something. Most likely

they have the client already included. And you see it also here, even if you work with IEI agent

frameworks like LANGRAF, PIDANTE, or the OpenEI agent SDK, so even if you do everything in code,

the client is still included. Developing a client isn't necessary, because the client is already

included in the framework. This is why I think developing a client is not really that smart. Of course,

also in Anadana it's already included. You just saw this, just used the note that is already included.

So it's only necessary if you want to connect to MCP servers that aren't using an established MCP

host or framework. And like who wants to do that? Let's just be honest, if you want to connect

to a server you will most likely use a host, some sort of host, and most likely the host has already

included this. Maybe you are developing an app, or you already have developed an app, and you want

to connect with this app to a MCP server, but even then just use a framework. If you have an app

in Python, for example, try to do a work around with one of these IEI agent frameworks like the OpenEI

agent SDK Landgraph by the NTKI or whatever you want. And if you still need to develop a client

for yourself, you can totally do this. You have a really great documentation, how you can develop

clients like at OU, I would not recommend it. Everything that you can do is to copy this page, and then

you index it into cursor and you tell exactly what you want to develop. Also here you can go on

Python, or if you are a Java developer, you can come on Java or note. You can also find the complete

code if you simply follow this link here. So here on GitHub you will find the complete code,

how you can set all of this up. First you need to set up your environment with UV, this should be

really easy. Then you need to set up your API keys, for example from UnTropic. Then you need to

create your client. These are here are just some basic code examples, and you always use the class

as MCP client. So instead of tools and so on, here you work with the class as MCP client, you need

similar libraries as with the MCP servers. Then the server connect management, you also need to give

for example the transport way that you want to use as TDIO is the easiest one. Then the query

processing logic, most of the time the role is user and the content is query. We always communicate

with JSON and LLMs like this format like a lot. You need always the name, the tool description,

and the input schema. And you can simply take a look for yourself. Then the interactive chat

interface if you need to create something, the main entry point, anterior should also take a look

at the key components. They explain everything really great in this documentation. And lastly you

can run your client with UVrunclient.py. They also explain you in detail how it works, the best

practice, security, and so on. So they can look at this documentation. And if you want to have even

more insights you can come on this Python SDK, on this Python SDK you come to src slash MCP.

Here you come into client and here you should come into the session.py to see for even more

documentation. Here you get an example code you can feed this to cursor to wipe code your thing.

They show you like a lot of possible scenarios, how you can code up your client if you really have to.

Long story short, I do think that you should invest your time wisely and I don't think that your

time is invested wisely developing clients because every single host has a client already included

if it's a popular host. If it's a host that is not popular like why do you want to use it?

If you develop something for yourself, just work with a AI agent framework and you can also include

this client really easy because they are already included. If you work with flow wise,

where lang chain and lang graph works in the background you have your client included.

If you work with an add-on you have your client included. If you work with cursor, wind surf,

cloth desktop, answer one, lovable, you have your client included. If you work with the open

AI agent SDK by the anti-Ki or even lang graph and a lot more you have your client included.

It doesn't really matter where you want to include an MCP server. Most of these frameworks have a

client already included and that's why I think it's not really wise to develop a client for yourself.

With this said you can totally do this if you don't know what you should do else.

See you in the next one.