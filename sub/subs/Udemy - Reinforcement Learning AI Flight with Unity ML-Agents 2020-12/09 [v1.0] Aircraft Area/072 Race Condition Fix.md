# Race Condition Fix

In this video, we're actually coming back to the aircraft area and we're going to address a race condition

bug and we'll talk about how to fix it.

So I was done recording most of the videos for this 1.0 update, and I realized that there was a bug

in certain circumstances in the aircraft area.

So what happens usually is a wake is called and it populates this aircraft agent's list with all of

the different agents that are in the scene.

And then it populates all of the checkpoints by going through and setting all these up.

Well, there are certain circumstances where actually an agent is spawned and reset, agent position

is called before the aircraft agent even wakes up.

And in that case, the aircraft agent has this this function called and checkpoint's is no and aircraft

agents is no.

So that's unfortunate.

But we can fix it.

And the way we're gonna do it is basically if this gets called and checkpoint's is no or aircraft agencies

no, we're going to call this code because the air, the agents and the checkpoints.

It doesn't matter when we create the checkpoints or when we find them.

We just need to make sure we don't accidentally do it twice and that it's done on time.

So what we'll do is we'll extract these out into their own functions.

So let's do this awake function first and we can.

Select all of this right, click on it, do quick actions and refactoring us and extract method.

And this is going to create a new method and we'll call this one.

Find aircraft agents.

And hit enter.

And now you see that it's created this new private void function.

And we'll just say finds aircraft agents.

In the area.

So this is going to call this automatically.

But there's a chance that this will have been called somewhere else.

So you'll say if aircraft agents equals equals no, then we need to find aircraft agents.

OK, then we are going to put this after the start function just because I want to keep awake and start

together.

We also want to do the same thing for the checkpoints.

And we'll see.

We'll select this whole thing and we will do quick actions and refactoring and extract method and we'll

call this one.

Create checkpoints.

And.

We'll say creates the checkpoints.

OK, so now we've got these two functions, and I kind of wanted this one to actually go seconds, so

I'm going to.

Pace this after.

We need to do the same thing here.

If.

Checkpoints equals equals.

No.

Then create checkpoints.

Then we can copy this line.

And we need to put it down here so that if reset agent position is called, then we check doesn't know

where all the other agents are.

And.

Does it have the checkpoints yet?

And then, regardless of which gets called first, whether Reesa agent position is called first or Awake

and start are called first.

It's going to check.

Kate, has this been populated yet?

Has this been populated yet?

And it's going to process what it needs to do.

So this will prevent that weird race condition where sometimes this gets called first and sometimes

this gets called first.

Now, it doesn't matter which ones are called first.

It always does the right thing.