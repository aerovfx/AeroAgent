# Training ML-Agents

Once this is done we're ready to train but we do need to do a C.D. dot dot again to hop back up to this

next directory.

Now we're going to use the training command that shows up in the basic guide.

So once you're done installing you can click on basic guide.

I have it open in another tab and this gives you a bunch of setup instructions which you might need

to do if you're having some issues.

But what I'm gonna do is skip ahead to the training part just to show you the command that we need to

run.

So this is the command that we need to run in order to train an environment.

So what we're passing in we use this M.L. agents dash learn command.

We have to give it a trainer config path.

So it's the relative or absolute file path to the training configuration.

So that is inside of our

MLA agents directory.

It's inside of config.

And this is the file that we're actually going to pass in trainer config that Yama.

And then you pass in a run I.D. and you set that equal to some value that you get to choose.

They chose first run.

In this case so you can name it whatever you like.

You just want to update this for every time you do a new training so that they keep them separate if

you rerun it with the same name again.

It will overwrite the previous training that it did and then you do this dash dash train command so

we're going to run this command email agents dash learn and you know I'm gonna try and make this a little

bit bigger just so you can see what's going on properties.

Font so make this 28 Well that's big.

OK.

Well now it's a lot harder to see what was happening behind it.

But we're going to M.L. agents dash learn and then the command we're going to type after that we have

to do a path to our config which is under config dash trainer underscore can figure out your.

So config Slash trainer underscore config dot Yama and then we need to and I you know I don't think

it matters on windows whether you do a backslash or forward slash but if you're on a Unix platform it

probably needs a forward slash.

So I'll just try it with forward slash and hopefully that works for everybody.

Then we need a run I.D. run dash I.D. equals.

So we're gonna say basic run underscore 0 1 and then we will have to do dash dash train.

OK.

So then we'll hit enter and it's gonna run or it's gonna show a bunch of stuff and then it might pop

up a Windows security alert.

I generally just allow access on both and if it shows this unity thing then things are probably in a

good shape.

And then it says start training by pressing the play button and the unity editor.

So we will go to the Unity Editor and press play

it seems to be stuck.

And sometimes when this happens I realize that there's like this thing here.

If you enter it seems to magically like unfreeze itself.

So fortunately that's what happened to.

I'm actually kind of glad that that happened because that'll show you if it's if you see that little

cursor then it might be stuck.

So you can just hit enter.

So now it is training and this little character is moving either left or right.

And it doesn't know what it's supposed to do yet but it is learning gradually.

And you may see a bunch of tensor flow warnings.

I'm sure that they'll fix these before they release AML agents.

You know the official non beta version but it looks like we're getting some warnings because we're using

some older versions of tensor flow libraries.

But as long as you start seeing lines like this that say step a step number and a time elapsed and a

mean reward and a standard deviation of reward.

Then things are things are training properly.