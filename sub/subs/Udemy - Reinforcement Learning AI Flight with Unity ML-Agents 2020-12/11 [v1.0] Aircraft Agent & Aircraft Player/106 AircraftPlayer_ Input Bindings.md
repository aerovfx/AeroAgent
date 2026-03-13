# AircraftPlayer_ Input Bindings

In this video, we're going to update the input bindings.

So the new unity input system has a pretty cool way of setting up inputs for your scripts.

Basically, this input system, if we look here, we've got these four different input actions that

are going to be coming in.

We're allowed to specify what these things do.

And then it makes it easier to read those values in.

So this first input here pitch.

We're gonna add a one D axis composite.

And what this means is there will be two buttons.

One that makes it negative.

And one that makes it positive.

And those two buttons that we're going to use are W.

S.

So if you've used any sort of first person shooter controls on a keyboard before, usually the W A.

S and D keys are what are used for moving forward backward, left, right.

Well, we're gonna use W and S to control the pitch of our airplane.

The negative is going to be if you double click on this, you can type in S. so that the negative means

it will pitch down when we press s.

And.

We have this s keyboard option here.

We want to set this one to W. So type in W up here after you double clicked and then find W on the W

keyboard option.

Then we're going to add gamepad input, too, since we're here.

So if you click on this, you can do add binding.

This one's a little different because it's going to just be the left stick on the gamepad.

And if you double click on this, go into GamePad and find the left stick y axis.

So this will change the pitch.

Your input is very similar.

So we're going to add a one dee axis composite.

We'll call this a D.

Negative is a on the keyboard.

Double click on this positive is deep on the keyboard.

And then we want to add a binding.

And this will be the gamepad left stick x axis.

Boost input.

We're gonna make this be the spacebar.

So we don't need a composite for this one because it's either on or off.

We add a binding double click.

We can find.

Well, we'll just type in space up here.

And then now we've got the space keyboard for boost input and then we need an alternate here.

We need a button on the controller.

And I was going to use the B button on an X box controller.

So if you look at the game pad, you don't actually have A and B, you can specify specific buttons

for certain controllers.

But if you use a button east, it'll use like if you imagine the buttons on the controller being north,

south, east and west.

The B button is in the east position, so we can just use a button east.

Hopefully that makes sense.

So now we have these input bindings on the aircraft.

Player.

And when we.

Oh, I forgot.

Actually, let's do pause input before we go any further.

Pause.

Input is going to be.

We'll use the escape key.

On the keyboard, and we can use the start button, so at binding on the gamepad.

Start is down at the bottom.

OK.

So these buttons now, anytime they're fired, as long as the script is on here and these inputs are

enabled, it should respond to whatever the value is when heuristic is called.