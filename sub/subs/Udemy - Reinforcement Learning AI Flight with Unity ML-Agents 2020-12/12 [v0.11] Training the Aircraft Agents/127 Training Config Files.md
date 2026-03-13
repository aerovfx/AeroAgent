# Training Config Files

Training requires some configuration files in order to work.

Basically it's going to read these files and configure some different settings so that our training

works properly because there are a lot of well knobs figuratively that you can turn and settings you

can change that will dramatically affect the way that you train your neural networks.

So I want you to go into your MLA agents directory and find the config folder and we're going to copy

this and then we're gonna go back into our aircraft MLA folder and this is where your Unity project

is.

This is the one that contains your assets and your logs and your packages and all that.

I have a get in and get ignore or file in here.

These are so that I can basically keep version control history in here.

So you may not have these few didn't set that up but we're going to paste our config file our config

folder into here and the reason we'll do this is for the same reason I'm backing things up with my project

to get Hub I want to have a version history of my configuration files to so let's just take a quick

look in here.

There's a bunch of these.

Trainer config files there's a gale config off line B.S. config.

We're not actually gonna use these for just the trainer config so we can delete these and then the curricula

contains a couple folders we're gonna need one we'll create a new folder called aircraft and I just

want to show you what's going on in here.

So the curriculum folder is what controls a sort of gradual increase in difficulty as you train.

So the idea is that if your if your area is particularly difficult to solve meaning it's too hard to

solve the problem just by taking random actions.

Sometimes it can be a lot faster to work with a curriculum where you make it a lot easier at the beginning

and then gradually make it harder as you go.

And if you remember in our aircraft agent and this is in the agent action method there's something here

that we talked about.

This is the checkpoint radius so we're going to gradually reduce the size of the radius that the agent

has to get within to get the checkpoint using a curriculum.

And let me just show you really quick what this sample one looks like.

This wall jump one so we can open up this Jason File and I have mine set to open in Visual Studio code

but it doesn't matter where you open it really.

So this is a Jason File that determines a few different things.

So there's a concept of thresholds.

This is at what point do we increase the difficulty.

And then there's a concept of parameters.

So these are the things to change once we've passed this threshold.

So once we've got passed I think this probably means 10 percent of the progress.

Then we will change the big wall min height here two to zero from zero to four and we'll change the

max height from four to seven.

So that's what this is doing.

We're gonna do this as specifically for our airplane.

Shortly then out here the trainer config.

This is what does a lot of the parameters or hyper parameters I should say for machine learning.

If you haven't done deep learning machine learning before hyper parameters are basically what sort of

defines your network and then how it's trained.

So there's a lot going on in here and I don't expect you to try and understand all of it.

There are a few things that we'll be modifying so that our network trains better and just is as optimal

as it can be

what I do want to point out is that there's a set of default parameters and then each basically learning

agent for their different examples has its own specific parameters that are overwritten.

So these values actually override these default parameters.

So we just need to find a project.

One of the examples that works best that's most similar to our projects so we can kind of take.

We can copy it and the one that we're actually going to borrow from is this pyramids one and I just

want to talk about the pyramids really quick.

So this is in their documentation the MLA agent's documentation there's this learning environment examples

which I'll link to in the course materials if you scroll down you can see all the different examples

and how they work and what they mean.

If you go down to the bottom at least as of this recording the pyramids scene is the one we're copying.

And the reason is because it actually uses a bunch of casts to see and it moves around in this environment

so it sort of scoots around in this environment and then it uses Ray casts to see what it's doing.

So I figured that's pretty similar to what we're doing.

So that was my starting point for which one of these I wanted to use for configuration.