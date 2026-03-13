# Fixing Snow Level Loading Bug

Now the reason that this did not work properly.

There's a couple reasons.

One we need to add the snow scene to the build settings.

So we'll go to file build settings and then we need to add this open seen the snow seen to this to these

build settings.

Otherwise you can't load this new level while the game is playing and then the other thing is in main

menu.

We need to go into this main menu canvas and we have our list of scenes here.

But the drop downs actually aren't updating properly.

So this was something I I was mistaken on.

We need to go to the on value changed and this set level actually needs to be main menu controller set

level dynamic and and what that'll do is it'll use the selected menu item.

Let's go to the difficulty dropdown and do the same thing set difficulty now that should actually feed

in the right value.

And I think that maybe before what was happening was the difficulty wasn't updating either when we changed

it.

So let's try this.

So we're gonna do snow and hard and now it's loading up.

So I should be playing against some really hard agents now in the snow

and they're just boost in like crazy.

I'm not gonna be able to catch up.

I don't think unless they crash which they don't seem to want to crash.

So probably out of luck

so there we have it.

We have a complete game here.

So you know it's got the pause menu still the pause menu works going to resume and I'm gonna try and

finish out this course so that we'll see the game over screen and then it should take us back to our

main menu where we can select Oh I might actually pass someone Oh it's gonna be it's gonna be tough

to stay ahead of him I'm already behind

then as soon as we get back to the main menu we could choose to play the dessert level again

all right.

So that should be the end of the race.

Now I can go back to the main menu and it's gonna default to these because we didn't set anything to

remember what our last selection was but now we have the dessert scene again.

So we have this fairly complete game at this point which is pretty exciting.