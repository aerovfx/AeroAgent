# Introducing Randomness

In this video, I wanted to show you something that I talked about way back when we were working on

the aircraft area script, but I never really explained in detail.

And that is this line right here.

This position offset.

So, first of all, I just want to show you what it does.

This is what positions?

The airplanes so that they're not right on top of each other.

And to do that, I'm going to hit pause and then press play.

And what it will do is it will spawn the airplanes spaced out by roughly 10 meters along this start

line.

So you can see that it places one in the center and then it places one to the to the right and then

two to the left.

And that's what this does.

If I was less lazy, I would make sure that it was perfectly centered.

But I guess I didn't do that.

But there's this weird part here.

Random dot range, nine, 10.

It's between nine and 10.

We're not doing exactly 10.

And I want to show you why that is.

So let me stop this.

If we do exactly 10.

So let me say times 10.

And then comment out this random part.

And we go back to this and Pressplay.

We're gonna try and watch what happens here and look for a pattern.

OK, so let's see.

It was white, blue, yellow, red.

Order!

And then there's this other thing when it's coming around.

Just pay attention.

We've got the yellow to the left and the white behind us.

All right, we're going to try it again.

And I want you to notice that the airplanes do the exact same thing every time.

So the order was white, blue, yellow, red.

And then as we go around this corner, you're going to see that again, the yellows to the left and

the white is behind.

And if there was a point in the course where one of them was going to crash.

Then it would crash in the exact same place every single time.

So this is a really interesting quirk of how M.L. agents work.

But it's also a quirk of just neural networks in general.

So once the neural network is trained.

If you feed in certain observations to it, it's always going to observe the same thing on this Coursey

Yellow, blue, white.

It's always going to start in the same position and it's always going to observe the same starting point,

and at every single step it's going to have the same observations and therefore it's gonna make the

same exact decisions based on those observations.

Every time it has a an observation, it's going to make the exact same decision.

Unless you add some randomness to it.

And so the way that I did that was I removed this times 10 directly.

And now it's between nine and 10.

So it's just slightly off.

It doesn't start in the exact same position every time it randomize it and then shoot.

Let's see you fix this.

Still need to multiply.

Then I should be able to play this and assuming my demonstration works out, then you're going to see

that the order of the planes is no longer exactly the same.

It might be very similar, but it won't be exactly the same.

So let's see.

So coming up here, the yellow is on the left and the white was behind.

Now it's different.

Just that slight nudge meant that in the first step.

All of their observations were slightly different from what they were previously.

And that throws off the entire course.

It's kind of interesting because in a in a race like this, it's kind of predetermined, actually,

who will win at the starting line, especially if you don't randomize it at all.

Of course, adding a human player in there can add some randomness.

It might nudge them off course or something like that.

But in general, just adding that slight bit of randomness to make it so that things work the way that

we expect them to, then that makes all the difference.

So I'm just I wanted to make sure that I explained kind of what that was for, since I know I kind of

skipped over it earlier.