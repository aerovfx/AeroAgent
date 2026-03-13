# RaceManager.cs_ Variables & Hook Ups

So the first thing we'll add to race manager will remove these and we'll add a public int num laps equals

three.

So this will be how many laps the player needs to go around this race track to finish the race.

And actually three might be too many.

Let's just do two.

And then we can increase it if we want to.

So let's add a tooltip and we'll say number of laps for this race.

And what this will allow us to do we're going to have a race manager in every level that has a race

track so we can change the number of laps per race track.

Some might be really short.

So you might want him to go around three times or four times.

Others might be really long and you only want one lap.

It's completely up to you.

Next we'll add a public float checkpoint.

Bonus time we'll set that equal to 15 seconds.

And so what this is going to be I mean just add a tool tooltip really quick BONUS SECONDS TO GIVE.

Upon reaching checkpoint so the idea with this is that if you don't reach the next checkpoint within

this amount of time 15 seconds then we'll automatically reset you to the last checkpoint that you did

go through.

So every time you hit a new checkpoint we're just going to add 15 seconds to your timer.

Next we're going to need a new serialized Bill.

So we're going to add serialize the bill and it doesn't know what that is to do control period.

So we're going to use using system.

So do this inside of brackets because we're going to add a public struct difficulty model and this is

going to show up in the inspector the serial sizable part is what allows it to show up in the inspector

which I'll show you what that means in a moment so we're gonna do public game difficulty difficulty

and then public and end model which it doesn't know about yet.

So control period and will we say yes using Barracuda model and what this will be is it's a we're going

to use it as part of a public list of difficulty model called difficulty models and this is going to

be the list of neural networks that are associated with a difficulty.

So right now our two options are normal and difficult or normal and hard and we're going to add a matching

neural network model for each one of those.

So if we open up unity

and in our desert scene we can start we'll create an empty called Race manager and I'll just zero out

the position and then we can add a race manager script to it.

And now we have the option to change the number of laps the checkpoint bonus time and then difficulty

models.

We have two different options so we're going to provide right now and the first element is going to

be normal and the neural network model for that is this aircraft learning normal that we imported earlier

and then we're going to choose one for hard and that one is going to be the hard one.

So that's how we're going to tell the race manager when you load up look up which difficulty we're using

from the game manager and then use this associated neural network model.

So what's cool about using it this way is you could train different neural network difficulties not

only for the entire game but for each level in particular if the planes need to train specifically for

a certain type of level you could have a specific neural network model for that level.