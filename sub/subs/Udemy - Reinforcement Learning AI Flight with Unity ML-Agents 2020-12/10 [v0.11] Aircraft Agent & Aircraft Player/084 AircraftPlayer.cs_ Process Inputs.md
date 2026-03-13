# AircraftPlayer.cs_ Process Inputs

All right.

So now we're going to override public override and we're gonna override initialize agent and we're gonna

still call based initialize agent.

So it's going to call this function first.

So we'll have the area the rigid body in the trail we don't necessarily need those in that order but

we will make sure that that still gets called.

Otherwise you're going to have problems later.

And then we will say pitch input dot enable your input dot enable boost input dot enable and pause input

dot enable.

If you don't do this it definitely will not work.

I've learned that the hard way.

Next we need to add an override.

Public override and we want heuristic.

So this is the function that allows us to feed in our own inputs into the agent action.

So basically whatever we return from the heuristic function is going to go into this vector action thing

assuming we have heuristic turned on and what I mean by that is on the airplane it might not let me

like this if I have any builders.

Let's see hopefully this works.

Yeah.

So here on this behavior parameters thing that I said we'd get to but we're still not really gonna get

to yet.

There's this use heuristic thing if you have this checked it's gonna try to call this heuristic function

and on a normal agent it's not going to be there we're not going to use it but on a special kind of

agent called an aircraft player then that method will be here and we will implement it as such.

Let's actually add a comment really quick.

We'll say reads.

Player input and converts it to a vector action array and it's going to return an array of floats for

Agent action to use.

We do not want to return base heuristic.

We want to return our own thing.

So the first thing we'll get is the pitch.

And remember that pitch is either 1 4 up 0 4 none or negative 1 4 down books down.

Now we of course are going to feed this in as 0 1 or 2 but pitch coming in from the controller is going

to be up 0 or down.

So I know this is a little confusing.

Think of it like a joystick.

There's a on a joystick on your gamepad like an Xbox controller if you press up on the left thumb stick

then it's going to give a positive value.

If you press down on the thumb stick it's going to give you a negative value.

So that's what we're actually capturing here is sort of an axis between negative one and one and then

we will convert it if we need to so we'll get that float pitch value so we're getting this from our

input now equals math f dot round because we want to round to the nearest integer.

We're not converting it to an integer it's still gonna be a float but we're rounding it to the nearest

integer pitch input dot read value float

so we're gonna set this up so that we can use the keyboard or a gamepad if we want to and it won't care

either way it's going to read the pitch input and get the value from it ya is 1 means turn right zero

means none and negative 1 means turn left so we will call this float yea value equals math.

FDR round

and we're going to pass in your input.

Dot read value

and now boost

is either 1 means boost or zero means don't boost no boost.

OK.

So this one float boost value equals math after round boost input.

Dot read value and we're gonna take in a float again even though this is a sort of true or false we're

still reading it as a float.

Now we need to convert negative 1 meaning down to a discrete value of two.

So we'll say if pitch value is equal to negative 1 F pitch value equals to F and then we'll convert

negative 1.

Turn left to discrete value to so we'll say if your value is equal to negative 1 your value is equal

to 2

and then the last thing we need do need to do is say return the new float.

So we're going to return a new pops a new array of floats.

Then we make sure they didn't mess that up and then in curly braces we can initialize this with the

pitch value the turn value flips or not turn your value and the boost value

OK so that's all that needs to happen.

So now whenever the this is the code that's acting as the agent then it's going to take in the values

from our inputs and then apply them via the agent action.

Now we need to add a little bit more code in this function.

This is actually to head off a bug that I found later on as I was recording the course so that you will

not hit this bug like I did.

So it turns out if you enable these inputs but do not disable them when the agent is destroyed then

you can have some issues.

What was happening for me was when I would finish one game go back to the main menu and then start a

new game.

Then this pause input seemed to be hooked up to some previous version of pause input.

So what we're going to do I want you to copy all of these and then come down here and we're going to

add a new on destroy method.

If you type in on destroy it'll create this private void on destroy.

You can paste this down in here and then here's a little trick if you do the space base to line all

three of these up you can hold down the old key and select all of these lines and you can type NDIS

loops don't hit enter.

Then I'll put on the new line but controls.

And then you can just pop this back and now this will properly destroy and it will stop listening to

these inputs after the aircraft player has been destroyed.

I suspect that because the input system has been told to do something then we don't actually turn off

that and the input system then it doesn't clean certain things up.

So this is definitely important.