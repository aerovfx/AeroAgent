# AircraftPlayer.cs_ Airplane Prefab Setup

In this video, we're going to complete setting up our airplane so that we can hook up the aircraft

player script to it.

So go ahead and open up the prefab.

And make sure you don't get either of the variance, because we want to modify the base prefab here.

And we want to start out by adding a rigid body component to this.

To type in rigid body, and then we're gonna set the mass to 500.

The drag to five and the angular drag to twenty five.

Then the freeze rotation.

We want to expand the constraints and then choose X, Y and Z.

The reason we're freezing rotation is because our script is going to.

Automatically change the rotation, we don't want physics to be changing the rotation on us because

our turning in flight mechanics kind of rely on us having complete control over the rotation.

Then we want to add a trail render.

The trail renderer is going to be a line, basically a thick line that comes out the back when we're

boosting.

By default, it is emitting.

So we'd like to turn that off.

And then we'd also like to add a material here, because right now it probably won't show up anything

at all.

We need to add a material that it will use for when it shooting out that line behind us.

So we're going to go into materials and we're going to create a new material.

And we'll call this trail.

And we're going to change the surface type from opaque to transparent.

And then the base map, we're going to edit this color.

And the color we want is white, but we want to turn down the opacity here.

So we're gonna change the Alpha down to like halfway.

And the smoothness will turn all the way down so that this isn't reflective of vapor trail for an airplane

should shouldn't be reflecting in my experience.

And then we're gonna turn on emission as well and then click on this and you can kind of turn up the

emission to this white value.

So now this trail should be kind of see through and we'll be able to add it to this trail renderer.

So go back to airplane learning and find in the trail renderer where the material goes.

And you can put that right in there.

Now, at this point, the two airplanes are going to diverge.

The two airplanes are the A.I. controlled and the player controlled.

So this one right here, this prefab, this airplane learning, this is going to be a A.I. controlled

airplane.

And we need to create our own version of it.

A new version of it for the player.

Everything about it.

Up till this point is gonna be the same, so all the capsule's colliders and then the rigid body and

the trail render, those are all the same.

But the scripts we attach are gonna be different.

So go to your prefabs and pick the original airplane learning prefab, not any of the variance, and

then do control D to duplicate it.

And one of them is going to be called airplane learning space one prefab.

We're gonna rename this to Airplane Player.

And double click that to open up the airplane player prefab.

Now, we should be able to.

Click on this airplane player at the top level and under the trail render.

We're going to add a component aircraft player.

Aircraft player is that variant of the basically variant, the wrong word that inherited class of aircraft

agents.

So it's a special kind of aircraft agent.

So that means we're gonna see all of these input bindings here, as well as all of these public variables

here in aircraft agent.

So that's right.

Here we see these movement parameters.

And then the input bindings.

We also see this behavior parameters script, which popped up.

This we are going to have to modify.

So, first of all, let's take a look at this.

It has a behavior name for our player.

We can just call this aircraft.

Well, let's call it airplane player.

I'll call it aircraft.

Got to be consistent here.

Aircraft player, and then we have the vector observation.

Well, in this case, at this point, we don't have any observations yet.

We'll be updating this.

But for now, set it to zero.

And then for vector action, it's set to discrete.

I mentioned earlier when we were coding that there was discrete and continuous.

Well, discrete is the one that we're gonna use.

This is what allows it to make choices rather than pick a value on a continuous spectrum.

Now, the choices that we need to make are dependent on the inside aircraft agent, the on action received.

Remember, we have these three choices.

The pitch yea and boost.

So we need three branches.

And then the first branch needs three options.

And that's for pitching up down and zero.

So we need three there for ya.

We need the same.

So choice choice zero is going to be.

Don't move at all.

Ah, don't change.

Your one is term one way and then two is turn the other way.

And then this one right here is going to be two options, either boost or don't boost.

So that's what these three are.

It's gonna be the same on our airplane learning.

The one that's using the A.I. to control it.

It'll have these same controls.

So regardless of whether you're controlling it or the A.I. is controlling, it has these same options.

And you can skip over the rest of this for now.

And then the aircraft player controls, you can keep all the same here.

But we're going to need to update the pitch, your boost and Porres input bindings.

So we'll do that in the next video.