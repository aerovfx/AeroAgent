# Rotate.cs

In this video, we're going to add rotation to our checkpoints and the propeller.

So if you look at this scene right now, these checkpoints don't move at all.

And I thought it would be cool if they rotated around a little bit just to draw some attention to them.

So we're going to add a script that rotates and we might as well reuse that script for the propeller,

too.

So we're going to add one script and make it customizable enough that we can use it in both of these

cases.

So let's go to the we can stop playing this, we can go into the aircraft scripts folder and then right.

Click and create a new C sharp script and we'll call this rotate.

And go ahead and open that up in Visual Studio.

And then let's right off the bat add this to the aircraft namespace namespace aircraft, and the nice

thing about adding it to this namespace is that it's going to make it so that if there's any other script

somewhere in your unity project that uses that's called rotate, since that's a fairly common name,

then we won't have any conflicts.

So inside of here, we're actually going to use both the star and the update function, so we'll keep

them in there and we're going to first start with a new variable and we'll call this we'll just add

a tooltip for this tooltip.

The speed at which to rotate.

And we don't really want to do just a float.

No, we want to do a vector three.

Public vector three.

Rotate speed.

And what this will allow us to do is tell it how fast to rotate in each direction or rather around each

axis so that we can basically specify an access to rotate.

Then we're gonna add another one tooltip whether to randomize the start position.

Public bool randomise equals false.

Now, with the checkpoints, it's fine if they all rotate together in sync.

I think it makes sense that we would want them all to rotate together.

But with the propeller's, it actually is pretty jarring to look at three different airplanes flying

together and see that all of their propellers are perfectly in sync.

It just doesn't make sense to the human brain to see all those together.

So we want the option to randomize the start position and then it'll make sure that they don't look

exactly the same as they're flying through the course.

So inside the start function, we are going to add a comment.

And this is where we're going to randomize the start position.

And the way we'll do that is we'll do a quick check if randomise, transform, rotate.

And then we'll say rotate speed dot normalized times, unity engine dot, random dot range zero F and

three 60 F.

So it's going to pick a random rotation and then it will start rotate rotating from that point.

In the case that we say yes, do it.

Randomize this.

Then in update, we'll say transform, rotate, rotate, speed times, time, dot, delta, time, space,

self, webspace, dot self.

So this will just perform the rotation regardless of whether it's randomized or not.

It'll just start from where it is and then keep rotating every frame.

All right.

So we have this rotate, got C.

S, and we want to apply it to both our propellor and to our checkpoints.

So let's open up the prefab for the checkpoint first and we'll add a component.

We're going to add the rotate script.

And this one, we're going to we're not going to randomize it, but for rotation, I believe it's the

Z axis.

Yes, this blue axis is where we want to rotate it around.

So we want to rotate this.

And I think when I was testing this earlier 20, it was what worked.

So let's try this.

We're going to hop back out and we'll hit play.

And there's our checkpoints rotating, and that looks pretty normal to me.

I don't think I'd want it to go any faster than that.

The finish line isn't done yet.

So let's do the finish line.

We'll open up the prefab at the rotate.

Set this to 20 and then that should be good.

Then before I test that out again, let's add that rotate script to the airplane as well.

So I'm going to click into the airplane prefab and then click on the propeller.

Add a component rotate, and I believe this will also be rotating around the Z axis.

But this one, if we did 20, that would be really slow.

So let's try and go really fast.

Let's try like a thousand and see how that works.

And we also want to turn randomise on.

So let's go back to the scene and press play.

And that looks pretty good.

I don't know if we can go much faster than that and have it work well, so let's just while it's playing,

it's not going to persist, these changes.

But let's try.

Just go into two thousand.

That looks pretty good.

So we'll use two thousand.

Let's go into the prefab and update this to two thousand.

And then.

We should.

I'll just save this scene and then click play.

And the propeller looks pretty good to me.

I'm going to look from the scene.

And now we've got the finish line is rotating as well.

So now we've got our rotations going.

This already looks like a much more dynamic and active game, which is pretty cool.