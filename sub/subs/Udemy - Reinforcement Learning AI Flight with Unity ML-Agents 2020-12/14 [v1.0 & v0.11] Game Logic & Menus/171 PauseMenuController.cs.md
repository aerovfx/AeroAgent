# PauseMenuController.cs

Now let's work on our pause menu controller so we can go into our scripts for that.

Let's find our pause menu controller and you can go ahead and delete what's inside here will of course

be recreating all the functions we need so the first thing we're going to need is a private void Start

and this is going to be game manager dot instance dot on state change plus equals on state change

state change.

OK.

So we're gonna create a function now that is going to be called anytime the state changes private void

on state change.

So now we're just actually defining that method if game manager dot instance dot game state is equal

to game state DOT playing

we'll say game object set active false.

So if the state changes to playing then it's going to hide this menu

then we need to add a couple of functions four buttons.

So we're gonna do public void void on let's see resume button clicked so any time the resume button

is clicked we're gonna call this function and we'll say game manager dot instance Dot Game state equals

game state DOT playing

and then we'll do public void Main Menu button clicked

and we'll do game manager dot instance load level

menu let's make sure that I named that correctly we need to make sure that it matches the name of the

scene that is our main menu.

So we want this to be main menu not just menu main menu and then we're gonna set the game state equal

to game state DOT main menu

and then finally we're gonna add a private void on destroy

and inside here we're gonna say if game manager dot instance does not equal null game manager dot instance

dot on state change minus equals on state change

so that should be all we need for the pause menu controller let's go into unity and we will hook that

up.

So once this is done OK now we can do ad component pause menu controller and we need to hook up the

buttons so the resume button if we go down hear this on click area we need to hit the plus button and

we're gonna drag this pause menu into here so that we can access the pause menu controller and call

resume button clicked and we'll do the same thing for this one drag that pause menu down in there so

that we can call pause menu controller Main Menu button clicked.

So now we should be able to pause and resume this menu will pop up when we pause and resume and our

pause and then we can either resume or go back to the main menu.