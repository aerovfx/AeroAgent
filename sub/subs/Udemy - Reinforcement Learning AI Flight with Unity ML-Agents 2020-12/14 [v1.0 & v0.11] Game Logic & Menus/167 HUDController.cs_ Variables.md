# HUDController.cs_ Variables

Now let's go into our code for this.

I'm to make sure I save this before a switch out and the code we want to start editing is the HUD controller.

Now we already have this one part here that's the follow Agent but we've got a lot more to add.

So within the public class HUD controller let's create a new public text mesh pro you g you.

And it doesn't know what that is yet.

So let's do controlled period and you can hit enter and it'll add that using team PRO UP THERE AND THEN

WE'RE GONNA DO place.

Text

and we can add a tooltip for this and this is going to be the place in the race e.g. first.

Now we need public text mesh Perot you gooey time text and this is going to be tooltip tip the.

Let's see it'll be seconds remaining to reach the next check point e.g. time nine point three.

Now we're going to add a lap text

like that and we'll do a tooltip current lap e.g. lap two.

Now we need to do the checkpoint icon.

So we'll do public image checkpoint icon not image conversion on a public image and I guess it doesn't

know what that is so we'll do control period and we want to use Unity engine UI OK.

So now it knows what an image is will add a tooltip

the icon indicating where the next checkpoint is

and then the last one is public image checkpoint Eero

and the tooltip will say the arrow pointing toward the next checkpoint.

So that should be it for the things that we need to hook up.

And now we need to just add a couple more variables here.

So we're going to need a public float indicator limit and set this to point seven f.

Now I kind of struggled with how to describe this but here's my best attempt at it.

It's basically the screen is going to have a limit on it.

That's sort of an oval shape for where we want this.

This indicator to go so we don't want it to go all the way out to the top corner of the screen because

then we couldn't see the arrow pointing if it was in the top corner of the screen we couldn't see the

difference between the arrow pointing sort of up over here or over here.

So we want to have some sort of limit to say that this indicator only goes out to a certain point and

then it starts pointing in that direction.

So that's what this is.

It's the point seven just indicates that it's sort of 70 percent of the way to the edge so it's at a

tooltip that says At what point to show an arrow toward the checkpoint rather than the icon centered

on it.

That's another thing I kind of glossed over.

Basically if the that oval that I talked about once this pops up

is something where if it's inside of that Oval we don't need an arrow pointing toward it we're just

gonna lay this right on top of the center of that checkpoint.

Now we have this follow agent here.

So we're going to add a comment for this the agent.

This heads up display shows info for and this is where you're just going to change this from internal

set to just set.

Technically that's correct but this is shorter and then we need a private race manager called Race manager

and that's it for the variables that we need at the top of this.