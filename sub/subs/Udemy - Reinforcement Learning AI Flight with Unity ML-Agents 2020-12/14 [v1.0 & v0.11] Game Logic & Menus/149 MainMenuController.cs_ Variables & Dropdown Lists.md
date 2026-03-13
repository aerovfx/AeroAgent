# MainMenuController.cs_ Variables & Dropdown Lists

Now we need a script to control this menu.

So go into your aircraft directory and go to scripts and let's right click Create a new C sharp script

and this one's going to be called Main Menu controller

and we may want to organize these better.

But for now I'm just gonna leave them as is so we can open up this script.

And it should open up.

It didn't want to open because I had inconsistent line endings.

I'm going to uncheck this so I can ignore it.

OK.

And if that happens you can always click save all and it'll save all of those ones that are edited so

Main Menu controller is going to control this main menu.

So that makes sense right.

We're going to put this in the aircraft namespace

and then we can get rid of what's inside here.

So we're gonna need a couple of public variables public list string levels.

This will be a list that we can set of level names that can be played in the game.

So we'll add a tooltip for this tooltip the list of levels seen names that can be loaded.

So what's cool is because these are just strings they will match up with whatever scenes show up in

here.

If this thing's ever going to load so we can call one dessert.

You can also add spaces to these which I just learned recently so you know if we had like city big or

city night or something like that with this I don't know.

Something with a space then we could put that in this list as well then we're gonna do a public T MP

underscore dropdown which we don't know about yet.

We're gonna do a control period and then it's going to suggest using team Pro.

Now it knows about this and this is going to be the level dropdown

and this will be let's add a tooltip the dropdown for selecting the level

then we need another dropdown.

So we'll do a public tempi dropdown and this will be the difficulty dropdown

at another tooltip the drop down for selecting the game difficulty

so those should be all the public variables that we need we're going to add a couple privates.

Private String selected level and private game difficulty selected difficulty.

So now we need to define the start function.

So void Start and we're going to fill up the dropdown lists in here so I'm gonna add a comment that

says that automatically fill the drop dropdown lists

and the first thing we'll do is a debug assert and we're going to assert that level stock count is greater

than zero.

And if not we're gonna say no levels available and that'll at least warn us if we forget to set this

list of levels that this isn't gonna work.

So we'll say level level dropdown that clear options so that'll clear out everything that was in there

level dropdown dot add options and we're gonna add our list of levels and then we'll say selected level

equals levels zero.

So we're just gonna default to whatever the first level in the list is we'll do the same thing with

difficulty difficulty dropdown dot clear options difficulty dropdown dot add options and we're gonna

use a little trick we want to just use that list of difficulties from this numerator here.

So the way we can do that is actually enum and it doesn't know about this capitalized version of it.

So we're gonna hit control period and we're gonna do using system.

So enum dot get names type of game difficulty and then dot to list which it doesn't know about control

period.

That's gonna suggest using System dot link will hit enter and then we can finish this line off and then

we'll just say selected difficulty equals game difficulty dot normal.

So this is just the default.

But now we have options that are this list these number of names.

So even if we had like an easy one we had normal one hard very hard it's going gonna default to normal.