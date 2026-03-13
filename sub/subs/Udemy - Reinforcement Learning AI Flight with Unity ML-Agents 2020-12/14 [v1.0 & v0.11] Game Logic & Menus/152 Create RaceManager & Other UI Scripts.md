# Create RaceManager & Other UI Scripts

Now we're going to work on the actual logic that controls the race.

And so we're going to switch into our desert scene.

I don't know that we really need to but I'm just doing that to sort of talk about it a little bit.

I'm going to switch altitude view.

So we're going to need something that determines which place the different agents are in and whether

they've completed a lap and a bunch of other logic.

So let's create that script it's going to be called Race manager.

So we'll create a new C sharp script race manager and race manager is going to need access to a lot

of other scripts.

And so rather than have a bunch of red squiggly lines in the code we're going to create those scripts

now so that we can reference them without having any issues in the code so got a few to create and create

a C sharp script.

The first one will be called Count Down UI controller so the countdown UI controller is going to show

three two one go at the beginning of the race.

We're going to create another one.

This one is going to be the pause menu controller that's pretty straightforward.

We're going to create another one.

This one's going to be the HUD controller and that's it's not let me change it.

I don't know why it did that.

Delete it just so that I don't have to rename it in code.

Because when you when it does that it it calls the class new behavior script.

I'm just going to delete it and then I'm going to create a new one OK create a C sharp script and this

one is going to be the HUD it's doing it again isn't it.

Okay.

Can't catch a break.

All right I'm just gonna do it this way.

H you d controller and this is short for heads up display so it'll be the thing that shows what lap

you're on.

Which place you're in in the race.

Now I'm going to hopefully successfully create a new script here.

This one's going to be the game over UI controller.

Game over UI controller

and this is what's going to show up at the end of the race so that should be all the scripts we need.

We need to open these up and add them all to the aircraft namespace now.

So I'm going to go into visual studio and look at all these new scripts that I have so race manager

is going to go in name space aircraft

and I'm going to save myself a little bit of time and just copy this copy both of these so that I get

the curly brace and then all I have to do is paste and then do that.

So race manager is done now.

I need to do the Steve the countdown UI controller so I'll add that to the namespace and then we have

the game over UI controller

and we have the HUD controller which for some reason didn't want to behave so we'll rename it here HUD

controller

add that to the namespace then the main menu controller should already be in that namespace.

And the pause menu controller needs to be added to the namespace as well.

OK.

So now we can work on the race manager without having a bunch of red squiggly lines all over the place.