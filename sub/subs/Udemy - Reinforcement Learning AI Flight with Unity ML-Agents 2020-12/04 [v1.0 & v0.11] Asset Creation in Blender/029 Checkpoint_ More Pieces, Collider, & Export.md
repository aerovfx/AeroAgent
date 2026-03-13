# Checkpoint_ More Pieces, Collider, & Export

So it would be nice if we could have done that with all of them but unfortunately let me hit seven again

on my number pad to get to the top you.

Unfortunately because they were at an angle we can't just lock them to an axis and move them down.

They're all on weird angles.

Aside from this top one.

So what we're gonna do is use a technique to basically duplicate them at a specific angle.

And actually as I'm saying this I was going to use the array modifier to do this but I'm gonna do this

in an even simpler way.

So I'm gonna hit R sorry I'm gonna hit a and then we're going to do shift D.

And then we can hit R which rotates it.

That's not what we want.

We want to make sure that it's rotating around the 3d cursor.

So this what this does is it makes it so that it rotates around the 3d cursor which is right here.

If you've somehow managed to get your cursor somewhere else just know that shift C will reset it.

All right.

So now that we have the rotation mode set the pivot point is this.

We still have all these selected.

We can hit R and then we can rotate it some number of Greece degrees the number of degrees we want is

actually seventy two.

In this case OK.

So basically what we want to do is create a few more of these.

So I'm going to select all of these again and here's a tip.

So if you select like this what's not going to get selected is anything that was behind it.

So you can either come and look at it from that angle or you can go to the top and you can choose this

option which will show x ray and it will allow you to select all of these we're gonna do shift D again

and we're going to rotate it with the AR key and we want this to be about here.

So it's seventy two times two.

So we're rotating Seventy two degrees twice.

So the rotation if you look up in this top corner it's about one forty something.

Well seventy two plus seventy two is one forty four

okay.

Now we want to do the same thing here.

Actually we can do this.

Probably an easier way.

If we select this and shift select this and we do shift D we've got both of them now we can rotate this

and all we want to do is rotate 144 again OK so now we've got this shape.

This is the shape that we want for our checkpoints.

I'm going to view this from the top again.

I'll rename this to checkpoint and I'm going to then create a new shape.

So we're going to go to add mesh and we're going to add a cylinder and we're gonna use five for the

vertices.

The radius.

Let's see I think I tried 14 before when I was testing this.

Yes.

So that's about right.

So if we do the radius of 14 and then a depth of one this will make it so that you can't just fly through

this top part of the checkpoint and get it.

You have you're forced to actually go through the checkpoint.

Navy will be a little more generous.

Let's do 15

I'm 16.

I like 16.

Okay so we're gonna do 16.

So now you can click away from that and you can see that we've created this central part.

This is the collider that we'll be using.

So it's a simplified version of this shape.

And if the plane hits it then it will get a point basically.

So we'll rename this to Checkpoint collider and then the last thing we need to do is select both of

them so we can select like that and we can hit our key.

The X key and then we want to rotate it 90 degrees so you can see right up here it's 90 degrees there

and we can just type in 9 0 and enter.

The only thing that's left is to apply this rotation.

So we go to object apply rotation and now we have our checkpoint ready to export going to select the

first one on the outside.

I'll switch back into sort of opaque mode.

We'll go to file export FBI X and I'm going to go to my assets folder that I've been working with we

want selected objects we want apply transform and I'm going to call this checkpoint

and then we want to select this second one file export FBI X keeps selected objects experimental apply

transform and we'll call this checkpoint collider

all right so that's all we need to do for our checkpoint.