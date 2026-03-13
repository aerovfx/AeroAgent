# Checkpoint Prefabs

Now let's do our checkpoints.

So back in the meshes folder the last two things that we haven't dealt with yet are the checkpoint and

the finish line.

Let's do the checkpoint first.

So if we drag this into our scene now you can see that this is it is going through our sand here.

But that's OK.

We can we can still see it well enough.

So this is our checkpoint and it's going to need a material and it's going to need a collider.

So this checkpoint you can see the airplane has plenty of space to go through it.

But as it is now if we did a mesh collider it would only get points if it collided with these edges

which is why we created this checkpoint collider.

So let's add a mesh collider to this and then we'll select from here our checkpoint collider and then

we can select convex and then it'll make it so that the airplane can get points when it goes through

this.

And finally this is important.

Make sure you choose is trigger because otherwise we'll just collide with this as if it's a regular

object.

We don't want it to be like as if we collide with a rock.

So we'll make it so that a trigger will be triggered when we run into it and then we'll be able to fly

through.

But it will trigger some special code.

So now we need a material for this.

So let's go to our materials directory and we will create a new material and we'll call this checkpoint

and you can choose whatever color you want for this.

I think I'm going to go for sort of like orange ish red maybe somewhere in between there is kind of

like this reddish orange and then I'm going to make it smooth I think and let's just apply this and

see how it looks so that to me looks pretty good.

I don't know if I want it to be quite as smooth as it is and we probably want to have it be somewhat

transparent.

So let's let's try that so we can go to surface type and we can change this to transparent.

And then when we go into here we can actually change the alpha a little bit and it might not reflect

right away so I'm going to just change it and just see when it shows up.

I've found that for some reason sometimes this takes some time before it actually shows up properly.

OK.

So.

So now it's showing up.

It's a little bit too transparent.

I'm going to make it more toward like right here there's just so transparency so I can kind of see through

it.

But it's it's mostly visible and that's that's too shiny.

I think you're just tiny bit shiny so you can play with this.

Whatever you decide you like it's up to you.

You can also mess with the emission if you want to make it kind of glow a little bit.

You know lots of options here.

We could see how this looks.

But ultimately I think that's probably gonna be a little too intense.

See if it updates I found this rather frustrating about this is probably just a behavior of the 20 19

not three beta.

Hopefully they'll fix this.

Okay so there's now the emission is kind of showing up you can see that it's quite a bit brighter.

So you know if you like it keep it.

If not do whatever you like.

So now back to the checkpoint.

We do need to make this into a prefab so let's go into prefabs.

We'll rename this to be a capital C and then we can drag this down into here and create an original

prefab and we'll do the exact same thing with the finish line.

So let's go into meshes and we'll drag the finish line in we will create a mesh collider on it.

We'll choose the finish line collider set it to convex and is trigger and then we want to get that material

on there as well.

So we'll go to checkpoint and we'll just drag this onto here.

So now this finish line is good to go.

So we'll set the capital and then we'll drag that down into prefabs as well and create an original prefab.

So now we have this version that's quite a bit larger that will indicate that this is the finish line

and then these will be placed around the scene to indicate where the player has to go through next so

we can remove both of these from the scene.

Now.