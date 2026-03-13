# AircraftAgent.cs_ OnTriggerEnter()

In this video, we are going to do our on trigger enter, and that is for when we collide with a checkpoint.

So let's go down somewhere to the bottom.

Let's go after our last private function.

You make sure I'm lined up.

And we want to add a private void on trigger enter, and that's going to take in a collider called other.

This is a unity built in function that's called any time the Aircraft Agents Collider hits a trigger

object and our checkpoints have trigger objects in the center.

So this is what's going to happen when we collide.

Basically, when we collide with the checkpoint.

We want to double check that, of course, but our comment is going to say react to entering a trigger

and other is the collider entered?

And this is pretty simple in here, we're gonna say if other dot transform, dot, compare tag and we're

gonna compare the tag checkpoint.

So all of our checkpoints should have this checkpoint tag on them.

And then if we hit a trigger that has a checkpoint tag on it and other game object is equal to.

So equals.

Equals area dot.

Checkpoints.

Next checkpoint index.

Then actually shift tab that.

Then we want to say got checkpoint.

So this is just a simple test to see.

Is this, does this have a checkpoint tag on it.

And is the game object in our checkpoints list.

And does it match up with the checkpoint.

That is our next checkpoint.

And we call that same function got checkpoint as we do up in here.

Because this is what happens when checkpoint radius is set to zero.

It has to wait until you hit a trigger.

That is a checkpoint and then we call got checkpoint.

So let's go back into unity.

And we need to add this tag to the checkpoint into the finish line.

So right now it's untagged.

So let's add a tag and we'll add the tag.

Checkpoint.

We can save this now.

That didn't actually add it yet.

That just created this new tag.

So now we need to click back to here and then we need to set this checkpoint tag.

And now we're going to do the same thing for the finish line, so let's double click on this.

Make sure that we're in the prefab view and then we can set this as a checkpoint as well.