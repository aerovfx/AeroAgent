# Resume Training

Now I want to make a more difficult version of this.

So what I'm gonna do is go into the training scene again and we're going to resume that previous version.

So we saved a copy of that neural network model.

It's in the assets directory under under the and then models so we can keep training.

And then when we decide to stop again it'll export a new neural network model that will overwrite the

other one in this folder.

But we already have this one saved off here.

So let's restart this training we'll resume it and the way you can resume it.

I just hit the up arrow to pull up the previous command.

You do the exact same command with dash dash load on the end.

You hit enter

and then you can go into unity and hit play

and it should pick up training right where we left off.

So we can see that they're going again.

Let's go into the scene view and just double check and you can tell that it's picked back up instead

of starting over because they are not spinning in random circles.

They're not you know they're not perfect and that's by design.

We do want them to occasionally make mistakes.

But we have this now resuming and if we look at the tensor board this should continue where we left

off.

Now the one thing I will point out is as soon as we start seeing the step counts again it's no longer

going to be like it was if I scroll all the way up.

Hopefully I can get there.

These are round numbers because it was every two thousand because we stopped training it is now resuming

the step count is correct but it kind of got cut off in the middle of one of those 2000 updates so now

these numbers these updates will be slightly different but they'll still show up in tensor Board released

they should.

And we can see this now.

I haven't done this a bunch I haven't really tested this a ton of times usually I just start training

over.

So hopefully this resumes cleanly if if it doesn't then it could be that my assumption is wrong that

you can just pick these back up and keep going and maybe it just needs to train cleanly from the beginning

but we're going to give it a try and see how it turns out.