# Behavior Parameters

So behavior parameters control the behavior of your agent and they're particularly necessary for non

human controlled agents.

So what happens here.

There's a behavior name and the behavior name basically will match up with some configuration files

that we'll get to later.

The vector observation is basically what does the agents see in the world around it.

It could use a camera but we're not using a camera in this.

It could use a distance to an object and in that case a distance would be a single float.

It could use a direction to something in the scene.

That would be a vector 3.

It could use a rotation that would be a and so for floats.

Essentially this is passing in a list of numbers that means something to the airplane.

Right now we're not doing that so we can just set this to zero.

We'll come back to this and we will do something about it.

The other thing is vector action so vector action we've talked about before vector action is close agent

inside of aircraft agent.

It's this.

So it's basically the settings for how many different indexes will we have in our case we have three.

We have one for pitch.

We have one for ya and one for boost.

And how many different options are there.

Per index.

So we have three options for index 0.

We have three options for index 1 and 2 options for index 2.

So remember those options are up none or down turn right.

None or turn left or boost or don't boost.

So that's what we're setting here.

So what we need to set we are using discrete so discrete means it's gonna be 0 1 2 3 et vs. somewhere

between negative 1 and one which would be called continuous.

If you want to learn more about that check out the documentation for unity AML agents we are only using

discrete right now.

So what we need is three branches branch 0 is 3 branch one is three branch two is two.

So this one is boost.

This one is your.

This one is pitch and model.

We don't have a model yet.

We haven't trained a neural network so we can't fill this in.

Meaning it currently can't run on its own without it doesn't have it doesn't have a brain essentially

but we are going to control it ourselves.

So we don't need a model just yet.

And we are clicking on this use heuristic.

So now that we have this setup properly we should be able to back out to our scene and now I think it's

going to work.

All right.

No errors.

And when I use my keyboard keys it's working so I can pitch up and down and I probably lose it.

I doubt I'll be able to go up there is so I'm able to do all these things.

And then if I let's see if I can.

OK.

It's really hard.

You can see why you'd want a camera actually following your agent.

We'll do that in just a sec but let me play again and then I'll just test the boost button and make

sure that that's working as well.

All right.

I'm going to hit boost.

And now you can see the trail render and he's going super fast.

OK so the inputs are working now which is great and hopefully I have a good idea of how the agent is

controlled with just a list coming from an array.