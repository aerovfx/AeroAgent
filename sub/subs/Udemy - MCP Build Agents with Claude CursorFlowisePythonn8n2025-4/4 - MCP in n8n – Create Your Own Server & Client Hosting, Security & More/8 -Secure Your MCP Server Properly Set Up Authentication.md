# 8 -Secure Your MCP Server Properly Set Up Authentication translated

---

Before we make our MCB server even more awesome, first let's just make it safe.

You already noticed, everybody that sees this URL, everybody that has this production URL.

If somebody sees this for whatever reason, they can connect with your MCB server.

This is really, really awful. But of course you use an authentication, just think about it.

If somebody wants to connect to this point or let's just make it even more practical,

let's just say you have a company and you make this server for example,

public with this cloud desktop config file. So let's just say you come here on file,

settings, developer, edit config and this config file, you make this for example,

public on GitHub or inside your company and you want that people can connect with this file.

It can be really problematic because everybody can access this. So even people outside of your

company can basically ask this things right now. They can ask list my leads.

If they simply come into cloud or into an adn or into whatever host they want,

they can use your leads, they can find your leads. Maybe you also connect a Gmail tool,

they can send emails in your name, they can read your emails, they can do really, really bad stuff here.

And now I want to show you how you can make this safe. If you come on this MCB server,

we simply use our identification and we have two options here. We have bear off,

you can simply press on it, then you can press right here, create new credentials and it's really

easy. You can simply open up the documentation and follow this documentation. So it's really,

really easy and I want to show you the more practical way the way that I like most is to use not

bear off but header off and header off is even better at least how I see it. It's also really

easy. You can simply press on these and if you use header off, you can come right here,

you need to create a new credential if you don't have any, then you give a name. I want to give

the name Arnie for example and now we need to give a value and the value should be of course right

now a code that you remember. I just use a code that nobody ever will guess right. You should not

share this code or you should just share this code with people that you want to give access.

Now you press save. Then of course we need to save and now we want to show you what happens if

we ask once again. What are my leads? Boom, it doesn't work. Error in sub node mcp client and this

doesn't work because we don't have the right to access the server. Same thing is true right now in

cloud. If I ask list my leads, I will get an error. Always allow. Boom, there we have the error.

I do not get my leads and now I want to show you how you can give people access inside of N&N

and also inside of every other client. Everything that you need to do inside of N&N is you come to your

mcp client. Here you come on out identification. It's of course header off and on header off you can

simply connect with the same account and on header off three. This will get automatically included so

if you press on it, you can of course also change it. The right thing will be included so the name is

Arnie and also my code will be here included. If this value is false, like normally this should be

automatically and if not, I will include it. Let's just see if it's automatically or if I have to

change it once again. So what are my leads? Safe, send it out. Client gets triggered and boom,

there we have once again my leads. Because of course we use right now the same

authentication and because it's in my account, I can access it. If you want the other people from

N&N can access your account, you need to give them your password and then they can access it.

And the same thing is also true for Clot. Clot will only work as soon as you update your config file.

And now I want to show you how we can update this config file. If we open up this config file right now,

you basically see that we do not have anything included about authentication and I want to show you how

you can structure this file so that this thing is working. And these things until here are

completely fine. Everything that you have to do is to take a new line, start with Quocean marks

and inside of your Quocean marks. You type in two dashes. It's of course header because we want

to authenticate with header. Then we go outside of our Quocean marks. We need to take a closer look

at the syntax and the syntax is then always a comma. So we take a comma, then we take a new line,

once again Quocean marks, Arnie was of course my name, then a double point spacebar,

and here you need to type in right now your password. And my password was extremely difficult. It was

1, 2, 3, 4. And this thing right now should work. And maybe you see that we have a syntax. And maybe

you also understand why do we have the syntax. Just look at it. Coma, comma, comma, comma, no comma,

you always need to have a comma. Just not on the last argument. So here you need to type in a comma,

boom, then the syntax is gone. If you have problems with this, you can also use ChatchyPD to create

this config files or most likely you can also copy just mine. So we save this right now. Then we

will close this down. We will restart Claude. So quit Claude, re-opement, make it big. Let's just see.

And then it's connected right now. What are my leads? Google sheet reads. And right now we have

once again our leads. Same thing is true for cursor. What are my leads? It will not work right now,

even not if I give access. So Rantul, Rantul, Rantul. I have trouble accessing the Google sheets at the

moment based on your previous data. So Claude just uses my previous data. If I come into a new

chat, my leads would be gone. Also this thing only works if we come into this config file and we

need to include the same things also here. And of course you can also just copy this if you come to

file, set things, developer, edit config. If you simply copy this file, so copy all of it,

throw it into cursor, save it, refresh. But I do think there's no point that I show you this once

again. This should work. And if it's not working, you just need to restart cursor. So long story short,

this is how you can make your MCP server safe. You can make a header with authorization. Just give

a name and a password and then you are safe. And you only share this password with people that you

want to give access of course. And if it's just for you, keep this password private. It's really

that easy and it's really important. See you of course in the next one.