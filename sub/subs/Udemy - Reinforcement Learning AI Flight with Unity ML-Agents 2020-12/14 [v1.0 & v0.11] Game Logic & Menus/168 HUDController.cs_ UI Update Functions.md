# HUDController.cs_ UI Update Functions

So let's get rid of these functions here and we're going to start creating our own.

The first one we need is private void Awake and here we're just going to say race manager equals find

object of type race manager.

So that's all we need to do in a week.

We just need to get that race manager and now we're gonna do a private void Update and inside of update

we'll say if follow agent does not equal no

update place.

Text update time text update lap.

Text update arrow.

Now these are all functions that we're about to write and I'm going to generate them in reverse order

so that they show up sort of chronologically.

Hopefully this makes sense in a moment.

So I'm gonna do.

Control period here and generate the method control period.

Enter.

So see it automatically puts it right underneath this method.

So I'm I'm making them go in order by doing this control period.

Enter out of order.

Okay.

Or in reverse order I should say.

So now we've got all these functions that are going to be called Inside the Update method so the place

text we're going to say string place equals race manager get Agent place and we're gonna pass in the

follow agent and then place.

Text text equals place.

So that's why we wrote all these functions and the race managers was so that we could call them from

the heads up display now and update time to say float time equals race manager to get Agent time follow

Agent and we're gonna say time.

Text dot text equals time space plus lap sorry lap.

I'm looking at the wrong thing time to string zero dot zero and what this does is it formats the number

that's coming in which is basically a seconds but it's it could be like three point 2 5 4 1 6 seconds.

So we want it to kind of truncate it so that it only says like three point two

and then the lap text we're going to say int lap equals race manager dot get Agent lap we'll pass and

the follow Agent

and we'll say lap.

Text don't text equals lab space and then plus lab plus a divided by sign plus race manager num laps.

So this is going to show something like two over three laps.

And then update Arrow is a little more complex

so that's going to start off by we'll just comment this add a couple comments first so first we're gonna

find the checkpoint within the viewport

then we're going to do position calculations and then we will update the checkpoint icon and arrow and

let me fix that so these are the different things we're gonna do in this function find the checkpoint

within the viewport means if the checkpoint is visible then we're gonna find the position on screen

if it's not visible we're gonna have to find sort of the position off screen so but it's all relevant

to the viewport position then we have to do some calculations then we just have to put it in place.

So here's how this is going to work we'll do transform next checkpoint equals race manager get agent

next checkpoint and we're gonna pass and the race manager on.

Sorry we don't need the race manager we can just pass in the follow Agent

then we need to say vector three viewport point equals race manager dot active camera world 2 viewport

point and we need to pass in next checkpoint dot transform dot position so this gets us a based on where

the camera's pointed what the viewport point is from the position of this checkpoint.

Now we're gonna add a boolean called behind camera that determines whether the the checkpoint is behind

the camera or not.

So we're gonna do viewport point dot Z is less than zero.

So that's how when this equal sign when this returns if Z is negative then it means that the thing is

behind the camera

and then we say viewport point dot z equals zero.

So we're not going we're gonna still display this in front of the user of course but we want to know

whether this is behind the camera or not so here are the calculations we need to do.

Vector 3 viewport center equals new vector 3 point 5 f point 5 f zero F so this is the center of the

viewport in terms of from 0 to 1.

It is halfway in the x and y and then Z doesn't count vectors.

Three from center.

So this is going to be a vector from the center point to the viewport point.

So equals viewport point minus viewport center.

Now we need a float half limit equals indicator limit divided by two F.

So this indicator limit remember we set that to point seven.

We need to know what half of that limit is in order to calculate our vectors properly because we're

coming from the center of the screen.

And then we have a bool show arrow and we're going to default this to false.

Now we need to kind of split our logic based on whether we're behind the camera or in front of the camera.

So if behind camera

then we'll say if it's right now if we'll say limit distance from center

viewport point is flipped when object is behind camera so that's kind of what I was talking about earlier.

It indicates that there is a that it's behind the camera with a negative z.

But for some reason the way that it works that kind of flip the point I don't know we just work with

what we got.

So we say from center equals negative from center dot normalized times half limit.

So this is going to pick a point on screen based on where it is behind us and then we'll say show arrow

equals true because it's def.

It's definitely going to need an arrow pointing to where it is if it's behind the camera.

Else if from center magnitude is greater than half limit.

So if it's if it's outside of this sort of Oval on the screen then it's going to point the arrow toward

it so we'll say limit distance from the center from center equals from center dot normalized times half

limit and show arrow equals true in any other case we don't want to show the arrow at all and now down

here check point arrow dot game object dot set active to whatever value show arrow is set to.

So we're either going to hide it or we're gonna show it then we'll say check point arrow dot wrecked

transform dot rotation equals attorney in dot from to rotation vector three dot up from center.

So this will rotate our arrow around to point in the correct direction and then finally check point

icon dot rect transform dot position equals race manager active camera viewport to screen point from

center plus viewport center.

So what this is doing is it's getting our active camera.

It's converting a viewport point to a point on the screen and the viewport point is that from center

position and we add on the viewport center.

So this will place it on our screen.