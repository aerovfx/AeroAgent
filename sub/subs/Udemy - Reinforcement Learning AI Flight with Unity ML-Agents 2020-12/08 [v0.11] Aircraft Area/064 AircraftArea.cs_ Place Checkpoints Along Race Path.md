# AircraftArea.cs_ Place Checkpoints Along Race Path

All right.

Next we're going to say set the parent position in rotation and so we need to place this checkpoint.

We've already we've just instantiated a new game object in the scene but we need to tell it where to

go.

So checkpoint transform set.

Parent then we want to set the parent to the race path dot transform.

So this will just become a child of the race path

and then is it complaining of me use of unassigned local variable checkpoint

Oh I missed something.

So this needs to say checkpoint equals instantiate game object because otherwise it'll still create

the game object but it won't set it to this variable.

So I'm glad that that showed up.

Now instead of way down the road so after we've set the parent we need to say checkpoint dot transform

local position and we need to set that to race path dot M. underscore waypoints I dot.

Position.

So what this does is it basically finds which checkpoint we're at.

And then it gets the position of that and now we need to say checkpoint dot transform dot rotation and

we need to get the rotation or rather the the direction that the curve is going at that point and this

is not necessarily or I should say it wasn't the easiest to figure out but the code we need is race

path dot evaluate orientation at unit and then we need to pass in AI and send a machine sorry send a

machine path base dot position units dot path units OK so not the most obvious code but it seems to

work.

And then finally we want to add the checkpoint to the list and that'll be checkpoints not add checkpoint.