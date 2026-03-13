# AircraftAgent.cs_ More Variables

In this video, we're going to pick back up where we left off in our aircraft agent script.

So we have this airplane that we can fly, but we don't have any opponents and they're not ready to

train yet.

So let's open up the aircraft agent script.

And I'm going to remove this breakpoint.

And then let's add some new variables.

So after the movement parameters section here, we're going to add a new header and we'll call this

explosion stuff.

And basically these are gonna be variables that have to do with what happens when the airplane runs

into something and explodes.

So it's at a tooltip and it's going to say the aircraft mesh that will disappear on explosion.

So we're going to show an explosion, but we want to make sure that the airplane disappears when that

happens.

So we're going to say public game object, Meche object.

And then just we will tell it what to make disappear in code based on what's placed in this thing.

So if you remember inside of here, we made this airplane object.

This is what we're going to be controlling.

The next one is gonna have another tooltip and that tooltip will say the game object of the explosion

particle effect.

So we're gonna use a particle effect for our explosion and it's gonna be called public game object.

Explosion effect.

Now, scroll down a little bit and we're going to add after the trail variable here.

I'm sorry I went too far.

We do need one more after explosion effect.

We're going to do another header and this one is going to be called training.

So we're going to have a specific variable that happens just for training.

And we'll do it tooltip for this.

And it's going to say number of steps to time out after in training.

And it's gonna be public int step time out.

Equals three hundred.

So the point of this variable is our agents will be learning.

And every step they're going to take some action and get some sort of result.

We are going to make it so that if they do 300 updates and they haven't made it to the next checkpoint,

we're going to reset them because they shouldn't take longer than that amount of steps to get to the

next checkpoint.

And it will just make it so that we can train faster.

We won't allow them to waste a bunch of time flying off into nowhere.

We'll bring them right back in so that they can get another chance.

So that's what that's for.

OK, now let's go down underneath trail.

And this one, I'm going to add a quick comment here that says when the next step, a time out will

be during training, private float, next step, time out.

So this is just it goes along with this step time out.

We're just going to keep track every time we had a checkpoint.

We're gonna increase this by three hundred basically, so that we know when to time out.

So if it keeps getting checkpoint's, it's going to be allowed to keep flying.

But if it gets lost, then we're going to stop it.

And then the other one is whether the aircraft is frozen, which means intentionally not flying.

Private Boole frozen equals false.

Now, there are a couple of cases where we want.

Frozen to be true and frozen will be true when we are paused, and it will also be true when we crash.

So the idea is that this plane isn't always going to be moving forward.

It's not always going to be flying if the game hasn't.

Or if the race hasn't started yet.

They're just going to be sitting still for a minute while the countdown goes, if the game is paused.

Obviously, we don't want the airplanes to go anywhere.

But we also don't want to completely freeze time.

We want, like the checkpoints to keep spinning and we want the game to technically be still going,

even though the airplanes aren't moving.

And then if the airplane crashes, we're yes, we're going to hide the airplane.

But we also want to freeze it so that the explosion doesn't keep flying on after it's done the after

it's crashed.

So that's it for the new variables for now.

In the next video, we'll go into some new functionality.