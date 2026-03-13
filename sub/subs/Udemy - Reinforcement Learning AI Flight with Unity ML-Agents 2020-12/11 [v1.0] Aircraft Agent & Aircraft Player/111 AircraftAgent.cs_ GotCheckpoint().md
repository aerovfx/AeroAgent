# AircraftAgent.cs_ GotCheckpoint()

In this video, we're going to define our got checkpoint function.

So let's add a private void got checkpoint

and we can add a comment called when the agent flies through the correct checkpoint.

So there's going to be two places where this is called.

One will be when we actually collide with the checkpoint trigger or fly through it.

And the other is here when we're training and we're within that acceptable radius.

So what we do here is we say next check, reached update.

We'll say next checkpoint index equals next checkpoint index, plus one modulo area dot checkpoints,

dot count.

So this is going to increase the next checkpoint index, but obviously we don't want to go over the

total number of checkpoints that exist.

So that's why we use the modulus to make sure that that stays within that range of zero to number of

checkpoints.

Then we'll say if area training mode, we're going to add a positive reward now.

So at reward point five F.

And we'll say next step.

Time out equals step, count plus step, time out.

So this is when we're training, going to give half a point for every time we go through a checkpoint,

every time we get a checkpoint, and then it's going to increase that next step time out by basically

three hundred.

In this case, so that we can always keep making progress like this.