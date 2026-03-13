# AircraftAgent.cs_ OnCollisionEnter() & ExplosionReset()

Let's handle collisions now.

So we handled what happens when we fly through a trigger.

But we need to handle what happens when we fly into something like the rock or the ground or the sky

or something or not.

Another agent or that's the one exception we're not gonna crash it me.

We're not going to blow up immediately if we hit another plane because that might get a little frustrating.

So we're gonna call this private void on collision enter.

This is another special method that gets called automatically on collision and the first check we do

is if not so the exclamation point.

Collision dot transform that compare tag agent.

OK so we're checking to see if this thing has an agent tag specifically actually I should say that it

does not have an agent tag because if it does have an agent tag we're just going to ignore it and I

forgot let's add a comment here.

React to collisions and this collision parameter here is collision info all right.

So immediately you'll notice that we probably need to add a tag to our agents.

So let's go in here and we will wait for it to go and then we'll open up our.

The only agent that we have so far this airplane player and this needs to be tagged we'll add a tag

agent we'll save that tag then we'll go back and then we'll apply that tag to this player.

Now let's try our best not to forget to add the agent tag to the learning airplanes when we like the

A.I. airplanes.

I'm going to try my best not to forget that.

So I'm mentioning it now.

And if if I forget it just know that there will be problems.

Well they'll just explode as soon as they hit each other which maybe isn't a problem maybe that's just

funny.

I don't know so inside of this function we'll say we hit something that wasn't another agent and we'll

say first of all if area training mode then we want to add a negative reward and that negative reward

is going to be one point and then we'll say done and return so we'll just make sure that if we collide

with anything that's not another airplane then just we're done and we're not going to do any special

fancy explosions or anything we're just going to reset because once done is called it's gonna call Agent

reset automatically.

Now we'll say else oh and I should mention the reason why when you call done Agent reset is automatically

called is because we have this box checked here reset on done reminds me I think we might have up above

said done somewhere and then agent reset.

This is actually unnecessary.

So we can remove this.

This is in Agent action.

We.

This would be redundant.

It would actually reset twice in a row.

So we probably do not want to do that.

So we just called on so we'll go back to where we were down here at the bottom.

So if we're not in training mode we're gonna start a CO routine

and this co routine is going to be our explosion reset and we need a CO routine because this is going

to take a few seconds to run and we don't want to stop the code while it's running we want this to just

kick off an explosion reset and then pick up where we left off.

So we're gonna let this generate the method for us and it's not a string.

It's actually an I in numerator

and this is going to be let's see resets the plane.

Well we'll say aircraft to the most recent completed checkpoint I'm intentionally trying to call it

aircraft more because I think there's potential for different aircraft not just airplanes.

So hopefully I'll be able to add some cool stuff in the future returns and this is we'll just say yield

return because that's kind of how these these things work.

If you're not familiar with how code routines work they're pretty cool.

I'm not going to get deep into how they work but they basically allow you to run code sort of sort of

asynchronously so you can start something and let it go and not block other code from running so in

here first thing we do is freeze agent.

OK so the we're about to show an explosion so we don't want the agent to keep moving.

So that's that's number one.

Then we want to disable aircraft mesh object and enable explosion so we're gonna take that mesh object

that we hooked up earlier and we're going to hide it.

So we'll say set active false then we'll say explosion effect dot set active true and then we're gonna

do a yield return new wait for seconds and it will pass in two seconds.

So to F..

All right.

So what this will do is it'll it'll stop here.

It'll wait for two seconds and then it'll pick back up once.

Two seconds has elapsed and then we'll say disable explosion re enable aircraft mesh so we'll say basically

we're doing all this stuff again so I'm gonna copy this just to save a little bit of time and we're

gonna set active to true here and false here.

So just the reverse.

And then we also want to do area dot reset agent position and we're gonna pass in our agent is gonna

be this OK and then we will only wait for one second.

So it kind of as soon as you get back to the checkpoint then it will only make you wait one second before

you can start going again.

And then the last thing is to thaw agent so essentially the what it does is it freezes the agent disables

it and it shows an explosion for two seconds and then it disables the explosion Reid shows the airplane

again and then we're off and racing again.