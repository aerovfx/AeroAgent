# 9 -More Possibilities Tips & Common Mistakes in Custom Server Development translated

---

In this video I want to talk about the options that we have and the biggest errors that a lot of people are making.

Before we talk about other options, let's just actually start with the errors.

I do see this all the time, redundant servers. Do you really need your server?

Please, just think for yourself, do you really need a server that uses, for example, the weather API?

Do you really need a server that uses, like also in our example, the calculator?

Do you really need a server that uses, for example, Postgres SQL?

Because, like on GitHub, you already find the servers.

So this is one of the biggest downfalls that I see.

We do not program redundant stuff.

I do think that at this point it is not really valid to include a lot of different tools in our own MCB servers

because we can find nearly every single tool that we want on GitHub.

If you find something to integrate, of course, you can totally do this and you should probably do this.

But please don't program redundant servers. This is just straight up, like there is no point in it.

Then the next thing that I see is to use too many tools.

You also saw it as soon as we used the SAP RMSCP.

If we include like 20-30 tools at some point, our server will no longer be reliable.

It will fail to call the tools reliable.

And there is also no point in include so much tools, so that the server doesn't understand what tool we need for what option.

At some point, this is just simply too much.

If you include a gazillion tools, if you include 30-40-50 tools, like the LLM can no longer decide when to use what tool.

So please make your servers slim and compact.

And the last thing is basically the same thing as this right here to complex.

Don't include too much stuff. Don't make it too complex.

Don't include like 50 resources and 20 prompt templates and on top of it like 30 tools.

At some point it will make absolutely no sense, just make a few servers.

If you have a lot of good ideas, make a few MCP servers.

And don't throw every single thing in the super gigantic MCP server, because this thing will simply fail.

Then the other options, what we can do.

We can use of course the SZ endpoint and also the stream of the HDDP, especially if you want to publish your server.

More on publishing your server in the next video, here we have a few options.

Then you can also add more tools, but please don't make it too complex. Don't overdo it.

You know how to integrate tools, you can add more if you want.

There is no point for me to go in like every single tool under the sun.

The concept is always the same.

You can simply come into cursor, you tell cursor I want to add tool X, Y, Z.

Here is for example the API that I need to call. Here is for example the API key that you need to use just include the stool.

And then you are ready to rock.

Then the next thing, hosting for example via Cloudflare.

We talk about hosting in the next video in a little bit more detail, but you need to be cautious because you should absolutely be safe if you want to publish your server.

And more on the general security of course in the next section.

So long story short, avoid making reddodend servers don't include too many tools, don't make it too complex.

And you have the possibility to use different transport ways, add more tools, and you can host your servers, but you need to be cautious.

A little bit more about hosting in the next video.