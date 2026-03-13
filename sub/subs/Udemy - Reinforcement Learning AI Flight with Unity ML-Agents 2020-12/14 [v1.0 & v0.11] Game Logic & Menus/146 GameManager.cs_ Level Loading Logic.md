# GameManager.cs_ Level Loading Logic

OK we're almost done with this class.

Actually we're just going to add some logic for loading levels.

So public void load level.

So this is a new function that we're creating string level name and then Game state new state.

So what this is going to do is it will load a level and then change into a new game state.

And so let's add a comment loads a new level and sets the game state

level to load the new game state and inside here we're going to add a new well I didn't mean for that

to happen.

All right we're going to do start co routine and we're gonna do load level async and we'll pass in the

level name and the new state so this function doesn't exist yet but we're gonna create it.

And the idea is we load this level but we don't stop the code we allow it to load in the background.

And so we have to create a second a second function to do this.

So this is going to be a private eye and numerator not an enumerable but in the numerator load level

async and then it's gonna take in these same parameters so I'll just copy them and paste them.

I don't see any reason to really duplicate this comment.

So I'm just going to leave it without a comment so in this part we're going to load the new level

we will say async loops a sink operation Operation equals scene manager and I don't think it knows about

this.

So let's do control period and we'll do the suggestion using Unity engine not scene management scene

manager Doc load seeing async and we need to pass in the level name

then we're going to say while operation dot is done is false

we're going to say yield return no.

So what this is going to do is it's going to keep doing this loop and yielding to whatever other code

wants to run until the operation is done.

So once this level's loaded then this code will resume down here.

So at this point we're gonna set the resolution seems for some reason that when you load a new scene

it doesn't automatically remember that you wanted to be full screen.

So we're going to do that here screen set resolution.

And actually when we copy this from up here we want it to be the same thing.

So I'm just going to copy all this pasted in here and add a semicolon at the end and then we're going

to update the game state.

And this one's pretty easy we're gonna say Game state equals new state.

And remember since we're using the capitalized version of this this will use the access or appear this

game state.

And when we set it it not only will set the value but it will also if anyone's listening it will call

this function right here and fire off that event so that should wrap up the game manager class.