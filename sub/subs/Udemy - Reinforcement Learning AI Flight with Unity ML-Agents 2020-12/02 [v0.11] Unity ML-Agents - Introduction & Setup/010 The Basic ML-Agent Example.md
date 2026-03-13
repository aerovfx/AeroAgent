# The Basic ML-Agent Example

Once unity has fully opened we can import our MLA agents project.

So we're going to go into the year from this MLA agent's directory we go into unity SDK assets MLA agents

and then what we want to do is click and drag this down into our assets directory and this will import

this entire folder into our project.

Now this will take some time hopefully just a minute or so and it might kind of lock up your screen

while it's doing that but it seems to have finished for me you might get some error messages or some

warnings.

I get some warnings saying that some type gooey layer is no longer available.

It seems that they probably built this project with a different version of unity and so there's some

some warnings that kind of pop up it's trying to open the MLA agents folder and then under examples

there is a bunch of examples that you can learn from.

Which is really cool.

So let's take a look really quick.

This is the example learning environments documentation page on the GitHub repo and it explains what's

going on in each one of these different examples.

So this one that we're going to take a look at first is the basic scene and it says setup a linear movement

task where the agent must move left or right to rewarding states and the goal is to move to the most

reward state.

So this little character needs to move to the left or to the right and it's I think the most reward

state is represented by the larger sphere here.

And it's only observation about the space.

Is this vector observation space here.

One variable corresponding to current state.

So the current state is either there's something to the left or to the right I believe and then the

vector action space are the two options that it has to do either move left or move right so it's about

as simple as it can get here and still visual and helpful to look at.

So let's open that one up we'll go to the basic folder scenes basic and this is our scene right now.

I think maybe the lighting is turned off.

There we go.

I had the for some reason this lighting button was turned off so I toggle it on and the lighting looks

a little better so this scene has several things that aren't super important to it so I'll just point

those out first main cameras just how we see this thing.

The directional light is just lighting up the scene.

The canvas watermark if you go into the game it's just this.

So nothing special about that and now there's the two things that are of interest.

The Academy which has some parameters and controls that actually facilitate learning within the scene.

And then this basic this is just a prefab that is containing the things we need for this scene to work.

So the most important one is this basic agent.

I think the rest of these are all just game objects.

So these are pretty simple.

There's a sphere.

There's nothing special about this.

No scripts attached to it.

Same with this one and then platform.

Nothing special about this either these are just shapes that are in the world.

This basic agent is where the interesting things are happening so this agent contains behavior parameters

and basic agent.

These are the two scripts that they work together to allow a neural network to control this character

so agent if you want to think about it is kind of the larger piece of script and it will potentially

if it has a neural network hooked up to it it will ask the neural network what to do based on what it

sees about the environment around it.

So it's going to get some sort of input that says that are what the state of the environment is and

then it's going to feed that into a neural network which might be fed in right here if it is right now

it's missing.

So it would not work.

In fact I'll just hit play and show you that it won't work.

So nothing's happening.

Makes sense.

It doesn't have a doesn't have a neural network but now if we switch to this folder if we go to TMF

models you go back to that basic agent and I'm going to drag in this neural network model.

This basic you'll see its basic dot and then if we play then we should be able to see it do something

so they've provided this pre trained neural network that tells the agent what to do.

So it's able to find this large sphere and move toward it every time so that's the basics.

That's called inference.

So when you run a neural network in inference mode you aren't training it.

It's not learning new skills.

It's just a static brain essentially that is being fed information and then getting outputs and those

outputs are being used by the agent to determine what to do.

So in this case it just moves one direction or the other.