# AircraftAgent.cs_ Initialize()

In this video, we're going to add our first function to the aircraft agent class.

So make sure that you are right after these private variables and not in between these two last curly

braces, you want to be inside the glass.

And then let's add a new public override.

Void initialise.

And if you're not familiar with how overrides work, basically this means it's going to override functionality

from the class that it inherits from.

So this aircraft agent inherits from the agent class.

So that means the agent says something inside that says, hey, I've got an initialised class, go ahead

and override me and do whatever you want inside of that function.

So by default, it puts this base dot initialize thing in here, which means that the first thing it

does.

Is it calls that base function?

So where is that base function?

Well, you can right click on agent and go to definition.

And then if you go to definition, well, most of the time, when you go to definition, it opens up

the actual file.

In this case, it says from metadata and you'll notice that you can see all these function names, but

you can't actually look at what they do.

So you can close that.

And you actually need to open up unity.

And you need to go into your packages.

Folder M.L. agents.

And then go to runtime.

And then find agent.

And if you open this up, then you can look at this file and there's a ton of functionality in here.

So don't try and read it all because it's like a thousand lines of code.

But if you click if you make sure you find the actual start of the agent class and click inside here,

then this list up here in Visual Studio will show up and you can find in this list.

And it's all alphabetical.

The initialize function.

And here is where they have comments about what it's for, as well as a link to some documentation and

a public virtual void, initialise with these just two curly braces.

So this basically says create a function that doesn't do anything but that any class that's inheriting

from can use it.

And the reason it's doing that is because it if we do control F and find this, there are other places

inside of this file or at least one place right here where it's calling that function.

So this agent is assuming that some other class in our in our case, our aircraft agent, it's going

to define its own version of initialise and then it will call that version that function.

And then it will use the version that we declared and that we made here.

So that's what's happening.

Hopefully that makes sense.

We don't need to call an empty function so we can remove that.

And then we're only going to add a couple of things here.

So we need to set the basically we want to set these three variables because they are empty when it

first starts out and initialise is called right away.

So let's actually add a summary up at the top called when the agent is first.

Egypt is first initialised.

And we're going to say area equals and we need to find the aircraft area.

Well, in this scene, the airplane is a child of the object that has the aircraft area on it.

So the function we need is get component inherent.

We need to specify that we're looking for an aircraft area.

Then we want rigid body equals and rigid body is going to ultimately be on the airplane itself, doesn't

have it yet, but we're going to add it here.

So we'll say get component, not get component and parent, get component, rigid body.

Same idea for the trail trail equals get component trail render.

All right.

So that's all we need to do inside of initialise for now.