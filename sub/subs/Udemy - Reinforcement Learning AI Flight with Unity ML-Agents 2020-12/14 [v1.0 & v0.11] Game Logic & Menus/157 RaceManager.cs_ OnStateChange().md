# RaceManager.cs_ OnStateChange()

Now we created a bunch of red squiggly lines in here so let's fix this.

Let's see if there's a potential fix for this generate method.

Race manager Don on state change that sounds promising.

Let's try that.

So now you've got this on state change method.

Let's give it a comment we'll say react to state changes.

Let's do this for start race and pause and put performed as well.

So we'll two quick actions generate this method and then we'll do this one and we'll generate this method

and these are kind of out of order.

It doesn't really matter what order these show up in so for on state change we're going to say if game

manager instance that game state is equal to game state playing.

So this is basically saying if we're playing and the state changes or rather if if the state changes

and it changes to playing then we're going to start slash resume.

Game time show the HUD a heads up display and thaw the agents so we're gonna say last resume time equals

time that time HUD.

Game Object set.

Active true and then we're going to say for each aircraft agent agent in aircraft area dot aircraft

agents agent dot thaw agent.

So what that'll do is thaw out all of the agents.

Now we'll say.

Else if game manager instance game state is equal to game state DOT paused

we're going to pause the game.

Game time actually frees the agents so we'll say previous.

Here let me scope scroll up.

Previously elapsed time plus equals time that time minus last resume time.

And we'll say basically the exact opposite.

So I'm going to copy this

and we'll say Agent Dot.

Freeze agent so we're gonna freeze them in time when we pause the game.

Now we need to do this for Game over.

So I'm gonna take a little shortcut here.

Copy.

Basically up through the dot and came over is the one that we want for this one.

We want to pause game time hide the heads up display freeze the agents so this one we're pausing the

game time again.

So let's just copy this.

It's the same thing we're doing with the time when it's a HUD game object set active false and we're

gonna freeze the agents.

So let's copy this to freeze them and then we need to show game over screen so we'll see.

Game over UI dot game object set.

Active true

and then the last.

The final instance here.

Else I must say absolutely make sure that's on a new line.

And then we'll say reset time last.

Resume time equals zero f previously elapsed time equals zero f.