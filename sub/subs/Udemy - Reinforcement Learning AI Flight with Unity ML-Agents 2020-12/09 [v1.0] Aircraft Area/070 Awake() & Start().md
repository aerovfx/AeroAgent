# Awake() & Start()

In this video, we're going to add functionality for what happens when the airplane first comes to life,

when it wakes up.

So the first function we're going to add is called private void awake.

And we're going to add a comment to the top.

So if you hit three slashes, we'll add this and the summary that we're going to add is actions to perform

when the script wakes up.

And inside of here, we want to find all aircraft agents in the area.

OK, so awake is the first thing that's called as soon as the scene sort of wakes up.

It's called before the start function.

So we're just going to find all of the aircraft agents.

And at this point, all of them should be children of the aircraft area.

So we just need to check inside of the list of children to find any aircraft agents.

We don't want to do this for the full scene because if there's multiple aircraft areas in there, then

it would grab those of other aircraft areas and that could get messy.

So we'll say aircraft agents.

So we're referencing this list of equals, transform, dot, get components in children.

And then we want to, in these angle brackets, say aircraft agent.

So we're finding any components in the list of children that have that are of type aircraft agent.

And then we want to do to dot to list.

Like this.

And what that's going to do is convert this into list format, because this by default will return an

array of aircraft agents instead of a list.

Then we want to debug a cert aircraft agent's stop count is greater than zero.

So we want to make sure that this has something in it now, because if we didn't find any aircraft agents,

then something's wrong.

We'll say no aircraft agents found.

All right.

And by the way, if this to list thing doesn't work for you, I believe it automatically added this

using system dot link thing up here at the top.

That's link functionality.

So if for some reason that didn't automatically happen for you, just know that that's that's what you

need for that functionality to work.

Now we're going to add the start function.

So private void start and we'll add a comment here that says set up the area.

So we wanted to do this right away, right when we were waking up.

But we don't want everything to happen right when we're waking up.

We want something, some stuff to happen a little bit later so that we are able to.

Have other things that need to be set up in the wake function happened before this stuff happens.

So what we're gonna do is create checkpoints along the race path.

So the first thing we'll do is a debug assert and we're gonna check if race path does not equal no.

Then race path was not set.

So we're saying make sure that race path is not null.

Otherwise assert and say race path was not set.

So that'll give us a warning if we didn't set it up correctly.

Next, we want to create a new list.

So check points.

We already created that above.

We want to initialize that as a new list equals new list game object just like that.

So now we have an empty list of checkpoints and we need to start filling it up.

So how do we know what to fill up this list of checkpoints with?

Well, we're going to need to reference our Sinna machine path and that snowmachine path has a number

of points in it.

So the first thing we'll do is figure out how many we need to create.

We're going to create a new it called Numb Checkpoints.

And this will be equal to it.

So we're gonna convert this to an end race path.

Dot max unit.

And then we need to get.

Well, it's it's already suggesting this for me.

Which is exactly what I want.

Snowmachine, path based position units, dot path units.

So this took some experimenting on my part, but this basically checks the race path and figures out

how many units, how many different.

Different points there are in it.

So that's what that is.

And then we need to loop through this number of times.

So we'll say for int I equals zero, I is less than num checkpoints.

I plus plus.

And we're going to want to instantiate a either a checkpoint or finish line checkpoint.

So depending on which one we're looking at, we either want to create a normal checkpoint or a finish

line.

So for that, first, we're going to do.

Game object check point.

So we've created a new place holder for this checkpoint.

Checkpoint.

And we'll say if I equals equals num checkpoints minus one.

Checkpoint equals instantiate game object.

Finish a check point prefab.

So this is going to be the only case where we need to do a finished finish line checkpoint and then

otherwise.

So we'll say else checkpoint equals instantiate game object.

Checkpoint prefab.

So once we've created our checkpoint, we want to set the parent position in rotation, so we don't

want to just place this in the scene, we also want to rotate it so that it's oriented in the correct

direction based on the curve of the course of the race path.

So the first thing we do is checkpoint dot, transform, set parent.

And we're gonna set the parent to race path, dot transform.

Then we will set checkpoint got transform local position equal to race path dot m underscore waypoints.

So this gets the list of waypoints from the race path.

That Index I.

That position.

And then finally, we're going to do a checkpoint transform dot rotation equals race path, dot, evaluate

orientation at unit.

And we want to pass in the position is I.

And then we want sinnett machine path based position units.

Dot path units.

So that's able to get the orientation or rather the rotation of the curve at that point.

And the last thing we need to do inside here is add the checkpoint to the list.

And for that, you just have to do checkpoints, not add checkpoint.

OK.

So now we have this basic setup here where we go through and we find any point on the on the list of

are the snowmachine path rather.

And then we create a checkpoint and then we position it and orient it and add that checkpoint to our

list.