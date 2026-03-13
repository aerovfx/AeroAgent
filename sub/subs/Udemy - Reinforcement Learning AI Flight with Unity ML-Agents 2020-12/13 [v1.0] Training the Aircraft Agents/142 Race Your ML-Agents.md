# Race Your ML-Agents

In this video, I'm going to try and turn on the airplane player and then race against these.

So I'm going to disable the airplane and enable the airplane player.

Because I'm controlling it.

I don't need to feed in a neural network.

But I do need to make sure that it's set to heuristic only.

So.

Once that's set up, I can save the scene and press play.

And there's one other thing that I forgot.

I have to hook up the virtual camera to.

The right agent here.

So the airplane player here need to hook up virtual camera to be airplane player.

And I just feel like I saw something that looked kind of off.

No, I think I think it should be OK.

All right, I'm gonna press play again.

And the camera is behind yellow.

OK, and now I'm flying against these guys.

I missed the first checkpoint.

Great.

I'm going to keep flying.

But eventually, if I crash, I'm going to go all the way back to the beginning.

So let me just show you that.

Yeah, I went all the way back.

Let me see if I can try this again and do a little bit better job.

But what I'm trying to demonstrate here is basically how difficult these guys are to beat, especially

if they get an early lead and you crash or something.

They're actually so good that they're near impossible to catch up to.

So one of the things you can do is stop training early.

So I'm going to stop this right here and just show you intenser board.

You know how when we got up to this point, we just pressed play and that stopped it and saved off a

neural network?

Well, you can also stop it early.

Let's say I only wanted it to get to this point.

Let's see, where was it successfully getting through?

Maybe about 17 minutes in.

That's like right here.

So I could have stopped it, like right around this point and then I would have a much better chance

of defeating these agents.

So I'm going to retrain it and then save it earlier, probably after, like 20 minutes.

And then I'll be able to have a second neural network.

And all you have to do is give it a different name and drop it in the same folder.

And then we'll be able to have multiple difficulties of agents that we can compete against.

So all we have to do is open up Anaconda and then we'll do aircraft of three.

Make sure that you are in the right scene because I am not part of the training scene.

And then you can.

Let's make sure you got the right Anaconda window hit enter and then as soon as it says it's ready.

Pressplay.

And let this train.

And so I just need to make sure I remember to come back and check on this.

Right now they're terrible.

So if I stopped it now, it would be really easy to beat them.

But I think I'm gonna let them go a little bit longer.

You know, somewhere in the, you know, 18 to 20 minute range.

And that way they're gonna be a lot easier to beat.

And by the way, this first aircraft learning doesn't even show up on the chart because that was a failed

run.

But aircraft 02, that one does show up.

And when you want to hide one or not, you can hide it like that.

So I could hide this one and then I could zoom in and it would focus just on this line.

But then if I wanted to bring this back in for comparison, I could just compare it.

So I'm gonna give this some time and let it train and then come back when I have a less good agent to

compete against.

All right.

So I have the training right now.

It is on the fourth stage.

The fourth step and the reward that it's getting is around 13.

It's been training for about 18 minutes.

So this seems like a good spot to just double check and see.

They're still flying kind of crazy, but they are making it mostly through the course.

So this is probably good enough and we can probably stop it.

And then I'm gonna open up this and models folder first and then find this.

New training run the N.N. model.

What I'm going to do is actually copy this and paste it and then rename it.

So I'm going to call this woops aircraft learning.

Maybe I'll call this easy and now call it normal.

We'll make this the normal one, and then the other one will be hard.

So then we can take this and drop it in here.

And then we can go back.

I'll save this scene.

We'll go back into our other scene.

The Desert One.

And then we just need to open up the prefab for the airplane learning and swap out the neural network.

So we can put in this aircraft learning normal.

And then we can race against them.

And they should be easier to play against.

We'll see if that's true.

I'm hoping one of them will crash.

Course, I missed the first checkpoint, so I better not crash.

Well, so far, they haven't crashed, but they should be easier to beat.

I'm not having too much trouble at least keeping up with them.

Aside from that missed checkpoint.

So.

We'll see.

Yeah, I'm able to at least catch up.

So that's a good sign.

So that's that's one way to make the airplanes a little bit harder.

Yeah.

Here we go.

One crashed.

You can make them a little bit harder or a little bit easier is just how much training they've had.

And then, you know, you can do it that way.

There are some other ways that you could potentially do it.

Look at that trick.

Nice to give them a handicap of some sort.

Like, maybe slow them down.

If you're too far behind something like that.

So you can get creative.

If you're if you're trying to turn this into a game and you just want to make it a little more fun for

the players, there's lots of things you can do.

That's an interesting issue with neural networks, is that if they're so good that they're unbeatable,

then it's not really much fun to play with.

So that's something to keep in mind.