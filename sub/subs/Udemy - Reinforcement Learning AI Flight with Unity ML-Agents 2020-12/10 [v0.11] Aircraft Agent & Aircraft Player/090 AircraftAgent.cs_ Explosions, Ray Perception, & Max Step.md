# AircraftAgent.cs_ Explosions, Ray Perception, & Max Step

And since we've added a couple new ones let's go into our prefab and make sure we update this.

All right let's open up our airplane player prefab and we need to do a couple of things here.

Number one let's take a look at the air craft player script and see what these new things are.

So we have this mesh object and this explosion effect.

So neither of these are actually ready for use yet.

We need to first of all edit this so that all of these are a child of a new object.

So let's create an empty and we'll call this airplane object it's probably good will set the position

to 0 0 0 and then we can take all of these and set them underneath here and now we can use this object

as our mesh object.

So it's not truly a mesh object I guess it's more of like the airplane that's going to be hidden.

But what this allows us to do is turn this off and it will hide this plane after an explosion and then

we need to get an explosion effect so if you haven't already imported it let's go up to our assets directory

and right click and we want to import it.

Well actually I'll do it this way.

We'll go into our assets directory the downloadable assets for the course and go into the unity assets

or wherever the DOT unity packages are.

And this mosaic explosion is the one that I'm interested in so I'm going to drag this down in here and

it's going to put it under the aircraft directory particles and then mosaic explosion.

So we'll import all of these

and as soon as that's ready it should show up under particles and we can take this prefab here and we

can just drag it here under aircraft player and you can see what that looks like.

If we restart it looks like that and then by default I'm pretty sure we need to have this turned off

at will.

Will enable itself as part of the script.

So let's go back in here and then we put the explosion effect in here and then the last thing we need

to do if you remember we added this Ray perception.

Let's add that as a component here the ray perception 3D.

Now this actually comes from the M.L. agents directory I believe under scripts maybe but I'm not gonna

I'm not going to guess.

Let's let's look for it.

Ray perception.

So Ray perception 3D this code is actually pretty complicated.

I've spent some time trying to understand it fortunately they commented it very well to help explain

but this is just the how the ray cast logic works.

So you don't really need to know how this works but we're going to use it.

And I wanted to show you where it came from.

So now we can safely query for this on the object and we'll be able to get it

so let's do that really quick.

This is going to be inside initialize agent.

We're going to say Ray perception equals get component Ray perception 3D and now we can access that

and also initialize agent before we leave.

Let's add part here.

Actually let me write the code first and then we'll add the comment.

So we're gonna say Agent loops lowercase agent parameters.

So that should be a variable that's available as part of the agent class.

Dot Max step and we're gonna set this depending on whether we're in training mode or not.

So the way we know we're in training mode is by checking the area dot training mode.

And remember this is a variable that we set ourselves here.

This is a or rather we declared it this bool training mode.

So we will enable this.

This isn't necessarily part of unity M.L. agents.

This is just a helper that we're going to use so if we've declared that this is training mode then we

are going to set this value to five thousand steps.

So that'll be the max step.

Otherwise we're gonna set it to zero which zero in this case means infinity so just never stop.

So the idea is if we're in training mode we do want to stop after 5000 steps and reset if we are not

in training mode.

We just want to keep going forever.

No Limit and we'll we'll of course stop the race based on whether they've completed enough laps and

checkpoints instead.

So we'll just add a comment here.

It'll say override the max step set in the inspector and then Max five thousand steps.

If training infinite steps if racing.

Okay.

And so if you go and look hold on one moment while this updates the code

this on the aircraft player or rather this is the agent part of it it has a max step set to zero.

So we're just overwriting this value value.

So doesn't matter what you end up putting in this it's going to change it.

But we do want reset on done checks that don't don't change anything in here.

The defaults will be just fine.