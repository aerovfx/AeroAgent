# AircraftAgent.cs_ CollectObservations()

Now we're going to finish up the aircraft agent class with the last function that we need and that is

public override.

Collect observations I'm going to add a comment to this and it's going to say collect observation used

by agent to make decisions let's say observations.

OK then you can remove this base dot collect observations so the first thing we're going to observe

about the agent is its velocity and we'll say observe aircraft velocity and this is going to be one

vector three.

So that's going to be equal to three values.

Now the reason we're keeping track of how many values this is is we're going to need this number how

many values since we're passing in one vector three that's an x y and z value.

So we have three float values that will be passing in the function that we need to call is add vector

obs and this will automatically handle basically whatever you throw at it.

So you can give it a bull.

You can give it a flow.

You can give it an int a quick turn in which would be four values a vector 2 which would be two values

vector THREE.

YOU GET THE IDEA.

THERE'S A LOT OF THINGS YOU CAN PASS IN HERE.

SO WE'RE GONNA PASS IN transform.

So this is the agents transform Di inverse transform direction.

And what this does is it transforms a direction from world space to local space.

If we did world space then it would have to the agent would have to be a lot smarter because it would

have to know the route it would have to convert to its relative position on the map.

We're going to have a few different versions of the map in our training scene and they're not all going

to be centered at 0 0 0.

So having local space transform makes a lot of sense here.

So we're gonna do rigid body dot velocity and then we can just close this off

and move forward the next one is where is the next checkpoint.

So this is also going to be one vector three so three values and we'll say add vector OBS

vector to next to checkpoint so remember we we cleared this earlier and it's it's the it's already a

local version of the vector to the next checkpoint.

So now it knows where the next checkpoint is relative to its current position and this might seem like

it's cheating but actually the way we're going to make the game work for the player is the player will

have an indicator on their screen of where the next checkpoint is.

It turns out I'm not sure if you've experimented with this much but in some cases it's not always obvious

which checkpoint is the next checkpoint that you're supposed to fly through.

And so it does make sense to at least have some indicator of which direction you should fly next so

this next one is the orientation of the next checkpoint

and this will be one vector three and it will be three values.

Now this one maybe isn't completely necessary for it to work but if you think about when you're flying

through the course it's really helpful to have an idea of which direction the checkpoint is sort of

turned because it gives you a hint at which direction you need to fly once you go through it.

So if the checkpoint is sort of turned to the left a little bit then you might want to sort of veer

to the right and then sweep in at it at a curve rather than flying directly at it and then having to

make a really sharp turn after you've gone through the checkpoint.

So this just gives that information in the event that the agent decides to use that as part of its calculations

for how to approach the next checkpoint.

So the way we'll do this is vector three next checkpoint forward

equals area dot checkpoints next checkpoint index dot transform dot forward.

So this is just getting the forward vector of that of that checkpoint and then we'll say add vector

OBS transform dot inverse transform direction.

Next checkpoint forward.

Now we're going to start doing our ray perception and Ray perception is a little more challenging.

So I want to show you sort of a visualization to to explain what I'm talking about.