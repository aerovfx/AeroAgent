# 4 - Installing NVIDIA AI Workbench translated

---

Installing Nvidia AI Workbench

Nvidia AI Workbench is a development environment manager designed to help you build,

customize and prototype AI applications using GPU resources.

I highly recommend installing it to help you prepare for the certification exam.

You can work with models using your local GPU or by using NGC inference.

Here's how AI Workbench can help you get started.

You can get AI Workbench up and running in just a few minutes.

It supports Windows, Ubuntu and Mac OS.

Download and follow the prompts.

Install it then, access the projects from Git or directly in the Workbench UI.

AI Workbench takes care of the tricky parts of setting up GPU accelerated environments.

It manages system dependencies like the Nvidia Container Toolkit

and handles GPU-enabled container runtimes automatically so you can focus on your project rather than the setup.

Plus, you don't need a massive local GPU to run a large language model.

You can switch between local machines and cloud servers.

It helps manage these deployments without needing a centralized service,

giving you more flexibility when moving between systems.

Here's a demo of a RAD workflow using the Nvidia Workbench.

The app uses a large language model as the core asset,

then allows us to embellish the results using a local vector database,

enabling us to create additional context to the results.

The app allows us to select which LLM we want to use.

I think we'll choose LAMAS 3.1. This is so easy to use here.

I'm going to ask a question, what is the current version of Java?

This is a bit too wordy, but might just come back and say, Java 17 is the current release.

That's super interesting because this week Oracle release Java 23.

Java 23 is the latest release.

Yet if I was working on a help desk and this chatbot was designed to help me answer questions,

well, it's completely out of date.

Hey, well, maybe it's an issue with the model, so let's try something else.

Let's go.

Mr. Al. Okay. Mr. was quite a well-known one.

That's good. Which model do you think you want to try with?

I think we'll just try this one. Version 3 lives one.

We'll just shorten our answer a little and we'll ask the same question.

All right? So imagine I've got an irate customer on the call just wanting to know

what's going on with the latest version of Java.

Oh, and again, we've got as of 2021 is 17.

No, no, no. Both of you are completely out of date, AC.

So a large language model is fantastic because it's going to answer a lot of questions for us,

but we need to have timely responses that are up to date.

The options we have are fairly limited, like fine tuning.

This large language model would take an awful lot of work where we would have to include

all of these latest pieces of information in our fine tuning process, which is very elaborate.

So luckily there's a second option and that's retrieval augmentation generation.

And what that does basically is allows us to add or embellish the response created by the engine

with our own vector information.

So what we're going to do is we're going to upload a press release from Oracle,

which is the one that we've just seen.

We're dragging a document in and we're basically vectorizing this information

in a way that can be augmented to our large language request.

So let's ask the same question again.

What is the current version of Java and with our augmentation turned on here?

Now what we can do also is show the context.

So what we'll do here is actually see what's going on in the background.

So our model, our inference has pulled up the information from the Oracle press release

and given us a response, Java 23.

Fantastic. Okay. So that's up to date.

Now let's embellish a little bit.

You know, we'll add a few more tokens just to let this talk.

This token control here is limiting how many tokens the engine has to respond with.

So I've just increased it to just give it a little bit more leeway in the temperature as well.

Let's take a little bit more liberty.

Tell me about the new features and how they compare to the previous release.

Let's just see what it does.

So here we are. The engines come back.

Let's look at its context.

It has taken nearly all of that response from the augmented document that press release we added.

And it's given us this fantastic response.

So here's the accurate version, version 23.

As of, what did I say September the 17th?

So very up to date.

Let's turn off our vector database.

So it's ignoring our press release documents.

We've augmented and asked that question again.

And let's see what response we get this time.

So this is like, imagine me on the help desk.

I'm trying to answer a customer's request.

And I'm going to start talking about the current version of Java 16.

And the customer is going to be extremely unhappy because that is completely out of date.

So there we are.

That's just a quick way of augmenting your large language model to make it contextual with up to date information.

So if you have a high frequency business fast moving goods of any sort where currency is crucial,

then rag is a much much easier approach than potentially trying to fine tune a model or just using a model on its own.

Because remember, large language models are snapshots in time.

And it doesn't matter which one we choose.

Like we can choose any of these and we'll get the same response.

So all of them are going to have a snapshot in time issue.

So that's a good example of the key benefit of retrieval augmented results.

Your chatbot responses can include up to the minute information.

And so avoid the snapshot in time issue that affects large language models trained on historic data.