# AircraftPlayer.cs_ Heuristic()

In this video, we're going to implement the heuristic function.

So to start with this, we're gonna do a public override.

And we want to find heuristic.

And you'll notice that this parameter here is a list actions out.

We need to fill this up with choices or with decisions that will then be fed into this right here.

So we have this vector action, zero one and two that correspond to pitch, yaw and boost that we need

to somehow feed in values.

So what we're gonna do is read in from these inputs and then convert those into appropriate actions.

Now, we don't want to call based out heuristic actions out.

Let me just show you really quick, because if we call this function, it's going to log a warning and

say that heuristic method was called but not implemented.

This is the same thing that will happen if heuristic ends up getting called on aircraft agent where

the heuristic function won't be implemented.

So to explain that a little bit more.

Basically, there's a way to set the agent to either use heuristic or just use neural networks.

So in the case where it's told to use heuristic, if it's not an aircraft player, then we're gonna

have some issues.

It's going to try and call the heuristic function.

It won't have it and won't know what to do.

So really, we only want to be using heuristic on our player, which is you controlling with your keyboard

or your controller.

So let's delete this.

And let's start reading in from these inputs.

So the first thing is pitch.

And in this case, one is going to mean up zero is none.

And negative one is down.

So we're going to say float pitch value equals math.

F dopp round pitch input.

Read value float.

And then parentheses like that.

So this is telling it to read a value from pitch input as a that's a type of float.

Round it to the nearest integer basically and then pass that in.

So then we have a pitch value that's either going to be one zero or negative one.

Then we're going to do the same thing with your yacht is one his turn right?

Zero is none.

And negative one is turn left.

So for this one will do.

Float your value equals math f dot.

Round your input dot.

Read value float.

Make sure that that is outside.

All right.

And then the last one is Boost.

One equals equals boost.

Zero is no boost.

So float boost value equals math after round boost input.

Read value of type float.

OK, so now we have these values, but these aren't quite ready to put into the actions out array yet.

So we need to convert negative one, which is down to discrete value to remember.

Our choices are zero one and two, not negative one zero one.

So that's why we're doing this conversion.

If pitch value is equal to negative one, F pitch value equals two.

So we're just gonna convert it.

Now we need to convert negative one, which is turn left to discrete value of two.

So if your value equals equals negative one, if your value equals to F.

And then finally, now that we've got these two values converted to some some choice of zero one or

two and boost is already zero or one, we can just feed those into the actions out array and then we're

done.

So actions out zero equals pitch value.

Actions out one day equals your value and actions out to equals boost value.

All right, so now we have these in this array.

And then when heuristic is called by the underlying agent class, it will ultimately get passed into

aircraft agent on action received and then will will essentially be converting it back in this case.

So you might be wondering why we even do that conversion.

Well, it just turns out that the implementation of how discrete choices like that are made in AML agents

is that it's just zero.

One, two, three, four, five, six, seven, eight.

What however many choices you need to have it if you want to use between negatives.

Negative one and one you can.

But that's a different story.

We're not doing that in this case.

So aircraft player is now complete.

Aside from I should probably add a comment.

So this reads player input and converts it to a vector action array and the actions out parameter is

an array of floats for agent action to use.

So that's this.

Well, actually, this this function changed the name of it change.

So this comment is actually out of date.

OK, so that now that we have that done.

Now this class is complete and we can use it any time we want the user or the player to control an aircraft.