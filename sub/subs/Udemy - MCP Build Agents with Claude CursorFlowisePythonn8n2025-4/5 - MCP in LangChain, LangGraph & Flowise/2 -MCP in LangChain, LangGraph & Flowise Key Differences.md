# 2 -MCP in LangChain, LangGraph & Flowise Key Differences translated

---

We need to talk about the Langchain ecosystem, at least for a brief moment.

If you come on Langchain.com, you can scroll down and see what Langchain in general is doing.

Generally speaking, you can create chat flows and maybe also AI agents with Langchain and especially with

the Langchain ecosystem. You have a complete agent that can include it. You can do orchestration,

here you need to use Langgraph. You can use a lot of different integrations with the normal Langchain.

If you want to do evaluations, Langsmith is the tool that you need to use. If you want to

deploy it, of course you can also do it in the Langgraph platform. Here you get of course a

nice little overview if you simply scroll down, so they have a really nice webpage. If you come

on this documentation you see that you can use the tools either in Python or in JavaScript.

Now you may be asked yourself when you should use Langchain and when you should use Langgraph.

If you come for example on Langchain, you see how you can use it. You have a whole documentation

and generally speaking you use Langchain for simpler automations for normal chat flows.

If you want to build agents, Langgraph is the thing that you need to use and Langgraph, I have to tell

you it's a little bit more techy, it's a little bit harder to use. Of course the overskate the

whole overview and if you come on the quick start you see how you can create simple agents here

for example with the weather API. But let's just come briefly back on these documentation.

Here you see that you can use it in Python or JavaScript like Adobe and you can use Langchain,

Langsmith and Langgraph. And now the cool thing if you come to Langgraph for example,

you can also see that you have the MCB integration. So of course we can use MCB, the

model context protocol also inside the Langchain ecosystem. But I also have to tell you that MCB

inside of Langgraph it's a little bit techy and you should know how to code like really really well.

This MCB integration work with the Langchain MCB adapters. This is a nice GitHub repo,

you can basically take a look for yourself if you really want to dive deeper. But what I want to

tell you is that we can use Langchain and Langgraph with the model context protocol included inside

the flow wise. Now what is flow wise? Flow wise is a nice and easy drag and drop interface.

It's similar build it than N&N, you can see it here. You can build powerful agents and it builds

on top of Langchain and Langgraph. This means you can simply drag and drop these nice things here

on a canvas just like in N&N and in the background works code from Langgraph and Langchain. And also

MCBs included. Flow wise is generally speaking a nice tool. You can run it locally with this

commands, you can also use the version directly from Flow wise or you can self-host it for example on

render and I do think it's a lot nicer to use than Langgraph itself. So basically you have simply

learned in this video that the Langchain ecosystem is big. For normal chat flows we can use Langchain.

For agents we would use Langgraph. If you want to do evaluations, Langs may fit the tool that we

need to use. Also the model context protocol is included thanks to MCB adapters and we will use it

in this section thanks to Flow wise. So it will be in a low code environment. Of course yes later

we build some stuff in Python but I do think that we should use the tools that are easiest to use

but still can get the job done really really nicely.