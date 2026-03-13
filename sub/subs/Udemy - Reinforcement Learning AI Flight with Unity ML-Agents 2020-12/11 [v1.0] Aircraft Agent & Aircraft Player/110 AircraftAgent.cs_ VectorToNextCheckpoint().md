# AircraftAgent.cs_ VectorToNextCheckpoint()

In this video, we're going to define the vector to next checkpoint function.

So underneath this function, so outside of the on action received function, let's create a new private

function called private vector three.

Vector two.

Next steps.

Next checkpoint.

And we can add a comment for this gets a vector to the next checkpoint.

The agent needs to fly through.

And it returns a local space vector.

So this one, since we need a vector to the next checkpoint, we're going to start off by finding out

what that checkpoint is and where it is.

And then we can compare it to the transform of the actual agent.

So vector three.

Next checkpoint there.

So direction.

Equals area dot checkpoints.

So this is a list of checkpoints that the area knows about.

And then we need to pass in next checkpoint index.

So next checkpoint index.

If you remember, we defined it a long time ago.

It was right here.

This is where we're going to keep track of what checkpoint the airplane needs to go through next.

So it's going to pass that in to get where the next checkpoint is or what the next checkpoint is, I

should say.

This is a game object.

So to get the position from that, we say dot transform dot position.

And to get a vector from our position to this checkpoint position, we just have to subtract, transform

position.

So now we've got a vector from the transform of this agent to the next checkpoint.

We're gonna make another vector three called Local Checkpoint Dir.

And this is equal to transform dot inverse transform direction.

Next checkpoint there.

And you can see right here, it says transforms a direction from WorldSpace to local space.

The opposite of transformed out, transformed direction.

So this is a worldspace vector.

And now we're converting it into a local space vector.

And we're just going to return local Checkpoint Der.

You could just return this directly, but I thought it would be a little more obvious what was happening.

If we just did it on two separate lines.

So now this is happy.

So it's able to use this vector to next checkpoint, which we'll be using in another place to test how

long that vector is.

How far away it is.

And see if it's within the radius.

So in the next video, we'll work on got checkpoint.