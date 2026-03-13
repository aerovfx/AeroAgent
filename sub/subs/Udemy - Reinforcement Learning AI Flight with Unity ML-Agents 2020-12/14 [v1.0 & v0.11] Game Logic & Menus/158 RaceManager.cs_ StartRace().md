# RaceManager.cs_ StartRace()

Now let's work on START race.

So let's add a comment for this starts the count down at the beginning of the race and it's a yield

return because this is going to be an eye and numerator not a string.

So this is an asynchronous method first thing we'll do is show Countdown so we'll say count down UI.

Game Object dot set active and we'll set it to true.

So this will show the countdown UI and basically what we'll have is a number that shows up it'll say

three two one go.

So we're going to show the UI.

Then we're going to say yield return.

Count down UI dot start countdown

which of course is not yet implemented.

So let's right click through quick actions and we'll generate that method so it's in here.

So we'll be able to come in here and we'll make this work later but we're just going to make this not

have a red squiggly and then we're going to initialize agent status tracking

so we're gonna keep track of the stat the status of each agent at all times.

So we have to kind of start that dictionary start that process.

So aircraft statuses remember this is a dictionary so it's equals new and then it should suggest dictionary

aircraft agent aircraft status.

So we're creating a new dictionary and then we'll say for each aircraft agent

in or sorry aircraft agent agent in aircraft area dot aircraft agents

so for each one of these we're going to create a new aircraft status.

Let's see this oh this is why I made it a class instead of a struct.

That's right.

So that we can say status equals new aircraft status

and then we can say status lap equals 1 status start time remaining equals checkpoint bonus time.

So remember that was 15 seconds.

So we're gonna set the initial time remaining to 15 seconds and the lap of course to the first lap then

we can say aircraft statuses dot add agent status so now this is ready for us to manage each time we

update this and now before the race can start.

We of course need to thaw our agents because they're currently frozen.

So we'll say let's see if we can copy one of these.

We want to thaw agents so let's let's just save ourselves some time.

Copy this

and then we can begin playing

and that will be game manager that instance Dot Game state equals game state DOT plane

and remember every time we change this an event is fired and that event we actually have this function

hooked up.

So any time that event is called it's going to hop down in here.

So if we set it to playing then it's going to go into this function and it's going to check and it's

going to find oh game state is playing so that it's going to set this last resume time equals time no

time.

And it's going to set this HUD active and then it's going to thaw the agents.

So now that I'm thinking about it this is actually completely unnecessary code.

I'm going to risk it and delete it and hopefully it does not cause any problems.