# Adding Randomness

Now I want to show you something that maybe you've noticed but maybe not.

It only is super noticeable if something really weird happens with an agent.

So if the agents are acting be normal then it's fine.

I want you to pay attention to first what the white plane does here.

He kind of scoops down like that and then he kind of continues racing.

No big deal.

So I'm going to follow these guys and then I want you to see the red agent with the red agent does right

here he crashes into the rock.

OK now I'm going to play it again.

And watch for what that white agent does.

So the White agent scoops down again and then these agents look a lot like they did last time.

Let's see what that red plane does this time.

He crashes into the Rock the exact same place.

So why is this happening.

This is happening because the agents have a neural network that is fixed the neural network doesn't

have any random inputs to it to make them make slightly different decisions every time they will make

the exact same decisions every single time they go through this race.

And as long as I'm not doing anything to interfere with them the race will go the exact same every single

time.

So we need to introduce some sort of randomness into this level with this game.

Otherwise it's not a very fun game.

I'm going to switch back into a 3-D view.

So I thought about a few different ways that I could approach this.

When I first realized that this problem was happening first I thought maybe random sizing the inputs

a little bit.

So adding some noise if you will to the inputs.

So like maybe occasionally shrinking the the velocity vector so that it seemed like they were or sort

of tweaking it a little bit to seem like they were going a little bit nudged in one direction instead

of the direction they were actually going or that we would change like how far away the thing was that

they saw.

That didn't work very well for me.

For some reason.

But I did find a solution that worked out surprisingly well to make them act slightly different every

single time.

So what I did was inside of the let's see need to find the aircraft area here.

There's a spot where we set the position offset of these airplanes.

So right now they're set it's set to find a spot sort of to the right and to the left of the center

point of the checkpoint that they spawn at.

And then Space those out by 10 meters each.

So all four agents are spawning 10 meters apart in a straight line right now.

The thing I found that actually worked quite well.

I'm going to put this on the next line instead of multiplying by 10.

So they're not going to be spaced out by exactly 10 anymore.

We're going to do a unity engine dot random dot range somewhere between nine and 10 so instead of being

tent spaced apart by 10:00 they're spaced apart by somewhere between nine and 10.

So each one is going to be chosen differently and each time you start the game their placement is going

to be slightly different so let's take a look.

We've got those two things that we can look at.

One is what the white plane does.

Does he scoop down.

So let's see he does scoop down.

OK and let's follow this and see if they behave exactly the same again.

Does the red agent still crash it does not.

OK so that's what we want.

We want something where every time we play it does at least a little bit different.

They don't have to do exactly it doesn't have to be super different every time.

Maybe the white plane always will scoop down at the beginning.

I'm not sure.

Let's find out.

Maybe it won't.

This time

he still scoops down a little bit.

Not really that big of a deal.

What's most important to me is that it's not the exact same race every time.

And I think by changing values just slightly like that we'll get a very different race every single

time and then we don't have that thing where a player might notice.

Mom I'm actually racing these guys exactly the same every time this is not really very fun.

So that's that's really something that you might need to experiment with.

It might turn out that that isn't a great solution for whatever environment you're creating.

You might need to come up with something else to introduce some randomness and it doesn't have to be

like what I have it could be something where there's like a moving thing that's randomly spawning in

the middle of of course or something like maybe at the beginning of the course you have like an enemy

like a big dinosaur or something that pops its head up at random.

Maybe that would throw off the agents a little bit.

There's lots of things you could mess with that could introduce this randomness but just know that it

is important to introduce that randomness.

Oh wow that's.

I had never seen that before in this course do a fair bit of testing in your courses because you might

find that you have spawn points that are way too close to a rock or something.

So here's an example of one right here.

If I go straight ahead I won't hit the rock but if I just turn slightly then I hit that rock.

So anyway that's just something I just discovered.