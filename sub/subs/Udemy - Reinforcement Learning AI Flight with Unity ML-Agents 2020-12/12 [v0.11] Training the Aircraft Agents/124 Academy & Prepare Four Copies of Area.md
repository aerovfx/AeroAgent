# Academy & Prepare Four Copies of Area

Now that we have this desert area scene prefab sort of all setup we can come back into training and

we'll definitely need to create an academy object so we'll call this aircraft Academy and I don't think

this is inside the area.

OK.

Just wanted to double check.

Then we'll say 0 0 0 just to center it and then we want this to be the aircraft Academy so I just already

had typed in aircraft.

So that's why it showed up and we want to change this.

I'm going to train at 50 times speed.

I don't know that going at full 100 really helps it definitely makes it so that it's harder to like

see what's going on because it can't keep up with the frame rate 50 is hard enough for my computer which

my computer's not top of the line machine I bought my graphics card.

Like I don't know.

Four years ago or something like that.

So it's it's OK but it's not like Don't worry my machine is not insane and it seems to be able to handle

this.

OK.

If it's if it's not seeming to work or it's like really really choppy then you might want to lower this

down to go maybe 10 or something like that and then we need to worry about our reset parameter so we

need to add a checkpoint radius and it doesn't matter what we said this to we'll just leave it at zero.

It just needs to have that in order to work properly and then we want to create a few more of these

desert areas we're gonna train with four of them simultaneously so that we'll have sixteen agents going

at the same time.

But before we do that let's hide this airplane player because he shouldn't be in there.

We're not going to be flying along with these while they're training.

So the four of them will be able to train and if we want we can create a copy of this a training area

prefab but I don't know that that's really necessary we're just going to duplicate this.

I'm going to move this up above and then I'm going to duplicate this with control D so that we have

four of them and then I'm just gonna move it over here

and then this one can move down and since I'm kind of picky I'm gonna make this twelve hundred even

and make sure that these are also

by the way.

This is completely unnecessary.

It's just me being neat and tidy.

OK so now we've got four of these and they should be able to train simultaneously.

Let's see what the camera view can see.

So the camera can kind of see a little bit.

You're gonna be able to see whether things are are moving at all but let's actually view from the top

and we'll pick one of these.

And then let's just view like this.

And then we can make sure the camera's selected go to game object aligned with view.

Why is that not visual.

Oh OK.

So the problem is that the view Rustom is not visible so if we move this down low enough you see how

that showed up in the camera preview because it would go.

So that should that should be good for visualizing this in the game mode or in the in the game view

while it's training and this can probably be worth the graphic.

Oh no I'm not even gonna bother with that.

Let's just leave it perspective for now.

OK.

So we have for these ready for training and now we can go into Anaconda and actually start training.