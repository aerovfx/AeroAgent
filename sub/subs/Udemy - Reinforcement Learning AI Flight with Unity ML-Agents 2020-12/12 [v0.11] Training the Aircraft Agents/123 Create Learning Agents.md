# Create Learning Agents

Now we need to create some training agents.

So if you look inside of the desert area we have the airplane player and then we have this airplane

and the airplane does have the aircraft agent script on it.

So this we can use to turn into our airplane learning sort of thing.

I'm going to just rename this.

Actually let's rename it down here to airplane learning

and then we'll rename it up here as well and we want to go into this agent and make sure that it is

up to date with everything it needs so the behavior parameters on this are not correct.

It's looking for a vector observation of space size 1.

Well we want this to be 61

so these are all of the observations.

This is where it knows about what observations it has

and then it needs vector action branch sizes.

So if you remember in our agent action we're using index to zero index 1 and index 2 and the first one

can be three different values up down or none.

Second one can be turned right turn left or none and then the third one can be there boost or not boost.

So we need those three branches and we need three three and two so and then make sure to leave.

Use heuristic blank because we want this to be controlled by either the training code or the neural

network model that will feed in once we have that we leave Max step at 0.

We set this reset on done.

Keep that checked.

We want our decision interval to be four and what this means is only make a decision every four iterations

but then do that thing four four steps so that it's not being asked to like Hey should you turn or pitch

up or whatever.

Every single time step it's every four.

This is kind of common practice and reinforcement learning from what I've seen then down here we can

leave all of our movement parameters the same.

And we need to get the mesh object and the explosion object in here.

So we did this for the player but we haven't yet done this in airplane learning so let's create a new

empty.

And what do we call it an air plane player.

Let's take a look.

So we had airplane object and then we had the mosaic explosion.

So we need both of those so we'll call this airplane object and then we will move all of these underneath

it and then we need to get our uh particles mosaic explosion and drag this in here

and then we can turn it off by default.

So now we can go up to this and we can feed those in.

So we want to get the airplane object into the first one and then the mosaic explosion into the explosion

effect.

So now these should be all hooked up.

It won't use the object in the explosion during training but it will use it during the actual race.

Once we get to that stage.

So it's best to just set that all up.

Now to wrap up the airplane learning prefab we want to do just a couple more things.

So one is to set the behavior name on our behavior parameters.

So this one will be aircraft learning and this is going to match a couple other places in our configuration

files.

So make sure that you spell this correctly with a capital A and a capital L no space in between them.

So aircraft learning just like it is here then we need to add a ray perception 3D so I had already typed

in Ray.

Here we want the ray perception 3D not the tutor's one and this is because the agent in its observations

uses that Ray perception 3D right here.

So if we don't have that hooked up then we're gonna get some error messages when it tries to observe

the environment.

And then there was another thing in here that's pretty important and that's collisions.

So right now on our on collision code on collision enter we have this logic that says if it's not another

agent then collide.

Well right now the right here the agent is not tagged.

So we want to make sure this is tagged as agent.

Otherwise these planes are going to collide with each other.

So we can come in here and if you don't we don't already have the tag from before you can add the tag.

You make sure you click the plus you go to agent and then you go back to here and then you add the tag

agent and now we just have to create a few more of these.

We want to go into this prefab first we'll go into the desert area first let's make this visible.

So if we zoom in on it we can see it.

And then I'm going to create a couple more of these so I'm going to duplicate it in here and I'm gonna

call this airplane red

OK.

And then I'm going to move it over to the side and there's the trail renderer showing up.

That'll go away eventually it just kind of it's a weird it's the way it shows up in scene mode.

It's kind of weird the trail render shows up but we're gonna make this have a different color so let's

go into our materials and we can sort of zoom in on this and change the color here.

You don't want to do this in prefab mode because then it'll change this one to read as well so we do

it in the just in the area and then we can go into prefabs and then we can drag down airplane red as

a prefab variant which means that almost every change that we make to this original prefab will get

will be set on this one with the exception of the color that we just changed for this variant.

So now we're going to duplicate this again

and we might as well duplicated a third time because we're going to have another two.

So this one will be white

and this one will be blue so let's move the white one over and the blue one over

OK.

So now at least we can see them all.

This won't be where they spawn remember our code will spawn them automatically but we can at least visualize

them here.

So let's go ahead and do the same thing for the materials on this one.

So white

I need to zoom in a little bit to see the landing gear and then the blue for this one

OK.

And then we just need to make prefab variants out of these others so we'll go into prefabs and we will

drag down the white one create a prefab variant and then the blue one and create a prefab variant and

you can tell the difference.

These little boxes here show up a little bit different than the original prefab and it also shows variant

in the name when it's selected.

So now we have the agents that we need for training.

Now our player is also yellow which means when we when we actually go into play mode will disable the

yellow airplane.

And then during training we'll keep the yellow airplane going so that we can have four agents training

simultaneously.