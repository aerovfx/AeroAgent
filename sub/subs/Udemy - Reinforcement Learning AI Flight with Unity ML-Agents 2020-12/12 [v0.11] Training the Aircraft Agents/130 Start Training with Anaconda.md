# Start Training with Anaconda

We're finally ready to start training.

So I have the training scene up behind this Anaconda prompt.

That's important.

You do need that ready because it's going to wait for us to hit play once we actually start training.

I have a completely new Anaconda prompt.

You can tell because it says base in parentheses so no environment is actually loaded yet so I'm gonna

run Conda in the list.

This is just as a refresher for how you actually get into a Anaconda environment.

And I'm going to pick the a environment that I need so we're working with the MLA agents.

Eleven or zero out eleven.

If you have a newer version then go with that.

Just make sure that your version here matches whatever is inside of your your Unity project.

If they don't match then the APC the remote procedure call logic that basically connects the python

training to the C sharp scripts inside.

That won't work.

So just make sure that you have matching versions so I'm going to now.

Now that I've I'm going to copy that to the clipboard by highlighting and right clicking and then we're

gonna do activate and then paste this by right clicking again.

And now I know because it's in parentheses that this is the right environment so the commands that we

need is actually for curriculum learning.

This is on the docs training dash curriculum dash learning M.D. page on the GitHub repo.

And if you scroll down there's actually quite a lot of helpful information about this but we're just

looking for the command right now.

So we need MLA agents dash learn.

So that's the first part.

So let's actually we need to make sure we're in the right directory first.

So let's I'm going to do a C.D..

So I'm on the desktop.

And then course and then my MLA agents folder.

So just for reference this is here the folder that has all this stuff.

And as long as you installed the stuff correctly the MLA agents stuff before with Pip then you should

have the MLA agents learn stuff if you need a refresher.

Go back to the beginning of the course and we set that up there.

So we need AML agents dash learn.

So that's the first part and then a space the next one is a path to the config file that we want.

Now they are using a relative path to the config that's in this directory inside the MLA agents.

Now ours is actually here in aircraft MLA.

So we're gonna use this one and if we just click on this and go copy path in the Home tab then it will

allow us to right click and paste that path in there.

So we're we're still going to the trainer config it's just a different trainer config the one that we

modified the next part is dash dash curriculum.

So let's do that

and you don't actually need an equal sign.

You can do a space sign to and then they just point to the folder inside the curricula folder that has

your stuff in it.

So we're gonna find that so it's under curricula and then aircraft.

So this is the folder we want and I'm just going to click on that.

Remember what's in here is that Jason File.

So I'm going to click on this and then copy path

and then we need to pass in a run I.D. and you can choose whatever you like for this.

Just make sure that it doesn't conflict with another run I.D. that you've already done.

Otherwise you're gonna have some interesting issues so it should overwrite the previous training if

you give it a name again.

But the tensor board summaries which I'll show you in a moment.

Those might be messed up.

So just be aware of that.

It's always good to pick just a new name.

When you start a new training so we're gonna do dash dash run ups run dash I.D. and then space and then

I'm going to call this aircraft underscore 0 1 and then the last part is dash dash train and I just

show you right there so then if we enter it's gonna start and we're gonna see a lot of text show up

but then we see this unity logo and it says start training by pressing play button in the editor.

So if you see that all seem all should be good.

You go into your unity editor and you press play

and it will take a moment to sort of get moving and a lot of text will start showing up in here including

quite a few warnings from tensor flow.

I've noticed and even runtime warning something about invalid value I don't seem to have any problems

with these warnings so hopefully they're just safe to ignore.

And there's a lot going on in here including you can actually see the hyper parameters that were used

for this training.

These are pulled from the config file.

The trainer config ammo file that we used.

So if you need to reference what those were when you started running it then you can see those here

so let's take a quick look at our scene and no errors in the console.

So that's a good sign.

And it looks it may be hard to tell in the recording but it does look to me like there are some planes

that are flying around here.

So that's a good sign.