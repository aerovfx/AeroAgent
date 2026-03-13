# Gameover Screen & GameoverUI.cs

Now we're going to create our game over UI so let's right click on race manager UI and let's add a text

mesh Perot or rename this canvas to game over UI and then this is going to be just the game over.

Well it's actually going to be the place text OK.

And then we need to make this a little bigger so let's make the with more like 400 let's make the height

one hundred let's center this and probably we'll keep it aligned to the top.

And then let's increase the size of this to like 50 60 60 looks pretty good.

And this will end up saying something like first place second place and then we're going to still provide

this Main Menu button that we used in the pause menu.

So very similar

so we'll just say place and then we need to go into the game over UI.

We need to create a button UI text mesh probe button and we will move this down to like right here and

let's hide to hide some of this.

At least the pause menu so we can see what we're doing.

And this is going to be the main menu button and so inside here we'll rename this to main menu.

And so it's going to say what place you finished.

I'm gonna move this up a little bit and then what.

And then you'll have the option to go back to the main menu.

So pretty straightforward.

Now let's create or let's work on this script.

So we need to go to the game over UI controller and I'll remove these and we're gonna say public text

mesh pro Yuji UI control period enter to get that using team pro place.

Text and I don't know why I chose to add a tooltip here but we will do it tooltip text to display finish

place e.g. second place.

So that's kind of what it's gonna say.

I guess we need the race manager so we're gonna do private race manager race manager like that and then

we'll do it private void Awake and inside of here we'll say race manager equals find object of type

race manager

and then we're gonna do a private void on enable so when this is enabled we're gonna say if game manager

dot instance is not equal no.

And just tab in game manager instance game state is equal to game state.

Game over

so I'm gonna tab that in like I intended to.

Then gets the place and updates the text so we don't want this constantly updating.

We wouldn't want to do it in the update function for example there's no reason to update the finished

place the entire time the race is going so we'll say string place equals race manager dot get Agent

place race manager dot follow Agent and we'll say this place text dot text equals place plus place.

So it's gonna say whatever that thing that comes back from get Agent place so like first place

and then down here will do.

Public void Main Menu button clicked so this is a new function that we're gonna call when that main

menu is button is clicked.

And then in here we'll see game manager dot instance to load level.

Main menu and Game state DOT.

Main menu.

So this one I'll just say loads the menu.

Main Menu scene.

Now let's look that up in Unity so we'll go to our game over UI in particulars.

Well we need to add this component so let's add a game over UI controller and then place text should

be showing up.

Something's not right.

OK.

There's an error there's a semicolon missing on line twenty seven it looks like.

So let's see.

Line twenty seven.

Yeah that semicolon try again.

This should show up OK so now our place text goes into here and our main menu button needs a on click

event so we'll do this we'll add the game over UI in here and then we will do the game over UI controller

dot Main Menu button clicked

and we can hide this.