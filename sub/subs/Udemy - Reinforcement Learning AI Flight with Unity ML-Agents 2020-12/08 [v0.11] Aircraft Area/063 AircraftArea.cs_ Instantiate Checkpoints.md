# AircraftArea.cs_ Instantiate Checkpoints

All right.

Let's create a new method.

This one is going to be private void Start.

Now sometimes I don't add comments for these Awake and Start ones just because they're so common.

Like anyone who does unity programming knows that Awake and Start our special methods but I'm just gonna

do it.

In this case I might not do it every time we do it start earthquake method in the future.

This one is gonna set up the area so the first thing we'll do is create checkpoints along the race path.

So just to make sure that everything's okay we're gonna say debug assert and we're gonna make sure that

race path does not equal no and we'll say race path was not set.

So that just make sure that we didn't forget to hook up the race path in the scene then we'll say checkpoints

equals new list game object and this is just going to create an empty list that we can put our checkpoints

in as we create them

we'll say int num checkpoints equals.

So now we need to figure out how many checkpoints to create.

So the way we'll do that is we're going to use the race path and we're going to have to essentially

get how many of these there are.

But there's not.

Unfortunately there doesn't seem to be a really clean way to just get that that that list.

This is the code that I found that works so we need it because this for some reason returns afloat.

I'm not sure why race path dot Max unit and then we need to pass in sin a machine path.

Base dot position units dot path units.

All right.

So I'm not sure why we can't just get a count of the number of points on this path.

My guess is that because I'm sort of using this sort of machine path for something that wasn't really

intended to be used for that it just is kind of missing some of the functionality that I would expect

to be there.

But fortunately I've found enough work arounds that we don't have any real issues.

So now that we know the number of checkpoints we can loop through and create a checkpoint for each one

so we'll say for int i equals zero pi is less than num checkpoints I plus plus.

So creating simple for loop and in stock inside we will instantiate either a checkpoint for Finish Line

checkpoint so we'll say Game Object checkpoint.

So we're creating a new game object here say if I is equal to num checkpoints minus 1 So this is just

sort of a test.

Is this equal to the last checkpoint in the list.

If so then we need to instantiate a game object

and it'll be the finish line prefab.

So we're just checking is this the last one.

If so then then that's the finish line.

Otherwise checkpoint equals instantiate game object

checkpoint prefab OK.

So this code just to kind of jump back out really quick.

It's gonna look for on here.

You just select one of these is it not letting me whoops

not sure why it's not letting me see.

Maybe it's because of this.

The way

oh I have to hit.

OK.

So if that happens I was in rotate mode I had to hit the W mode to bring these back before I forget

what's gonna happen.

So it's going to find the last checkpoint and set that to be the finish line.

So I actually might want to modify this.

I don't really want my finish line to start and end right here because then they'd have to immediately

make a really sharp turn.

So what I'll do is I'll bring this here think and then I can bring this up and then I'm gonna select

this first checkpoint and delete it.

By hitting this minus so now hopefully this is where I want it to be.

I'm just going to move this out a little bit this like this and then I think hopefully this will work

the way I want it to and it'll create the finish line right here and then this is technically the first

checkpoint.