# Low-Poly Airplane_ Propeller

Now our final piece is the propeller.

So let's take a look at this from the top because the front view.

Let's see the front view we'll have it as well but we'll look at it from the top.

And if we go into the top view seven key basically what this is is a cone with a couple of blades coming

out of it.

So what we're gonna do is create a six sided cone and then the sides we're going to extrude from to

make these.

So let's start by moving the cursor to about here.

Because we want the we want this cursor or we want this shape to have its origin be right here so that

when it rotates it rotates around this point so we can do this in the tool View menu and we can move

the cursor forward by changing the y position of it.

Let's try mode.

We go way too far whereas the cursor is going the wrong direction.

OK.

There we go.

All right.

So that's pretty good.

So about negative one point nine and if we view it from the side let's actually do it from the front

and then we can look at the front reference image.

Let's hide

all the other stuff here and then we can move the this up.

You can kind of click and drag it so that that's probably pretty good.

We can obviously move this later if we want to but I'm happy it's going to stick to the grid just by

default.

So let's look at it again from the top and we're going to add a new cylinder we're going to create a

mesh cylinder and then click down here before you click away from it so that you can modify the settings

for it.

So we want this to be six sides and a tab.

And it'll show up and we want the radius to be quite a bit smaller so if you click away and then you

can click and drag we can kind of bring this down to see how big we want this to be.

So probably about point 1 for looks good and then the depth.

We don't really know what the depth should be until we rotate it so let's rotate this around the x axis

and we want this to be 90.

So actually we'll just type that in 90 degrees and then we can see that the depth of 2 meters is obviously

way too long.

So we will just get it somewhere.

Doesn't matter what we do because we're going to modify these manually.

So this is good.

Now we can do a control a the reason we want to do that.

Control A.

Let's see click away.

So this this rotation is set to 90 control a is apply.

This is also up in here under object apply.

We can do a apply scale that was already done sorry.

Apply rotation and then it's going to set this so that we don't have it already being rotated before

we even start working with it.

So let's hit tab and we want to move these ones first but let's switch into x ray mode so that we select

all of them and we want to do G and y to bring this down.

And then G and y to bring this to about here and I do want to point out if we can hide the airplane

body it doesn't come all the way forward right now.

I think I'm gonna modify this body just to pull it forward a little bit to match this sort of circle

part here so just know that and while we're here let's rename this to airplane propeller.

OK.

And I think we want to scale this down at this point.

So if we do pass then we should be able to just scale it like this.

And as long as you have your pivot point set to median point it should work properly if you have it

set to 3d cursor then it's gonna scale it inward to which you don't want.

So now we have this propeller looking pretty good.

I think we want to do an edge loop cut here.

If we do a control are along this edge and then you can slide it to about here and then we can look

at it and I'm gonna turn off the x ray mode so that we can see what we're doing.

This Propeller is just going to have two pieces extruded from the sides now rather than do it twice

on either side.

What we're gonna do actually is delete all of these faces and mirror so we will select these with holding

down shift and I think we're gonna have to also do a cut through here.

But let's just delete these first X and then choose faces.

Let's actually just delete these two right here to delete the faces and then we can create a new face

for each one of these.

By doing this we select these three and then hit F and then we shift like these three and F and that

will create the faces that we need and then we do a mirror modifier on this and that will make sure

that when we start extracting this blade out of the propeller that it shows up on both sides.

So now in face mode you can select this one and we can extrude it and if we extrude it like this it's

gonna look kind of wonky so let's hit the X key it'll lock it along the x axis and we will just go out

to about there.

Now of course I'm looking at it from a weird angle so if we look at it from the top and maybe turn on

x ray mode we can see this looks a little bit better and what we also want to do if you switch into

a vertex mode is make sure all four of these are selected.

If you do a scale like you hit the S and then X like it to the x axis.

If we go all the way down to zero It'll flatten this out so we'll type in the numbers zero and hit enter

and then we can go g x and move it out to here and you can see that this reference image isn't perfectly

symmetrical.

It looks like it was maybe off by like two pixels or maybe just one pixel so we'll just work with that.

That's fine.

And then let's do a couple edged loop cuts here.

So we'll do one here.

It's kind of like this and then we'll do one here like that and these we can straighten these out with

s x 0 if we want.

I'm not going to stress it too much for both of them.

Then we want to select these and then we're just gonna do G.

And I'm just gonna I'm not even going to lock it to anything right here.

I'm kidding.

I'm gonna like both of these and then I'm gonna move them like that and maybe I will block them with

Y.

See that's that's pretty good.

And then I'm gonna do this one too G.

Why bring that here.

And then I want to bring all three of these g y to kind of come down like that okay.

Now let's view it from the front and we can see that this doesn't have that sort of taper look.

So let's select these and we'll scale it with s in the y axis by screen at the Y the Z Z kind of bring

it down like that and then we'll do the same thing.

S Z to bring it down like that a little bit.

All right.

So that should be pretty good.

It's a little fat on the end.

So I think what I'll do is I'll bring these.

Well you know bring these ones forward so I'm going to select both of those and I'll do G and y and

just kind of eyeball it just to make it a little more thin on the edge all right.

So let's turn off this and now we've got a propeller and so because we put the origin to this point

right here we can rotate it if you hit the.

You have to select it first if you hit the R key and you rotate it.

See it uses that as the pivot point.

If we lock it to an axis like Y then you'll see that it rotates just around that axis which is what

we're gonna do in code.

We're gonna we're gonna make it rotate like this so you can right click to just exit out of that if

you followed along and just so that you know if for some reason you need to change the origin point

you can move the cursor and if you move the cursor to you know maybe the front of the cone or the middle

of the cone or something like that you can go into an object mode you can go to object set origin and

you can do origin to 3d cursor.

So that's just a little trick for the future.

And then finally let's just to make this propeller look a little bit better.

Let's go into edit mode.

We'll do tab and we will select in face mode we'll just select these two faces and we'll bring them

forward with G and y to kind of make it I mean they don't need to be touching but pretty close.

I think maybe I'll bring it back a little bit GM y just to leave a little gap.

If we look from the top there's a little gap and that's OK.

And now we have our plane looking pretty good so we can hide the reference images and I'll tab back

into object mode and I will show all of these wings as well.

And now we have our completed plane.