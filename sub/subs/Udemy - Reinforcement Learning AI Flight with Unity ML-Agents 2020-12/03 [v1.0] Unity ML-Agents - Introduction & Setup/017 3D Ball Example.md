# 3D Ball Example

In this video, we're going to take a look at the 3D ball example.

So take a look in your email agents example's folder and open up 3D ball.

Go into scenes and then pick the 3-D ball one.

Don't do the hard one.

These little cube.

Agents are basically trying to keep these balls balanced on their heads.

And if you hit play right away, these are pre trained.

So they should be pretty good at balancing the ball on their head.

So they're not trained to perfection, as he saw that ball did fall off its head.

But in general, they're pretty good at keeping these balls from falling off of their heads.

So pretty impressive.

And let's take a look inside of each one of these.

You'll notice that there's 12 of them.

And we can look at just one in particular.

So inside of here, there is a ball and the ball is just a basic sphere.

And it has a material on it that makes it look like a checker and it has a sphere collider and a rigid

body, rigid body is what allows it to have physics and gravity and interact with the head of the cube.

Guy.

Then there's the agent.

So each one of these is an agent.

And right now we're looking at this one.

The agent has some scripts at the top level as well as a box collider.

And then underneath, it has just some visible pieces here.

So these don't actually have any physical components to them.

They're just for us to look at and for it to look nice.

The agent itself has three, four, four scripts here.

So the ones that are particularly interesting are this ball 3-D agent script and the behavior parameters

script.

So the ball 3-D agent is the script that they wrote.

That is specific to this particular agent.

And it controls what the agent does.

And I'll just double click this to open it.

So there are several functions in here.

I'm not going to go into detail, but I'm just going to point them out.

So first of all, this is inheriting from the agent class.

Agent comes with the unity M.L. agents namespace, and it contains a bunch of functionality, including

some functions that we're going to end up overriding for our airplanes.

But they've override it a few here for their own functionality.

So this one right here, anywhere you see an override.

It's using something from the agent class.

So it's overriding initialize.

And this is what happens when the game starts, essentially.

And then there's collect observations.

So it's observing things about the world.

And in this case, it's observing its own rotation in the X and Z axes, as well as the position of

the ball and the velocity of the ball.

It also has this function on action received, which is called any time the neural network makes a decision.

And it does some math to figure out how to convert a list of actions that come in as numbers and convert

them into rotations around the axons, the axis.

So we'll go into more detail on this.

But I just wanted to give a really high level overview.

It also handles rewards that it gets based on the position of the ball.

There's one for on Episode Biggin, which happens anytime a new training run starts here, Ristic allows

you to control these agents with the horizontal and vertical axes and set ball is to just reset where

the ball is.

So back in here.

Basically, this is doing all of that work while the game is playing.

Behavior parameters specifies some things about how the neural network hooks up to things.

So this vector observation space size.

This number eight actually corresponds to the things that are being observed here and collect observations.

We'll go into more detail on that later in the course.

Continuous means that it is taking actions that are somewhere in the range of negative one to positive

one.

So you could give it a point five or a plus one or negative one.

Negative point seven zero.

Something like that.

So those are the values that get passed in that say how much it should rotate in either direction.

Then there's this model here.

This is the pre trained neural network weights.

And those actually are in 3D ball T.F. models because these are actually saved tensor flow models that

have been converted into Barracuda format.

So Barracuda is just the neural network inference engine that's made by unity for unity.

Don't worry if that was completely over your head.

We're going to go into way more detail on all of this stuff.

But I just wanted to give kind of a an overview for those of you who are curious.

And the rest of this safe to ignore at this point.

So the thing that's important to know is that these are pre trained.

And if we want to retrain it, train it ourselves.

Or if you have a completely new agent, you're obviously not going to have a pre trained neural network

yet.

So I'm going to show you in the next video how you can actually retrain this.

And that'll give you an idea of what the whole end to end process is for creating a project like this,

writing a script like this and then training it, which will do in the next video.