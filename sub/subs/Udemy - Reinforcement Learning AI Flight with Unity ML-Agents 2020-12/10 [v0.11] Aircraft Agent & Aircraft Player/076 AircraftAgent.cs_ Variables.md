# AircraftAgent.cs_ Variables

This race track is pretty cool.

Has a lot of potential but our airplane currently is just stuck in space at least its propeller spins

but it doesn't really do anything.

So time for us to start implementing the agent class.

Now the agent class is going to do a lot of stuff and so I'm gonna try and break it up as best I can

and I'm going to start off by just making it flyable.

So we're going to control this airplane and you'll see kind of how decisions made by the neural network

might control this airplane so let's go into Visual Studio and we'll go to our aircraft agent and we're

gonna start adding a number of different parameters.

Now there are quite a few more that will come but I'm gonna try and do them in order of in an order

that makes sense so that you can follow along without getting too lost.

So the first things we're gonna do are we're gonna create a header because there will be quite a few

variables in the inspector.

This one is going to say movement parameters so these are gonna be configurable parameters that we can

use so the first one is going to be a public float thrust and we're gonna set that equal to one hundred

thousand that's a float and then we're gonna do a public float pitch speed we're gonna set that equal

to 100 a public float your speed gonna set that equal to 100 and then a public float roll speed and

looks like a typo there.

OK.

And a public float boost multiplier OK.

So these all hopefully make sense.

So the thrust is going to be how much power essentially the aircraft has.

The pitch ya and roll speeds are just going to control how much the airplane turns or pitches up and

down at different you know.

Per Per update.

And then the boost multiplier just controls when we hit the boost button.

How much faster does it go.

So we're gonna go twice as fast.

That's our current setting I thought about doing tool tips for all of these but they're pretty self-explanatory

so I'm going to skip over them and save us some time.

Then after the next checkpoint index let's see there's a few components we're gonna need to keep track

of but for now we're only going to keep track of what we'll do we'll do three of them.

So components to keep track of we'll start with a private aircraft area and we'll call that area so

each agent will know which area it belongs to.

And then we're going to we need the rigid body that's going to be attached to this.

So if if a if an object and unity needs to have physics happen to it then it needs a rigid body component

and in the past you used to be able to say game object rigid body and you'd be able to it would automatically

give you that rigid body but they've kind of deprecated that code and if you try and access it I don't

think it works anymore but it's still a great variable name and is helpful.

We just have to do a special syntax to tell them.

Yeah we really want to call it this.

Just use our version of it.

So that is new private rigid body rigid body

and then we're also gonna do it a trail renderer.

So private trail renderer trail

and then we have to add some controls and these are a bunch of private variables.

So I'm gonna say private float pitch change equals zero f a smooth pitch change equals zero.

F private float Max pitch angle equals forty five.

So basically pitch changes.

These are going to be calculated based on the input from either the neural network or from our controls

as the human player.

So the pitch change in the smooth pitch change are just how much we're going to change we need to smooth

it out because if we do the way that these agents actually turn is they either say turn or not turn.

And so there's no kind of in-between.

So it looks very jerky.

If the plane just immediately goes from not turning to turning it just kind of immediately tilts and

it doesn't look very natural so we're gonna use some smoothing on this to make it smoother.

We need a private float your change and we're gonna set that to zero.

Private float smooth your change and then we.

We don't need a maximum angle for the ISO just to be clear the pitch angle.

We're gonna make sure that we never pitch up or down more than 45 degrees because we don't really want

to allow doing flips and loops and stuff.

We're gonna lock it.

Same thing with roll We're gonna lock the roll so you can't do a full barrel roll but the ya can turn

all the way around in a circle so we're not going to limit it that way.

Otherwise you'd be kind of limited to how far you can turn okay.

So then we need the change we need a private float roll change a private float smooth roll change and

a private float Max roll angle and we'll set that to 45 degrees as well and then a private bool boost

and that'll just tell us whether we're boosting or not.