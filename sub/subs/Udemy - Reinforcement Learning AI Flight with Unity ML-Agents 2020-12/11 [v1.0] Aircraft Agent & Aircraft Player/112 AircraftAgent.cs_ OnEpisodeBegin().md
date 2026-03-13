# AircraftAgent.cs_ OnEpisodeBegin()

In this video, we're going to work on on episode begin.

So now that we're using this next step, time out.

Step, count, step, time out.

We should make sure that we're initializing it properly.

And the way we're going to do that is with a function that is actually an override.

Just like initialize an on action received.

There's a function that's called any time a new training session starts.

And that is public override.

On episode begin.

No public override void, actually.

Now, we don't need to call the base class here.

That should be empty.

What we're gonna do inside here, actually, let's let's add a comment called When a New Episodes Begins.

Pretty straightforward.

So what we're gonna do in here is first reset the velocity, position and orientation.

So the thing you need to know when you're training agents or flying agents or whatever, if they have

a rigid body on it and you reset the training, you always need to reset the rigid bodies, velocity,

rigid body and velocity equals vector three zero.

The reason you need to do this is let's say you're flying forward or sideways or whatever, depending

on what kind of agent you've written.

Then you reset the rigid body is still going to be moving at that same speed.

So you don't want to keep it going at that same speed.

You want to stop it so that it can start over fresh.

We also need to do that with angular velocity, rigid body got angular velocity equals vector three,

dot zero.

Now, in this case, I don't think the angular velocity should ever be anything but zero because we

locked the rigid body to not rotate.

But it's just good practice and it's nice to have this just to make sure that nothing weird is happening.

We're just zeroing things out just to make sure every time a new episode begins.

We're going to set trail emitting equal to false.

So this makes sure that the the boost trail is not still emitting from the neck from previous run.

And then we're going to call area dot reset agent position.

And the agent we're going to pass in is this.

And sometimes it's a little unclear when you're passing things in a little trick with C sharp, you

can actually say which parameter you're passing in with a colon and then you can do it like that.

And randomise we're going to pass in area training mode.

So if I didn't say what these variables were, it might be confusing what they were for.

So we're we are telling the area to reset the agent position of this aircraft agent that is calling

this function.

And then also we want to randomize it if it's training mode.

We don't want to randomize it if it's not training mode.

So I mentioned earlier that if we're flying through the course and we reset agent position, generally

we want to be reset to the main checkpoint.

But in the case of training mode, we actually want to be reset to a random checkpoint so that we can

train equally or mostly equally from every single checkpoint.

Hopefully that makes sense.

The last thing we want to do in on Episode Begin is update the step.

Time out.

If training.

So we'll say if area training mode.

The next step time out equals step, count plus step time out.

So the step count.

At the beginning, we'll be zero.

And since this is set to three hundred, our next step.

Time out will be at 300 steps.

But if we've started a new episode.

I suppose the step count should, in theory, still be zero.

But if for some reason it was higher than, we would also make sure that this was updated.