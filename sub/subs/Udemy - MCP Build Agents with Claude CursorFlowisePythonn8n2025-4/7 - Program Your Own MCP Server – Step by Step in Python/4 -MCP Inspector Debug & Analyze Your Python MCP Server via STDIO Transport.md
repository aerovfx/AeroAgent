# 4 -MCP Inspector Debug & Analyze Your Python MCP Server via STDIO Transport translated

---

In the last video, we have coded our MCB server and in this video we need to talk about debugging.

If you come basically once again on this documentation you see that you can debug your server.

Of course you can do it the old way you can use the logs you can do a lot of things,

but the easiest way is to use the MCB Inspector.

And we have already opened up our MCB Inspector in the last video.

So if you come on Inspector you see how you can use it.

You can use it basically automatically.

If you code up by MCB server and if you start it the way we did,

it should be automatically included.

Installation and basic usage, the Inspector runs directly from MPX without requiring installation.

This is cool.

And then you can simply open this thing up and it will look something like this.

And we have already opened the last video.

And the great part is you can use every transport way that you want.

So STDIO, SSC or also Streamable HDDP.

You have the resource step to test your resources.

You have the prompt step to test your prompts.

Of course you have your tool step to test your tools.

That's what we will do in this video.

You see the notification pen with all your logs.

And if you have problems you can throw your logs inside of cloth and just ask about it.

One of the greatest parts is of course that you are connected every time.

If you want to do debugging with cloth, for example,

you have to restart cloth like a gazillion times and this is really painful.

Here the best practices, just start and launch the Inspector.

Then you can work with your server and always check in the Inspector.

And you can test your edge cases.

So you see this is the server.

We have simply typed in the comments.

And then you basically also get this thing back as soon as you open up your URL.

You will get this thing back.

Here are some logs basically.

And then you can come to the ZemsyPins Inspector

and you can use the Tronstopboard type.

We use right now STDIO as the default one.

We have the command, the arguments and so on.

And you need to press connect.

We already did this.

Now right now it's important that you should simply see if your server is working or not.

We have only tools included.

So you press on tools and now you press list tools.

And then the magic should type in if your server works.

Our server works.

We have the add tool.

We have the subtract tool.

We have multiply, divide, power, square root and factual.

And you can always see what the tools are doing.

Add two numbers together.

So if you press on this tool, you can basically see it here.

Add two numbers together.

Number A would be for example 10.

Number B would be for example two.

Then you press run tool and you see the output is 12.

You can test the next tool.

For example, the subtract once again 10.

Here I type in two and then you press run tool and we should get 8 back.

And you can simply work yourself through these tools and see if these tools are working.

And if these tools make problems, you would come back to cursor

and you need to describe the problems exactly.

And then cursor will fix your problems inside of your code.

But we get lucky.

We have no problems here.

And one quick info.

Sometimes if you spin up your MCB server, it can happen that it starts your MCB inspector.

Your MCB inspector is still listening to this URL.

But then you get a session token.

This is for security.

And you need to use this session token in order to start your MCB inspector.

This is really important.

So use this token to authenticate requests or set dangerously on it off at true

to disable this authorization.

The easiest thing is probably to simply open up this inspector with this pre-filled token.

So you can simply use this URL and you press follow this link.

And then your inspector will get opened up and you are once again connected.

If you, on the other hand, use this URL and follow the link.

And then you press connect.

You are not able to connect here.

So this is important to understand.

If you get this without token, you should simply follow this URL and then you can use it safely.

This is basically the URL that is safe.

And if you press connect, then you are connected.

By the way, also here you will find environment variables.

And you can press on them and here you see that this thing is automatically filled out for you.

Because you have opened this thing up with the authorization token included.

If you use for example a streamable HTTP,

you will also find here the authentication.

And here you need to have a header name and the error token.

So keep this in mind.

If you include for example, out identifications with the streamable HTTP,

you should also always give a header name and the error token.

But let's just keep it simple.

We work over STDIO right now.

And if you get this thing right here, just open it up with this line and you are ready.

This is basically everything that you need to know about this MCP inspector.

It opens up automatically and it will help you fix your problems.

If you come on resources and if you press list resources,

we don't get any because we have nothing included yet.

If you go on prompt and you press list prompts,

we get nothing back because we have nothing included yet.

We only get this tools back.

Clear list tools.

You see all the tools.

You can press on them.

See for yourself what these tools are doing.

You can test these tools out, press run tool and see if the tool is working or not.

Then you can come on ping and you can press ping server to see if your server is working.

You can come on sampling, routes and OAuth.

So if you include OAuth, of course, you can simply work with all of this.

But right now it's only important that our tools are working, so this is completely fine.

And now I want to show you something else.

If we use for example the SSE transport type and we press reconnect.

You see that our server is not working because we haven't specified this, of course, in our server.

If we use streamable HDDB and press connect,

our server is also not able to connect.

On streamable HDDB it's also possible that we use the not the right local host you are

well because I do think that we use let's just see.

Another local host, the local host should basically be something like this port.

But nonetheless, right now we only work with STDIO, so you can connect and then your tool is working.

If you want to also communicate via SSE and streamable HDDB we need to do this later.

Long story short, the debugging is not needed what we need to do next.

It's to connect our server to the front hosts.

And that's what we will do in the next video, so the debugging is completely fine.

So we need to connect it in the next video to the front hosts, see if the host integration is working.

And then we will add more capabilities to our server.