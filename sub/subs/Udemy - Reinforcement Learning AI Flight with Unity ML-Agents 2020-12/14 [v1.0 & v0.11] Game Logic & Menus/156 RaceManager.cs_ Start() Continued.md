# RaceManager.cs_ Start() Continued

OK so now we need an else for this

and we'll say set the difficulty and what we have to do here as we say Agent dot give model and what

we pass in here is a behavior name and then a neural network model.

And then I guess that's it.

So we'll say game manager instance for instance game difficulty dot to string.

So we're gonna get the difficulty.

So it's either going to be normal or hard and then we have to pass in a neural network model.

So let's do this on the next line just to have some extra room we'll say difficulty models.

So it's going to go through this list.

We're gonna use a lambda here.

We're gonna do dot find X and then equals and then the greater than sign X dot difficulty is equal to

game manager dot instance Dot Game difficulty dot model.

So what this is doing is it's looking in this list and it's finding something where the difficulty is

equal to the current difficulty of the game and then it's getting that and end model from it and passing

it into this give model function

after we do that we need to.

This is after the for each loop so make sure you're outside of that for this next piece of code we're

going to tell the camera and the heads up display what to follow so we'll say debug assert first we'll

see debug data assert virtual camera does not equal no and if it is we'll say virtual camera was not

specified so we're just doing a quick check.

So this will help us prevent us from making mistakes.

So we'll say virtual camera dot follow equals follow Agent dot transform and virtual camera Look at

equals follow Agent dot transform so this will automatically set it up so that the camera follows our

player and then we'll say hood dot follow Agent equals follow Agent so HUD doesn't yet have a follow

Agent.

So this is going to have this be red squiggly let's just show potential fixes and let's just generate

a let's see do we want a property or field let's do a property generate a property and so that'll do

that inside of the HUD controller.

This is fine we'll just save it and come back.

So now we don't have that red squiggly we'll be coming back to that next we want to hide UI so we'll

say HUD Dot Game Object dot set active and we'll set it to false we'll do the same thing with pause

menu game object set active false and I'm just gonna copy this for the next couple count down UI game

object set active false.

And game over UI a set active to false so this will hide all of these UI if they're visible and then

we will start the race.

And so the starting of the race will be a co routine so we're gonna do start co routine and we're going

to call a function that we need to define called Start race.