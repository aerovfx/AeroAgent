# ResetAgentPosition()

In this video, we're going to add a function that's able to reset an agent's position.

So this function should go at the end and it's going to be called public void reset agent position,

and it's going to take in an aircraft agent called Agent and a Boole called randomise, which defaults

to false.

And let's add a comment here.

Hopes to actually create my races there.

So it's going to say resets the position of an agent using its current next checkpoint index unless

randomise is true.

Let me actually put this on the next line.

Unless randomise is true.

Then we'll pick a new random checkpoint.

So this doesn't quite exist yet, but the idea here is that the agent is going to need to be reset at

some point during the race, either from crashing or if we're training.

We need to reset it in a random position.

Or just at the beginning of the course.

So that's what this function does.

And it needs to know the agents next checkpoint index so that it can place it back there.

Let's say it got to checkpoint three and then it crashed.

Well, we need to be able to go back to that checkpoint so it can continue the race.

So that's what that is.

And then this parameter agent is the agent to reset and randomise is, if true, will pick a new next

checkpoint index before reset.

So let's start out with this.

The first thing you'll notice is that since we don't have a next checkpoint index, we probably need

to figure that one out.

So let's do that right now.

We're going to.

Find our aircraft agent and we can clean this out.

Let's add it to the namespace aircraft,

and then we just we're not going to go into this class yet, but we're just going to add one thing,

and that's a public.

The next checkpoint index.

And this is gonna be an access or so we'll say, get set, because we're gonna need to be able to get

it and set it.

So that should at least allow us to finish this aircraft area.

Function.

So the first thing we need to check is whether randomise is true.

So if randomise and then inside here, we're going to pick a new next checkpoint at random.

So we'll say Agent Dot next to checkpoint index equals random dot range zero comma checkpoints, dot

count.

So we're going to look at how many checkpoints we have and then we're going to pick something between

zero and that top number.

After this, if block, we're going to say set start position.

To the previous checkpoint.

So to do that, we do it at previous checkpoint index equals Agent Dot.

Next checkpoint index minus one.

So for this one basically just to explain.

So the next checkpoint index means, let's say, a past checkpoint three.

If I'm the agent, then my next checkpoint index is now four.

So that's why we need to figure out what that previous checkpoint is.

Now, there's a weird scenario here where if this is zero than the previous checkpoint is negative one.

And we don't want that.

So if previous checkpoint index is equal to negative one, so equals equals negative one.

We're just going to say previous checkpoint index equals checkpoints.

Dot count.

Minus one.

So we're setting it to the last checkpoint index.

Then we're going to need a start position.

So this is the start position for this agent to be reset at.

So we say float start position.

And why would this be a float?

Well, the race path has sort of a series of path units, and we can place it somewhere along that race

path based on a number.

And that number is based on the units.

So we'll do.

Start position equals race path, dot from path.

Native units.

Previous checkpoint index, comma, and then we want to do sinnett machine path based position units,

dot patha units.

So that's going to get us a start position as a float.

Next, we want to convert the position on the race path to a position in 3D space.

To do that, we create a new vector three, we'll call it base position.

So this is the position on the path.

Equals race path.

Dot evaluate position, start position.

So it passes in this float and then it figures out where that position is.

And that this function right here returns an actual point in space.

Next, we want to get the orientation at that position.

So we'll say get the Orien Tatian at that position on the race path and that's going to be a new quote.

Ternium returning an orientation equals race path, dot, evaluate orientation.

And we want to pass in start position.

So this now gives us the rotation we want.

Next, we need to calculate a horizontal offset so that agents are spread out.

So if we don't spread out the agents when they respond, then they'll all show up in the exact same

spot and they will just kind of get blown apart, I guess.

So we don't really want that to happen.

We want to intelligently spaced them apart.

So to do that, we're going to save vector three position offset equals vector three dot right times.

Aircraft agents, dot index of agent.

So we're looking up the index of this particular agent that we're passing in right here, the one that

we're resetting.

Minus your craft agents dot count divided by two.

And then we're gonna multiply that by.

Random range nine F 10 F.

All right.

This one's a little weird, so I'm going to explain it.

Basically, we're going to figure out.

The index of the agents.

So let's say there are four.

The index of the agents will be something between zero and three.

So zero one, two, three.

That's four agents.

Then we have to subtract the count divided by two.

So we that would be two.

Four divided by two is two.

So that way you have basically anything that is positioned to the left or right is off by.

It's kind of hard to explain.

We're multiplying this sort of spacing logic by a vector that points to the right.

And it might be a little hard until we're able to visualize it.

So I'll just leave it at that.

We're also going to multiply this by a random number.

And I originally, when I first designed this, did it so that you always were spacing these 10 metres

apart.

But then I realized there was a problem.

Where if you don't randomize the start positions a little bit, then the airplanes will never experience

anything different.

And they will always fly on the exact same paths.

So that's a really interesting quirk of neural networks and I won't get into it now.

But this is necessary at this stage.

Then finally, with this position offset.

We want to set the aircraft position and rotation agent dot transform dot position equals base position

plus orientation plus or sorry times position offset.

Then we'll say Agent Dot Transform.

Rotation equals orientation.

So we're just setting the position in rotation now.

So now these aircrafts, no matter when we reset them, they should be spaced evenly apart.

So even if three were to crash at the same time, they wouldn't automatically be reset to the same exact

position in space.

And that wraps up the aircraft area.