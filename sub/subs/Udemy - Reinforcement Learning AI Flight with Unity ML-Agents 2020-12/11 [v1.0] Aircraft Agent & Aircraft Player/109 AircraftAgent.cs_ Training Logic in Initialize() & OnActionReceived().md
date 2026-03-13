# AircraftAgent.cs_ Training Logic in Initialize() & OnActionReceived()

In this video, we're going to update a couple of our existing functions with some training specific

code.

So let's go into the initialise function.

And underneath the get components up at the top, we're going to add a comment that says override the

max step set in the inspector Max.

Five thousand steps if training.

Infinite steps if racing.

So here we're going to set Max Step.

This is something inherited from the agent class equal to area dot training mode.

Questionmark.

Five thousand Kolan zero.

So this basically checks.

Is it training mode?

If so, then the next step is going to be 5000.

Otherwise, zero.

So 5000 means it's going to stop training and start over again after 5000 steps have elapsed.

Zero means that it will go infinitely.

So it will never stop.

And we use that when we're not in training mode so that we can just keep going.

We don't ever get automatically reset.

Next, go down two on action received.

And we're going to want to add a small check here if frozen return.

And what this does is it will process all of our inputs here, but it won't do anything with them.

So you can actually actually this probably belongs up at the top.

If frozen return, because we don't need to process any of these inputs if we are frozen.

So, no, no real point in taking in boost and changing the boost when we're frozen.

So that will prevent anything below it from happening.

So we won't process the movement either.

Then after process movement, if area training mode.

So this only happens in training mode.

We'll add a small negative reward every step.

And this is the first time we're talking about rewards, so rewards are what helps the agent learn.

And in the case of a negative reward, you can think of that as like a punishment.

So what we're going to do here.

It may seem it may seem kind of cruel, but we're going to add a reward that is negative one F divided

by Max Step.

So we're just gonna give it a very small punishment.

Basically, one divided by 5000 every single step that it exists.

So it just hurts to be alive.

I guess this seems to help with reinforcement learning.

Giving it a small negative reward encourages it to take actions.

Otherwise, if it just sits still or doesn't do anything, then it's going to get.

It'll get a negative reward.

So it's encouraged to experiment, basically.

Then we're going to make sure we haven't run out of time.

If training and this is where our step time out comes into play.

If step count.

Is greater the next step.

Time out.

We are going to add a reward of negative point five F and then we will end episode.

So if we've run out of time, remember, this happens.

If we haven't touched a checkpoint within 300 steps, then we're going to give it a negative reward.

And and we start over, basically.

But if we make it past this, then we need to do a calculation to see if we got the next checkpoint.

So we'll save vector three, local checkpoint Dir for direction equals vector two.

Next checkpoint.

And this is a function that we're going to write soon.

So it's not going to exist yet.

So just ignore that red line for now and we'll say if local.

Checkpoint Dir.

Dott magnitude.

Is less than.

And this once something new that we're that we haven't talked about yet either.

This is going to use something called curriculum.

I'm going to type it and then I'll explain it.

Academy dot instance, dot environment parameters, dot get with default and then we want to type in

all lowercase.

Check.

Check point.

Underscore radius.

And then after that.

End quote, comma, zero F and then no semicolon.

Then we want to add curly braces here.

So what this is saying is if the length of the vector to the next checkpoint is less than a checkpoint

radius that we're going to specify.

Then we're going to say got checkpoint.

Now, the reason we're doing this is.

We are going to use something called curriculum and curriculum basically starts with an easier challenge

and then makes it harder, progressively harder, so that the agent can start to learn at a more easy

challenge.

In our case, we're going to check is it within a certain radius of the next checkpoint?

Not actually.

Is it flying through the next checkpoint?

So the curriculum configuration file, which will be setting up later, can be accessed through this

function right here.

It's going to check for something called the checkpoint radius, which will start at like 50 meters.

And then we'll once it's good at getting within 50 meters of the next checkpoint, then we're going

to lower it to 30 meters and then 20 meters and then 10 meters.

And then eventually it's gonna have to fly through that checkpoint to successfully get it.

So that's what's happening here.

It'll default to zero.

So if we don't specify a curriculum at all, then it's going to just say, OK, zero, you must be you

must actually fly through the checkpoint to get it.

But this is sort of checking for that right now.

This is intended to only be during training.

At no point are we actually going to be flying in the race and have a radius be acceptable for getting

a checkpoint.

But this does speed up training quite a bit in my experiments.

I've got checkpoint obviously doesn't exist either.

So we'll come back and we will define those functions in the next couple videos.