# AircraftArea.cs_ Reset Agent Position Continued

OK.

So now outside of this if statement we're going to add a new code that says set start position to the

previous checkpoint.

OK so we're gonna say it.

Previous checkpoint index equals agent dot next checkpoint index minus one so that seems to make sense.

But what about the case where the the next checkpoint index is zero.

Well we want to we don't want the previous checkpoint index to be negative one because that doesn't

doesn't make any sense.

So we'll say if previous checkpoint index equals equals negative one then previous checkpoint index

equals checkpoints count minus one so we're setting it to the last checkpoint.

Now add this code float start position equals and this is gonna be another thing from the race path.

So race path dot from path native units previous checkpoint index Senate machine.

Path base dot position units dot path units so that'll give us our position on the path that we want

to start this at.

We need to convert

the position on the race path to a position in 3D space.

So right now what this is is it's a position along the length of the path but it's not a position in

3D space so we'll just say vector three base position equals race path dot evaluate position start position

and this base position will be the point on the line where we want this thing to start but we need to

offset it a little bit because if we spawn say four different agents that are supposed to race against

each other on the exact same spot then that's not going to be a very interesting race they're just going

to all crash over and over again because they'll constantly be spawning inside of each other.

So we'd like to spread them out a bit so I suppose we'll get to that in just a moment.

Let's get the orientation first get the orientation at that position on the race path so we'll say quit

turning

orientation equals race path.

Evaluate orientation start position and then we want to calculate a horizontal offset so that agents

are spread out

and so that's going to be vector three position offset equals vector three dot right times aircraft

agents index of agent minus aircraft Asian stock count divided by 2 F. times 10 F..

OK so this right here is a little bit hard to understand maybe but hopefully pretty simple.

Basically we have a we're calculating based on the number of agents so the count of agents and the index

of the current agent we have to figure out how far from the center it is.

So this basically just figures out how far in either direction from the line it is and then spread it

out by 10 meters each.

And then finally we're going to set the aircraft position and rotation so we'll say Agent dot transform

that position equals base position plus orientation times position offset and agent transform rotation

equals orientation now we're done with aircraft area.