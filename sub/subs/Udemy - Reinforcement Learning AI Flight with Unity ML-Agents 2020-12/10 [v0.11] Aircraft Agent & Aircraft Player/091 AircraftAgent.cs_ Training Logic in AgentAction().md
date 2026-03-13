# AircraftAgent.cs_ Training Logic in AgentAction()

Now let's go back to the code and we're going to add a couple things to Agent action.

So one thing we need to do is before we do any movement processing we need to check if this is frozen.

So if frozen return.

So this will just make sure that if we're frozen we don't move the agent at all.

We'll still read in all the inputs but we don't have to do anything else so then we want to update.

Oh yeah.

OK.

So after process movement we want to check if area dot training mode.

So we've got some special logic here that only happens in training mode.

We're gonna say let's see small negative reward every step.

So we're gonna start.

This is the first time we're actually talking about rewards in this context.

So we want to reward the agent for good behavior and we want to punish the agent for bad behavior.

Now too much reward or too much punishment ultimately won't get us the right reward.

But it's been shown through research not my own that a small negative reward given every time step will

make the agent be forced to take action because you don't really want it to get to the end without receiving

any feedback whatsoever.

A small negative reward will just encourage it to do an action faster than it might otherwise so we'll

say add reward and the reward we're gonna give it is negative one f divided by Agent parameters dot

Max step and I think this F is important.

I'm pretty sure if you do division with an integer first and this is another integer then you're gonna

get an integer result so you'll end up not getting a fraction you'll end up getting another integer.

If you do two integers divided by each other and then that'll probably round down to zero.

And that's probably not what you want.

So we want actually in our case Max step will be 5000.

So we want negative 1 divided by 5000 as a float.

And this just forces it to be a float by doing that negative 1 F

and then we want to make sure we haven't run out of time.

If training so obviously this is all in if training I suppose if get the step count.

So this is something coming from the agent class that you know the that we inherited from get step count

is greater than next step.

Time out.

So that's that thing that we're gonna be updating.

We're gonna add a reward of negative point five f k so that will punish somewhat a small amount.

Basically if we run out of time now these rewards.

My goal generally is to keep them kind of close to the range of negative 1 to positive 1.

So if you make super big rewards or very small rewards meaning very negative rewards then it can get

kind of difficult for you.

I think for the agent to tell the difference between like what does negative 5 mean versus negative

five thousand like it it's it's kind of hard to scale it properly and it's hard for us as the developer

to figure out whether we're appropriately appropriately rewarding something or punishing things so we're

going to say done after we've done this reward.

So if we time out we're done and then we'll call Agent reset

and then this last part here we'll say vector three local checkpoint there.

So this is the local checkpoint direction equals the vector to next checkpoint.

This is a method that doesn't exist yet we're going to write it but let me let me keep going here and

we'll get to that function if local checkpoint dir dot magnitude.

So this is the length of that vector so it's basically we make a vector from us to the checkpoint.

The next checkpoint that we have to get to as the agent and then we see how long that is.

So how far is it to the next checkpoint.

If we draw a straight line to it if we're checking and then we're checking if that's less than area

dot aircraft Academy dot reset parameters

and then checkpoint under escort radius.

All right.

So this part

I have to take some time to explain when I was first training these agents.

My goal was to get them to just fly through the checkpoints.

So it's too much difficulty to show you a checkpoint maybe let me know I'll do it.

Since we're here so I'll hop back out to here and go to the prefabs and just view one of these prefabs.

So when I had just these triggers these boxes right here as being the thing that determined whether

they got to the next checkpoint.

They took a very long time because if you remember we placed these checkpoints about 100 meters away

from each other and at 100 meters there's a lot of options that are wrong right.

Basically anything other than straight ahead and not turning either direction or going up and down is

the that's the only way to hit the target and it would be kind of like trying to play a game of darts

in the dark or trying to throw a ball that hits a target in the dark.

If you don't even know which general direction to go.

So what I did instead was I experimented with basically creating a giant like sphere of what I would

consider correct.

So the idea was if you got anywhere within say 50 meters of this thing then you would get points and

then gradually I would shrink that range that radius so that you were forced to actually go through

this as the agent.

So that's what this is doing.

This is using something called curriculum learning which we're going to talk about more in the future

and it's using reset parameters to get this checkpoint radius.

So we'll come back to this.

I just wanted to touch on that so you know what it is.

And then we're gonna call a function that we haven't yet implemented called got checkpoint to indicate

that we've we've hit this checkpoint.