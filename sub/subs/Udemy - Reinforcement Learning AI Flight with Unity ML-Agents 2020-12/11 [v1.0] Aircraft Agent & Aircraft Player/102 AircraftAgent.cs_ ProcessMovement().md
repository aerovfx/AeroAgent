# AircraftAgent.cs_ ProcessMovement()

In this video, we're going to build out the process, movement function.

And this is going to be a private void process movement.

We'll add a comment.

And this is going to calculate and apply movement.

So this one's pretty important.

We've read in our actions.

But we need to do something about them.

So that's where this is where we're gonna do it.

First thing we'll do is calculate boost.

And this one's pretty straightforward float, boost, modifier equals boost, questionmark, boost,

multiplier or one F.

So this is just a quick ternary operation that says if boost is true, then use the boost multiplier.

Otherwise use said the boost modifier to one F.

So one.

So don't boost essentially just go normal speed.

And then we're going to apply forward thrust.

So we want our rigid body got add force and the force is going to be transform Dopp forward times,

thrust times, boost modifier.

And then the forced mode is equal to or forced MODOK force.

OK, so this is just saying by default, we're going to go at the speed of forward times thrust.

But if the boost modifier is set to yes, we're boosting, then we're going to multiply it by this boost

multiplier.

Otherwise, we're just going to.

This value is going to end up being one.

So it'll go normal speed.

Now we need to figure out the new rotation, and to do that, we first need to get the current rotation.

We're going to call that vector three Kurr, our Otey.

So Kurr wrote for current short for current rotation.

Equals transform rotation.

Dot oilor angles.

Usually I write out my entire variable names.

But because this is going to show up a bunch of times, I figured I'd do a shorthand version.

Then we can calculate the role angle.

Which is between negative one eighty and one eighty float roll angle equals Kurr wrote dot z. greater

than 180 f question mark.

So if it's greater than one hundred JDF, we're going to set Kurr wrote Dot Z.

Minus three, 60 F.

Kurr wrote that Z.

So this is just saying, hey, if the role angle is greater than 180, subtract 360 degrees from it.

And we'll say if your change is equal to zero F..

We can assume that we are not turning.

So we want to smoothly roll toward center.

So basically, if the UI is changing, if we're turning, we're going to automatically roll the plane

a little bit.

And in this case, it's saying, well, we're not changing or not turning actively.

So we want to roll back toward just level.

So to do that, we just say roll change equals negative roll angle divided by max roll angle.

Else.

We're turning, so we want to roll in opposite direction of turn.

Rule change equals negative.

Your change.

So basically, if you imagine an airplane and you're watching it from behind.

If you turn to the right, you don't want your plane to just turn around the axis.

You want it to also bank sort of bank and turn into that like a more natural looking turn.

That's what this that's all this code does.

Next, we want to do something called calculate smooth deltas.

So what we're gonna do here is make sure that the turning is smooth.

When I first was working on this project, I had the planes flying just fine, but they looked super

jittery like they would be just like turning left and right.

Really quickly.

It didn't look good at all.

It didn't look like natural flight at all.

So to smooth it out, I ended up using this math f dot move towards functionality, which basically

says move toward a certain value, but only move so much at a given update.

So that's what's gonna happen here.

So smooth pitch change equals math f dot move towards smooth pitch change, comma, pitch change comma

to F times time.

Fixed Delta time.

So that's the Max Delta.

So we're applying a pitch change with a maximum of this.

Then smooth your change equals bath, FDR, move towards smooth your change, your change, and then

I'm just going to copy this because it's the same.

OK.

And then the last one is smooth roll change equals math f move towards smooth roll change, roll change.

And then I'm just going to paste that in again.

So now make sure that you matched up the right ones if you did a copying and pasting.

But otherwise, this is going to make sure that the change is much smoother than it would be if we just

use the raw values.

So at this point, we need to calculate new pitch, yaw and roll and clamp, pitch and roll.

So why do we have to clamp?

So if we were to allow pitch to be any value that would allow the plane to flip over backwards or to

flip over forwards.

Well, these aren't stunt planes.

And while we might be able to get that to work, I figured it'd be a lot simpler and more reliable if

we did not allow them to flip over backwards.

So that's why we're clamping the pitch.

We're only going to allow them to pitch upward to a degree of forty five and downward to forty five

degrees.

And roll is the same way if we are.

If we're turning to the right, we don't want to roll and flip all the way over and do a barrel roll,

that wouldn't make any sense.

So that's why we're clamping role.

So let's start out with a hitch.

And so we're calculating this new pitch value.

No float pitch equals Kurr wrote X plus smooth pitch change.

So we're applying this new change to the current rotation.

Times time got fixed.

Delta time, times, pitch speed, and I haven't mentioned this yet, but the reason we're using fixed

Delta time instead of fixed time is that fixed time.

Sorry, I misspoke.

The reason we're using fixed Delta time instead of just Delta time, which you may have used in previous

games, is that this function, this process movement, which is inside of an action received, is actually

called the fixed update step, not on the update step.

The update step happens every time a frame is updated and fixed.

Update happens every time the physics is updated.

And because we're working sort of with physics here and because M.L. Agents is by default set to train

at like 20 times speed, if you just did it with every frame update and it was going it maybe like 10

frames a second or something, this wouldn't work at all.

So you need to make sure you do these calculations with the fixed Delta time and fixed time.

So hopefully that makes sense.

So now that we have this new pitch value, we're going to say if pitch is greater than one ATF, then

we're gonna say pitch minus equals 360.

So this is just making sure that if this value is greater than 180, we subtract 360 so that we keep

it between the values of negative one eighty and one eighty.

Then we're going to say pitch equals math, FCC clamp.

And we want pitch comma, negative max pitch angle.

Positive Max pitch angle.

So now that we have pitch decided, we're gonna do your float, your equals, Kurr wrote.

Dot why?

Plus, smooth your change times, time got fixed.

Delta time, times your speed and your.

We don't have to clamp.

It's completely fine.

If it turns all the way around, that turns to the right.

Just over and over and over again.

That's completely fine.

Same to the left.

So we don't need to clamp it.

And now finally, we need to do roll.

So float roll equals Kurr wrote Dot Z.

Plus smooth roll change times timed to fix Delta time times roll speed.

And since we're clamping it, it's basically the same thing we did above, if role, it's greater than

one ADF role minus equals 360 F role equals math F to clamp roll.

And we're gonna clamp it between negative max roll angle and positive max roll angle.

OK, now that we've got the pitch, the Yea and the role all calculated, we just need to set the new

rotation and we're done.

So transform rotation equals attorney in Dot Foiler.

And then we want to pass in pitch JA rule.

So that is it for process movement.

So now we should be able to take in these actions and react to them appropriately so that the airplane

can properly fly.