# Main Menu Content

All right.

So the first thing you'll notice of course is that these are not titled What we want them to be titled.

So let's change that.

So if we click on this we go to text and we can change this to say start going to make it all caps and

then this one the quit button.

Let's make this one quit and the text sizes are the font size is twenty four and I would like for these

drop downs to have the same font size and I think we want to make these buttons a little bigger too.

So let's make them a width of three hundred and a height of 50

do the same thing here OK.

So now these no longer fit very well but we'll fix the alignment shortly and then I want to get these

looking right as well.

So the level dropdown right now let's increase this the width and the height.

So three hundred by 50 and then this one as well OK.

So now there's definitely not enough room for all of these.

So let me move this up this up.

Now we need to go in here and we need to update the label.

We will just rename this one to level four now.

This is going to be changed automatically in code.

So we don't need to worry about what we call these but just for our visual you know to know which one

we're working with Will we'll name it.

I'm going to change the font size to 24.

So it should match what's here and then I'm going to tell it to center itself

and then I think we need to change something in the template here too.

So template is whatever shows up in the dropdown actually let's just do this other label here really

quick so we'll set this to 24.

And this one is going to be difficulty

like that.

That's fine.

And then I'll center this one as well.

So what's going to happen when we load this up.

There are three default options in here.

I do not know why it just reset those but let's press play and we can see what drops down in these fields.

So if I click on this now it shows these different levels but they're kind of small so we may want to

increase the font size of these.

So the way that we fix that it has this kind of disabled or the deactivated template.

Here we can change the settings in here and that's the template that it uses for creating those extra

options.

So we probably want to leave this roughly the same and then inside here I believe it's the viewport

content item.

There's just there's so much in here that maybe it's not worth messing with.

But I'm going to at least increase the font size to 24.

I keep painting 25 accidentally and then center it and I'm going to see what that looks like and let's

just move this undo that.

Let me just move this over so that I can see what it looks like with that increased font size OK.

So they're overlapping a little bit.

So let's fix that as well.

We'll change the item label not the item label probably the item itself to be instead of 20.

Let's just make it 30 high.

And that should fix that problem

OK.

So now we can see these different options.

So let's do the same thing to our item in this difficulty dropdown.

So viewport content item and we're going to change the item to a height of 30 and the item label to

a font size of 24 and we'll center it as well so that should be good enough if you want to make your

UI look a lot prettier.

By all means do so.

This is.

I'm just making it functional for us.

So now we want to place this somewhere where it's not going to you know end up off screen or you know

be not aligned.

So we want to pick one of them and figure out where we want it to be and I think what I'll do is I will

anchor it to the bottom left corner so that all of these will definitely stack together and they'll

be on the bottom left side no matter what size side we work with.

So let's start with a quick button and we'll move it down like right here and let's look at whatever

the x position is.

And I'm just going to first of all we need to change the anchoring to the bottom left and I'll just

change this to a round number 170 and we'll just do 40 that should be OK.

And then the start button let's also do an x position of well let's change the anchor then set this

to 170 and then we need to figure out how high above this thing we want it to be.

So that looks pretty good.

1 0 5 maybe one.

So sixty above equip button then this difficulty dropdown and let's just do both of these will set the

set the anchors to the bottom left and we can change the x position to 170 for both of them.

And now we can come in and if we want to move this down we can.

So I'm going to do the difficulty dropdown and maybe like that.

So it was one hundred so sixty above that and then this one is going to be to 20.

That looks pretty good that looks aligned.

I'm just looking over here at this y position.

So this looks right.

I'm going to save it and let's try playing again and see what this looks like and then because of the

way we anchored it we can resize this and yeah it's not perfect if you had a super narrow display it

might not look right but this should look good enough including if we maximize it then it puts all of

our options down there we can see we can change these and we can click start.

Maybe you don't like it down in the bottom corner you want it in the center whatever you want to do

it doesn't bother me.

Go for it.

So that should wrap up what we need to do for creating the items in this menu.