# AircraftAgent.cs_ ProcessMovement() Completed

Now we need the float your lips.

I want to put this back here.

Float your equals cur wrote dot y plus smooth your change times.

Time to fix delta time time's your speed.

And remember what I said we don't we're not actually clamping how much you can turn.

You can obviously turn all the way around in a full circle if you want.

And then we want float roll equals clamp angle cur wrote dot Z plus smooth roll change times timed fixed

delta time times roll speed and we're gonna do that between

see right here do it between negative Max well negative Max roll angle and Max roll angle

and then finally now that we have those values we're going to set the new rotation transform dot rotation

equals quit turning in dot Euler pitch ya roll

all right.

So I know that was quite a bit to get through but that's that's basically the function that controls

the movement of this airplane.