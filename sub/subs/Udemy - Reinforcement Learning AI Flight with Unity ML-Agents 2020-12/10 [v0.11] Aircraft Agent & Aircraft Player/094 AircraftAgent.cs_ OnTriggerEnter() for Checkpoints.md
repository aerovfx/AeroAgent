# AircraftAgent.cs_ OnTriggerEnter() for Checkpoints

Now we're gonna add a new private function here.

I've been trying to keep these kind of organized.

No I'm not doing a great job but I'm at least keeping all the public methods together and all of the

private methods together I think.

So we're going to add a new private method and we might as well add it at the end.

So we're gonna add a private void on trigger enter and it should come up as a suggested method here.

This is kind of a special function in unity.

It's called any time the rigid body attached to this.

This transform this agent is going to go through a trigger.

So basically any time it goes through our I'm going to regret clicking on that.

It's rebuilding the code.

Okay.

So anytime it goes through this trigger you notice that this is checked as trigger then it will call

this function automatically for us so let's just add a comment here.

React to entering a trigger and what other is it's the collider entered

now inside here.

It's pretty straightforward.

We're going to say if other dots transform dot compare tag and we're gonna compare it to checkpoint

and

other game object is equal to area dot checkpoints

next checkpoint index then we'll say sorry we're we're going at the bottom here we will say got checkpoint

so we'll call that function that we declared earlier.

So basically we need to set something up so that the checkpoint is tagged as checkpoint so that we can

compare tags.

So let's go back into unity

and we need to add this tag to the checkpoint into the finish line.

So right now it's on tagged.

So let's add a tag and we'll add the tag checkpoint and we can save this.

Now that didn't actually add it yet that just created this new tag.

So now we need to click back to here and then we need to set this checkpoint tag and now we're going

to do the same thing for the finish line so let's double click on this to make sure that we're in the

prefab view and then we can set this as a checkpoint as well.

So now the agent should be able to find these checkpoints just by running through them.

So it makes sure that it hit a checkpoint and that the object that the check that the checkpoint was

was the next checkpoint.

So it doesn't just automatically update no matter which checkpoint you go through we have to go through

the correct checkpoint.