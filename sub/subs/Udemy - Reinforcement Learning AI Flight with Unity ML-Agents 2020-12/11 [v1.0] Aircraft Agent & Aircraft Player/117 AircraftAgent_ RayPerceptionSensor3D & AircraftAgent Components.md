# AircraftAgent_ RayPerceptionSensor3D & AircraftAgent Components

In this video, we're going to add ray perception to our airplane learning prefab.

So go into your prefabs folder and open up the airplane learning.

And then we're gonna want to add some ray perception components, but we don't want to add it to this

top level.

We're actually going to add it to some child objects.

So, right.

Click here.

Create empty.

And we're going to call this re's forward.

And we're going to move this so that it is in front of the airplane like this.

And if you want, you can move it up a little bit to it doesn't really matter tremendously.

So I've got it basically right in front of the propeller.

I'm going to add a component called Ray Perception Sensor 3D.

And you can see that what this does is it shoots out raise from the front of the airplane and it sees

if they hit anything.

They hit anything, then they'll turn red.

So the first thing you need to change is actually this sensor name.

We'll call this race forward.

And then for detectable tags, we want to enter.

And then for the first element, add untagged with a capital U.

And then for the second one, add checkpoint.

Then for re's per direction, you can keep it at three if you want, you can increase this or decrease.

Decrease this, but I think three should work just fine.

Max Ray degrees, probably 70 is good.

We can keep it, there is not really any reason why it would need to see straight to its side or anything

like that.

But if you did want to, you could always increase it like this.

So if for some reason you wanted it to spill the see behind it, like if you decided you wanted to see

agents as well, which right now it can't.

Then you could leave it at that.

So but we're going to just put it at 70.

And then here, this is actually helpful that this is showing up.

This sphere here is showing a sphere cast.

That's happening here.

By default, it uses a sphere that it tests to see if the sphere hits anything.

We're not going to use fear casts.

We're just going to set the radius to zero.

And that way we don't have any complications of this, perhaps having a sphere that hits itself or hit

something else that's really close.

We're just going to keep it simple and make it a normal recast.

And then the ray length, we're going to change to two hundred and fifty, so that's two hundred fifty

meters that it's going to be able to see out anything more than that and it will not be able to see

it.

So that's just something to be aware of.

Honestly, at two hundred and fifty meters out, these rays are so far apart that it's it's going to

have such huge gaps that it won't be able to see anything anyway.

So it's not super helpful at that distance or especially anywhere beyond it.

But still, we'll keep it at that distance.

And there are some other things in here like you can do filters up like what what these things hit.

You can stack the recast so it can see previous updates.

You can change the offsets if you want to.

Like, you could have it pointing up or down a slight amount.

It's really not very much that it lets you do.

So we're not gonna do it that way.

But I just wanted to point that out that that's their.

So now we can see straight ahead.

But it'd be nice if we could kind of see downward and upward, too.

And good news we can.

So we're gonna duplicate this.

And I'm going to call this one raise up.

And then we need to rename this sensor to raise up as well, and to be clear, this doesn't need to

match this.

It just has to be different from all the other sensor names that are on the same agent.

So this raise up one is going to see the same things, but we're actually going to rotate it.

In the X so that it's pointing up a bit.

So maybe like up about 15 degrees.

So that should help it so that it can see upward, like if it's flying downward sort of at a slant,

then it can actually see things ahead of it.

So we'll do negative 15 degrees there.

And then we'll also do a duplicate of this.

We'll call it braised down.

We'll make this a positive 15 degrees.

I was raised down.

And I don't know that we really need to have as many requests as we do right here.

It's not probably very harmful to have these extra recasts.

So we'll keep them in.

But if you if you were, you know, making something that had all of these rays and you wanted to make

it simpler, you could, of course, lower the number of rays per Direxion so that, you know, it could

only see like that or something like that.

But we're going to keep it at three because why not?

So that's our ray perception.

And you may be wondering how it knows to use these well on the airplane learning right now, there is

no agent on this, but let's add it.

So we're gonna do.

Aircraft agent.

We're going to add this component.

And we're gonna have this behavior parameters thing here, which we'll talk about shortly.

But I wanted to point out right here.

Use child sensors.

This is what makes it so that it uses these child's sensors that are children direct.

Children of this agent right here.

So that I just wanted to point that out before we move forward.

And I'm getting an error message here.

Tag is tag, name is null or empty, so let's just double check.

I think this is fine.

I think what happened is I don't think it's still happening.

I think it automatically started happening when we created this new detectable Tagg's list and didn't

fill in those right away.

I think it started showing an error message.

So just wanted to jump back in.

I confirmed that that was, in fact, the issue.

It was trying to look for those tags as I was typing them and it didn't find those tags.

So it thought that there was an error, but there wasn't really any sort of error.

So if you get error messages like that, you can safely ignore them as long as they stop.

When you press the clear button on the console.