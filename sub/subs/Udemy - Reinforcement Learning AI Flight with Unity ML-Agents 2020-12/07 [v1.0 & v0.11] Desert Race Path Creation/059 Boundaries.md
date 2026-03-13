# Boundaries

So as it is now the airplanes have nothing that keeps them from flying out of the map.

I don't think human players will be terribly interested in flying out into the abyss but because there's

not much to do out there.

But our agents may not have such reservations and they may fly off out into the abyss and that's probably

not quite what we want.

So we're going to create some invisible walls around the edges of this space.

So let's create a new empty.

And keep in mind we're still inside of our prefab Ed here.

And we're going to rename this to boundaries and we're going to create some planes around here not to

be confused with airplanes these are if you right click 3-D object plane so a flat shape.

And if I hit F to sort of zoom in on this you can see how small this is.

So we obviously want it to be quite a bit bigger than this.

So we need to scale this to be as big as our terrain is so we're going to click on this and just sort

of click and drag keep going until it's about that right size.

And that'll tell us how big this actually needs to be.

So OK our scale just needs to be 100 for this and really the the y axis doesn't matter here.

We can probably just leave that at 1 and it's going to have by default it will have a mesh collider

on it.

So if anything hits this plane then it will crash so this boundary let's call this

top I guess this will be the top boundary the bottom boundary will of course be the ground.

So we don't need to create that but we need to rotate this so that it's flipped upside down.

So we will rotate this around the x axis 180 degrees and we can just type that in over here and then

we probably want to move it up at this point.

And so we want to decide kind of how high we want this to go.

I'm going to view it from the side here and then I'm going to say maybe we want it like up here so this

would be 200 so if it tries to fly up above 200 meters of off the ground then it's going to crash into

the sky which you know maybe isn't ideal behavior but this is a video game so it's not going to be exactly

the way it would be in real life.

So now that we have this we can create our boundaries on the other sides.

So I'm just going to duplicate this and we're going to call this one north and I'm going to say that

if we view it from the top that north is up.

So this positive z direction.

So we want to rotate this so that it's facing inward.

So let's switch into rotate mode.

You can actually hold down control and then it'll lock to the way you want it locked to those solid

degrees.

So now it's set to a rotation of 270 and we can move this to about the edge there and we can see that

the Z should be 500

OK.

So now we've got a north boundary and then we've got a top boundary.

So let's create another one.

We'll do a controlled de and we will create a south boundary and this one is going to be negative five

hundred and we're gonna have to rotate this 90 OK.

So now we've got them on either side.

We're going to duplicate the top again and we'll call this one e and we're going to rotate it around

this axis OK.

So that's I don't know why these change too but let's just call this 90 and then I mean really I don't

know that we wanted this.

Let's let's try this.

Hold on.

We're gonna set this to zero and see rotating in the 90.

That should be OK.

And then we want the x value kind of pushed out this way so we'll do 500.

All right.

And then we've got this last one.

Let's just duplicate this and we'll call it w and we'll rotate it to 70 and we'll set the x position

to negative five.

OK so now if we view it from the different sides we should be able to see that there's a boundary on

all sides.

If we view this sort of from an angle we can see that these are way bigger than we need them to be.

So we can probably scale them.

Let's choose north and south first and figure out if we can scale these.

The X Nope it's the Z.

So we can bring these down something like that.

I mean it really doesn't matter.

I'm just gonna make this 50 and then east and west probably.

I'm guessing this one okay.

So now these boundaries are not way bigger than they need to be.

I mean there's still quite a bit bigger than they need to be but good enough.

We're going to make sure that none of these have visible measures on them now so we can just do mesh

renderer like that.

If we then we won't be able to see it and you can see that this plane is still quite a bit more complex

of a collider than we need it to be.

So we can click convex on all of these and then it'll simplify those colliders so honestly it looks

like these could probably be even cut in half again.

I'm gonna do that really quick.

I'm going to set this to twenty five and then set these to twenty five and then this probably needs

to be brought down to one hundred and then these need to be set to one hundred and I'm hoping yeah that's

a little better and you might want to just double check that you don't have any gaps like underneath

this terrain we don't want there to be any waste to escape out like a tiny hole that gets you out of

the map unless you want to add an easter egg or something to your scene which is completely up to you.

Okay.

So now we have these boundaries and I do want to mention something about these boundaries.

If you continue to work on your scene after you've placed your boundaries and you try to let's say we're

trying to place a rock it's going to drop it right there in the sky because it's actually hitting the

boundaries.

So I'm going to I'm going to delete this rock and I'm going to show you what happens if you then deactivate

your boundaries and place the rock again it'll place it on the next thing the next object that has a

collider so just know that if you're if you're trying to edit things and you can't figure out why when

you drag something into the scene it's placing it up in the sky or like way out at the boundary of the

map.

Well it's because it's hitting these boundaries.

That's why.