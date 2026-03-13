# Config Files

In this video, we're going to talk about the config files for training.

So in the source code that you can download that comes with this course, there is a config folder and

inside config there is a trainer underscore config di YAML file and a curricula folder that contains

aircraft learning, not YAML.

Now, these two files, I've opened them here.

They contain basically the configuration for how our training will run, as well as the curriculum data

that we're gonna use while we're training.

So let's talk about the curriculum first, because it's a little bit simpler.

Now, you do not always need curriculum to train a reinforcement learning agent.

Curriculum in this project is useful because it's actually very challenging for the airplane to fly

one hundred meters and hit the target perfectly.

So we are using it to make the task easier.

When it starts out and then gradually make the task harder and harder as it sort of learns what it's

supposed to do.

So you'll see a lot of examples in the Unity M.L. agents repo that don't use curriculum at all.

I found that using curriculum for this particular project just made a lot of sense.

Aircraft learning this curriculum here.

It matches with our airplane learning here.

And it has to match this behavior, name aircraft learning.

So these two have to match.

And what it is saying is.

Measure is reward.

So it's going to measure the reward.

The thresholds are two point zero two point zero four point zero and six point zero.

So what this says is when the reward hits a value of two.

Then switch from using a checkpoint radius of 50 to the next one in the list.

30.

And a while back when we were in our let's see, when we were in our agent.

Where are we?

Aircraft agent?

In the odd action received function.

There's a part where we check the Academy instance, dot environment parameters, dot get with default

checkpoint radius.

This right here matches this right here.

So they have to spell they have to be spelled the same and all that.

And what it is, is it is an accessor that allows us to set a configuration of parameters that can get

difficult, more difficult over time, basically.

So we're saying start out with a checkpoint radius of 50.

Then when you managed to get a total reward on average of two, then jump to 30.

So now we have to get within 30 meters of the checkpoint.

Then once you get a reward of two at that more difficult challenge, then switch to 20.

And now, after it's gotten very good at doing 20 metres away, then switch to four.

So it has to get a total reward of four and then 10.

And then six will be the total one where it finally goes down to a a radius of zero, meaning it has

to successfully get through the checkpoint and actually touch the checkpoint itself.

So to think about these thresholds, we give the agent a half a point of reward every time it gets a

checkpoint.

So to get a total of two point zero or higher.

It has to go through at least four checkpoints.

So that's why we say.

All right, we'll try it out, see if you can get within 50 meters of the first checkpoint.

And if you do, we'll give you half a point.

Then it has to get within 50 meters of the checkpoint after that.

Then it gets an additional half point and so on.

It has to do that at least four times, probably five times to get this to get past this threshold.

Then it's what switches to 30 and 20 and 10.

And then finally, zero.

This mean less in length means that it has to have at least one hundred lessons before it will do this.

So if by some freak chance all of the airplanes manage to just fly the entire course, which is extremely

unlikely, by the way, then it would at least make sure that 100 lessons had happened before it jumped

to the next one and then signal smoothing.

This one just makes it so that if you have any weird, like spikes or dips, then it kind of smoothed

that out.

So it takes that into account.

It doesn't it doesn't cancel everything.

If it, you know, has a horrible run or something like that.

So that's curriculum and it's access through the Academy instance environment parameters thing.

Now, the other one is trainer config Yamal.

This file is more complicated.

Basically, it's a bunch of parameters you can set that tell the training program how to set up your

neural network and how to do training.

If you've done some neural network stuff in the past, you might recognize some of these terms.

The trainer.

This is PPO, which is proximal policy optimization, which is a type of reinforcement learning batch

size, BITA, buffer size, hidden units.

These are all deep learning terms.

And rather than trying to explain what every single one of these means, I want to point you to the

documentation.

So the docs have something in here for training configuration file.

And in here, it has a description of what each one of these is.

You really don't need to understand what all of them are.

You can actually look at the examples to give an idea of which ones are most meaningful for changing.

So by that, I mean, you can go into this config folder at the top level of the Emmel Agents GitHub

repository.

And by the way, I mean the release to Branch, if you are in a later release, than it might look different

inside the config folder, there's this Trayner config dot Yamal.

This is where I got the defaults from that are in this file.

And then they've added some that customize it for each of the example projects that they have that are

in this GitHub repository that we got at the beginning of the course.

So you can look at these for more examples.

But in our case.

We're just going to change a few of them, so we're going to change the time horizon, that gives us

a bit more time to successfully get a check point and learn from that batch size and buffer size means

it's going to take on more experiences before it does learning.

Hidden units is basically how many neurons we're giving this or we're going to increase the size of

the brain.

We're doubling the brain power of this.

Bita, I remember what that means, but I was I guess I experimented with it and I liked this number

and Max Steps.

I basically just added two zeros to the end of max steps so that it would have enough time to train.

There's no necessarily right answer for how big this needs to be because you don't know how long it's

gonna take to train.

But I'm pretty confident that five hundred thousand steps, five times 10 to the fifth is not going

to be enough.

And so I just added a couple zeros and we can always stop it early if we need to.

So that's it for how these two things work.

We now need to move them into a folder where we can do some training, so go somewhere on your computer

that you have access to and create a new folder.

And we can call this training.

And then go in here and grab this config folder.

You can copy and paste it into your training folder, and that way it might be a little bit easier to

find it later.