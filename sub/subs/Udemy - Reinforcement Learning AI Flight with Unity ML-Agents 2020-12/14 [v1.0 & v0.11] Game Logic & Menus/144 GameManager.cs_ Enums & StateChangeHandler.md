# GameManager.cs_ Enums & StateChangeHandler

We're going to start turning this into a playable game so obviously we can race around the race track

but there's nothing that keeps track of who's in first place or which checkpoint you should go to next.

So we're going to create our first new script in awhile so go into your aircraft scripts directory and

then let's create a new C sharp script and we'll call this game manager

and unity even treats the game manager as a special kind of script.

So it gives us this little gear icon.

That's kind of cool.

I don't think it does anything special it just shows up as a gear so let's open this up and let's edit

this script.

So the first thing we'll do is we'll put it in the aircraft namespace

then we can go ahead and just clear this out just to have it nice and clean and now inside here we can

create a couple new names that we'll use a couple enumerators.

So public game state.

And this will keep track of what state our game is in which should make sense as we start defining what

the states are.

The states will be default Main Menu preparing playing paused and game over so most of these are self-explanatory.

What I will explain preparing versus playing when you load up a new level we're going to go into the

preparing state which basically means the countdown is starting.

So before the race starts we give a little.

We're going to give a little countdown that indicates that the race is about to start but we're not

actually playing yet.

So that's the difference between those two then we're gonna need another one.

Public you know game difficulty and for now we're just going to have normal and hard

and then we're going to create a public delegate void on state change handler.

And what this will do.

This is going to basically be called anytime the game state changes.