# Training 3D Ball Example

In this video, we're going to setup and start training this 3D ball environment.

So as I mentioned before, you need Python to train MLA agents and you should have downloaded Anaconda.

And so we're going to open up the anaconda prompt.

Now.

So I'm going to open Anaconda prompt, and then when you open it for the first time, you're going to

get a black window that says base on the left.

And then it should have a folder that you're in.

The base is the base environment.

Anaconda works with things called environments, which are basically sort of safe sandboxes where you

can install any sort of python libraries you want without messing up any other environments.

So we're going to create a new environment and the command for that is KONDA.

Space create.

Dash n dash end means we're going to put a name.

So the name that we're going to give, this is something like Emil agents one point zero.

We're actually going to call this for this course.

Emil Agents Dash one point zero point two point two.

That's the version that I'm going to use.

And actually I'm going to put a dash in there as well.

Emil Dash agents dash one point zero point two.

And then you have to type space and then Python equals three dot seven.

So that's going to specify what version of Python you want to use.

Once you've run that, it's going to ask you if you want to proceed with installing all of these things.

Go ahead and hit the wiki and hit enter.

And depending on.

Internet connection and whether you've installed some of this before, it may go very quickly or it

might take some time.

At the end, you should get a command like this konda activate.

We're going to run this KONDA activate Emmental Dash agents dash one zero two and hit enter.

And now you'll see something new on the side here.

So this is in parentheses, this environment.

So now we know this environment is active.

In the future, if you want to reload one, you just have to do Konda Ian V list and it will show your

list of environments with a little asterisk next to the one that you're currently in.

So I have a bunch of these from different things I've been working on.

This is the one that I just created.

Now we need to install MLA agents.

The version I want you to install is version zero, DOT sixteen.

So type in PIP P.P. install.

And then M l AGP and T.

S.

Equals equals zero dot one six, dot zero.

Enter.

And this is going to take a moment because it's installing quite a few different things.

Including Tensor Flow and Tenzer board.

And just a lot of different things, so this will take a moment.

So go ahead and let this run.

And when it's done, we'll come back and we'll start training.

All right.

So when you see a prompt like this, again, that means it's done installing and we're ready to start

training.

Before you start training, make sure that you do have unity open and that it's open to the scene that

you're ready to start training in.

Now, the command you want is M.L. Agee n t s dash learn, lta r n and then you need to specify a config

file.

So the config file that you want is in the folder.

This M.L. agents release two folder that we downloaded under config.

Trainer config.

So you want to copy the path to this so you can click on Copy Path on Windows or if you're on Mac or

Linux, then you'll just need to get the actual path to it.

And then you want to use that eye, right?

Click to paste this into the second part of this command.

And then you need to specify a run I.D., so dash, dash, run, dash I.D. and then we can give this

any name we want.

But I'm going to call it 3-D ball underscore.

Zero one.

So I typically give it a name like that so that if I mess up one of these training runs and I have to

run another one, then I'll just call the next one.

Three ball underscore to.

When you're ready, go ahead and hit enter.

And it's going to show a bunch of stuff.

It may also ask you if you want to allow access, and you do.

And then the important thing here is it says, listening on PT. five thousand for start training by

pressing play button and the unity editor.

OK.

So I also want to point out, if you have this highlighted like this, it may not actually pick up.

So you'll want to enter just to make sure that it's still running.

For some reason, it doesn't like to work when it's highlighted and then go to unity and hit play.

And it should start going OK.

So what we're looking at here is that all of these are trying to train simultaneously.

And you'll notice that the ball is falling off their heads.

If you right, click on the game tab and click on maximize, it will hide this.

And open up the project settings.

If you don't see a tab for it, you can go to edit projects settings and find the time section.

This is running at 20 times the normal speed.

So change this to one really quick to see what they look like at normal speed, and you'll see for sure

that they're not very good at this.

They're the balls are just falling off their heads.

So we can speed this back up.

So I'm going to change it back to 20 and let it go.

You can't go faster than 20.

But sometimes if you go too fast, then the physics start acting weird or you end up actually having

things happen where the training will slow down because it's trying to run the game too fast.

So 20 seems to be a pretty safe, sweet spot.

And as they're training.

In the Anaconda prompt window, you'll start seeing these steps count up and the time elapsed.

Now, before I say that, show you about that.

I'm just going to show you really quick.

You might get some Kouda errors if you don't have Kouda installed on your machine.

And on this machine, I.

I don't think I've installed Khuda yet.

So I have these Kouda arty errors.

Those in my experience have been safe to ignore because we're just training with the C.P.U.

So these right here, you'll notice that there's a time elapsed in seconds.

And then there's a mean reward.

So the average reward of all of the agents at that point.

So it started pretty low at around 1:00.

And then as we've gone, it's gotten up to a mean reward of one hundred.

And it looks like it's maxing out.

So I think that's about as good as it can get.

If we go back here, we'll see that the ball doesn't fall off their heads.

They've actually learned very quickly how to balance the ball on their heads.

And if we slow it back down to one really quick, we can see in real time that they're very good at

balancing these on their heads.

When you're pretty confident that this is done training, which, by the way, this project trains extremely

fast, our airplanes won't train quite this fast.

Most of the agents that you build probably won't train this fast.

These are pretty simple agents that are able to learn very quickly.

So just wanted to get that out there.

When you're done, there's two ways of stopping this.

You can do control see here and that'll stop the training or you can hit play in the unity editor and

that'll stop training.

You should see that it saved the model.

And down here at the bottom, it says Dunn wrote, dot slash model's 3D ball underscore zero one 3D

ball, dot and file.

So this is basically a new version of this, an end file.

And it says it went into the models folder.

Well, the models folder is somewhere where I believe.

Let me just double check.

I don't think it would have gone in here.

No.

It goes into a models folder in the folder that you were in.

So I made a mistake here.

I should have I should have actually showed you in a different folder, but it dropped it right here.

So I'm going to go to that folder.

On Windows, you can just hit start period and hit enter.

And then in here, there should be a new models folder.

And under here, you'll see that there's this 3-D ball dot and.

And in case you're curious, what 3D balled up in is, if you go in here, these are actually tensor

flow files.

And what it does right here.

This last step after training is it converts this tensor flow model into an end file, which is a barracuda

file.

So this file up here can be dragged.

I'm not going to do it because there's not really much point.

But you can drag this and file into here, and it will.

Be possible, actually, why not?

So I'm going to show you really quick, if you if I were to drag this in.

There would be a conflict with this one.

So I'm going to rename this to zero one and then I'm going to drag this down in here.

And if I go to inside of this prefab and go to my agent.

I can update this model.

In drag, this in here.

And go back out.

And when I press play, it's going to use the new model that we just trained.

And you can see that it's working really well.

So that's the gist of how training works.

And, well, we really glossed over a lot of the details.

Now you have a pretty good idea of how the you know, how things work in MLT agents going from an example

to training and then having a neural network that can be applied to your agent for running what's called

inference and inferences, just where it uses a pre train neural network.

It's not doing any training.