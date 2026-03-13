# AircraftAgent.cs_ Even More Variables

Now there's another component that we want to keep track of.

So we'll add a private Ray perception 3D and this will be called Ray perception

and what Ray perception is is it's basically a bunch of Ray casts that shoot out and then can detect

things in the world.

So kind of the laser pointer of the airplane that points out and tells us how far away something is.

So we'll add it here as a private variable and then we'll we'll get it in this initialize agent.

We need to add a couple more things.

So let's add a new little section here.

This will be when the next step.

Time out will be during training.

And it is private float.

Next step.

Time out.

So every time we hit a checkpoint we're going to increase the next step.

Time out to the current time plus whatever this value is.

So plus 300.

So if we're at a thousand is I guess this is steps in the training.

Then we hit a checkpoint.

Then it's going to increase the step time out next step time out to thirteen hundred and then we need

a private bool frozen.

We're gonna set that to false by default and this is whether the air craft is frozen meaning in tension

only not flying.

So there are times where we're going to want to freeze this agent.

Number one being when we pause the game we want the agent not to fly.

So we'll freeze it in space.

It'll still the game will still be running but the agents won't move.

And the other time is when a crash happens we want to freeze the agent in place while the explosion

happens and then we'll eventually reset the position

so that should be it for our new variables that we need to worry about.