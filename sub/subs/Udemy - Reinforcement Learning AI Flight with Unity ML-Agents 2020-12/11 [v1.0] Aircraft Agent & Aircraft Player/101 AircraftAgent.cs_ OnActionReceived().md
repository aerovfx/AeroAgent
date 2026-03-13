# AircraftAgent.cs_ OnActionReceived()

In this video, we're going to start working on the on action received function, and this is another

override, so public override and we're going to look at this list for on action received.

Now, on action received is again, it's something that's inside of agent, and we can just look for

it really quick.

We look for on action received.

You'll see this is also empty.

And it's got actually quite a lot of description of what this does.

But let's talk about it instead of reading documentation.

So, first of all, let's just remove this.

This.

Function is basically.

What happens when the agent makes a decision?

So whether it's a neural network that's making decisions or it's a human that's making decisions or

it's an algorithm that's making decisions.

Those decisions will be passed into this function.

It'll it'll call this and it'll pass in a list of decisions in the form of an array of float numbers.

So rather than being like a list of, you know, in in English decisions that say, oh, turn left,

turn right.

It's a list of choices.

So in our case, we're going to have three different choices that need to be made.

And the first choice is how much to change the pitch of the airplane.

So sort of tilting back and forth.

The second choice is going to be how much to change the.

So that's turning left and right.

And the third choice is whether to boost or not.

So those choices, if they're gonna be floats, they're going to be represented as numbers.

So for us, we're gonna say if that decision made, if the choice is choice zero in the first slot of

this list, then we're not going to do anything.

We're not going to change the pitch at all.

If the choice is one, then we're going to pitch upward.

And if the choice is to, we're gonna pitch downward.

So we need to can sort of convert choice zero one and two into something that can be actually applied

as a pitch change.

So let's add a comment really quick.

Read values.

Read action inputs from vector action and then vector action is the chosen actions.

OK, so the first thing we're going to do is read values for pitch and your.

Pitch change equals vector action.

Zero.

So we're looking at that first choice and it's going to be either a zero one or two representing don't

change the pitch.

Pitch up or pitch down.

So we're going to say this first one is up or none.

So the reason that works, and I'll just add this second line, it's gonna make more sense if it's if

pitch change equals equals two, then we're gonna say pitch change equals negative one F and that's

gonna represent down.

So basically, we're either gonna get a zero one or two.

If it's a zero or one, we're gonna keep that pitch change value.

If it's choice, if it's option two, then we're gonna say, well, pitch change is actually negative

one.

So that's down.

We're going to do the same sort of thing for ya, so ya.

Change equals vector action of one.

So this is that second decision that was made and we'll say this is either turn right or none.

And if your change is equal to two, then we're going to say your change equals negative one F and that's

gonna be.

Turn left.

And then the last one is for boosting.

So we're going to read value for boost and enable slash disable trail renderer.

So to read this in all we have to say is boost equals vector action.

Two.

So this is that third choice.

If it's equal, equal to one.

So we're basically saying if it's a zero, then boost, it's going to be false.

If it's a one, the CHOTE, if the choice is one, then boost is gonna be true.

If boost.

And not trailed emitting.

Trail dog.

Clear.

So this is saying if we're boosting and the trail is not emitting, then we want to clear the trail.

And we want to set trail emitting equal to boost.

So this trail that clear means it's going to make sure that you don't see the trail anymore.

So if if we move positions or something like that, you don't want the trail renderer to do a weird

effect where it kind of like shows a trail that goes way across the level.

So that should be it for reading the actions.

Now, they don't actually do anything yet.

So we're going to need to add a function that's going to do something with these values.

So the last thing we're gonna do for now is add a new function here.

Process movement.

And this is a function that doesn't exist yet.

But I just want to put it there so that it's in our minds that we need to do something with these values.

In the next video, we'll come in and actually define this function.