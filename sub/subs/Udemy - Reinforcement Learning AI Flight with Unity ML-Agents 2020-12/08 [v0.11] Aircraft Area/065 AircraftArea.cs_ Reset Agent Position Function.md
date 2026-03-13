# AircraftArea.cs_ Reset Agent Position Function

We need one more function and then we're done with the aircraft area script.

So this function is called Public void reset agent position and what this function is going to do just

at a high level is it's going to take an agent and the aircraft area and knows where all its agents

are.

And then it's going to position it back to somewhere on our race path so we'll say aircraft agent agent.

So something is going to tell this area hey place this agent at a certain place on the path or reset

it.

And then there's a bool randomize equals false.

So what randomize will mean is if randomize is set to true it's going to pick a random checkpoint to

spawn it at.

Otherwise it's going to like reset the agent position to the last checkpoint that it went through.

Now let's add a comment to kind of cement that logic in stone here.

So we're gonna say resets the position of an agent using its current next checkpoint index

unless randomize is true then we'll pick a new random checkpoint and then the agent parameter is the

agent to reset and randomize is if true will pick a new next checkpoint index before reset

now in here first thing we'll do is we'll check if randomize

so if randomize is set to true then we're going to pick a new next checkpoint at random so we'll say

agent next checkpoint index.

And that's why we declared this access or equals random range zero check points that count.

So it's going to play it's going to create a new one based on it's gonna pick one between the range

of zero and the number of checkpoints.

Now this is complaining at me because we did a private set which we do not want.

We want this to be a public set.

We'll save that.

And then this will be OK.