# AircraftAgent.cs_ AgentAction() + ProcessMovement()

Our only other value that we need to read in is the boost value.

So we'll say read value for boost and enable slash disable trail render so we'll just say boost equals

vector action at index to is equal to 1 so if it's 0 then boost is false.

It's not gonna boost if it's 1 then we will boost and there's no instance where boost will be a value

of 2.

So we're just going to handle that case and set it to a boolean value.

Now we say if boost and trail emitting is false then we'll say trail dot clear.

So what this is going to do is if we've been told we're boosting now and we weren't already emitting

from our trail then we're going to clear the existing trail that's showing up behind this may not be

clear the trail render or you'll it'll be very obvious what's happening.

Once we start playing.

But we're gonna say trail dot emitting equals boost.

So it'll basically clear the existing trail of vapor I guess is what it would be behind an airplane

and then based on whether we're boosting or not it would either turn it on or turn it off OK.

So then now we have to actually process the movement controls that are coming in so we're going to separate

that out into a new function called process movement so that it doesn't get too crowded in this function.

So if we right click on this go to quick actions and we generate a new method.

You can also do that with control period.

It'll automatically generate this method for us.

I may have done that a little fast.

Hold on I'll redo it if I right click quick actions and refactoring and then generate method creates

it.

Okay.

So for this scroll down to my notes

we're going to calculate and apply movement

so the first thing we'll do is calculate boost so we're gonna float and create a float called Boost

modifier and that's gonna be set to either 1 meaning there's no boost Just go the normal speed or it's

gonna be set to the boost multiplier which in our case we set it to 2 up above.

So we need to check.

Are we boosting.

If so then you set this to boost more modifier sorry boost multiplier if not we set it to 1.

So that's a ternary operator there to do that.

Check

then we apply forward thrust so we use our rigid body that we got in the initialize function.

We say add force and the force we want to apply is transform dot forward times thrust times boost modifier

and then we want this force mode to force

so we're just applying and whether we have a boost on or not it'll apply it either by it'll multiply

it by one or two.

Basically

next we're going to get the current rotation and we'll call that a vector three cur wrote equals transform

rotation dot Euler angles.

In case you're ever wondering how to pronounce this it's it's actually Euler who knew and then we need

to do the roll angle.

So this is a little more involved here calculate the roll angle and this will be between negative 1

eighty and one eighty so.

So the roll is not coming in from player input at all.

We're actually going to calculate it based on the your value.

So if you're turning to the left we're going to automatically bank your plane so that the bottom of

it is rolls to the right so we'll say float roll angle equals cur wrote dot Z is greater than 180.

So if it's if the current rotation around the z axis is greater than 180 then we want to set it to cur

wrote dot ze minus 360.

Otherwise we do curve road that the that's the OK.

So this is just doing some logic to make sure that we roll in the right direction we'll say if ya change

is equal to zero scroll

we're going to say not turning smoothly roll toward center.

So the idea here is if we're not trying to turn it all we want to gradually sort of roll the plane back

to being completely level it feels very unnatural to turn your plane and then have it be stuck being

sort of rolled at an angle.

So this just fixes that.

So role change equals negative roll angle divided by Max roll angle and then else this would mean that

we are turning so turning roll in opposite direction of turn and we'll say roll change equals negative

your change now for this logic I don't want you to feel like I knew how to do this and just wrote it

out and it worked perfectly.

This and the code that we're about to write was actually very difficult for me to figure out how to

get working so hopefully it makes sense.

Hopefully I wrote it in a way that you know the comments explain what's happening and how it actually

works and why it's smooth.

But don't worry too much if it doesn't make a lot of sense.

It should work as long as you use the code as is.