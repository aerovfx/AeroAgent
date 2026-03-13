# AircraftAgent.cs_ Variables

In this video, we're going to start working on the aircraft agent.

And we'll be doing just some variables at the top of the class.

So go ahead and open up your aircraft agent script in visual studio and make sure that it looks like

this to start.

It should have a next checkpoint index accessor in it and it should be in the namespace aircraft.

The first thing you need to do is change model behavior to agent.

An agent is in lips, is in the unity M.L. agents namespace.

So make sure that that using statement shows up up there.

If you're if that ever doesn't work, you just do quick actions and then you can add it by default or

add it automatically.

And then let's start out by adding a number of different public variables.

So I'm adding a bunch of different things here.

We're not going to customize them in this course, but they are intended for you to be able to try them

out and customize them if you'd like.

So we're gonna start off let's add a header and header is just something that shows a sort of a divider

in the inspector view.

So it just keeps things organized.

And we'll call this movement parameters.

This is gonna be the only header that we had in this video.

There will be more variables coming in later videos.

But I didn't want to overwhelm you by just dumping every single variable that we're gonna need in this

class, because there are a lot.

So the first one is a public float called thrust.

And I want you to set that to one.

Zero zero zero zero zero.

So that's five zeros.

One hundred thousand public float.

Pitch speed.

And that's gonna be one hundred F public float.

Your speed equals one hundred F.

Public float rolls speed equals one hundred F.

And public float boost multiplier equals to F.

So the different speeds here thrust is for pushing the airplane forward.

So if we take a look at this oh, come on.

See if I can focus.

There we go.

OK.

So thrust is going to be a push sort of in this blue, this zie direction.

And then your is going to be how much we turn.

We rotate around the y axis.

So it'll be like trying not to mess this up.

But this is your.

Undo that.

And then pitch is X.

So like this this is changing pitch.

And then roll is like this.

OK, so make sure you leave that all at zero zero zero if you felt the need to experiment with me,

but that's the idea with these different controls.

And then the boost multiplier is just how much we're going to add some extra force to this when the

airplane is boosting.

Then we're going to skip over this public and next checkpoint and next, leave that alone.

And then we're going to add some private variables and just had a quick comment here that says components

to keep track of.

And we want to keep track of a few things.

We're gonna start with private aircraft area and we'll call that area.

And this basically the agent, the aircraft agent will want to know about which area that it's in,

which aircraft area.

So that's what that's for.

We want to keep track of its rigid body.

So unfortunately, you can't just use it.

Let me show you really quick.

Private Bridgid body.

If we call it just rigid body, which is what I would like to call it, it's gonna give us a warning

to get that warning to go away.

You can just say new, which tells it.

Yeah.

I wanted to call it that because it conflicts with something that's deprecated.

So then Private Trail Renderer and we'll call this trail and basically we're gonna add something that

makes it look like there's sort of a vapor trail coming out of the back of this airplane when it's boosting.

Then we're going to add a number of controls and we've got a few different things here.

I'll talk about how we're going to use them in a bit.

But for now, we'll just sort of cruise through and define them all.

So we're gonna do private float pitch change equals zero F. private float.

Smooth pitch change equals zero f..

Private float max pitch angle equals forty five F..

So that's forty five degrees.

Making sure that it can't do a complete loop de loop and flip all the way over on itself.

Private float your change equals zero f..

Private float smooth.

Your change equals zero f..

Private float roll.

Change equals zero f..

Private float.

Smooth.

Roll.

Change equals zero f..

Private float max roll angle equals forty five F.

And private bool boost.

OK.

Sorry about that.

I know that that was a lot to type, but just double check and make sure you spelled everything right

that you don't have any typos in there.

I'm doing that myself right now.

Looks like miraculously I got them all.

Boost is going to default to false.

You don't have to explicitly say that.

Technically, you don't have to explicitly say it with the zeros either.

But I just like to make sure it's clean.

So that's it for the.

The parameters that we need for now, these are just parameters that we're going to be able to change

later in the game if we want to experiment with faster airplanes or allow them to, you know, pitch

or yard or roll faster or if we want them to have a mega booster or something like that.

And then the rest of these will be using later on as we're filling out more functions in the aircraft.

Agent Glass.