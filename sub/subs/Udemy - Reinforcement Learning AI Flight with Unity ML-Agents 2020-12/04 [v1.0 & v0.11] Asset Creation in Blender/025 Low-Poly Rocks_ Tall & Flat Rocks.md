# Low-Poly Rocks_ Tall & Flat Rocks

So we will hide this rock using the little eye some symbol and then we're gonna create a new biosphere.

And this one we're actually going to scale it in the in the z direction up and down.

So we'll do this.

Set that to two and now it kind of looks like an egg but we're not going to leave it as an egg.

First we need to go to object apply scale and then we can go into sculpting mode and use the same tool.

So I'll kind of zoom out here and just kind of start.

I didn't want to take that much off.

Let me start more in the middle and then kind of keep shaving stuff off.

And so the same thing is true of the other one.

But what I didn't say was basically all of these triangles are still there.

You can't see them because they're so flat but they're not going anywhere.

So the the point is just to kind of flatten them.

And what we're going to want to do is not necessarily use this rock as is for the collider portion.

So the problem is because there's so many vertices the the collider meaning the thing that things run

into in the scene will be overly complicated.

And since that's not something we want we're going to make a more simplified version of it that we can

use in unity for our collision physics calculations so that hopefully will become clearer in a moment.

So that's another one if things aren't looking right.

Obviously you can always start fresh.

There's also a smooth tool that you might be interested in like if you get a corner that looks a little

too sharp or something you can kind of smooth it out actually kind of like that sharp corner so I'm

going to leave it as is and then what you can do is let's see rename this to we'll call this rock t

for tall.

And then we can hide this and we can create another one.

So we'll go back into layout and we'll create our last one loops add mesh because fear we're gonna make

a flat one this time.

So I'm going to scale this maybe in the x level by like one point seven five and in the z to one point

I think three was what I had before.

So this is gonna be good for like a large flat rock that might comprise the top of a tunnel or something

like that.

So we'll go into sculpt.

Actually let's apply the scale first object apply scale and then we'll switch into what am I doing.

We'll switch into sculpting and then you can kind of look at it from the top and I'm using the wrong

tool undo that and make sure I switch back into scrape mode and kind of just apply this oh that's not

quite what I want to do that try again

I keep accidentally flattening out these these sides I'm gonna try and come in here and kind of do it.

Do the sides first so that I don't keep making them sharp

that this one.

Good grief.

All right.

Let's see if we can smooth this out and make it a little more Oh boy.

Oh it's not terrible.

Rather than try and keep fixing it I'm just gonna be happy with it the way it is

sometimes the weirder looking things are just OK.

No that was too much too weird not OK.

All right.

That looks not too bad.

Except for that part that I just messed up.

Let me smooth this out just a tiny bit.

Here we go and think.

I think I'm just gonna keep that as is.

That looks like a decent rock.

Not too bad.

OK so now we have these three rocks.

Let's actually name this last one rock.

F for flat.

You can name them whatever you want.

We're not going to access them with code or anything like that.

We'll just be accessing them later.

So these are three rocks we've got.

We'll be able to place them around our scene.

But as I said these have very complex geometry to them.

Like if we switch into modeling mode and I hit it I'll have to select it hit tab.

You can see that there's quite a few vertices there's actually six hundred forty two for each one of

these.

And that's too complex for mesh.

Well it's not too complex but we can do better we'll get better performance if we simplify it because

we're gonna place so many of these rocks in the scene you know if you have a hundred of them.

Well now you've got sixty four thousand vertices that just are part of your physics calculations which

is just going to be too much.