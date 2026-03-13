# AircraftAgent.cs_ RayPerception Observations Code

So the first thing we'll have to define we'll say observe Ray perception results so one of the things

we need to pass into the Ray perception is a list of tags that we'll be using.

So we're gonna create a an array of strings called detectable objects and we're gonna initialize it

with two strings on tagged which is literally anything in the scene that has a collider on it but does

not have a tag on it.

So that's our entire like all the rocks and the train and everything.

And then checkpoint.

So that's the checkpoint in the finish line.

I did experiment with being able to see the agents as well but it didn't seem to add really any extra

skill to the players and it just added a lot more complexity because it does a an extra check for every

single every single one of these these tags.

So now that we have this defined we need to do our three different sort of angles so we'll do look ahead

and upward.

So that's the first part.

So it'll be add vector obs and then we're going to pass in Ray perception dot perceive

and we're going to let's do this on a few different lines here and I'll just add the semicolon at the

end just for good measure.

So on the first line we're gonna do Ray distance we're gonna set that equal to 250.

We're gonna do Ray angles so that equal to a new array of floats so new float and then the angles are

gonna be 60 90 and 120.

Now I'm not sure why they did it this way but for some reason 90 is straight ahead.

So the 60 and 120 hour 30 degrees to the side from that then we need detectable objects and we're gonna

pass in detectable objects.

That's right here detectable objects

then we need a start offset of 0.

Now this is actually a y offset meaning in the in here it's where would this start on the y axis.

If we set this equal to some value it would actually lift it up to be maybe up here so we would set

it to like 20 and then it would be 20 meters up that it would start and then it would start coming either

down or across or however we want depending on the offset on the end offset.

So we'll add an end offset and that one is gonna be set to 75 so the reason it's so big is because our

rate distance is two hundred and fifty.

So what's happening is we have a two hundred and fifty long Ray that is seventy five meters up.

So the angle is something like this.

It's just a lot longer

and let's say what this is going to be in terms of how many values this is.

So this is two tags plus 1 hit slash not and plus 1 distance to object.

So what this.

This is kind of how the ray cast or the ray perception about perceived works.

It I'm just showing you the math.

You can go in and look for more details but this is kind of how the math works.

And then three Ray angles.

So that's gonna be two plus one plus one is four times three equals 12 values.

So that's if we added another tag then you could see that this would then become five times three 15

values so it adds three extra values for every new detectable object to add.

So now we want to do this across the horizon.

So I'm going to copy this just to save some time and I'll actually paste it twice because we're going

to do the ones along the bottom two and we can come back to that one next.

But let's do this one is look center and at several angles along the horizon.

And this one is still two tags one hit not hit one distance to object and then it's going to be this

time seven Ray angles.

So we're gonna have 28 values so we keep most of this the same except we're gonna add onto this.

So we're gonna do 60 F 70 so my my drawing may have actually been a little incorrect.

I made a little mistake we're actually gonna do more like since we're going in between these these values

we're gonna be more like in between

and between these.

So to every 10 degrees.

So not quite as wide for the four the ones in the center I would say so 70 80

90 100 110.

So it's going to fan out and it's gonna give a little more resolution I guess you might say.

And then our end offset will be zero.

So that it's straight ahead and then the last one is look ahead and downward and it's gonna be the same

number of values.

And the only thing we need to change is this end offset to negative seventy five and then we can calculate

the total

observations equals and that's gonna be three plus three plus three.

Okay.

So that's these first three up here we've got twelve twenty eight and twelve

and that equals sixty one so that's our total number of observations that we're taking in and we'll

need this number to pass in on the actual game object in the scene.