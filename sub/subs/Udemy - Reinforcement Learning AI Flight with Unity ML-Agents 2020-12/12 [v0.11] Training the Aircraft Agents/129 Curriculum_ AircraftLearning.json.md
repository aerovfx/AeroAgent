# Curriculum_ AircraftLearning.json

Next we're going to create our curriculum file.

So make sure that you are in your config folder under curricula aircraft so that directory that we created

earlier and then we want to create a new text document and this one is going to be called aircraft learning.

Got Jason.

And make sure that the capitalization and spelling are correct for this and that it doesn't have a dot

t t on the end or something like that.

Then we want to open this up.

I'm going to openness in my visual studio code and this is a pretty short file.

Start it with some curly braces like this.

And then the first thing we want to create is measure and make sure your formatting is correct.

Because Jason is kind of picky in how it formats things.

So we want quotes double quotes like this around measure and then reward is the type of measure we want

to use.

So there's a couple of different kinds you can use.

One is progress and one is reward.

There may be another one but those are the only two I'm aware of.

Progress seems to be sort of a percentage of your training and reward means pay attention to what the

average reward is then the next one is thresholds

and these are the points at which we're going to increase the difficulty.

So the thresholds we're going to use are one point zero.

So after the average reward is won and if you remember the positive points that we give to the airplanes

as they fly are half a point per checkpoint reached.

So after two checkpoints have been reached we'll be we'll have a total positive score of 1 but we're

also taking away points for each time step.

So you end up getting you'd probably need to get at least three checkpoints to possibly get one point

zero or higher for your average score then the next threshold will be two point zero then four point

zero then six point zero and basically each time we're going to make it slightly more difficult and

force it to get further in the course before we'll make it difficult again.

If you could make this 1.0 1.0 1.0 1.0 or whatever values you want you could make these negative if

you like but these you're just going to have to experiment with if you're building your own project.

I experimented in these seemed to work pretty well so then a comma and then the next line we're going

to do Min underscore lesson underscore length

and that's going to be 100 so that just means we have to pass at least 100 lessons and that's across

all agents not like 100 updates.

I think it's since we have 16 agents training simultaneously you know one hundred divided by 16 whatever

that number is is how many lessons need to happen before we increase the difficulty assuming the average

reward is over the next threshold

then our next one is signal smoothing and we'll use true and I'm pretty sure what signal smoothing is

is it's like if you look in your tensor board when you smooth things out it's less jagged.

So there might be a time let's say in this training this orange one right here where I crossed over

the threshold of six here but clearly this thing was not on track.

It's not actually getting six very much it it might have jumped up over that threshold very briefly

and then it drops back down if you do smoothing then it doesn't allow it doesn't pay attention to those

huge outliers it's more of a gradual increase.

So I'm pretty sure that's what that means and now here's the part that we get to have a little more

say over and that's parameters

and we need some more curly brackets for this and then inside here we're going to have in quotes checkpoint

underscore radius and make sure you get this spelling right in your underscore correct.

This will need to match what goes into unity and and when I say goes into unity it's actually the.

Also the value that goes into your aircraft.

Agent right here.

So this.

This needs to be exactly the same and you might even want to copy and paste it just to be extra sure

that that is correct so these checkpoint radii are what will show up at each threshold.

So we're gonna start with a radius of 50 and then we're going to decrease the radius.

So let me show you what that looks like.

So I have the checkpoint opened up in blender again and I have a little sphere here.

This fear is currently a radius of 1 so I'm going to scale this to be 50 and you can see up in the top

corner where the scale is so I'm going to increase it to 50 roughly.

I can just type in 50 actually.

OK.

So I'm going to enter and if I do I want to do wireframe mode.

OK.

So this is how close a an airplane needs to get during this first part of the curriculum in order to

get a half a point.

So you can see if we had multiple of these checkpoints it really doesn't have to get that close but

it's starting to get some rewards for getting in the right area then we're going to decrease it down

to 30 then 20 then 10 and make sure you put a comma in between each one of these.

And then finally zero point zero and you just need to have if this has one two three four five you need

to have at least four of these thresholds so that it can when it hits this then it goes to the next

one and so on.

So let me show you really quick.

I'm going to save this.

We're actually done with this file.

I'm going to show you what that looks like at 30 20 and 10.

So this is 50.

So I'm going to undo that with controls.

And I'm going to scale this up to 30 so you can see that it's smaller.

It's definitely needing to get closer but it's still pretty easy.

And if the plane were flying at an angle like this it could hit like right here.

And even though it wouldn't have gotten the point we're still giving it some some reward for that and

then we went down to 20 and 20 is about the size of the actual checkpoint itself but it has some volume

to it instead of it being so thin and then the last one is 10 which almost seems a little silly because

if it's flying near this checkpoint it's probably going to go through but there is still a little bit

of volume.

So it gives it a little bit more grace when it comes to getting it right.

And then finally of course if we scale it down to zero you know it's it's no longer using that as a

measure for whether it should do it.

It's just going to use that collider.

It'll work only if it flies through the collider.

So in each of these times if it were to somehow like if we were here and it managed to fly through here

through the collider it would still get points.

So that's the idea of the curriculum.

It just gradually makes things more difficult over time.

And I will show you really quick here.

If we increase this lesson here you can actually see going to see if I can select just this part.

You can see where the lessons changed.

If you decrease the smoothing.

So this is where each lesson Change now on the orange one it took quite a while before it hit that threshold.

And then on these these three it was it got there pretty quickly.

It took about 28000 steps or ten minutes and then it jumped up and then it only took another two minutes

and then it took another one minute like it went very quickly to get through those and it turns out

that that really does help quite a bit with training if you start with if you don't do this with curriculum

which you should certainly experiment with if you're curious then I do not think it will work very well

at all.

It will take a lot longer for it to learn which general direction to fly.