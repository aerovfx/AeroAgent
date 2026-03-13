# 13 -How to Integrate Multiple Vector Databases into Your MCP Server translated

---

The RMSP server is not just limited to one single vector database.

Of course, you can include more.

And especially if you want to talk about various different things,

and you have various different knowledge sources,

of course, you can simply include more vector databases.

Now, I already have a vector database in bindcomb and it's called scrape.

And I have basically just scraped some information about prompting.

The prompting information that I have included is here on this chain of draft prompting.

I have already shown to this PDF a few times, but I do think this is a great information source.

It is relatively new. It is from 2025.

And most LLMs are not trained on this data.

And I do think that an LLM should know this training data,

this training technique.

And if you want to talk about prompting with an LLM,

it can make sense that you include this data.

Of course, if you have your own company,

you can include here various different data sources,

maybe one apartment about sales,

the other apartment about marketing, the other apartment about product.

And you can simply make different vector databases with different sources.

This makes more sense to use different databases because it is in a better structure.

If you throw every single thing in one single vector database,

it can make mistakes.

And this will be a quick video because it's really easy.

Because everything is set up, you simply press plus we use once again the bindcomb vector store.

Of course, we need to give it a name.

This time, let's just call it prompting.

We copy this.

The name of this knowledge, let's just say prompting underscore info.

Use this tool for info about prompt and jean hearing.

Of course, you can also read everything like in small letters.

This is just from my German background, a normally speak German.

Then the bindcomb index is this time, of course, scrape.

I have told you.

Then the limit, so the top care result will still leave it at 4.

You can play with this a bit, but 4 is a general rule of thumb that works always great.

And then of course, we need to give a namespace.

And the namespace in this thing is of course prompting,

so we are copiedies to make no mistakes.

And we include this namespace.

And then we are basically done.

We rename it at boom.

And what we need to do right now is of course, once again,

to use an embedding model.

The same one that we used to embed this document.

I have used the text embeddings for a small.

You already know how to create this vector databases.

So I will not waste your time and boom.

Right now we press save.

And you can also ask stuff about prompting or about the chain of draft prompting inside of an embed.

So for example, what is COD prompting?

And normally an LLM is not trained on this data,

but because our agent will talk to the client, the client to the server.

The server will search this knowledge.

It will absolutely know what chain of draft prompting is.

A normal LLM has most likely no info about this,

but you can include, as you know, every single concept that you want.

And boom, we have an error.

And I hope you see it.

My prompt was of course, what is COD prompting?

And the answer is not right.

This tool tells me that COD prompting stands for chain of thought,

the composition prompting.

And this is not right.

And you may be also see that we have not triggered our MCB client tool.

And this is now a great chance in order to improve our system prompt

to get the right answer spec.

Because sometimes as soon as these tools get to big,

as soon as we use a lot of stuff on our server,

it can happen that the agent no longer understands that it needs

to use MCB client for our new information.

It's also important to press save from time to time.

Maybe I have also forgotten to press the save button.

I have deleted my output here.

And we get also an error.

Why we do get this error?

I will tell you, if we come to executions,

you see that we did not search our PDF.

So basically what we do is to come into the agent

and simply tell the agent if you got questions about

COD prompting used the MCB client.

And now we ask once again, let's just see if this is working right now.

What is COD prompting?

Right now we trigger the client.

The client will now talk hopefully with the server.

The server will search the prompting vector database

and we will get back.

That COD prompting is of course the chain of draft prompting.

In our previous conversation, we got the wrong information back.

And right now boom, we are done.

It is working just perfectly.

So you see it is the chain of draft prompting.

And if we come on executions right now,

let's just see the newest one.

You see that we used our vector database for our information.

In our previous conversation, we got something back that was not right.

You see it did not use to the MCB server and not our vector database.

And the question was once again, what is COD prompting

and the thing thought that COD prompting stands for chain of thought,

the composition prompting.

So basically it was absolutely wrong.

But now after an update in the system prompt,

we get of course the right answer back.

COD prompting stands for chain of draft prompting.

And I hope that I don't have to tell you that if you come back into cursor, reload it.

You also have here your prompting info.

And if you restart CLOT and we wait until our NIDEN MCB server comes through,

there it is.

We also have here the prompting info.

So I do think this is really powerful.

You can connect more than just one vector database to your MCB server.

And you can split out everything just perfectly fine.

And you will get the right information back as easy as possible.

This is a powerful concept if you have different apartments in your company

if you want to do specific stuff.

With different vector databases, you should absolutely include different vector databases.