# AircraftPlayer.cs_ Variables

All right so let's go back into a visual studio and into our aircraft player scene or code file here.

And this aircraft player is actually going to inherit from aircraft agent so it's going to be an agent

with some additional functionality on top of it so the first thing will add is a header and it's going

to say input bindings.

And the reason you particularly want a header here is because it's going to still show all of these

variables from this aircraft agent in the inspector it's just going to add onto it so we want for these

public input action.

It's not going to know what that is.

So hit control period and then you can choose this using Unity engine input system and then we'll say

pitch input we need another one public input action.

This one is going to be your input public input action boost input and surprise.

There's actually going to be one more that we'll just add right now public input action pause input

so that's good.

Those are the only ones that are going to exist the pause is basically just going to be the start button

on your controller or the escape key so you can pause the game while you're playing it.