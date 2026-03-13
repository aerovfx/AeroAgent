# 4 -Create an MCP Server with Memory Persistent Context & Long-Term Recall translated

---

In this video I want to show you the self-improving agent.

If you are docking with an AI agent or with a client, as you see here,

of course it would be nice if this client always knows what you are docking about.

And the coolest thing is that you can dock first with Cloud Desktop

later with an IDEN and lastly, in cursor, wind serve, whatever you want.

You will always get full context and you AI agent will hold your hand and knows everything

that you are docking about. Let me show you how this works.

I want to start with OpenChat and I tell here in this chat for example,

I like to eat pizza, save this. The agent works, MCB client gets triggered and this should be saved.

And right now I also want to do something like this. I like to go to the gym.

Yeah, I do like pizza and gym, not the best combination.

Also right now my client gets triggered. And if I ask right now, what are things

that I like? My client will go on, searches our vector database and it knows

that I like for example pizza and the gym. And right now I can also do something like this.

Today I have a meeting with Paul at a random time number and then I can ask like,

when do I have a meeting? When do I have my meeting with Paul?

Here you can also save really really big stuff. Meeting with Paul is at this time here.

So here you can save everything that you want because we store stuff in a vector database.

And right now we want to show you the coolest thing. When is my meeting with Paul?

Search my memory. So you can also work with different clients and this clients will always have

full context if I allow this. My meeting with Paul is at this time. It's of course 4 pm if we

talk in English here. And I hope that I don't have to tell you that I can do the same thing in

cursor, I can do the same thing in lovable win-ser of whatever. And of course also in an add-on.

And if I ask, what is stuff that I like? Search memory. Also cloud will have full context.

Also cloud knows that I like pizza and going to the gym. So you can save whatever you want.

And right now I need to show you how we do this. This is basically relatively simple.

What we have here is a workflow that uses an AI agent with a simple chat trigger.

I work without any prompts because the best prompt is no prompt and for this workflow no prompt

is needed. Here I use our open-yard chat model. It doesn't really matter. This is just a small model.

And I have an MCP client included. This MCP client triggers our MCP server. And this MCP

server triggers first one vector store and this vector store is our memory. Use this to search

and get memories. So from this tool we get memories from a bank on index that is named

flowbys with the namespace of memory. And we use of course our embedding model right here.

And then the next cool thing is the following. We need of course to absurd stuff in our

vector database. And for absurding we cannot include a bank convex to database because absurding

is not allowed to include in an MCP trigger. But what we can do is we can include call and

add and workflow with call and add and workflow. We simply connect to this workflow. This is right

now workflow 18. And this thing gets now executed and this vector database inserts documents in

the same vector database and here we use the same namespace that's called memory.

We use our open-yard model, our default data loader and our recursive character text splitter.

Generally speaking you know all of this but this is a workflow that is really cool. And if we

come in our bank convex to database you see that we have right now three things included here.

And if I come back of course I can include new stuff even from cloud desktop or from whatever

you want. So you can simply communicate with this vector databases from every single client that you

want. Save this in memory. I need to finish my MCP course until Sunday and I need to remember to

include the lectures about safety. For example and if I send this out our MCP server will get triggered.

Cloud desktop tells me that this thing is saved. And if I come right now into an add-in for example

and if I open jet reload it and I ask when do I need my MCP course and do I need to include

something specific. This thing will search as once again our vector database and it will tell me.

You need to finish your MCP course by Sunday. Make sure to include lectures about safety as part

of your course content. And if we come into this vector database you see that we have four records

added right now. So I do think that this is one of the simplest and yet most powerful workflows

that you can do. I have never ever seen somebody use such a workflow but I do think this is one of

the workflows that I use the most. This is something that is really really cool. And of course I will

share this workflow. Let me just call this workflow MCP memory agent. And right now you can simply

remember what you are doing like from every single client that you want. From add-in you can also

connect this to flow wise. You can connect this to cloud desktop. You can connect it to cursor. You

can connect the server to whatever you want. And of course you know how to connect it to cloud

desktop. I hope I don't have to tell you this. If we come into the settings developer and into the

config file. And if we open this config file right here you simply include this code and then

the production URL right here. We have already covered this like a few times. So just use this workflow

and give your agents like the real power and remember stuff in every single host that you want.

If you work for example with business data all the time you need to remember and it doesn't really

matter in what tool you are working. Maybe you like to work with an add-in but still some things you

do in cloud desktop. And you create for example your code in cursor you can ask whatever you want

from whatever host you want. And maybe you are a frontend developer that uses lovable for the frontend

and then you can also ask in lovable. So you can work with all of your relanams together and you can

save whatever you want. You can also save small code blocks. You can save whatever you want.

Because of extra database is big and you can save a lot of stuff. And as you of course in the

next one I do really think that this is a genius workflow. Free dots, download and of course I will

give you this agent.