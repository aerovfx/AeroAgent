# AircraftAgent.cs_ AgentReset(), FreezeAgent(), & ThawAgent()

All right.

Now let's handle what happens when the agent resets.

So we're gonna put this after Agent action it's a public override and it is Agent reset and it's pretty

straightforward.

What this does I'm not even going to bother with a comment so we're going to reset the velocity position

and orientation so we'll say rigid body dot velocity equals vector three dot zero and then rigid body

dot angular velocity equals vector three dot zero.

So just in case it was spinning for some reason it shouldn't.

But just in case we're going to make sure that it's not spinning out of control then we'll say trail

dot emitting equals false

and area dot reset agent position this and then randomize is area dot training mode so actually this

first one.

I'll just say agent we can just be very explicit about what these parameters are that we're passing

in so that it's clear what's happening.

So we're saying reset the agent position remember we we wrote this function earlier in the aircraft

area we're passing in this agent.

So whatever agent this is it's running and then whether or not we decide to randomize is based on whether

it's training mode.

So if it is training mode then we randomize the position we pick a random a random checkpoint to set

it to.

But if it's not then we just reset to the previous checkpoint that was past

then we need to update the step time out if training so we'll say if area training mode next step time

out equals get step count plus step time out and that's all for Agent reset

we've got a couple other ones that we might as well get to right now we have public void freeze agent

so this is something that's going to be called anytime we want to stop the agent from moving so the

comment will say prevent the agent from moving and taking actions and then inside here the first thing

we'll do is a debug assert cert we wanna make sure that we're using this correctly.

So we'll just check area dot training mode is equal to False

and if if this is for some reason if training mode is true then we're using this wrong.

So we'll say freeze slash Thor not supported in training.

There's no reason for us to bother freezing the agent except in just a regular race mode in training

we just want to reset the agent immediately we don't really want to worry about showing explosions and

stuff that just isn't necessary for training so we'll say frozen equals true rigid body dot sleep so

that we'll make sure that the rigid body any forces that are on it will be paused temporarily and then

trail emitting equals false.

Now we need a public void thaw agent so this is the opposite

and fill out a comment resume agent movement and actions and we're going to do the same thing we can

actually just copy this and paste it down in here and then we'll say frozen equals false and rigid body

dot wake up.

So now we can use these methods to freeze and thaw our agent.