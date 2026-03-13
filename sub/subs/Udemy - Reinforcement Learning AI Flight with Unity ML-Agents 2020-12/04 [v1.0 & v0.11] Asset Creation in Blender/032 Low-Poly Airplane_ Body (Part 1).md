# Low-Poly Airplane_ Body (Part 1)

Now we're going to come in and start shape forming the shape of this airplane from the side.

So switch into the right view and we're going to select this cube that is the airplane body and what

we'll do is switch into edit mode so you can either hit the tab key or you can click on this object

because we are in x ray mode.

If we select with this marquee select tool just click and drag it will select the vertex behind it as

well.

But I do want to show you if you just pick a vertex and then you rotate you'll see that this does not

get selected.

So I just want to make that distinction earlier so that you know why it's not working.

If you're just clicking so we're gonna select both of these hit G and then Z to lock it to the z axis

and then we're gonna drag it down like that and do the same thing below G.

Z and kind of bring it up to the bottom of the plane.

This one is gonna be g y because it's the y axis.

And this one's gonna be g y as well to bring it back to the back of the plane.

So now we've got a shape that's pretty close to the size of our plane and we want to do some cuts.

So we want to add edges essentially so we can hit control.

Ah.

And that's going to show this yellow line is long as you hold it near one of the edges that you want

to cut.

It'll show up in the middle.

If you were to be over here then it's going to show up as cutting this edge or this edge.

So just make sure you're along this line and then you click with the left click and then you move it

to maybe like right here at the base of this.

This sort of curve and then you click again and then it locks it into place I would recommend not overdoing

it with these.

They're harder to remove than they are to add later so if we find that we need more curvature here we

can always add an edge loop and modify it a lot easier than it is to remove the edge loop in my opinion.

So then we'll do control are quick and we'll move one right here.

Control are control are control are and that should be pretty good.

So now what we want to do is select these and then just do G and then Z to lock them onto the axis and

then move them down.

So we want to form the shape of this plane.

And they just need to be close enough

and just to be clear you don't really need to lock them to the z axis I don't think at this point except

for maybe at the edges at the far ends they could technically have like an angle like this.

I just am not doing it that way.

All right.

So now we can see this maybe it doesn't look quite the way we wanted it to.

So we can do.

Control R and add one more here and I'll just place it like that and then I'm going to move this one

down and I'll move this one up just a little bit.

OK we've got a shape that looks pretty good for what we want to do.

I do want to make sure that this shape is in here too.

So we're going to select this face here.

If we switch into face select mode it's kind of hard to see which face we're selecting.

But you want to look for the dot that's in the center of the face that you're wanting to select and

then click near the dot.

If you click in between these two dots but closer to another dot even though this face is technically

on top it'll select the one that's closest to the dot.

So it's like that OK.

And then we're going to switch back into the side view.

I'm going to extrude this with the EKG and then I think probably see if I go all the way up to here.

I'm not sure that I'm gonna get quite the result I'm looking for so I'm going to I'm going to do it

to here and I'm going to switch back into vertex mode and I'm going to move this I'm just going to hit

G.

And then I can move it wherever I want.

I'm going to do the same thing with here G and then I'm gonna make it so that they're actually in line

with each other here and I'm going to select both of them.

And this is a little trick to make sure that they're actually aligned.

You can it s and then Z.

And it locks it to the z axis like this kind of.

And then if you type in the numbers 0 then it scales it to 0 which means that they're aligned along

the z axis.

And we just extrude it one more time with the E key and then I can move both of these in and I'm gonna

use I'm going to lock it to the y axis with the wiki.

So G Y

All right.

So now we've got this the way we want

and I know I did this edge loop here.

I actually am having second thoughts about how this looks but we'll see how it goes.

If we need to remove it later we can.

So the next part is going to be to slide this in.

But first let me just show you how to mirror it properly.

So if we want to work in this axis sort of from the front we don't want to have to change this side

and then also change this side.

The exact same.

That's double work.

So what we'll do is we'll mirror this over the over this axis.

So first thing you need to do let's switch into the front view with the one key and then we'll just

move this over so that the x value is zero so we can actually click over here and do zero and then that

locks it right there and then we want to actually let me hide these planes just to show you what's going

on.

We actually have these faces are still here.

We want to mirror this over the Axis but we don't want these faces to be here so we can switch into

face mode just to make sure that we have the right ones selected and then we can hit X and then we want

to delete the faces.

All right.

And then finally we want to go into this little wrench icon here and add a modifier and we want to add

a mirror modifier and then anything we do on this side is going to show up on the other side of the

axis.

Now one last thing I wanted to talk about really quick.

Our plane is currently facing down the negative y axis and there's a reason for that.

So and you can look at this gizmo here.

This is the positive y axis kind of going this direction the x axis is positive going this and the Z

axis is going like this.

The reason we are pointed in the negative y direction is because when we export this and then import

it into Unity Unity is Z positive axis which is the forward axis is actually blenders negative y axis.

So I know that's kind of weird but basically anything you want to be facing forward in unity you want

to be facing toward the negative y axis in Blender.