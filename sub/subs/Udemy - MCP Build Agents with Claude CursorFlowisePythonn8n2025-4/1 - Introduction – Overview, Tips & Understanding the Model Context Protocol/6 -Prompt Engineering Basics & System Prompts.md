# 6 -Prompt Engineering Basics & System Prompts translated

---

And this would want to talk bravely about prompt engineering.

And we will do this relatively fast because this is not like a complete prompt engineering course.

We need to focus mostly on the model context protocol.

And I do expect that you have like some kind of understanding how to talk to on LLM.

If we talk about prompt engineering, we have always two different sorts of prompts.

First, we have the prompt that we type in in our LLM application.

And second, we have the system prompt that we as a developer need to set up.

So the normal prompt that you type in is always like in a bar.

So you can type in some kind of words or prompt into chatch.bd for example.

You can do the same thing on cloth.

You can do the same thing on cursor.

So if you type in stuff right here, this is the prompt that you type in.

Of course, also into an end if you open chat and type in stuff right here.

Or maybe also into flow wise.

So this is the prompt that you as an end user type in.

And generally speaking, what we need to do is we need to give context to the LLM.

If you don't understand how to do this over this course, like we will do it sometimes,

but I will not explain every single time what we do exactly.

If you have no understanding whatsoever how to talk to an LLM, I have a complete prompt guide.

This complete guide comes from a tropic.

It's normally only available if you have the bait plan from a tropic.

But I have created something really similar for myself and you can simply read this yourself.

I just want to go over some general tips.

Be clear and specific.

So you need to structure your prompt clear.

A bad prompt would be for example, help me with a presentation.

And a good prompt would simply give some context.

I need help creating a tensileite presentation for our quarterly sales meeting.

The presentation should cover our Q2 sales performance, top selling products and sales targets for Q3.

Please provide an outline with key points for each slide.

And why is this better?

The good prompt provides specific details about the task, including the number of slides,

the purpose of the presentation and the key topics to be covered.

So the LLM can simply reason a bit better and you will get the answer that is rarely, rarely precise.

Besides that you should always give examples if possible.

So instead of write me an email, you will do something where you give an example email.

You should then carriage thinking with a prompt like this.

And so it goes on so you can simply read this yourself if you have no clue how to dock to an LLM.

But generally speaking, it's like also not our main point of this course.

You should have at least some understanding how to dock to an LLM.

And the easiest thing is simply that you need to describe clearly what you need to tell to the LLM.

And now we come to the second part to the system prompt.

In nearly everything like the or host, we have the possibility to set a system prompt.

And the system prompt will work every single time.

This will get send it out in your API calls and gives the LLM additional context.

Without the need of typing you this stuff in here over and over again.

If you are in chatch ebd, you can come for example right here.

Then you come on personalized and here you can give a system prompt.

If you work with an add-in, you can come for example on AI agent.

You can press add options and you can include a system prompt here.

If you are in low-wise, the same thing is true.

If you come on these messages and press add message,

you can use the system message and here you can add your content.

Or if you come to cursor and press on file, preferences, cursor settings, you can come on the rules.

And also these rules, these cursor rules, these are system prompts.

And we can eventually set the system prompt.

Here we can give additional context.

And right now I want to talk briefly about system prompts.

Before we do that, I want to tell you that the best system prompt is no system prompt.

Because a system prompt will make your application a little bit slower.

More token will get send it out to the API.

The API request also gets more expensive because we paper, token.

And if the system prompt is not really needed, like we should not set one.

As soon as we create our applications,

you will see when and how I do set the system prompt, but here's some general tips.

You can structure a system prompt like this.

Most of the time you start with a role.

So what is the task of the agent?

Then you should give it a goal.

So what should be achieved?

Then you should describe the tools or like the MCB capabilities.

What tools does the agent have access to and when should they be used?

Then some rules.

So how should to this thing behave?

Then the style for example, don't language formatting rules.

The output format.

So maybe you want everything in markdown.

This right here is by the way, also markdown and markdown is a structure that works perfectly for red alarms.

And if you set the system prompt, you should always use markdown for your system prompt.

Then you can give some examples.

This is also called short prompting.

This is the same thing as you typing in prompts.

You can also do this in your system prompt.

And you can give some variables, for example, like local date, time, user names, and so on.

Here is one simple example of a system prompt in markdown.

You are an AI business analyst who summarized and explains current developments in AI, tech and finance in a simple way.

They learned for solo entrepreneurs and developers.

The goal.

Summarize complex content from up to date news and reports.

Provide clear action steps for people who have little time but want to stay informed.

Then we describe the tools or the MCP servers that we have access to.

We have the web scraper MCP, a summarizing MCP, a insight, gen MCP, and we give some informations like date, time and weekday.

And here we use variables because this thing is always dynamic.

So your agent always knows what date and time is and this is important.

If you do, for example, web scraping first, the agent need to understand what the day is today.

Then we give some rules, keep it short and concise.

Always start with a one sentence summary.

Then follow with three to five key points.

If possible include a recommendation or evaluation.

No hallucinations. All claims must be backed by sources.

Use bold to highlight important terms.

The style here we give the language is English.

The tone is direct professional yet casual.

The structure clear and logically organized.

And the length less than 300 words.

The output is marked down once again date and time.

And lastly also an example of a summary that we like.

So one sentence with key insights of the day.

Then the key points point one, two, three, four.

Recommendation and outblocks and lastly the sources that need to be included.

So this would be a really really great system prompt.

If you have trouble creating system prompts, you can use this to create or craft your own system prompt.

Besides that you have also the possibility if you work for example in flow wise

to press on this thing right here and then describe what you want to do.

For example, summarize that document.

If you use this and press generate, your system prompt will get generated automatically by an AI model.

And boom, here you see you have everything.

So here is a complete system prompt.

And you also see that we have marked down as a structure here.

As a nice bonus tip, you can also come into the open AI playground.

And you can also set here some system messages.

And if you press here, you can also describe what you want to have.

I want an agent that summarizes docs.

And if you send this out also here, your system message will get generated automatically by an AI model.

And you have a great starting point for a really really nailed down system prompt.

And you can simply read for yourself if you go conform with these.

Maybe the output format is a little bit too short.

You want to have like 200 to 300 words, but the rest is fine for you.

So with this tip, you can create system prompt really, really fast and easy.

If this is too much for you right now, like don't worry.

Yes, I will show you all the interfaces as soon as we install this tool.

So we will install this tools.

I will show you the interfaces.

I will show you once again how to set all of these things up.

But I just want to give you some general sense how you should structure your prompts as soon as we start out.

So that you understand what we are doing because I will not explain system prompts and normal prompts all the time as soon as we type

something in in our applications.

And I have also told you that most of the time the best system prompt is no system prompt because your replication gets lower.

And I want to show you something really cool.

All of these LLM providers itself, they set are really, really strong and big system prompt.

And this is the system prompt that always counts.

I want to show you the system prompt from Cloud 4 from ontropic.

So you see the system prompt from Cloud 4 is gigantic.

You see these are let me just see 368 lines of code and you see like the lines they are big.

So generally speaking, I really, really nailed down system prompt how the whole model should behave is already included.

And the system prompt from the provider itself is always a lot more powerful than the system prompt that you will give.

And here are a lot of things included like how to call tools, how to do thinking with the test time compute and a lot more.

There are also some hard code that examples included like for example, who is president right now and so on so that you cannot mess with something specific in your system prompt.

So this system prompt will always be a lot stronger than your system prompt.

So I would always recommend you as soon as you develop big stuff to start with no system prompt.

Maybe you create a agent with identity, K.I. or whatever.

First work with no system prompt.

See if your tools get called correctly.

See if your mcb server gets called correctly.

And if it doesn't get called correctly or if you have some kind of errors, then we start to prepare our system prompt and we will do it iteratively.

So we will start for example just with the part that has messed up.

Maybe the agent doesn't understand that it needs to search the web today.

So we give for example one simple variable.

We would come for example in an agent, we come on expression, we make this big and we type in right now for example date and time.

Then we open up for example a chava script variable with two curly brackets and we type in dollar sign now.

And as soon as you do this, you see that the local time and date gets automatically included and then your AI agent will search the web for right now.

So always just include stuff that get messed up.

You don't want to send like a gigantic system prompt every single time if it's not needed.

If your mcb server gets called correctly and it doesn't need to have more information just leave it how it is because your application will work more reliable, faster and cheaper.

Now once again we have always two different types of prompts.

First the prompt that you type in in your application as soon as you want to talk with your application or review the web and application for other people, the stuff that other people are typing in.

This is the normal prompt engineering and you should simply take a look at the guide from a tropic that I give you as a markdown file and you can read through it.

The second type of prompt is always the system prompt and the system prompt will get send it every single time to the API provider.

For example on tropic, opmi, grok, jemeni, whatever and this system prompt will be set.

If you set the system prompt once it will get send it every single time and this adds latency and make your application a bit more expensive to use.

Yes you have prompt caching that makes also your system prompt cheaper but generally speaking more latency and a bit more cost is included.

And that's why the best system prompt is no system prompt we only add a system prompt if our application fails to do the task correctly.

And then we will build our system prompt iteratively.

You can use a yi for a rough outline and then you need to cut things down that you don't need to include.

If you only need time and date you only include time and date.

If only one API call gets messed up you only tell the application in the system prompt that this specific application needs to be called when x, y, z happens.

If one of your mcb servers doesn't get called correctly you tell the AI when to call your mcb server.

So yes we did this fast but like at older this is not the prompt engineering course.

We need to dive deeper into the model context protocol and that's what we will do next.

And don't worry if you don't understand some of these ideas that we use right now some of these hosts that we use right now.

This was just an overview and also as soon as I set the system prompt I will tell you over this course.

And if you have no clue how to talk to llm's you also see how I am talking to llm's but I will not tell you ever a single time why I will do specific stuff it's because of this video.

See you in the next one.