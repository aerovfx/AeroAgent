# Config_ trainer_config.yaml

So we're going to add our own section for our agent and we're going to copy the pyramids one and then

write our own.

So I'm going to copy this entire section from pyramids not visual pyramids.

That's a different one that one actually uses cameras.

This one uses Ray casts.

So we're gonna go down to the bottom and we're going to add this in so we're gonna paste this in and

then immediately we want to rename this to aircraft learning and then we need to change a few of these

values so these values are all defined in the documentation for the course.

And in fact it's on this training dash PPO page that you can learn all about them.

So we're gonna be changing a couple of them.

And so I'll talk about them really quick which ones we're gonna change.

So we're gonna change the batch size the batch sizes the number of experiences used for one iteration

of a gradient descent update should always be a fraction of buffer size.

So and then they give typical ranges.

So I experimented with this and I figured maybe having more experiences used for one iteration of a

gradient descent update might be good.

So the change that I ended up using you can comment these out with a little hash sign and then you can

change your own.

So five twelve was the batch size that I ended up using.

I like to do this just because sometimes if I'm tweaking them I can remember what it previously was

so batch size this one and then we're also going to change the buffer size and I'll go back to the documentation

and show you that in a moment I ended up with forty ninety six for this one so batch size buffer size

up here corresponds to how many experiences.

So Agent observations actions and rewards obtained should be collected before we do any learning or

updating of the model.

So this these definitely seem to be linked and it gives a typical range.

So it says typically a larger buffer size corresponds to more stable training updates.

So having more stability definitely sounds like a good thing.

So increasing this number make some sense then hidden units.

If you have ever seen this some I'm going to set this to 128 if you've ever seen a neural network drawn

out before which you probably have.

It's like a column of nodes and then another column of nodes and then there's a ton of lines like kind

of it crossing over each other to connect the two columns.

That's a neural network sort of represented on a page.

And we are doing one hundred and twenty eight nodes in our column and then two columns of that.

So that's what that's the complexity of our network essentially.

And if you want to read about that that's in here somewhere to number of layers.

So that's that's you know how many of these and then hidden units correspond to how many units are in

each fully connected layer of the neural network.

So explaining this part how the hidden units work and how neural networks work is definitely beyond

the scope of this course.

Unfortunately

then we're also going to change the max steps.

So Max steps is just how many total steps there are in the environment before it stops training.

So this one is set to stop after five hundred thousand steps and we would like to increase that upper

limit.

So five point zero E six.

So now we're we have five million steps.

The reason I've decided to do it this way is rather than try and come up with the perfect amount of

steps that this thing should train for.

I want to leave it open ended so that you can stop it whenever you like.

I'm going to open this really quick and just show tensor board.

These are some training runs that I've done recently.

And what's interesting is I only made a very subtle change between this orange run which I ran first

and then these three other runs.

So a subtle change can make a huge difference.

And this orange run ran for about 18 hours 19 hours and still didn't get even to the point where this

thing was at after one hour.

So sometimes you will find that you can get to the same training quality or results in terms of how

much reward your agents are getting just over time.

And other times it'll just scoot right up depending on just very subtle changes in how you how you train

that can be in this hyper parameter document or in the way you reward your agents.

And so I like to leave it open ended.

So if I want to if you'll notice the step count at the bottom of that black box there says three point

six nine four million.

So if we had cut it off after only five hundred thousand steps then we would be way back here around

here and our training would be not good at all.

So that's why I like to leave it open ended and then you can you can stop it early at any point if you

want to and then we have to change one more value in here and I'm going to change this num epoch to

6 and do make sure it's possible that they change some of these hyper parameters I would just recommend

you look at each one of these line by line and make sure that yours matches up with it if you're having

any trouble but the NUM epoch.

I do want to talk about this in the documentation

num epoch is the number of passes through the experience buffer during gradient descent the larger the

batch size the larger it is acceptable to make this decreasing this will ensure more stable updates

at the cost of slower learning so that was why I started messing with this because I was curious to

know if I could make it faster by increasing it I went all the way up to 8 and in my in some previous

runs I was able to get eight to work pretty well in the current training at least with the rewards in

the environment that I'm working in six seemed like a sweet spot where I was getting very fast training

and you can see right here these were a few that were run with six I ran a couple in a row at the exact

same environment so that I would rule out any just pure chance situations where I was getting much better

and it seems to be consistently working quite well so that should wrap up our trainer config one last

thing just make sure that this has the correct capitalization in spelling because it will need to match

other places in our project.