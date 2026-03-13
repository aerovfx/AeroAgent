# AircraftAgent.cs_ Freeze() & Thaw()

In this video, we're going to work on the freeze and thaw logic.

So let's add this after overrides.

Before the private function.

And we're going to say public void Prix's agent.

And this is going to prevent the agent from moving and taking actions.

And what we're gonna do here is say debugged cert area, dog training mode equals equals false.

A comma and then freeze slash thar not supported in training.

So this is just a warning message for you.

If you accidentally have your area in training mode and you call frees agent.

That doesn't work in training mode, it's not intended to be used in training mode, so that's why I

figured putting this cert would be a good idea and we're gonna get frozen equal to true rigid body.

We're gonna call that sleep on it.

So that's gonna make it so that physics no longer apply to this while it's sleeping or frozen.

And then we're gonna say trail dot emitting equals false.

Then we're going to add a public void for agent.

So the opposite of freezing.

And we're going to use this same message and actually we can probably just copy and paste all of this

because we're going to basically undo everything we're going to.

Well, we can remove trailed out, admitting we're actually not going to automatically turn that back

on.

We will keep debugged, assert because we want the same thing frozen.

We're gonna set two false and rigid body.

We want to wake up.

And we can add a comment to this that says, resume agent movement and actions.

OK, so now we've addressed what that frozen thing is for.

We haven't used these functions yet, but we at least now have this functionality so that they can be

used in other functions.