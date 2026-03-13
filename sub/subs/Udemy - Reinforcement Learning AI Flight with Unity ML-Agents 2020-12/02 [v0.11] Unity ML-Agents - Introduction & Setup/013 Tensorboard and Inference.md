# Tensorboard and Inference

Now by highlighting that I just froze it again.

So I have to hit enter again in here to continue training.

So just don't highlight things apparently that's a bad idea in in here while it's training but we'll

gradually see this mean reward.

So the average reward increase over time.

It gives us a step update every two thousand steps.

So it started at a mean reward of zero point for eight.

And it's kind of gradually trending toward being better.

Now I want to show you a cool dashboard called tensor board that that you can use to visualize this

and a graph instead of just viewing this as text.

So if you middle click on this Anaconda window it will open up a new one.

That's just a little trick to get it open on windows.

We need to open up that environment so kinda activate M.L. agents dash 0 eleven 0 like probably make

sure I get this right.

There we go.

And remember you can do conduct EMV list to see your list of environments if you forgot.

And then we need to go into our directory the desktop slash course slash MLA agents and then we're going

to use what's inside of the summaries directory so this summaries directory is going to contain a bunch

of information about this current training thing that something called tensor board can use.

So we can type in tensor board dash dash log dir and then we can just type summaries and that will use

this summaries directory that's inside of MLA agents

and assuming things work correctly and that you don't already have a tensor board running that's make

sure you don't already have tensor board running because you might you might have some issues then you

can copy this don't do control C because control C will quit but you can right click on it.

And then that should move it to your your clipboard then you can go into a web browser and you can paste

in this you url and you can see the training happening.

So this is the same information as what's in our Anaconda window.

So let's see if you look right here in the black box that's underneath my cursor here.

It shows the step it's kind of the middle value there 2k for K six K eight K so let's look at step ten

K right here or.

And step twenty K.

So you can see that it's changing quite a bit and there's two lines here.

One is the smoothed out line and one are the actual values.

So you can see those in the black box so you've got smooth and the smooth.

Value is zero point 1 5 the value the actual value is point to 5 5 2.

So if we go and look here when we hit 10k it was point to five five.

So that's what we're seeing here is this actual value.

And then this smoothing just kind of helps us see what the general trend is.

In the case where you've got something like this where it's kind of all over the place and in fact you've

got some outliers that are off of the chart you can click Ignore outliers and then it will include those

in the chart and you can change the smoothing and that will smooth things out so you can see a more

gradual change.

Or you can move it way down and then it will fit the line better but it might be more jagged like this.

Generally when you're training something the the two that I'm most interested in our cumulative reward

and lesson lesson is for curriculum learning which is not curriculum learning happening right now.

So that one's not relevant but cumulative reward is so we can click on this button which we'll expand

it you can zoom in or out by holding down the altar key and scrolling or panning by clicking and dragging.

So that's a helpful tip.

And you can also click and drag on a spot to zoom in on that spot.

So those are just some tips.

If you click this then it will fit the the entire graph.

So this thing is fully trained it's getting a reward of one.

And if we go back into unity now we can see that it is successfully going in the right direction every

single time so that's how training works.

This is of course way simpler than what we're going to do but that gives you an idea of the whole process

of you create an environment you give it some rewards and things we didn't touch on that yet.

But then you can train it and then once you're done you can hit this play button to stop early and then

in here it should save and export a dot and file case so that dot and file is under model's basic run

0 1 dash 0.

So let's open that up under models and go in here and now we have this dot and file so we can.

I'm going to rename this to dash original we can take this drag it down into our TIF models folder and

we can go to our agent and we can replace this.

Now this is the model that we trained and we can run it

and now it's able to do the same task using our trained neural net.