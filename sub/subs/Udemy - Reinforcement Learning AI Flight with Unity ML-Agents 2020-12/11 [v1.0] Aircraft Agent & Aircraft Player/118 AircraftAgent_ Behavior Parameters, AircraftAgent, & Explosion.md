# AircraftAgent_ Behavior Parameters, AircraftAgent, & Explosion

In this video, we're going to setup the rest of our aircraft agent and behavior parameters.

So the first thing I want to point out is our behavior parameters needs a behavior name, and this should

be called aircraft learning.

So this spelling and spacing and capitalization and everything is important.

So make sure that you match what I have right here.

This aircraft learning because it's going to need to match something that we put into a training configuration

file later in the course.

Now, this vector observation size on the player, we set it to zero, but on our agent right here,

we're actually observing nine.

That's what this total observations was.

So we need to pass in nine here so that it matches up and it expects nine different things that are

going to be passed into it.

Now, just like the player, this is going to use discrete vector action space with three branches and

branch one is the pitch.

Branch two is the Yaw and Branch.

Three is the boost.

So that should be everything we need to set up on the behavior parameters.

Make sure, of course, that you leave this on default.

Don't change it to heuristic only or inference only at this point.

Slavet at DePaul.

And then down here, an aircraft agent.

We've got this new section here that is not yet hooked up.

So let's do that.

If you haven't already.

We need the explosion prefab.

So that's in the downloadable game assets and under here, you should find a mosaic explosion unity

package.

So go ahead and drag that into your project.

And go ahead and import that.

And then once it shows up under particles.

Then you should be able to grab this cube here and drag it under airplane learning.

And you can see the explosion happened there if you click restart.

And I had someone ask me how this was done.

Actually, what I did was I took one of the explosions from the unity, had an example explosion in

one of their example projects.

And I took the the image from it.

See if I can.

Well, this up a bit.

And I just took it into GIMP and I put it triangulate effect on it.

So that's how I did that, just for anyone who's curious.

So this mosaic explosion now.

We're going to start it from code any time it explodes.

But we want it to default by being off.

And then click on airplane learning.

And we want to put this explosion into the explosion effect and then the mesh object should be here.

OK, so this airplane learning is now setup correctly.

It's ready for training.

Our airplane player, however, now needs to be updated.

So let's go into prefabs and airplane player.

And if we go into the aircraft player section, we also need to get that explosion effect.

And the mesh object in there, too.

So if we go into particles, mosaic explosion, we'll drag this here.

And we'll default it to being off.

And then we'll drag this.

Into that slot.

Here.

And the mesh object is here.

And I'm not 100 percent sure if this needs to be set to nine or zero.

It might give us an error message.

So let's just experiment.

We're gonna play.

And see if it gives us any warnings in the console about not having enough observations.

OK, so we've got a couple of errors here.

The first one.

Let's take a look.

I think it might be helpful if I try and just debug this on the fly here.

So I've got no reference, exception, object reference, not set to an instance of an object.

And it's saying the vector sensor line is the problem in aircraft agent Dot.

See us at line 130.

All these other ones.

Agent Agent Dot.

C.S. Academy.

Those ones.

That's not code we wrote.

So it's very likely to be in our code at this line.

So let's take a look.

So we did this sensor add observation.

I'm guessing that what's happening is because we set our observations to zero, then it's trying to

add to this sensor that does not yet exist.

So let's see if that is the case.

And I'm actually trying this right now, I have I have no idea.

I'm hoping.

So this is set to zero.

Well, we know that it's set to nine on our aircraft learning, and that's how many observations we

are expecting.

So my guess is that because it's calling this collect observations on the base class of aircraft agent,

even though it's an aircraft player, it's calling this and it doesn't have a sensor setup, that that's

the problem.

So let's now that we've got that setup.

Let's go back out to the scene and give it another try.

And no error message.

So that's good.

See if I can.

Make this bigger and I can fly and let's crash.

Boom.

OK.

So the only thing that didn't work for me there was I got this tag agent is not defined.

So let's see.

Leave.

We need to go into our agents.

Just open up the learning and I'm going to tag this at a tag agent.

And just click on this and set the tagged agent.

And same thing on the player, go here and Agent Tag and then, you know, just for good measure, I'm

going to save my scene and try pressing play again.

And hopefully.

Crashes without any error messages.

Right.

So hopefully it was helpful to see me debugging through a problem like that, if you hit no reference

exceptions like that.

Generally, the best thing to do is to look in the code at that line.

And I just want to point out really quick before I show you that again, this is the last checkpoint

I'm about to go through.

So if I crash here.

I should go back to that checkpoint and start over again.

And indeed I do.

So that's pretty cool.

So I'm I'm actually the checkpoint logic is working properly.

And I'm able to crash.

So anyway, what I was saying about the about the errors like that, if you had a no reference exception,

always check what it is.

Go to that line and try and figure out what's going on.

If you still can't figure it out and you need to, like, figure out what is the no reference exception

in question here, you can set a breakpoint attached to unity.

And then you can press play.

And then it should drop you into.

Visual studio.

As soon as it starts, as soon as it hits that, and then you could hover over this.

And in this case, I think sensor would have been no.

And that's the point where you would say, oh, OK, I think something's wrong.

And that gives you a hint as to what the problem is.

If, for example, maybe rigid body was no, then that would give you a hint that maybe you weren't

setting rigid body correctly.

Hopefully that little thing there is helpful.

I don't know, I I know that debugging can be a little overwhelming, and especially when you get tons

of no reference exceptions, it can be very confusing.

So I hope that that's helpful.