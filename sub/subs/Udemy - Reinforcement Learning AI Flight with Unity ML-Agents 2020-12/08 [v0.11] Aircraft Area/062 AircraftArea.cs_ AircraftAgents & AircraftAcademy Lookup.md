# AircraftArea.cs_ AircraftAgents & AircraftAcademy Lookup

Now let's create these classes so that we don't have to have these red squiggly lines.

So we're going to create a new script new C sharp script and this one is going to be aircraft Academy

and then we'll create another one really quick aircraft agent.

All right.

Now we can go back into visual studio if you get these inconsistent line endings.

I always just hit.

Yes and then it's going to have it's going to have this edited it's going to change a few things you

can just click save all and it will update that.

So let's open up the agent first and we're going to have first of all let's just delete what's inside

here.

We're gonna have this inherit from a class that's part of the M.L. agents namespace.

So we're gonna say agent and it's not going to know what this is.

So we'll control period and we'll click on using MLA agents.

It'll add it to our list of uses.

And now it knows what this is.

Now there is a a variable that will need for our area.

So we're just going to add this now.

We're gonna have a public next checkpoint index.

Sorry.

This is a this is an integer so public next checkpoint index and this will be a get a private set and

we'll come back to this.

So you just add that to your aircraft agent and and we'll we'll do a lot more work inside of this class

and then aircraft Academy has to also inherit so we'll inherit from Academy

and we'll just remove what's inside here and then we have to do control period using AML agents OK.

So that adds this using intelligence.

And surprisingly there's actually nothing else that we need to do with this word.

We're actually completely done with this script.

So we're gonna hide that

so we can come back into aircraft area.

Now and we can write our first function and you can see that.

Now these are no longer giving us those red squiggles so we're gonna do private void Awake and we'll

add a comment actions to perform when the script wakes up and what we're gonna do here is find all aircraft

agents in the area.

So we're gonna set this right here so aircraft agents equals.

So in order to get all of these aircraft agents we're just going to say transform dot get components

get components in children you want the plural form components not component and inside of these angle

brackets we'll do.

Aircraft agent

and then in this form what it actually returns is a an array of aircraft agents we want this as a list

form so we can say to list and as long as you capitalize this correctly you can hit control period and

you can do using System dot link so that that will allow this functionality that allows us to turn it

into a list.

Now let's add a little helper for us just in case we forget to add some agents to our area.

So we'll say debug assert.

So what this is going to assert it's going to make sure that it's true that aircraft agents account

is greater than zero.

And if it's not it's going to say no aircraft agents found.

So that's just going to help us as we're building out our scene if we ever forget to create this we'll

get a little warning their message and then we'll say aircraft Academy equals find object of type aircraft

Academy.

So it's just gonna find an aircraft Academy in the scene for us so that we don't have to do any sort

of manual hookup.