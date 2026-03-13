# New Training Scene

In this video, we're going to prepare a new scene for training.

So go into your aircraft scenes folder and right, click to create a new scene.

And go ahead and call this training.

Open it up and you can take your prefab, your desert area prefab and drop this into the level.

Now you're gonna want to go into the lighting tab and generate lighting.

And remember, if you lose that lighting tab, it's just under window rendering lighting settings.

Now it looks quite a bit better.

And we want to use this to train our agents.

So now that we have this desert area in here, we have an airplane player and we have a an airplane

in here.

We probably want to put in our other airplane variance at this point.

So let's go in and we have our airplane.

Let's disable the airplane player for now.

We'll turn on the airplane and then we want to drop in these other variants.

So let's grab the blue one, the red one and the white one.

OK, so the way I set these up when I dropped him and they were already placed at these, but you might

want to position them just so that they're not on top of each other.

This isn't where they'll spawn.

They'll automatically be spawned at the starting line.

But it's helpful to be able to see them.

So we just want to double check and make sure that all the behavior parameters are set up properly and

the aircraft agent stuff is set up.

It looks like it is in this case.

I do notice one thing that's wrong, but I'm not going to call it out right now.

We'll see if you catch it.

You should be able to see it on this scene.

But on this screen, we'll.

We'll see what happens.

Then we have.

All four of these ready to go.

We're going to also.

Turn the training mode to on in this prefab.

We'll turn it off later, once we're once we're in the desert area again.

But for now, we're gonna turn it on in the in the prefab.

And one cool thing about email agents is that as long as you have.

Things separately set up, you can train multiple agents at a time and even multiple of these areas

at a time will work.

That's the way this particular project is designed.

And in our case, we're just going to have four of the same thing.

But let's say you had four different race paths in different environments.

You could train all four at different times.

You could also swap out different ones.

Maybe you train on the desert for a little while and then you were to train on something else for a

little while.

I haven't actually experimented with that a ton, but I think there's a lot of opportunity there.

For now, what we're gonna do is just duplicate these.

So we'll duplicate.

Duplicate, duplicate.

And let's move one probably maybe in the X direction, like 500.

No, that's not enough.

Let's try a thousand.

OK.

Barely enough, so I'm going to maybe do 15 hundred.

OK.

And then we'll do this one.

Fifteen hundred.

And in the Z.

As well.

And then we'll do the last one.

Fifteen hundred in the zie.

So now we've got four of these that can train simultaneously.

It could be if you have a slower computer, that this is a little bit too much.

So if it is, then you can experiment with turning these off and seeing if it still works.

So now we've got these four desert areas set up.

We've got our airplane learnings all ready to go.

I will suggest that you just double check on all of these to make sure that none of them are set to

use heuristic under behavior type, because that is something that has got people stuck in the past.

And then the next thing for us to do is set up our configuration files and we can start training this.