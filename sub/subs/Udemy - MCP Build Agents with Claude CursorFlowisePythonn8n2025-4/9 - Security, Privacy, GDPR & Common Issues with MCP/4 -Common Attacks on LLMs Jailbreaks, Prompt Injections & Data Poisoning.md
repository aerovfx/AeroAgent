# 4 -Common Attacks on LLMs Jailbreaks, Prompt Injections & Data Poisoning translated

---

In this video I want to talk about the classic attacks of LLM's, named prompt injections,

jail breaks and the standard data poisoning. This is not MCP specific and I have explained

these things in other courses in detail, but still I just want to give a brief overview.

One of the coolest things that you can do is to come on X to this profile,

planning the liberator. This is like the goal if we talk about jail breaks.

Now what's a jail break? A jail break is basically just something that we can

dip into an LLM model and the LLM model tells us stuff that it should not tell us.

And people can also basically jail break your MCP server. If they are typing in specific prompts,

they can get stuff out that is really harmful. And if you for example publish an MCP server

and this MCP server spits out stuff that it should not spit out, this can be eventually problematical.

Long story short, I do think that you should take a closer look at this profile.

This is also relevant if you work with cloth desktop with cursor with whatever.

And every time as soon as an LLM works, this jail breaks can occur. If you type in the prompt

in a specific way, this models can get jail breaks and this can eventually also be harmful

for your MCP server. Especially if on your MCP servers are tools included that can do interesting stuff.

For example, people can jail break your server and read stuff from your MCP server that they

should not be able to read. They can read for example system instructions or tool descriptions or

stuff that you include for example in ii agent in an idn and if you don't want that people

read these instructions you need to be careful because if somebody jail breaks your application,

they can read all of this. Besides these, we have also the prompt injections. You also saw an

example of a prompt injection in the last video. But prompt injections can occur with every LLM

and if you develop a server and this MCP server has for example access to the internet or so

here a prompt injection can occur. If your server searches for example the web and on the web can be

for example a white page and on this white page is white text that you can not see but the LLM can

see it. And on this text for example stands forget our previous instructions and right now you do

xyz. This is for example a prompt injection that can come into your MCP server into your application

and you need to be cautious with this. As soon as you give internet access or as soon as you

view include the vision for example in one of your MCP servers over an HTTP request you can eventually

get a prompt injection even if your tool is great. So keep also this in mind.

Chail breaks and prompt injection can happen and also data poisoning, the normal data poisoning

can eventually happen but normally here you are safe. All of this is not really MCP specific.

That's why I just want to bring it up briefly. Take a look at blinding the liberator,

take a look at what he does and read for yourself a tiny bit. If you do want to have more information

like a dole in a lot of other courses I go into this in more detail. But I do think this is not

really MCP specific but you should still have this on your radar. See you in the next one.