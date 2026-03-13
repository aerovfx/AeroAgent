# Heads Up Display UI

Now we're going to create a quick heads up display for our agents.

So the idea would be that in the game view we're going to have a place so like first second third down

in the bottom left corner then up in the top right.

We're going to show the time remaining to get to the next checkpoint and which lap the agent is on and

then we'll also need something that shows where the next checkpoint is.

So we're gonna have sort of an indicator that points toward the next checkpoint so let's create as a

child of our race manager Let's go in to UI text text message pro and this is going to be the place.

Text.

All right.

And then let's duplicate this two more times.

We're gonna have one that becomes the time text

and we're going to have one that becomes the lap text

all right.

Now the time and the lap will be going up in the top right corner.

So we want to be able to see all these.

And of course we're looking at this from the back.

If we hit this 2D button we'll be able to see it from the front and we can move them down generally

into where we want them to be.

If you hit the w key or you click this button up here then you'll be able to move it down.

I'm going to move it kind of down here I'm not going to get these perfect.

The goal is just to get it good enough so that we can have a decent looking game.

So time text is gonna be up in the top right.

And the lap text will be right underneath that.

So let me just make sure that these two are aligned by select both of them.

Position x.

I'm just going to set it to four forty just make sure that they're both aligned and then the font size

for both of these maybe I'll set it to 40.

Just make sure it's big enough and I'm going to justify it to the right so that it kind of comes out

from the right side of the screen and that should be good enough for the for these two pieces of text.

I'm going to just for good measure I'm going to just label this one time and this one lap so that we

can see what they are.

In this display but these will automatically be updated by code and then we have our place text down

in the bottom left corner.

So I'm going to name this zero place and it's kind of hard to see because though the rocks are including

it.

So let's go into the game view here and then we can see that it's really small.

So let's make this a lot bigger and we'll start off by making it bold and then we're going to increase

the font size to 100.

And now it's off the screen so let's make sure it's justified correctly before we go messing around

with it too much.

So bottom left justification or anchoring I guess is the right term.

And then we need to move it up so I'm going to just mess with the position y here.

If I click and drag kind of something like that let's make sure that this is aligned with the bottom

here the alignments at the bottom probably didn't even need to mess with that y can leave it like right

there and now even if this became like one millionth place we would like for it to have some extra space

to work so let's make sure the width is greater.

We probably don't want to have a million agents in the scene so maybe one hundred is a good maximum.

And then we need to make sure that the x position is in the right spot.

So something like that so then we just need to make sure that it still makes sense even when there's

a short.

So that's the right kind of format we want we're not going to support much bigger than you know 100

hundred places in this race.

If you need to go ahead and mess with it.

So now we probably don't want these to just be pure white because pure white is kind of hard to see

at the bare minimum.

I think an outline is a good idea.

So I'm going to check this outline thing and increase this to about Point 1 3.

So now we've got an outline around it and you'll notice that it updated this one too.

And that's because there's two materials that are being used here or rather there's only one material

for the two different sizes.

I'm okay with the way this looks.

I'm not going to mess with it.

I will change the color this to something kind of yellowish orange.

I'm kind of copying Mario Kart here they've got kind of that yellow color for their UI and other than

that I'm not going to worry about doing different fonts.

If you want to do different colors if you want to do you know this font is different than this font

you're going to have to create multiple text mesh pro materials to do that but that's outside of what

we're gonna do in this course.