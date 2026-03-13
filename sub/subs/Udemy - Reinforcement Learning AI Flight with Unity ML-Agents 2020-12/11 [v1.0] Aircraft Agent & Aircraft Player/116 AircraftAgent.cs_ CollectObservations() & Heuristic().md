# AircraftAgent.cs_ CollectObservations() & Heuristic()

And this video we're going to work on collect observations and heuristic, and those are both override

functions and they'll be the last couple of functions we need to write for this class to be complete.

So right after.

Let's put this right after the odd action received that keeps all of our override functions together.

We're gonna type public override and we want collect observations.

So up until this point, we haven't written any code that helps the airplane observe the world around

it.

And we're about to change that.

So let's add a comment.

Collects observations used by agent to make decisions.

And this parameter sensor is the vector sensor.

So this vector sensor has a red squiggly underneath it.

And that is because we need to add using unity M.L., Agent Stutt sensors.

Once that is added, then that should go away.

And basically, this is a sensor that we are going to fill up with information, we can remove this

line.

So the majority of the observations for this airplane are actually going to be recasts.

But we don't have to do them in this function.

This collect observations function is purely for things that are non recast that we are just observing

about the world.

And they have to be in the form of numbers, basically.

So what we're gonna do is start out by observing the aircraft velocity, observe.

Aircraft velocity, and this is going to be one vector three.

Which equals three values.

So the code for this is Sencer dot ad observation.

And we want to pass in the transform dot inverse transform direction, rigid body dot the lost city.

So this ad observation function can take in lots of different kinds of values and actually let me do

this again really quick so that you can see all the different overrides here.

I'm hitting up and down on on the Iraqis, by the way, so it can take in Boole, it can take a float,

an int a quick turning in a vector to a vector three or a list of floats.

So basically we're observing floats.

And what I mean, there is a boolean in this case is going to be converted into a zero or a one I believe

float is already a number and it will be converted into a float.

Equity anyon is actually for floating point numbers.

So you'll have four floats.

Vector two is two floats, vector three to three floats, and then a list of floats is some arbitrary

number of floats long.

So that's what these observations are.

We are observing numbers that describe the environment.

And the first one we're doing is the velocity relative to the agent itself.

So it knows which direction and speed it's going.

Then we're going to say where lips?

Where is the next checkpoint?

And this is one vector three and it's three values.

And I've added these three values here and here because we're passing in vector three in this case.

So it's an X, Y and Z.

And those are all floats.

So it's the same thing here.

So Sencer, add observation vector to next checkpoint like that.

Now, the next one is orientation of the next checkpoint, and this is one vector three and it's three

values.

Vector three next checkpoint forward equals area DOT.

Checkpoints.

Next checkpoint index dot transform dot forward.

So we're getting a vector.

Of the next checkpoint's transforms.

Forward.

So this basically gives us sort of an orientation, a a vector that says which direction the next checkpoint

is pointing.

And we're going to say sensor dot, add observation, transform dot inverse transform direction.

Next checkpoint forwarder.

So now we have these three different observations and we.

So that's the velocity of the airplane, the vector to the next checkpoint and the as well as the orientation

of the next checkpoint.

So the airplane should have some idea of where that next checkpoint is and whether it's flying toward

it.

And these observations, let's just add them up so that we can refer to this later.

The total observations equals three.

Plus three, plus three equals nine.

And we're gonna need this number later because we're going to specify how many observations the agent

should expect to get.

Now, the last function in this class is heuristic.

So we'll add this after collect observations.

Public override, void heuristic.

And this one, actually, we're not going to use it in this class.

We're only using it in aircraft player.

But if it's called accidentally on aircraft agent, I want to give a helpful warning message just in

case this happens to you.

So we're going to say in this project, we only expect heuristic to be used on aircraft player.

So actions out is going to be an empty array.

So we're just going to make this be debugged, log error heuristic was called on space and then end

quote.

Plus game object dot.

Name plus.

And then on the new line, we'll do space, make sure only the aircraft player is set to behavior type

heuristic.

Only.

So this is just a safety check where if you're Ristic gets called on the aircraft agent because you

have your behavior type set to hear is stick only you get a warning message.

This has happened to probably a dozen different students.

So I figured I would add this in now that I'm updating the course just to make sure that that doesn't

happen.