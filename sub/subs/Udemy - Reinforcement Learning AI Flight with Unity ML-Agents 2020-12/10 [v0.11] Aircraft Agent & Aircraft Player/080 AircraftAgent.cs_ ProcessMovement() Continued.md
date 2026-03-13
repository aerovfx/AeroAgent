# AircraftAgent.cs_ ProcessMovement() Continued

All right.

So now that we have our role change and we already know our pitch change in our your change from up

above when we did this up here we did this calculation from our inputs.

We're going to calculate the smoothed out version of those so we'll call we'll say calculate smooth

deltas.

And Delta is just another word for change so smooth pitch change equals math f dot move towards smooth

pitch change

pitch change to f times.

Time that fixed delta time so just to explain what's happening here.

Move towards takes a value the current value so this smooth pitch changes the current value and then

it has a target value so pitch change.

And in this case it would either be negative 1 0 or 1.

Those are the three different possibilities that pitch change can be based on our input and then it

has whatever this is currently at.

So it's going to be somewhere between where it was and that target and then it's going to move toward

it at a certain speed or basically a max delta.

So a max change.

So it only is able to move toward that thing a little bit at a time.

And we used fixed delta time because this agent action happens in the fixed update rather than in the

regular just plain old update.

So now we need to do this for smooth ja change that's another.

Basically it's the same calculation.

So that's the same thing we just use smoothing change your change and then the last one is going to

be smooth roll change we're going to set it to the same thing.

I wish I could copy and paste but I'm afraid I'd mess it up.

So we're gonna do smooth roll change role change and then I guess I can copy and paste this.

So I will

OK.

So those are smoothed out movements and then we're going to calculate new pitch ya and roll and we need

to clamp pitch and roll.

So why do we need to clamp these will we will clamp them because we don't want to be able to roll all

the way around and we don't want to be able to pitch as far back as the plane wants to go.

This is just going to make it a lot easier.

There's no you know law that says that we need to clamp these or anything it just works better for our

type of game makes it feel more arcade style like you can't you can't get yourself into difficult positions

if we were doing like a space simulator or something.

You might not want to do this at all.

It just becomes a lot harder to fly so before we start working on these we're going to need a new method

and that's a way to clamp the angle.

So why don't we do that now before we start writing this.

We're gonna create a new method.

Private static float clamp angle and we're gonna take in a float called angle and a float called from

a float called to

and we'll say if Angle is less than zero degrees we're gonna set the angle too so we're gonna say angle

equals 360 degrees plus angle.

So basically if you have a negative angle we're going to add 360 degrees to it to make it a positive

angle then we're gonna say if Angle is greater than 180 degrees we're going to return math f dot max

of the angle and 360 degrees plus from K so this is essentially where we're reclaiming it and then we'll

say otherwise return math left men of angle or two so that even as I'm looking at it again I don't remember

exactly how it works the math there.

We struggle with like this kind of math for some reason but I've tested it it seems to work out great.

So I even think I might have found a version of this on stack overflow or something like that.

That's where I found this code.

Anyway we're gonna say this clamps and angle between two values and this is the input angle.

This is the lower limit.

And this is the upper limit and then we just have a couple more things to finish in here.

So we're going to use this float pitch equals hopes pitch equals clamp angle cur wrote dot x plus smooth

pitch change times time dot fixed delta time times pitch speed okay then we need to give it the well

let's do it down on this next line negative Max pitch angle and Max pitch angle so we're clamping it

between these two values but the value that we're clamping is the current rotations x value Oh I spelled

that wrong.

Hold on.

There we go and we are adding the smooth pitch change times the fixed delta time times the pitch speed.