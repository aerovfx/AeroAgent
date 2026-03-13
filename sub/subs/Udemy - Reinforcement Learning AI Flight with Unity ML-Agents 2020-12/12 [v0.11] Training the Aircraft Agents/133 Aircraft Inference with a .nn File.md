# Aircraft Inference with a .nn File

OK.

So this has been training for about 20 to 23 minutes now.

And we can see that the cumulative reward for it is right around 14.

So that's pretty cool means that if we assume that each checkpoint is worth half a point each which

is what we set it to in the code then they're getting through an average of 28 check points per training

run which is pretty awesome.

So and then I also want to point out we've moved beyond we're up to the fourth and final tier of the

training lessons so they are they're already at the checkpoint radius of zero.

So they're forced to fly through these checkpoints at this point so let's take a look in unity and what

that looks like and I'm going to view it from above.

So if I click on this little y sort of cone thing I should be able to see and we can follow this around

and we can see that they are making it through all of these checkpoints.

So here's what I'm going to do click play and what that does is it's going to stop training and I want

to stop training early if you compare it to a previous run that I did.

I'm stopping it pretty early.

Let me turn down smooth or turn up smoothing here so you can see the difference.

The smoothing actually makes it a little misleading in terms of what your value is here because it's

still catching up to how quickly this this trained but it got you know we got up to about twenty two

or so up here for this other run.

If we stop it down here where the actual values like 15 16 then this I'm hoping will be a pretty decent

skill level for a normal player.

So what I'm going to do is show you what happens when you click play when you click play after it's

been training.

It should stop the training.

So it was at step sixty four hundred sixty four thousand here mean reward of sixteen and it saves or

it exports a dot and file for this.

So we can get this in the model's directory.

This is a trained neural network that we can feed in to our unity environment.

So I'm going to go into the models directory under MLA agents and then we need to find the right directory.

I need to make sure that I'm in the correct one here.

This is the one from today.

And I can then import this into unity.

We're gonna go into the project.

We're gonna go into the aircraft directory.

We're gonna create a new folder.

We're going to call this an model's and then we're going to import this song gonna drag this down into

here so I'm going to hopefully this will be a decent skill level.

I'm just going to call it underscore normal.

So I'm going to have a normal and I'm gonna have a hard and I might do an easy one also.

And then we can hop out of this training level for just a minute.

Here we can go to scenes desert and I'm going to open up the you're playing this airplane learning prefab

here and then I'm going to insert this new neural network model and I'll just actually do it by clicking

on this circle and I'll do aircraft learning normal and then if we play we can now play inside this

scene.

We are a player we need to disable one of these so I'm I'm actually going to disable this first one

that we changed but all of these variants also have an end model updated because we updated the main

prefab I'm going to save this scene and then click play and then we should see some trained agents flying

around

and something's not right.

Let's see here Oh I disabled the wrong one.

Okay let's try this again.

Let's.

This enabled this one will disable this one.

I'll save the scene again and then I'll click play.

All right.

So here's our agents flying through the course.

They're not boosting permanently which is good.

I do have a chance of catching up but you can see that they're actually really good.

I mean 4 4 What was that twenty five minutes of training that's it's pretty impressive how good they

are and they didn't even really train like to fly in a pack.

They they trained with random spawn locations so it just kind of works out that they're able to fly

like this and not collide too much so I'm really pleased with how this has turned out.

They seem to be behaving.

So while I'm having a hard time catching up with them they they aren't so skilled that they're completely

impossible to beat.