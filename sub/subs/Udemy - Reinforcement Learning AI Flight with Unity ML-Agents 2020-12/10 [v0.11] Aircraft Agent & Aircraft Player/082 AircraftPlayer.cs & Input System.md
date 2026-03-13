# AircraftPlayer.cs & Input System

So this agent action function is going to be called automatically by the Academy and that happens using

the neural networks when we have basically an A.I. controlled agent.

But if we want to have a player controlled agent then we need to add some code that's going to feed

values into this essentially using inputs from either the keyboard or a gamepad or a joystick or something

like that.

So we're going to add that it's going gonna be a new class.

So let's go into aircraft and we'll go to scripts and we're gonna create a new class a new C sharp script

and we'll call this aircraft player.

So this is going to be the script that we use to control the aircraft using our own controls so we can

open this up and then let's add it to the namespace aircraft

now for input you could use the classic input manager.

But we're gonna use a new input system that Unity's been working on.

It's still technically in preview but it seems to work pretty well and I really think it's great.

So we're gonna try using that.

So if we go to window and package manager we have to find a preview package.

So go to advanced and show preview packages and then we need to find input system so it's down here

input system.

Currently it says it's in preview but it's the one point zero version.

So it's a pretty good preview.

Then we want to install this

and it says this project is using the new input system package but the native platform back ends for

the new input system are not enabled in player settings.

Do you want to enable the back ends you want.

Yes but notice here it says doing so requires a restart of the editor.

This is super important.

If you're only half listening start listening we need to restart the editor after we do this so we're

gonna say yes and then we're gonna have to close down the editor and reopen it.

OK so I think it's imported now.

So what I'm gonna do is just for good measure I'm gonna save the scene I'm gonna save the project and

then I'm going to close down the editor and I'm going to have to reopen it.

So go into unity hub

and then I need to find where my directory is it's the right one.

I think it is.

Sorry I have I have so many versions of this project at this point it's kind of hard to tell the difference.

OK that looks right.

So now we should be able to use the input manager.