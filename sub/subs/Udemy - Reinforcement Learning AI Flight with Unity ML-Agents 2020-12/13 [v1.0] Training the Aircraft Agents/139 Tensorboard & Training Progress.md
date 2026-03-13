# Tensorboard & Training Progress

In this video, we're going to open up Tenzer board.

So I'm going to right click on this to open a new anaconda prompt.

And then Konda in the list.

And then copy this, Konda activate.

And then I need to make sure I get into that directory again, which the training directory now should

have those summaries in it so we can see D space.

And then.

Right, click to paste that in.

And then we want to run Tensor board.

Dash, dash, log, Dehra.

Summaries of.

And if we copy this right, click and go into our browser, then we're gonna start seeing stuff in here.

So what we're looking at here are the aircraft runs.

So this is aircraft 02.

This is the one that's going right now.

And it looks like we're at about Minar Award of negative point six three nine.

And here we're seeing about that area somewhere around there.

So this is reflective of the training that we're watching here.

And we can just let this go for a while.

It hasn't been training for very long.

Only about three minutes, three and a half minutes at this point.

So you're gonna want to give it quite a bit more time than that.

And then after some time, hopefully, this graph will continue up and we can come back and talk about

it.

OK.

So the training has been going for a little while now.

If we hover over the end point here in this black box, you can see that about 13 minutes have elapsed

now or one million steps and the episode length is going up.

And you see if I can lower the smoothing a bit so that we can see more of this chart.

You can also see that the step is going up.

So it starts on step zero and that corresponds to the checkpoint radius of 50.

And the threshold here.

And then step one, step two, three and four.

So as it manages to get past those thresholds, it's going to make it more difficult, which is why.

Right at the same spot.

So this is at about eight hundred and eighty thousand steps.

You see a dip, a drop off right here in this chart.

That is where the curriculum got more difficult.

And then it got more difficult here again.

And at this point, it's actually on step three.

So zero one, two, three, which means that we are now zero.

One, two, three.

We're at 10 right now.

So it's getting very good at successfully navigating this course.

So just looking at this, I can already tell as soon as we look at these agents, we're going to see

that they are succeeding at getting through some checkpoints at least.

So if we try and sort of you see if I can zoom in here and maybe watch one fly through.

Yeah.

You can kind of get the sense that they are succeeding in flying through this course, which is really

exciting.

They have a ways to go still.

I would say, but the fact that they're making it through this course mostly without crashing is pretty

impressive.

And in so little time, too, I mean, it's only been training for 15 minutes at this point.