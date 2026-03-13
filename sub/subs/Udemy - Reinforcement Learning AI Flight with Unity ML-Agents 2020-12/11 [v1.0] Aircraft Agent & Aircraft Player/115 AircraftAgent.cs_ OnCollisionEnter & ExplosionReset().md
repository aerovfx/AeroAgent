# AircraftAgent.cs_ OnCollisionEnter & ExplosionReset()

In this video, we're going to handle collisions with solid objects.

And solid object collisions aren't necessarily a good thing for our airplanes like these trigger collisions.

So for this, we need private void on collision, on collision enter.

This is another special function.

That's anytime it collides with a solid collider and we'll just say react to collisions.

And the collision here is collision info.

So the first thing we want to do is check to see if what we collided with is not an agent.

So if not collision, dot, transform, dot, compare, tag agent.

Basically, we want to be able to hit the other planes, but we don't want to immediately explode if

we hit another airplane because that would be kind of frustrating.

You could of course, experiment with turning it back on and see how that goes.

But in my experimentations, it's just seemed better to allow the agents to hit each other and they

can kind of bump each other into the walls.

That's fine.

But if you just auto explodes, it's kind of not fun.

So in this case, we hit something that wasn't another agent.

So if it's area training mode, then we want to add a reward for this of negative one.

So that basically is a big punishment for collision.

Anytime you collide with something, it hurts.

Now we're gonna end episode.

And just for good measure, we're going to return this to make sure that we don't keep going in this

function after we end episode.

Another I'm looking at it, this does this there's no point in this.

I was clearly just an extra line I had in my notes then.

Let's see after this, so we're going to have an else.

We're going to start Cobh, routine explosion reset.

And this is a function that we're that does not yet exist.

So let's define this function next.

This is what happens when we're not in training mode.

We're gonna do an explosion.

So this is going to be called private eye enumerator.

Explosion reset.

And this should make this thing not be a red squiggly.

But I spelled it wrong.

So there we go.

Right.

Explosion, reset.

Well, that's happy, but this isn't happy because I haven't yet returned to value.

OK.

So we need to add a comment for this.

And it's going to say resets the aircraft to the most recent complete checkpoint.

And returns.

Yield, return.

So if you haven't done a lot with a enumerators and start Kosenko routines and stuff.

Basically, what it means is it's going to be able to wait.

It'll do things.

It'll kick off this this function and then it'll keep executing new code after it so it doesn't stop

the code execution.

The first thing we need to do is freeze agent.

Then we're going to disable aircraft, Meche object, enable explosion.

So we're gonna take the mesh object.

And say, dot set active.

False.

So this is going to hide the mesh object that we're gonna say explosion effect.

Dot set.

Active.

True.

So we're gonna have an object on the aircraft.

That is an explosion.

And we're gonna make it visible as soon as we hide the airplane.

We're going to say yield return new.

Wait four seconds and we'll wait for two seconds.

After two seconds, we're going to disable explosion, re-enable aircraft Meche.

And we're gonna say mesh object, dot set active.

True.

So we're making it visible again.

Explosion effect.

Dot set.

Active.

False.

We're also going to reset the position.

So we can let's just say reset position here.

Area, dot reset, agent position.

And we're going to pass in a parameter called agent.

This so it's going to reset the position of the agent and then yield return new.

Wait for seconds.

Is not.

Wait for a frame.

Wait four seconds.

Two seconds.

One second.

Actually, this time.

And then we can thaw agent.

So at this point, the agent has been reset back to its checkpoint, previously passed through checkpoint.

We wait for one second.

And then we thawed out and let it continue.

So it doesn't it doesn't automatically start flying immediately as soon as it teleports back to the

position.

It's going to we give it a second for the player just to kind of get its bearings.

So that's it for explosion reset.

And now we've handled collisions in both of the different forms where we hit a checkpoint and where

we hit something solid.