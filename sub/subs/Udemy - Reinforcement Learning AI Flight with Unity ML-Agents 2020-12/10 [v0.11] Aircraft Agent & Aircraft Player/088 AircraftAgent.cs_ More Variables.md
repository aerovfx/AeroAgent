# AircraftAgent.cs_ More Variables

This agent can fly but it's gonna need a lot more functionality before we can use it for training and

of course for racing.

So let's go back into aircraft agent and keep working.

So up at the top we're going to add another section of parameters.

Basically this one is going to be called Let's Make an header and we'll call this explosion stuff and

this one is going to have a public game object mesh object.

And let's give a tooltip for this one because it's not super obvious what it is.

The tooltip will say the aircraft mesh that will disappear on explosion.

So basically what we're gonna do is if this runs into something then we're going to disable the mesh

object which is the airplane.

We're just going to hide it so that it can

show an explosion instead and then eventually we'll bring it back to life when we respawn or reset the

position.

And the next one we want is public game object explosion effect and we'll add it to tooltip for this

one.

I'll say the game object of the explosion particle effect

so the last one we want to do we're gonna add another header section here and this one will be training

parameters.

So we will just this one is pretty small.

It's just public int step timeout and we're gonna default that to 300 and let's add a tooltip for this

one to and the tooltip will say number of steps to time out after during or after.

Let's see that's a little confusing.

So basically it's number of steps to time out.

Two time out after

in training hopefully that's clear.

Basically we don't want this to be able to keep going forever if it's not headed toward the next checkpoint

eventually.

We want this thing to time out.

So that's what that means.