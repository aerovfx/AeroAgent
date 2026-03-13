# Start Training

In this video, we're going to start training.

So we have our training area open, ready, set up, and we can now open Anaconda prompt and we can

start training.

So earlier in the course, we set up Anaconda so that we could use it with unity, Emil agents one point

zero.

So go ahead, open it up and type in KONDA in B list to list your different environments.

Find the one that you set up.

So this was the one that I set up earlier and I.

Right.

Clicked I highlighted and right.

Click that to copy to keep to the clipboard.

By the way.

And Konda activate.

And then that name is all you need to get that going.

And make sure that in parentheses it shows M.L. agents one point zero point two.

And then you need to make sure you go into that directory, that new folder that you just created for

training.

And I'm going to.

I've been C.D. Space and then your folder name that you're going to.

And once you're in here.

The command is M.L. Agents dash learn, and then you have to specify the path to the.

Trainer config.

So this one's under dot slash config slash trainer.

Big doesn't want to work for me.

I'm going to just copy the path.

Because this is a more foolproof way to do it.

So if I copy the path and just put in the full path to it, then that'll work for sure.

The next one is dash dash curriculum.

And then you have to give it a.

YAML file.

So you can copy this path and paste this in dash, dash, run, dash I.D., and then you just have to

specify a name and you can give it any name you want.

I'm going to call it aircraft underscore 01.

And then hit enter.

And I'm going to ignore the Kouta errors.

And as soon as it says that it's ready and start training by pressing play button, I'm going to switch

over to unity and press play.

And you can see that things are spinning really fast and what's happening here is it's running at about

20 times speed.

So we talked about this earlier at the beginning of the course.

But if you go into your projects, settings and time, you can see that it's running at a time of 20.

And we can kind of see some airplanes that are flying through here because it's.

But we're pretty far away and you'll see them fly for just a short period of time before they end up

disappearing.

And that's probably because they're crashing.

But it's kind of hard to tell.

So if we switch this to one, we should be able to see real time what's happening.

I don't know why this is jumping around like crazy for me.

Something is going horribly wrong for me.

The airplane is just sinking.

So I'm going to have to figure out what is wrong with that.

No errors in the console.

And then the airplane.

I knew it.

I knew I would forget this thing.

OK, I did this on purpose, I swear.

And then I forgot that I did this on purpose.

OK.

So it is not working.

And the reason it is not working is because.

Well, two things.

One.

Airplane learning has gravity turned on for me.

I did not turn off gravity, so turn that off.

And then the other problem is that it does not have a decision requestor.

So we will add the component decision requestor.

And once that's on.

I hope it'll work.

I still don't know why this is so jittery for me, I don't I do not know what's going on.

If I focus in on that, it's like when I'm panning, it doesn't want to.

Now, that's a little better.

All right.

So now say the scene again.

And let's try this again and I'm gonna do.

Aircraft underscore zero two and Pressplay.

And.

We'll see if this works better.

OK.

First of all, it's already looking different.

And now we're starting to see these airplanes fly through.

So when you have the the area selected, you can actually see the gizmos for it, so you can see those

recasts as they're flying around.

They are not flying at the checkpoints at all.

They're just kind of flying around randomly at this point.

And we can take a look at our training so far and see how it's doing.

So the mean reward is actually not zero and it's not negative either.

It's actually.

Just kidding.

That's a little negative signs.

They're kind of hidden.

OK, just kidding.

So it is it is pretty, pretty bad right now, but the good thing is it's learning to not crash as much.

And one thing I've seen from a lot of people is that the first thing they learn to do is fly up straight

in the air because they're less likely to crash that way.

And that can be pretty frustrating.

It can sometimes take a while before they start actually learning that they'll do better if they fly

to the next checkpoint.

But just be aware that this takes some time to train.

So you'll be able to watch this.

I wouldn't recommend just sitting here and watching it because that can take a long time.

In the next video, we'll talk about how to get tenser board up and then we can watch it from there.