# RaceManager.cs_ OnDestroy(), GetAgentLap(), GetAgentPlace()

Only a few more functions left and then we're done with this glass finally.

So there's I think one more private function left so we'll do that down at the bottom here.

Private void on destroy.

And so when this race manager is destroyed WE'RE GONNA SAY IF game manager instance does not equal no

game manager instance on state change minus equals on state change.

So we're gonna stop listening to events from this when we're destroyed

then we'll say if aircraft player is not equal.

No aircraft player pause input.

Performed minus equals pause input performed so we're not going to listen to.

Pause pause events anymore either.

So now we've got a couple more public methods to do this get agent next checkpoint.

I seem to have as a public function so I'm going to change this because we might be using it somewhere

else and I'm going to copy this or I'm going to actually cut it.

So do control X and I'm going to move it up to the top because I like to keep my public functions together.

If I can so while all the way up to the top so let's paste this here.

Okay so now we've got a few more public ones to do so we gonna do public int get Agent LAP AND WE'RE

GONNA PASS IN AN AIRCRAFT agent called agent and this one is pretty self-explanatory.

Get the agents lap and it's the agent and it returns the lap.

The agent is on.

OK so in here we just return aircraft statuses of agent dot lap start lap

we're going to do another function called public string.

Get agent place.

So these are gonna be actually used by the UI.

It's going to ask the race manager Hey what's the what's the lap of this agent.

What's the place.

What places it in it's gonna keep asking it every every frame basically so that it can keep these values

updated in the heads up display so we're gonna pass in another aircraft.

Agent Agent and let's add a comment gets the race race place for an agent.

I.e. first second third etc and of course we're passing in the agent and we're returning the place relative

to other agents and in here we'll say int place equals aircraft statuses of this agent top place.

Let's do that on the outside.

Place if place is less than or equal to zero return stringed empty.

So what this will be is basically if for some reason places zero or lower than it's clearly not valid.

So we're going to return an empty string but otherwise we're going to return a.

The proper thing.

So it's either gonna say first second third 21st fiftieth you know they all end with different endings

so we want to make sure we do that correctly so we're gonna do a switch statement place mod 10

and in the case 1.

So Case 1 means like let's say we had the it was in 21st place then we're dividing by 10 enough times

that the remainder is 1.

So the suffix is s t so 21st.

So we would return place dot to string plus as T.

So any time it ends in a one it's an S T and then we're gonna kind of do the same thing here a couple

of times in a row.

So I'm just going to copy this and save myself a little bit of time a little bit of typing and we don't

actually need for cases we need a default okay.

So then there's the case where it ends in a two.

So that would be like second 20 second 30 second one hundred and second.

So we end in and D and then there's three.

So it's third and twenty third looks like maybe not thirteenth.

Boy didn't consider that case.

So right now it would be would be like 13 nerd is what I currently have this working as I'm not sure

that I care enough to fix that.

You can fix that if you care maybe so t h is the other case.

Is there any other case.

So let's see.

So 12th would be T H.

So what I'm gonna do here we're going to need some sort of special case here.

So maybe I'll just do.

I'm gonna do this on the fly so we're gonna say if place equal equals twelve We're gonna return

this

this and I guess it's twelve or place is equal to thirteen.

Same with the eleventh.

So I'm gonna say I'm gonna say greater than or equal to

11th and less than or equal to 13 so we need do and then we're gonna return t h OK.

Otherwise it's gonna come down here so hopefully that makes sense.

Basically there's some cases some weird cases the 11 through 13 that don't end an NDA or already or

s t.

But they fit and whatever.

Anyway this is this is done.