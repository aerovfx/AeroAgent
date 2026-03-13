# RaceManager.cs_ Awake() & Start()

OK.

Now let's start writing some functions so our first one is a private void Awake and what we're gonna

do is just find a bunch of objects in here so going to say HUD equals find object of type HUD controller

then we're going to say count down y equals find object of type count down UI controller

pause menu equals find object of type pause menu controller

game over UI equals find object of type.

Game over UI controller.

Now we'll find the virtual camera so that equal to find object of type

A MACHINE

virtual camera

then we need aircraft.

Area we'll set that equal to find object of type aircraft area

then active camera we'll set that equal to find object of type camera and then we're done.

So one way that is often used in unity is we would make these public variables and then you could click

and drag and make all these connections.

This just saves us some time so that we don't have to do that.

This just automatically finds them.

It's maybe not the most efficient way to do things but it will make things easier for us right now.

Next we're going to need a start function and that will be private void.

Start and in here we'll do the initial setup and start race.

So when this scene starts up and the race manager begins then it's going to start doing all this stuff

stuff.

So the first thing we do is game manager that instance on state change plus equals on state change.

So this is a function that does not yet exist.

So we'll just leave it red squiggly for a minute and we'll come back to that.

So next we need to choose a default agent for the camera to follow in case we can't find a player so

we're going to set the follow Agent equal to aircraft area dot aircraft agents zero.

So it's gonna just choose the first agent here

and then we're gonna do a for each loop through each aircraft.

Agent Agent in aircraft area Dot.

Aircraft agents.

So we're gonna loop through every single agent and we're gonna first we're gonna say Agent dot freeze

agent so we're gonna make sure that they can't move then we'll say if Agent dot get type equals equals

type of aircraft player.

So this is checking to see if this is the player rather than one of the other agents found the player

follow it.

So we're gonna say follow Agent equals agent aircraft player equals and then we have to cast this aircraft

player of an agent because by default this is an aircraft agent we need to cast it to an aircraft player

then we'll say aircraft player dot pause input dot performed

plus equals pause input performed.

OK so what does this do.

This is if you remember we created the aircraft player a while ago we added this pause input action

here.

This is basically subscribing to that event.

So if we click or if we hit pause or do the escape key then it will call this function which will define

a little bit.