# Setting Up an Anaconda Environment to Train

Now I'm gonna show you how you can train your own neural network using a scene that's set up like this

so we're gonna continue using the basic environment because it's so simple and then I want you to open

up your Anaconda prompt.

So right now we are in the base environment and the base environment is not where we actually want to

do our work.

We want to create a new environment a new Python environment.

And the first thing I generally do is kinda EMV list say misspelled kinda kinda EMV list and that will

show me all the different environments that I already have created.

So you can see I've been doing MLA agents for a while and I'm going to create a new environment for

this MLA agents zero dot 11 not zero.

So the command for that.

And by the way the commands for how to use Anaconda are in the anaconda documentation.

I'll link to this page but it's the managing environments page provides a lot of help for how to create

new environments and how to modify them.

This is essentially the command that we're going to use this condo create dash and my the end.

What we're gonna do is kinda space create dash n and then we're gonna call this M.L. dash agents underscore

0 eleven 0 and then Python we're gonna set equal to three dots seven because the according to the MLA

agent's documentation you want at least three dot six dot one but three dot seven is or at least does

seem to be supported so I'm gonna hit enter and this will take a little bit of time while it downloads

packages so it's telling us what new packages will be installed type Y for yes and enter and then it

will install all of these packages into this environment.

So now we can use python and Pip and all these different things when it completes the command to actually

go into this environment that we've created is kinda activate M.L. dash agents underscore 0 1 1 0.

Now these this part right here tells us that we are in this new environment.

So if if this didn't work you can also try it with just activate that might work if you're not on Windows

I think its source activate there's a few different ways this works depending on your platform so just

know that you might need to reference the documentation to figure out what works for your platform so

now we need to install some of this stuff from the MLA directory.

The installation instructions if you are interested are in MLA agents.

The docs there's an installation one and I'm showing you this just in case you.

Well you probably will forget this in the future so it's good to know that this is here.

And I'll point out there's two ways that you can install the first one here Pip install MLA agents.

This will install it from something called Pi Pi which they the MLA agent's team at Unity publishes

the latest release of MLA agents to this sort of cloud server where it pulls from.

But if you want to make sure that it definitely is using whatever you used in your folder whatever you

downloaded in your home and your MLA agent's directory here then we can specifically say that.

So we're going to use this version of it installing for development.

So what we need to do is go into our directory.

So I'm going to do D.

And then I'm going to change into desktop slash course slash my intelligence folder.

So obviously if you put this somewhere else this is gonna be a slightly different command.

But now I'm inside of this folder.

And so these are the commands that I need to do.

So we'll do CDE M.L. dash agents dash in ves and this actually really quick.

I'll just do a DIY command.

This will show us that we are in this folder so we're changing directory into this directory first.

So I'll type CDE and agents dash and these then I want to run pip install dash e dot slash I've found

that once you're in Anaconda and you've initialized it with a python 3 7 you don't actually need to

type Pip 3 you can just do pip install and what that'll do is it's going to install all the things necessary

in this folder and it knows what to install because this setup Pi tells it what to do.

So that's just a little bit of what's happening under the covers so that one worked.

So now I can do a dot dot C D and L dash agents so I'm just following these and then I hit up on my

keyboard I can go back to previous commands and I'm going to run pip install dash e dot slash.

This one takes a little bit longer.

So we'll come back when this is finished.