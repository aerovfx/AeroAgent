# AircraftAgent.cs_ AgentAction()

Let's go back into visual studio and into our agent script and we're going to add a new public override

and this one.

We want the agent action.

The first one not the one that has the extra custom action in there.

We just want this one and we can delete this which is already in there.

And let's add a comment to this one.

We want this to read.

Action inputs from vector action vector action is a list or an array of floats.

And I'll explain that in a moment.

The chosen actions and for text action this would be the chosen text action but we don't use it so I'm

just gonna say unused so Agent action is overriding a method because it's actually called as part of

the MLA agent's sort of loop.

Basically there's a loop that's always running when these agents are going and the Academy which is

this is derived from inside this academy there's a lot going on.

And one of the things it does is it calls these functions automatically each time step.

So it's going to call Agent action after it's made some decisions about the environment.

So it's going to decide OK I want to turn left or turn right or turn or pitch up or pitch down or boost

it's gonna make those decisions.

It's going to pack them into an array and then send them in that way.

So we basically in this function since we're not using text action we basically just need to convert

from those vector actions that are in float list form essentially and convert them into what to do in

terms of movement.

So I'm going to write the code and then try to explain it as best I can so the first thing we'll do

is read values for pitch and your SO if you're not familiar with airplane movement basically the pitch

is when you tilt your aircraft up or down.

So if you're flying straight ahead and you want to fly upward then you would pitch backward and the

nose of your aircraft would point toward the sky and you'd be pitching up if you wanted to fly downward

you would pitch down your is just a word for turning.

So you're turning on your up and down or vertical axis essentially.

So in the case of our airplane here if we look at here your is how much to rotate around this green

y axis.

So this is your OK.

And then this is pitch and then roll is this.

OK.

So these are the different things we're going to control so first let's read in pitch sorry pitch change

and we'll set that equal to vector action zero so in this first index we're going to have three potential

values that it could be the first value that it could be is zero.

And if vector action of zero this is the index is equal to zero then we won't take any action on the

pitch we'll just go straight forward.

If it's one then we will pitch upward so it's either going to be zero or one in this case and we'll

say up or none.

Now the way that a discrete AML agent works is it's going to pick a number from zero on up an integer

number.

So in our case zero means don't pitch 1 means pitch up and 2 will mean pitch down.

So we have to convert that.

If it does equal to we need to convert that to a pitch change of negative 1.

So we'll say if pitch change equals to then we're gonna set pitch change equal to negative 1 and this

is what happens when we're pitching down.

So that's basically just making sure that even though we're actually going to get a value of 0 1 or

2 that we convert that 2 into a negative 1 we're going to do the same thing for ya.

So your change equals vector action at index 1 and this will mean turn right or none or don't turn essentially

but if your change is equal to 2 then we want your change to be set to negative 1 and this will mean

turn left.