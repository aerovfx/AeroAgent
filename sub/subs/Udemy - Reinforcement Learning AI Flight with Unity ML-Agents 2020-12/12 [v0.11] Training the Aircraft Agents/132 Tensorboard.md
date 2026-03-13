# Tensorboard

So we can see a lot more than just from this scene we can first of all we can look at our Anaconda prompt

and see that now that it's gotten past some of the initial warnings and things we're getting these step

counts.

So step 4000 a time elapsed of ninety eight seconds.

It gives you the mean reward.

So the average reward of all the agents and then the standard deviation of reward which is kind of then

maybe just look up standard deviation.

But it's essentially like how much did they vary from that average.

Because some of them are a lot higher some of them are lower.

So that's kind of what that means.

Now we may want to visualize this in a more graphical form and to do that we can use tensor board like

we did earlier in the course.

So you can middle click on this to open a new one or you can just go to the start menu like you would

with any other program.

And we want to do kinda in B list and then we want to start up that environment again.

So I'm going to copy this the right click activate

and then I need to change into the desktop of course directory and then my Intelligence Directory and

just to show you what's going on in here you can do DVR.

This is the folder that's well it's this folder right here that we're inside.

And the thing we're going to be using is this summaries directory summaries.

I already have several in here but there's a new summary that's in there.

Aircraft 0 1 This is the one I deleted my previous aircraft 0 1 so that I could show you.

We're going to use tensor board to see these in graph form.

So the command to do that.

If you ever forget go to the documentation for AML agents and find the using tensor board.

And this is the command.

You need this tensor board dash dash log order summaries.

You don't.

The port seems to be optional I never type that in and it seems to work just fine.

So tensor board dash dash log their and then summaries so summaries tells it to open whatever logs are

in this summaries directory and if it works properly you should get a link that you can then paste into

a new browser tab.

So I'm going to copy this by selecting it right click control C will quit this command so don't do that

and then we'll open this up and paste this in and we should be able to see some graphs so as I said

there are some other runs that I ran.

This is kind of like a cooking show where you know they show you how to make the dish and then they

magically pull one out of the oven that they cooked earlier.

So let's hide these other ones that were already in the oven and we can isolate it to just the one that's

currently going.

So this aircraft 0 1 aircraft learning if you click on the circle it will isolate it to just that so

these graphs aren't terribly enlightening right now.

And one of the problems actually is that ignore outliers is set.

If we uncheck this it'll show us the the parts of the graph that were cut off and we can expand this

if we click the square and it will show us what our current reward is.

So it looks like we're starting to trend up which is great.

We can click this button and it will.

It should sort of show us.

Well if you hold down all to your able to zoom out a little more.

And if you hold down all too you can kind of pan this around drag it around.

So those are a couple tips.

And then because this is smoothed somewhat.

These are the actual values.

This this right here.

And if you turn down the smoothing we'll see that it matches that perfectly.

The smoothing is there so that when you have a very jagged path like Let me show you one of the previous

runs that's already done.

You can see how jagged this is.

And let me expand this if you smooth it.

It shows you a more easy to understand.

You can tell if it's trending upward or not.

Sometimes it's difficult to tell if it's still trending upward especially out here.

If we just view it like this it's kind of hard to tell is this getting better or not.

Or is it just flat.

But if you smooth it almost all the way and I suppose all the way is just fine you can still see that

it is trending upward a little bit but it is kind of flattening out.

So like I said this is a previous run and hopefully we can view both of them at the same time hopefully

this new green option here will start to follow this exact trend and we can watch it as it progresses.

So it's only gone about eighteen thousand steps right now.

And this thing really started to do well getting a cumulative reward of about 15 up around here.

So that was after over one hundred thousand steps.

So about 42 minutes compared to the six or seven minutes that we've been running and then I also want

to show you this lesson thing.

So lesson is interesting because it shows you which part of the curriculum you're on so if we pull up

the curriculum remember we have these different thresholds.

So as we increase threshold we're going to switch from lesson zero to one to two to three to four and

that's what you can see here.

I'm going to draw a box around this and expand this and you can see if I turned down smoothing this

is where it switched from lesson 0 to 1 and then to 2 and 3 and then 4 and there were only four lessons

so it stayed at this one from then on.

So once it got to this point it was training completely on that checkpoint radius of zero.