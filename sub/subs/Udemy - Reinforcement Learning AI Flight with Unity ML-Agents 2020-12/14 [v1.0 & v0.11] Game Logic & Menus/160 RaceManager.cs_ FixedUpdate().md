# RaceManager.cs_ FixedUpdate()

Now we're gonna do.

Probably the largest function that we have to worry about.

So I'm going to go down underneath on state change and we're gonna do private void fixed update.

There's a lot of functionality that happens.

Each update for the race manager first thing we'll do is if game manager loops game state game manager

instance dot game state is game state DOT playing

we're going to update the place list every half second so rather than check literally every fixed update

which happens every point zero two seconds I think we're going to do this every half second.

So if last place update plus point five F.

So that's half a second is less than time got fixed time

we'll say last place update equals time dot fixed time.

So we need to update this or else we're going to end up just doing this check every time.

Anyway we'll see if sorted aircraft agents is no

get a copy of the list of agents for sorting so we'll say sorted.

Aircraft agents equals new list aircraft agent

put this here and then we initialize it with this aircraft area.

Aircraft agents so we're not going to sort this aircraft agents in fact we can't it's a private set

so we can't change this list.

We're going to keep our own version of it that's sorted inside race manager

and then after this if statement we're going to recalculate

race places so we'll say sorted.

Aircraft agents dot sort and for this we're gonna need a special comparison algorithm.

The reason is it's not obvious how to sort this with a simple check of their position or something we

need to check not only how many checkpoints they've passed but how many laps they've done and how close

they are to their next checkpoint.

And we need to factor in all of those things when sorting these by place so we're going to say a common

B in parentheses like this equals greater than place.

Compare come compare like that a come a b and this is a function that does not yet exist.

So we're going to have to write it but I'm going to leave it as a red squiggly line for now.

But it's going to do that comparison to see which which planes should go first.

Basically we'll say for int i equals zero.

I is less than sorted.

Aircraft agents dot count I plus plus.

So we're going go through the list of sorted agents and then we'll say aircraft statuses

of that sorted.

Aircraft agents at i

dot place equals I plus 1 so we are going through our list of sorted agents and then we're updating

that place.

And it's I plus one because the index starts at zero and we don't say that a plane is in zero place

we say that they're in first place second place third place etc. So that's why we add one

now we need to update our agent statuses.

So this is after the update the place list every half second

so outside of this if we're gonna say update agent statuses we'll say for each

aircraft agent agent in aircraft area.

Dot.

Aircraft agents

and then in here we're going to get the aircraft status we'll call it status equals aircraft statuses

agent.

OK so we're we're looking up the status of this agent we're storing it in a temporary local variable

we're going to update agent lap so to do that we'll say if status dot checkpoint index is not equal

agent dot next checkpoint index

status dot checkpoint index equals agent dot next checkpoint index status dot time remaining equals

checkpoint bonus time if status dot checkpoint index equals as equal to zero.

We're going to say status dot lap plus plus if Agent is equal to follow.

Agent and status stop lap it's greater than num laps

game manager instance Dot Game state equals game state DOT.

Game over.

OK so let's just walk through what just happened there.

So we're checking first to make sure that the checkpoint index doesn't equal the next checkpoint index

where we're updating it to set it to that next checkpoint index.

So we're we don't want to do this if they haven't reached their next checkpoint basically is what's

happening we're not doing this every single update where we're making sure that we only do it when they

reach the next checkpoint we're increasing the amount of time that they have to get to the next checkpoint

and then if they hit a checkpoint index zero meaning they hit the finish line then we're going to increase

the lap by 1.

So now you're on lap 2.

You went through all the way and then we're going to say if this is the follow Agent meaning like the

player basically and the lap is greater than num laps meaning the the player has made it through the

number of laps time then we'll do game over.

We don't want to check and stop as soon as any agent finishes the race we would like to allow the player

to finish out the race so that you know if they want to come in third or something then they can do

so

and then make sure I get this in the right spot.

So this is still inside the for each loop but it's after this update agent lap if statement we're gonna

say update agent time remaining we'll say status dot time remaining equals meth f dot Max and the first

value is 0 F and the second one is status dot time remaining minus time fixed delta time so we're going

to just update this time remaining here and if the time remaining is so small that subtracting fixed

delta time from it would go into a negative number we're not going to say that we have negative time

remaining we're just going to limit it at zero and then we're going to say if status dot time remaining

is equal to zero

we're going to say aircraft area dot reset agent position agent.

So we are going to reset this agent now that we've the time ran out and we'll say status time remaining

equals checkpoint bonus time.

So we're going to give it some more time and that's it for the fixed update function.