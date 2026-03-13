# AircraftPlayer.cs_ Follow Camera, DecisionRequester, & Test Flight

In this video, we're going to finish setting up our airplane player and then we're going to try and

fly it.

So if you have your airplane ready to go, all of your input bindings are setup, then you can hop back

out to the main scene here and we want to go into the desert area prefab.

So in the prefab mode right now, we have this airplane.

But this is not the airplane player.

Remember, this is the one that we're gonna be turning into the agent.

So let's disable this for now.

And then let's add an airplane player in here.

My course actually goes in this direction, so I'm going to move it over here so that I can test it.

And I just hit the key to switch into rotate mode and I hit the control key or hold the control key

that I can sort of lock it so that it's at a 90 degree angle there.

So this airplane has plenty of space to start flying.

And I want to try playing it.

So let's hit play.

All right.

Well, that's kind of cool, but it's not doing anything.

So there's two issues here.

The first one is that our camera is not actually centered on it.

This is the main camera of the scene.

It's it's in my case, it was pretty close to where it should be.

But that wasn't actually.

It wasn't gonna follow the airplane, so let's add a Senate machine, create virtual camera.

And then what that does is it places a special component on the main camera.

And then we can tell it to follow and look at this plane.

So we're gonna do.

Airplane player.

And change the follow.

And the look at to that, and now you'll see that this camera has moved to be right behind this airplane.

Then also go down and let's make this so that it's negative.

Negative 15.

OK.

Doesn't want me to do that.

So I'm going to just drag this manually.

Not sure why it's not letting me do that.

And then I'm gonna move.

Why up?

Like, probably three.

Something like that.

And then we want to set the yard damping to one.

All right, so now if we look in the game view, we can see this is what it looks like.

If we if you want it to be higher up or lower or something like that, you're welcome to experiment

with what you think feels good.

But I'm just going to leave it roughly right there.

And then we can try pressing play again.

All right.

Well, the camera's in the right place, but it's still not flying.

I'm doing this on purpose.

By the way, I in the past, other students have had a lot of trouble getting stuck at this point where

the airplane seems to be or it should be flying, but it's not flying.

So I just wanted to intentionally go through this.

So the first thing you'll notice is this message that says couldn't connect to train around Port five

thousand four using API version one point zero point zero will perform inference instead.

This is actually good.

This is not an error that you should be concerned about.

It's saying that there's no trainer attached to this right now, that it's just going to try and use

inference on any learning agents in the scene.

Well, yeah, we're not training.

So this makes sense that this would show up.

So that's perfectly fine.

What actually is happening here is none of these scripts are being called aircraft agent.

Let's see.

Go into scripts and aircraft player.

Sure.

And the way you can test that is you can actually set a debug breakpoint.

So let's go into heuristic.

Now we can set a breakpoint right here.

And then we can attach to unity.

And what this will do is it will stop on this line of code when it's called.

So if this heuristic function is being called the code or the debugger will stop right here.

So that's how we can test to see if anything's working at all.

So if we go into here and we press play.

Ideally, we would want that heuristic function to be called.

But as we'll find out.

It's not it's not being called so.

Turns out the reason why this happens is I'm going to go ahead and stop debugging and I'll press play

again to stop this.

You need a decision requestor on an agent.

So if it's just sitting still and doesn't seem to be doing anything, making any decisions or anything,

go into the prefab actually like that.

So I am in the airplane player prefab.

Scroll down to the bottom after your aircraft player script.

Add a component and find decision requestor.

You need to add this, because if this is not on here, there's nothing that's telling it to take new

decisions.

So what it's doing here is it's saying every five steps make a decision.

So it's going to read in the observations, which we haven't yet coded yet.

So if there were observations, we would read those in and then it would feed those into the neural

network and make a decision.

Or in our case, it's going to check the heuristic function for what to do next.

So that's every five steps.

And then it also takes actions in between decisions.

You might be wondering why it's every five steps.

Well, every.

By default, it does at every point.

Zero two seconds.

So one step is point zero two seconds.

And that's actually specified in the project's settings under time.

It's this fixed timestep point zero two.

So if you make a decision every five steps, then that's every point one seconds.

So making a decision even more frequently than that, you can imagine that every point zero two seconds

would be kind of overkill for making new decisions.

You haven't even moved the plane very far.

So that's why we're doing that five step gap.

And then it still takes actions between decisions.

So it's still applying those those decisions.

Each step.

So now that we have this decision requestor on it, it should work.

So let's press play.

And now your plane should be working.

So you should be able to fly it around and you can use the W, A, s and D keys to control your pitch

and your your.

And then you can use the spacebar to control the boost.

So give that a try.

I know it's really quite challenging to control this thing, but, you know, I know that everyone has

a keyboard.

So having keyboard controls makes a lot of sense from creating a course.

So then I'm going to press play again and I'm going to show you that now if we have this attached to

unity.

Then we can press play and that heuristic function is going to be called.

See, so this means that it is indeed working and that the heuristic functions being called and you'll

find that actually the on action received function is going to be called as well.

So if I set another break point and hit continue, it's going to go right here.

And then you can see that the vector actions that are passed in are zero zero zero because I'm not actually

flying or doing anything.

So that should give you an idea.

Obviously, if you keep hitting play, it's going to keep hitting these lines because it does it over

and over and over again every step.

So if you're done looking at this, you can press stop.

It won't stop your game.

It'll just stop debugging.

And then you can go back to flying.

So I just wanted to show you that because that was that has been a sticking point in the past at this

point.

I suggest that you try flying through your course and see if you can make it all the way through.

If it is extremely difficult or even impossible to navigate certain parts of the course, I'd recommend

that you change those now.

Keep an eye out for any places where your checkpoints are kind of digging into the sand or touching

a rock or something like that, because those could be spots that your agents could get stuck on.

And while we're gonna train.

So that the airplanes can start at any checkpoint.

It could be you know, it'll learn most of the time, but there could be one particular checkpoint that

it always dies on.

And then that could really slow down training so or prevent training from working altogether, I should

say.

So just keep an eye out for those.

This one's a particularly tricky one, but I'm going to leave it in and we'll see how it how it does

with training.

But anytime you've got sort of a challenging obstacle there, that's a there's a risk that your agents

won't be able to properly navigate the course.