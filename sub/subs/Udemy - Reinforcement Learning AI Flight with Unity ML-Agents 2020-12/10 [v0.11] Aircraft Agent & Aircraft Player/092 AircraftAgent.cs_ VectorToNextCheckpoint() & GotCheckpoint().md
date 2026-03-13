# AircraftAgent.cs_ VectorToNextCheckpoint() & GotCheckpoint()

So let's implement these two methods.

So I'm going to implement this vector to next checkpoint one first so we'll go to quick actions generate

method and this one will add a comment for it.

Gets a vector to the next checkpoint.

The agent needs to fly through and it returns

a local space vector

and this is going to you can remove this part.

We'll say vector three next checkpoint there.

So this is the direction to the next checkpoint equals area dot checkpoints.

So we're gonna get the checkpoint that is representing the next checkpoint.

Index and then we'll get its transform and then it's position.

So we have the position of the next checkpoint.

We're going to subtract the position of the agent.

So transform dot position so that gives us a vector that goes from the agent to the next checkpoint

then we're gonna create a new vector three local checkpoint dir and this will be basically we feed this

into a function that's transform Di inverse transform direction.

And what this does is it transforms a direction from world space to local space so this gives us a more

relative direction and we'll say next checkpoint DIR dir.

So that's going to convert this and it looks like I have a little typo there and then we will just return

that value

case so that's all there is to the vector to next checkpoint and then we need a got checkpoint one so

I'm going to do control period this time and generate this method and we will let's add a comment first.

And we'll say called when the agent flies through the correct checkpoint

and we'll replace this.

And the first thing we needed to do in this case the next checkpoint was reached so we want to update

that.

So that's pretty straightforward.

Next checkpoint index equals next checkpoint index plus 1 then modulo area dot checkpoint stock count.

So we're just making sure that we don't go over the number that are actually in this list and then we'll

have some special logic if area dot training mode.

We're going to add a reward of ADD reward point five F and we'll say next step time out equals get step

count plus step time out so we'll update that time out.

So we only give a half a point every time we go through one of these checkpoints and we've got quite

a few of these checkpoints in the level we've got about 20 of them.

So if it successfully makes it all the way around the course then it's going to get about 10 points

which kind of breaks my rule that I said earlier of trying to keep it between negative one and one.

But I found that this training seemed to work pretty well.

It's really critical in the first stage to make sure that it gets at least one point meaning it got

through two checkpoints that means it probably wasn't a fluke.

But then beyond that it seems to work just fine.