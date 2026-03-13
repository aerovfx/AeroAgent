# RaceManager.cs_ More Variables & Accessors

Now back in our race MANAGER We're going to continue on.

We're going to have something called public aircraft agent follow Agent and this is just going to be

which agent out of all of the agents in the scene.

Are we following which one is the camera going to follow in which one is the Heads up heads up display

going to show the status of so this is going to be a get and a private set

and then we'll just add a comment because it's not super obvious what this is.

It's the agent being followed by the camera

and then public camera active camera

get private set.

OK.

So these won't you'll be able to access these from the other scripts in particular these these different

menus but they won't be able to actually change them at all.

Now we've got a long list of private objects to keep track of.

So we're going to do private SeÃ±or machine.

We want to send a machine virtual camera we'll call that virtual camera

and let's do a control period on this and then we'll use.

We'll do that using send a machine.

So now it knows what that is.

We need a private count down UI CONTROLLER AND WE'LL CALL IT COUNT DOWN YOU I NEED A PRIVATE pause menu

controller and we'll call that pause menu private HUD controller we'll call it HUD private.

Game over UI controller we'll call that game over UI private aircraft area we'll call that aircraft

area

and a private list of aircraft agent called ops we'll call this and make sure I don't lose my place

here sorted.

Aircraft agents and I accidentally missed one private aircraft agent.

No aircraft player my mistake aircraft player OK.

So let's talk about these since there were so many center machine virtual camera is the controller of

our camera that flies around behind the airplane the countdown UI controller pause menu controller HUD

controller.

Game over UI controller.

All of these we need the race manager to have control them because it will decide when to show them

and when to hide them.

So it'll show the countdown UI at the beginning and then it will hide it.

And then if you press pause it will show the pause controller.

But as soon as you unpack as it'll hide that.

So that's basically what it is we're gonna have a bunch of different you guys that can be controlled

by the race manager.

Then we also have this aircraft area that's just going to know in the scene which are what the aircraft

area is which is this this desert area.

In this scene and then the player is whatever the human player is so this keeps track of which of the

agents is the is the player and then the rest.

Is this aircraft agent the sorted aircraft agents.

So we need to keep our lists sorted so that we know who's in first place and we're gonna do some special

sorting logic to make sure we know who is furthest along in the race.

So we got a few more to do here so we're gonna do private float last resume time.

We're gonna set that to zero.

So this is has to do with pausing so we're gonna keep track of the last time we resume the game.

Private float.

Previously elapsed time

and I'll be honest I don't remember off the top of my head what this is.

It definitely has to do with pause logic.

So I'm just gonna say pause timer's and we'll be using it later so it will have some context around

it once we get to it.

We're going to do private float.

Last place update.

I'm gonna set it equal to zero so this is at what point did we last check the order of all the different

agents.

We don't want to sort the agents every single point zero two seconds or something like that.

That doesn't make a lot of sense.

So we're gonna sorted every half second I think is what I had it set to that we're going to have a private

dictionary

of aircraft agent.

So that's the key.

So you pass in an agent and then you're gonna get something called aircraft status back which doesn't

yet exist.

We're about to define it on the next line and we'll call this aircraft statuses

so we need that class.

So it's gonna be a private class aircraft status

I guess technically this could be a struct I'm not sure why I wrote it this way.

Public int checkpoint index equals zero public int lap equals zero public int place equals zero and

public float time remaining equals zero.

So basically we're gonna have a dictionary that we can quickly look up what the any given agents checkpoint

is what their lap their place and their time remaining is

then we're gonna do for the last part before we start writing some functions we're gonna have an access

or for the public float race time

and this will be the clock we're keeping track of race time considering pauses.

OK so this is this is gonna be sort of a smart timer so we're gonna have just to get for this we're

not even gonna need a set and we'll say if game manager dot instance dot game state is equal to games

state playing

so inside of that if we're going to return previously elapsed time plus time dot time minus last resume

time.

So this is how much time had previously elapsed.

And then we're adding on the current time of the game and then we're subtracting the last resume time.

So basically we keep track.

When was the last time in the game that we resumed.

So let's say we were playing and then we got to one hundred seconds in and then we paused the game.

We need to figure out what the time is.

If it's playing then we check when the last time we resumed was the total amount of time that had had

passed.

So that would be one hundred.

We're gonna add on this new time and then we subtract the last resume time and then it's maybe a little

confusing but it does keep track of the current race time.

So else if game manager instance game state is equal to game state DOT paused so if the game's paused

we return the previously elapsed time because we're not actually the time is not increasing when we're

paused.

So it's just going to use whatever that previously elapsed time was so you say you paused it.

One hundred and twenty seconds had elapsed.

Then we're going to just return 120 because that's the current game to game clock and in any other circumstance

we're just going to be safe and we're going to return zero.