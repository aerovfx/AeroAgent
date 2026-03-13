# HUDController.cs_ Hook Up to UI

Now to wrap up the hood Let's rename this canvas to be hood and let's add a HUD controller component

to this.

So if you type in HUD and then you find the HUD controller and then we can add a place text to this

field.

The time text here.

A lap text the checkpoint icon and the checkpoint.

Aero.

So now this should be all set.

This part's ready to go.

Unfortunately we can't test it right now if you test it.

You're gonna hit errors.

Unfortunately the way that this is all written it's kind of all tied together.

The race manager is going to assume that there is a pause menu and a countdown menu and a game over

menu.

And if you remember if we inhere in the race manager there were some places where we were setting like

right here we do set active right at the beginning.

And for us to comment out all of these sections just to test the heads up display right now would be

too much work and probably mean that we would make some mistakes.

So we're going to keep going and we're going to finish out these other menus before we can actually

test it out.