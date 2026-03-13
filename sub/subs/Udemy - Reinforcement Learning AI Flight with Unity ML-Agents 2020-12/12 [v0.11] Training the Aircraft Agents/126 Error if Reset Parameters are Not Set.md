# Error if Reset Parameters are Not Set

I do want to show you really quick what happens if you don't set this checkpoint radius.

So I'm going to remove this and then I'm going to I can probably disable all these for this test really

quick and I'm also going to turn these off because they won't work without a neural network in them.

So I'm just going to use airplane player for this test.

You don't need to follow along.

I just want to show you this.

So now the last thing we need to do is keep training mode on.

Now if I hit play I should get an error message because it's asking for that reset parameter and nothing's

telling it what it is.

So this is the error that we find and I'll just show you what's happening here.

So this is the error message the given key was not present in the dictionary.

Well that's not terribly enlightening.

So we need to look down here key not found given key was not found in the dictionary.

OK whatever aircraft agent action.

So this is where the problem is happening.

And it's called by a bunch of other stuff.

So we got there by being in fixed update environments step agent step agent action.

But this is the code that we've written where there's a problem.

OK so if we go to line 1 0 2 you can actually click on it.

It says it's right here.

So this is this is line 1 or 2.

So what's happening is it's trying to access that aircraft Academy reset parameters checkpoint radius

and it's getting an error that says the given key was not present in the dictionary.

So that will happen if your aircraft Academy doesn't have that checkpoint radius and I'm just gonna

copy this

checkpoint radius.

So now this error message should go away

OK.

So the reason by the way that we don't have a camera following our plane is that we never set up our

camera to follow using this in a machine thing.

We don't really need to do that for training because we don't necessarily want to follow just one airplane

for training we want to kind of look at them from above.

But I just wanted to explain that really quick.

So now I kind of need to undo all this stuff that I've done.

So let me make sure that I do this correctly so training mode was set to checked airplane player was

disabled and then these these four were enabled and that should be should be good.

So what does that mean.

That means that we need to update the aircraft Academy in our other scene so we'll go to the desert

scene and make sure that this also has that checkpoint radius in there.

Otherwise we're going to have issues.

Once the agents try to fly around in this without being told what the curriculum is so we can save this

scene.

And that should be all we need to do for those reset parameters.