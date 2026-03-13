# AircraftArea Prefab Setup

In this video, we're going to set up the aircraft area on the desert area prefab and then make sure

that checkpoints show up.

So let's go into that prefab.

You can double click on the desert area and then make sure you click on the desert area, top level

game object here and then add a component and you want to type in aircraft area and we'll be adding

this script right here.

So the first thing that it's looking for is the race path, and it's a Senate machine smooth path.

Well, we have that right here.

This is our Senate machine, smooth path with all of these checkpoint spots along the way.

So let's drag that race path into the race path field.

Then we can go to the prefabs folder and it's looking for a checkpoint prefab so we can drag our checkpoint

in here.

And then it's also looking for the finish line, so we can drag that in here and we'll leave training

mode alone.

Now, let's hop back out to the scene and if we hit play.

Then it should spawn the checkpoints along this list of different points.

So I'm in game mode right now, so I'm going to maximize this and then hop out to scene and see if I

can take a look at this a little bit.

So it looks to me like everything's spawned in place.

You can see that these checkpoints also are sort of facing the direction of the path.

And you can see the finish line right there as well.

The important thing at this stage is to make sure that none of your checkpoints are in the sand or colliding

with a rock or something like that.

You need to make sure that there's enough clearance so that they see if I can get closer in here.

So see this airplane here?

You want to make sure so that at any point when in the course, in the in along the race path, if it

crashes, it's going to go back to one of these checkpoints.

So if it crashed in between this checkpoint and this checkpoint, let me make sure I'm going in the

right order.

So if it crashed in between, let's say, this checkpoint and this checkpoint in that order, then it's

going to restart at the last checkpoint it went through.

So you need to make sure that there's enough room so that if it does crash there, it can respond.

And the way that we're spacing these out is it's if there's four, then it's going to space out one,

two, three, four along here so that you can see how much space this takes.

In general, if you have enough room for the the checkpoint and a little extra space, it should be

just fine.

So just take a look throughout your your little course here and then maybe even use the.

I'm holding down, by the way.

I'm holding down the right click and then holding and then using the WASC and keys to fly around.

You might want to try flying through your scene and just see if there's anything that looks like it

would be a problem for the airplanes to navigate, because now is an easier time to fix it than when

you're training and you can't figure out why one of your airplanes keeps crashing or why one of them

just never seems to get past a certain point on the course.

So this is to get that out of the way.

Now, if you are in that case where you need to move something, all you need to do is go into your

prefab again.

Click on the race path and then.

Take a look at the different points here and let's say this one was messed up.

You just click on that.

And by the way, if you don't see this right here, it's because you need to be in the move mode or

hit w if you're in, like, rotate.

You won't see all these points.

So make sure that you have the move.

Tool activated.

So that you can see these.

And then just move it around until you get it to a point where everything has enough space.

And also just make sure that they're close enough together, because if they're too far apart, then

the airplanes won't be able to see the next checkpoint and they'll have trouble getting their.