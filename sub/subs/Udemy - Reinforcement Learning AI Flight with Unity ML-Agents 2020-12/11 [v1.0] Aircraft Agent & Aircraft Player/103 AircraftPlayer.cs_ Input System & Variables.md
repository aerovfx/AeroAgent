# AircraftPlayer.cs_ Input System & Variables

In this video, we're going to work on the aircraft player script.

And this is a new script that we're gonna have to create.

So head into unity and go into your aircraft folder and scripts and create a new C sharp script and

call this aircraft player.

Then go ahead and open it in visual studio.

OK.

And this class is actually.

Well, let's add it to the namespace first namespace aircraft.

This is going to inherit from our aircraft agent class.

So this is technically an agent as well.

It is also an aircraft agent.

So this is just going to add functionality on to our existing aircraft agent function or agent class.

I mean.

So let's clean this out.

And what we want to do is start out with.

We're gonna import the unity input system, and you need to actually add that, be the package manager.

So head to.

Window package manager inside unity.

And then find the input.

Leave.

Input system right here.

So right now, mine is version one point zero point zero.

This is different from the default input that's built in.

So go ahead and install this.

And it says this project is using the new input system package.

But the native platform back ends for the new input system are not enabled in the player settings.

This means that no input from native devices will come through.

Do you want to enable the back ends doing so, we'll restart the editor and we'll disable the old unity

engine.

Input.

API is answers, yes, but that means that we do need to restart the unity editor.

That's not a problem.

So we'll just say, yes, we'll let it do its thing on the back end.

Looks like that's done.

And it closed down unity for us.

I don't know if that was a crash or if that it was intentional, hopefully intentional.

I think I had my project saved.

And then we'll need to open it back up.

All right.

So input system should be installed.

Now it looks like it reopened this for me.

I didn't have to do that manually.

And this now is the new input thing.

So I think here under input manager.

Yes.

Indicates that it's using the new API.

So I think think this should work just fine.

So go back to the aircraft player script and we're going to add using unity engine dot input system.

And as long as that shows up, then it should have installed correctly.

And we're going to add some public variables at the top and we'll start with heter input bindings.

And this will be helpful for separating these public variables from what's in the base class aircraft

agent up here where we have this heter.

So first one is public input action pitch, input, public input, action, your input, public input,

action, boost input.

And then.

Actually, let's add one more, we will be using this later.

We we don't need it quite yet.

So public input, action, pause, input.

So we'll be using this later.

It's just more convenient if we just add it now.

And then we need to do something with these values.

So let's add something that's going to initialize them.

This is actually going to be a public override and we're going to override the initialize function.

And this is where this based on initialised comes in handy, because this is going to call initialise

on aircraft agent.

So it's going to call this first and then it's going to court and then it's going to do whatever we

tell it to afterward.

So that's what's nice.

Aircraft player is basically just an aircraft agent that has some additional input logic in it.

So what we want to do is enable all of these inputs.

Pitch input.

Enable your input.

Enable boost input.

Enable and pause input.

Enable.

So if you don't enable these, then nothing will work.

So that's important to know.

And then I'll also mentioned, if you don't disable them later, then you might have problems, too.

So let's just add that right now.

Private void on destroy.

We want to basically do all of these.

Again, I'm just going to copy them and we want to change this out for disable.

So make sure that all four are disabled.

And we probably want to add comments to both of these.

So while I'm on this one cleans up the inputs when destroyed and then initialise calls base initialise.

And initializes initial.

Yeah, I guess I did spell it right.

Input.

Now, there's nothing actually happening with the input now.

The function that we want to use is called heuristic.

And I'll explain that.

And then we'll go into it in the next video.

So heuristic basically is the ability to take input from the user and feed that in to.

This function on action received, so on action received takes in a list of choices.

As we talked about before, but it does that regardless of whether that's coming from a neural network

or that's coming from user input.

And the way we handle user input is this heuristic function.

Heuristic is actually on the agent class here.

And if heuristic is called or rather, if the agent is told to be using heuristic, then this function

will be called for making decisions instead of the neural network.

So we'll implement that in the next video.