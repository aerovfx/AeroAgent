# Low-Poly Terrain_ Setup

I have blender two point eight open right now and this is the default scene.

They always start with a cube and a camera and a light and we need none of them.

So what I'm going to do first of all is I'm going to open up this side panel here.

I'm going to enable something you won't have here it's an add on that you can get through the preferences

but it's a shortcut viewer or so down here it'll show you what I'm doing.

Like if I click the left mouse then it's going to show that.

So that should be running and then we'll go up to the item tab and you can proceed.

So first thing I'm gonna do is make sure my mouse is hovered over this window because if it's hovering

somewhere else then the shortcut keys do different things.

So hover over this hit a to select everything and then X to delete it and then you can click this to

delete.

So now we have an empty scene and we can start creating.

So we're gonna create a terrain and there are terrain tools in unity but because I want to have a low

poly feel to this scene I'm forced to create my own.

That's not a big problem.

It's actually better because we have better control over these things just know that that's why we're

not using the terrain inside of the Unity Editor so the first thing we'll do is we're gonna add a plane.

So if we go up to the ad menu mesh plane what this created is a two metre by two metre plane.

Each of these grid lines at least at this zoom level is one meter and we want this to be one kilometer

square two meters by two meters isn't a very big space for planes to fly around.

So in order to do this I'm going to click here and I'm actually going to type in one K M one KLM and

it automatically will convert it to 1000 by a thousand which is pretty cool.

So now if we scroll out oh this thing gets cut off.

So we want to fix that and we can go into this view menu here and we can change the clipping start and

end Well point one metres so this would be 10 centimeters is probably fine.

We don't need to get super close up but what's happening is it's clipping it.

Anything that's further than 1000 meters from the view camera will get clipped off.

So we want to make this quite a bit bigger.

Let's just make it five thousand.

That's probably enough.

And if we have trouble then you know.

OK.

Yeah.

That lets us get pretty far away before we have any trouble so if we go back to this item tab we can

see that the dimensions are right.

But the scale is now 500 by 500.

And when we import this into unity we're ultimately going to want this to be one one one not five hundred

five hundred one.

So this is important.

We want to apply this scale now.

Not only do we want it to be 1 1 1 in unity but if you weight than the sculpting tools we're going to

use in just a moment won't work as they won't work the same way.

So let's apply this scale.

And so the way to do that is object apply scale.

So now you can see that the scale is 1 1 1.

That's what we want.

All right.

Now what we're gonna do is we're going to sculpt this terrain so you can switch into the sculpting mode

here and the first thing you'll notice is if you scroll out well now we're back to this same problem.

So we have to click this out and we have to go into view and change this to 5000 as well a little update

as of Blender 2.8 1 the default color of anything that is gonna be sculpting will be this gray color.

It's easy to change that.

You don't have to but if you want to if you want it to look like the brownish red color that I have

for the rest of these videos you can go up into this drop down menu make sure you're under matte cap

click on the sphere and then you can choose from any one of these.

And the one that is set to for the rest of these videos is this brownish red mud color and now we're

ready to sculpt.