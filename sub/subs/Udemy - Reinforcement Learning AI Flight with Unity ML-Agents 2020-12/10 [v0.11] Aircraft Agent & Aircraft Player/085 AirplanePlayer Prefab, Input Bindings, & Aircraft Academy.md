# AirplanePlayer Prefab, Input Bindings, & Aircraft Academy

Now this player is not yet in the scene.

We don't have a an agent that is a player yet.

So let's go back in here and we're going to create a new version of this.

That's a player.

So let's open up the prefabs directory and we're going to rename this to airplane player and I'm going

to drag this down in here and create an original prefab out of it.

So now instead of this being an airplane it's now actually an airplane player and we're gonna open this

up and we want to remove this aircraft agent's script.

So we will click on this and remove component and then we need to hold on I'm gonna undo that controls.

I need to go into the actual prefab first.

So I'm going to double click on here.

Okay that's better.

Now we can remove this aircraft agent component and for good measure let's just remove this behavior

parameters went to OK.

And now we need to add the player so the aircraft player script and then it adds its own behavior parameters.

So that was automatic.

And now what's different is we have these input bindings that we just declared.

So that doesn't show up in the regular airplane.

It does show up in the airplane player now.

So this is what we need to hook up.

We need to hook up our inputs and the way this works is actually pretty cool.

So we're gonna hit this plus button and we're going to add a 1 D axis composite and we're gonna call

this w s so we're gonna control the pitch with the W in the S Key on our keyboard.

If you've ever played like any video game that has first person shooter controls then you're familiar

with W.A. and SSD as movement controls it's basically so you can use your left hand instead of using

your right hand for the arrow keys so we're going to set the positive to be W and the negative to be

s.

So if you double click on this then you can change the path and we're gonna change it to keyboard and

let's see we want w so if we type in w up here we can click on that and then for negative double click

on this and you can probably just type in S and then find s..

Keyboard All right.

So now we have this input that is the pitch.

We can also add gamepad support.

So I'm gonna do that now.

I will click plus you can go add binding and if you double click on this you can go to for the path

and back out here go into gamepad and you can do the left stick.

Why.

So what this will do is it'll support using the left joystick on your gamepad whether you're using an

x box controller or I think they also support PlayStation controllers right now and more controllers

are supposed to be accepted in the future but you kind of get the idea of how this works.

You pick something that controls the pitch will do the same thing for ya.

So yea is the turn value so we're gonna do a one day axis composite.

This one will be called a D.

And let me double check.

I can't remember exactly the.

Let's see.

So negative value for the yaw is going to be turn left.

So we want that to be a so let's set this to keyboard a

and then positive to be D.

Keyboard D and then we can add another binding.

And this is gonna be the left stick again on the gamepad we want left stick.

X So this is the x axis on the gamepad not to be confused with the X button.

Or in fact the Y button on the gamepad.

These are the X's on it.

Boost for boost we're going to use the spacebar so we can add a binding for the keyboard and we just

need to find spacebar in here

and then we're gonna add another binding and on the gamepad it's going to be the B button.

I've been playing a lot of rocket league in the rocket league.

The B button is the boost button so.

Oh right.

OK so here's the thing with these generic controllers rather than have a b x and y like it is on the

X Box controller.

It's different on a Playstation controller.

They don't call it a b x and y I think it's circle cross triangle and something else square.

And forgive me I'm not a playstation owner.

So what we want is button e so e is going to equate to the B button on my x box gamepad and north would

be the top button.

W would be the left button you get the idea and then for pause we're just gonna use the escape key for

keyboard so I'll double click on this and we'll use keyboard.

I'm just gonna type in escape OK.

And then we need to add a binding for the start button and we want gamepad

start.

See if I can find that I'm going to just type in start.

Oh boy there's a lot of options there.

Let's see if I can find it.

Start.

OK cool.

So now these input bindings should be hooked up so that when we have an airplane player in the scene

it should work.

Now there's one thing that will probably mess up but I'm gonna I'm gonna see if I let it mess up and

then we'll fix the problem.

So I'm gonna make the console visible.

The only warning we're getting is something that's part of the MLA agents scripts directory.

It's just saying that this use heuristic is never assigned to and will always have its default value

false.

You can ignore that.

It's OK so let's say we do need to.

Now that I'm thinking of it we do need to turn on this use heuristic thing so that it knows what to

do

let's save the scene and we do need to put this under desert area.

So I'm going to delete this.

Open up the prefab for desert area and I'm going to disable this airplane and I'm going to add an airplane

player to the scene and I want to make sure I'd put it somewhere where he's not going to immediately

crash into the wall.

Let's see.

I'll put it back here and you can see the trail renderer there actually.

It doesn't look very bright so we might have to go in and fix that but we will see how it works.

So we'll come back out here.

I'm going to save it and then I'm going to hit the play button and I'm guessing I'm going to get some

errors in the console.

Yep.

So no reference exception object reference not set to instance of Object.

So what's it complaining about.

Agent line two seventy nine.

On enable.

Well let's figure out what that is.

I think there's a few things that I forgot to do so let's figure out what's on here.

Huh.

So this is in the agent's script.

It's trying to access the Academy for the first time and we don't have an academy in our scene.

So we're going to add an academy so at the top level not inside of the desert area.

We're going to create an empty and we'll call it aircraft Academy and I'd just like to zero out the

position and then we'll just add an aircraft Academy.

All right and then that should fix that problem.

The other problem I noticed was that you couldn't actually see the airplane when it started.

So let's see if we f the Where's the main camera.

Main cameras up here so let's see if we can move it back okay.

So now you'll be able to see it.

It won't follow the airplane just yet but you'll be able to see it so I'm going to save it and we'll

hit play again

okay.

And now we're getting a new air.

This is the area that I was expecting to get.

So we'll hit play again and you'll notice we got three hundred and ten of these.

So clearly this is happening every time step.

It's happening over and over again and it's always good practice to go up to the first error message

not the last one because you never know if something else is causing it this error message you'll probably

hit more than once when you're working with MLA agents says vector observation size mismatch.

In continuous agent airplane player was expecting one but received zero all this means it's actually

pretty simple really is inside your agent the behavior parameters are saying that we're going to observe

a value but we are not observing any values yet so I suppose it's probably time to start talking about

this.