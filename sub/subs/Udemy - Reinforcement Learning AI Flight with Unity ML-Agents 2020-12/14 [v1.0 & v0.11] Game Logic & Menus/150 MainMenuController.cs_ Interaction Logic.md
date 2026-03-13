# MainMenuController.cs_ Interaction Logic

All right.

So the next function we want to write is a public void set level.

And this is what's going to be called anytime that we change a value in our level dropdown.

So it's going to get an index and this is just the index of the list item that was selected in the UI

and since we automatically set that list we know what that level index is.

It's going to match with this list of levels they're going to be in the same order.

So we can say selected level equals levels level index.

That's one of the benefits of setting this in code instead of just filling it in manually in the UI

settings.

Can I add another function public void set.

Difficulty SAME IDEA.

WE'RE GONNA GET AN INT Difficulty Index and then in here we're going to say selected difficulty equals

and then we're gonna cast game difficulty.

Game difficulty on this difficulty index so this basically we're getting a number that's going to correspond

to all the different genomes and we just have to convert that number into whatever it's game difficulty

is

now we're gonna add two functions for when the buttons are clicked.

So public void Start button clicked

and let's just add a comment.

Start the chosen level and in here the first thing we'll do is set game difficulty and that'll be game

manager thought instance.

So here's the first time we're using our game manager game difficulty equals selected difficulty

and we're going to load the level in preparing mode and we'll do game manager instance load level selected

level.

Remember this is a string and then Game state DOT preparing so that we load up the level and it will

be in preparing mode.

And then the last function we need in here is public void quit button.

Let's make sure I get the capitalization right quit button clicked

and then this one's pretty straightforward it is let's quit the game.

And we'll just call application dot quit so these are all the things the different actions that can

be taken by our UI.