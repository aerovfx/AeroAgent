# Race Path

Now, to create this path, we're going to use something called Sinnett Machine.

So go up to a window and go to package manager.

And we want to find Cindy's machine in here.

So that should be right here.

And we want to install this now Cinna machine.

We're going to use for a couple of things.

One is we're gonna use it for the camera to follow our planes.

So it provides a lot of functionality that we are going to take advantage of so that we don't have to

write a bunch of custom logic for the camera to follow the plane as it's flying around.

So it'll smoothly follow the plane just by.

Once we tell it what to look at and how far back to follow.

But it also provides functionality for creating paths that cameras can follow.

But we're not limited to just cameras that can follow these paths.

So I'll show you what I mean.

We'll go to let's just view it from the top.

For this part.

And we're still in the desert scene.

Ah, the desert area.

Sorry, not seeing the desert area prefab.

We're going to go to a machine.

This is a new menu that's here now.

And we want to create a dolly track with CRT.

We're not going to use the cart, but we need this track.

So it'll create what's called a Senate machine, smooth path.

So let's hide our environment and we'll rename this track to Race Path.

And we can delete the dolly cart.

Don't need that.

So right now, this isn't terribly interesting, but we can add some weight points to make it interesting.

So what we'll do is we'll click this plus button and you can't really see it, but there's a zero here.

Let's create another one.

And now we have two different waypoints on this path.

We need to decide which direction we want the planes to fly through.

I'm going to have them flying this way around the course.

So what I'll do is I'm going to choose this.

First, this No one here and I'm going to try and grab it, may have to zoom in pretty far.

Grab it and then you can move this.

Point.

So that it's kind of far away from the first first point.

OK, so I'm going to I'm going to place this first one here, number one, and then I'm going to move.

No, this is zero one.

See if I can move this.

Sometimes it's kind of hard to make sure you're actually moving the zero and not the entire race path.

But I seem to have gotten it by zooming in far enough.

And the zero is essentially going to be the finish line.

So wherever you want your finish line to be, I'm going to make it like right here.

That's where zero should be.

And then your first point should be about 100 meters away.

From this zero.

So the way that you can kind of gauge for how far that is, we can look at this and we can see that

it's just the X value that's changed.

So it's gone from negative 70 to negative one ninety one.

So that's about one hundred and twenty meters.

That's fine.

I'm I'm going to modify it just a little bit less so that.

We now have a point that's about 100 meters away.

And we can add a new point, and it's going to automatically place it, the exact offset that the previous

point was.

So that is part of the reason why we want to view this from the top and also not change the the y value

of this yet.

Because if we change the Y and we well, I'll show you, if I changed the Y, let's say I want to do

it like that and then I create a new point.

Well, it's going to keep going up and that's going to make things difficult to work with.

So I'm going to undo this.

Undo that.

And then.

Create a new one.

So let's view this from the top.

And we want to just make our path go around this course and be.

You know, none of.

We don't want any of our points to be too close together or too far apart.

Something like this is probably good.

So I'm going to keep creating points along this line.

And every point that we create is going to be a spot where a checkpoint is placed.

And because we have this automatically like it, it smartly chooses curve positions for us that allows

us to decide which direction the checkpoints will be.

We want like the ring to sort of loop around this path.

So that'll be clear once we actually start doing it.

But we'll create another one.

Because we're going to in this case, I'm going through my little tunnel area and I'm just gonna keep

placing these until I end up with a completed course.

So this is kind of my straight away area, so I'm going to make it so that they're not too.

Far off, like if you use some real squiggles, it will or squiggles.

It will make your course harder, but not necessarily more fun.

In my experience with police, one right here.

And this is maybe going to be kind of a sharp turn.

So I do want to make sure that I don't have super sharp turns through here.

This one's gonna be pretty sharp.

That's OK.

OK, so we're coming around and then we're almost done here.

Create one more.

Kay.

And then you can click Loopt and then it'll create this Loopt path.

All right, so now we have this path.

That's, of course, way too high.

So we probably want to just start bringing these down.

I don't think we can select multiple at the same time.

No, we can't.

So we're gonna have to just do this manually.

So what I'm gonna do, I won't I won't bore you with going through this entire thing, but I'm going

to select these.

And the thing you need to know is let's see if I can sort of zoom in on this.

Don't go too far in anywhere that we have agents spawning.

So anywhere along these checkpoints, any one of these checkpoints, an agent might respond there.

Like if he crashes, then he'll be respond back at this last checkpoint.

You want to make sure there's enough space for the agent to respond, because we're going to have some

logic that says, OK, if there's four agents, then spaced them out along this spot.

So even if two were to crash at the same time and respond, they wouldn't spawn on top of each other.

So wherever you place this, just make sure that it's not in a place where there's not enough room to

place a few airplanes.

And if you for reference, we can we can just place an airplane here.

I'm going to move him over here just so you can kind of see how many.

Well, it's kind of hard to see, but you can see that multiple planes could be placed in this because

it's it's big enough.

You can use your plane for reference.

Your airplane for that.

For reference.

So I'm going to go through and I'm going to place all of these these points and I'm going to pay particular

attention like through here to make sure that I don't create a checkpoint path that's like impossible

to for the airplanes to follow.

So, like, right now, of course, it looks a little confusing because I haven't moved down the others.

Move them like that.

And then you can see that it's possible for to hit a checkpoint here and then get to another checkpoint

here.

And you may need to tweak these once you actually do some play testing.

But that's kind of the idea.

So this is not where I want to you know, I'll move it down anyway.

I'll go through this and then we'll come back.