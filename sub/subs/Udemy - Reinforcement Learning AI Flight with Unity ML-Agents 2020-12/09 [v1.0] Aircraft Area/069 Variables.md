# Variables

In this video, we're going to create our first script and that's going to place all of the checkpoints

around our race path.

So go into the aircraft folder and create a new folder.

We're going to call this script.

And hop down into there and we're going to create a C sharp script called Aircraft Area.

And once that's created.

Create a second script.

Called aircraft agent.

I'm getting an error message probably because this is not the first time that I've tried to create these

scripts, so let me try and open it up and make sure that that goes away.

OK, let's take a look.

Make sure that this.

They clear this.

OK.

Everything seems to be fine.

Now, we're not going to work on aircraft agent quite yet, but it's needed for aircraft area to build

properly, so that's why we created both go ahead and open up aircraft area.

And the first thing we'll do is put this in a namespace named space aircraft.

And this will just keep our code organized so that we don't have any naming conflicts.

Once you're in here, go ahead and delete the start and update functions.

And the first thing we're gonna add is a variable.

And I like to add tool tips for variables that are gonna be visible in the inspector so that you can

hover over them and you'll get a little hint at what it's for.

So type in tooltip.

And then in parentheses and quotes, type the path the race will take.

This is going to be a reference to our race path.

Public Cinna machine.

Smooth path.

And then race.

Race, path like that.

Now it's going to be zigzag, underscore, underline there if you right.

Click on this and you go to quick actions and refactoring.

You'll need to add using SINTA machine.

And if for some reason snowmachine isn't showing up, then make sure you went to the package mannered

manager and that you installed the latest version of Sinnett Machine.

You're still having issues that I'd suggest checking out the unity forums or maybe creating a clean

project, because sometimes snowmachine can be a little finicky.

But it should work at this point.

Next, we're going to add another tooltip and that one is going to say the prefab to use four checkpoints

and this will be a public game object called checkpoint prefab.

So we're just going to give it the prefab that we want it to duplicate and create a bunch of different

checkpoints for.

And then we want the same thing for the finish line.

So tooltip a prefab to use for the start.

Slash and checkpoint.

Public game object.

Finish, finish, checkpoint.

Prefab.

So we'll be hooking these up manually when we add this to our CNN.

Next tooltip.

And this one's going to be, if true, enable training mode.

So this will control whether we're in training mode or not.

We have some slightly different behavior based on whether we're training or not.

And this is going to be a public bull called training mode.

And since we're not setting it, it's going to default to false.

So it won't be training mode by default.

Next, we're gonna need a couple of lists.

The first one is going to public list aircraft agent.

Called this one with a capital letter, air craft agents.

And this is going to be get cold or semicolon private set.

So this is just a an accessor of a list of aircrafts that are going to be in this particular aircraft

area.

There will be when we're training, there will be multiple aircraft areas at the same time.

And so we want to have a list of all the agents that belong to a particular area.

And since this is pretty self descriptive, I'm not going to add comments for these.

The second one is public list game object.

And this will be called checkpoints.

And this is also a get semicolon private set.

And if you're not familiar with this syntax, basically what it means is create a variable and allow

anything public to this to access it, but only allow it to be set from inside of this class.

Right here.

And that's it for the variables in the next video, we'll start adding some of our first functions.