# RaceManager.cs_ PlaceComparer()

Now let's define this place compare.

So I'm going to right click on this.

Two quick actions and generate a method for it.

So please compare is not actually going to return an object it's going to return an integer.

So int and let's give it a comment it compares the race place that is so i.e. first second third etc.

and a is an agent and B is another agent and it will return negative one if A is before B zero if equal

and one if B is before a so this place compare is what allows us to sort the agents up here or wherever

it is that we sought them.

I lost track of it but we passed this in and it will do that comparison and work with the sorting algorithm.

That's sort of default to sorting lists.

So we're gonna say aircraft status status.

So we're gonna get the status of the first agent equals aircraft statuses

then we want aircraft

status status B equals aircraft statuses B OK.

So now we have both statuses.

Now we're gonna get the checkpoint that each one of these are on.

So int checkpoint a equals status a dot checkpoint index plus status a dot lap minus one

times aircraft area dot checkpoints dot count.

So what this does is it figures out what lap are they on if they're on the first lap then it's going

to multiply 1 minus 1.

So zero times the number of checkpoints if they're on their second lap it's going to say ok 1 times

the number of checkpoints.

So let's say there were 20 checkpoints if they're on their second lap.

We know that they've passed 20 checkpoints already and then we can add the checkpoint index and that

will give us what checkpoint they're on.

So if they're on checkpoint index six of their second lap then checkpoint would be twenty six.

We're gonna do the same thing for B and I'm going to take a little shortcut here.

I'm going to copy this and I'm just going to change B status B status B OK.

That was easy.

Now we'll say if checkpoint a is equal to Checkpoint B then what we need to do is compare distances

to the next checkpoint.

So they're on the same checkpoint.

So we just need to figure out who's closer we'll say vector three next checkpoint position equals get

agent next checkpoint eh.

Now this is a function that doesn't exist yet but we will implement it dot position say int compare

equals vector three dot.

Distance a dot transformed position next checkpoint position

dot compare to and I'm just doing this on the next line.

You could do it here but it's gonna run off so I'm just gonna do it on the next line dot compared to

vector 3D distance.

Disaster.

Whoops.

I did it up here too.

Let's do distance distance.

Be that transformed.

Position next checkpoint.

Position and then I can just race all this white space and put a cone semicolon.

And then we will return.

Compare.

So this is just going to use this compare to to see which one is bigger or smaller.

Else.

So in the case where they're not on the same checkpoint we need to compare number of checkpoints hit

the agent with more checkpoints is ahead a lower place.

So we flip the compare all right.

So basically we're gonna compare the number of checkpoints so let's say one of them is at 15 and the

other one is at twenty five.

If we compare them then we would say that the second agent the one that has twenty five is actually

higher but if they're at twenty five.

The place is lower.

So they're there maybe in first place while the other ones in second place even though they have more

checkpoints so that's why we have to flip the comparison value so it compare equals negative one times

checkpoint a compare to Checkpoint b return.

Compare so that's all for the place compare.