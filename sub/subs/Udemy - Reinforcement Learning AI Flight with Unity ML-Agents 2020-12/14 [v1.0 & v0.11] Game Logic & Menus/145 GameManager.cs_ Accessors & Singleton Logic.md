# GameManager.cs_ Accessors & Singleton Logic

So now that was all done outside of the class.

Still inside the namespace but outside of the class.

Now inside of the class we're going to add a public event

on state change handler.

So we're using this thing right away and we'll call it on state change.

And this is the actual event and we can add a comment for this event is called and the game state changes

we'll need a private game.

State and then game state.

Make sure you get your capitalization right and then we're going to have a public game.

State access or you can just see that the capitalization is different here.

We're gonna have a get and this is going to return game state so it's returning this variable and then

a set

which is going to set game state equal to value.

And then if on state change does not equal no we'll call the function on state change.

You have to do this little check her out.

Sometimes you get some errors when you're when you stop your game for example or load a different scene

so we'll add a quick comment for this current game state

then we're going to add an access or for public game difficulty and this will be called Game difficulty

and we don't need a private variable for this because it's just going to be a standard Get set.

This is just a shortcut to do that.

We don't need to do any like events when we set the difficulty to something different it's just a straight

up.

Basically access to a variable now we're going to add a public static game manager instance we're creating

what's called a singleton and this is not something that special to unity nor is it even special to

C sharp.

It is just a programming pattern that allows you to avoid having more than one instance of this in your

environment essentially.

So what this will do is it.

It will allow us to have one game manager that lives throughout the entire life span of our game.

And even if you try to access a game manager somewhere else or have a new one in a scene it will immediately

get rid of itself.

So we'll add a comment.

The single ton game manager instance and if you're more curious about how this Singleton thing works

just you know get on the Internet search for a singleton or even unity Singleton and you should get

some more information about what they are and how they work.

So this one's just going to be a get private set

now it gets interesting in the wake function.

So private void Awake and I'm actually going to add a comment here manage the single ton and set full

screen resolution.

So first thing we do is if instance is equal to no meaning this has never been called before.

This will be the first time we've ever called a game manager for instance we'll say instance equals

this meaning it's equal to this game manager don't destroy on load.

That's a special command to unity that says hey don't destroy this thing it's important so we pass in

the game object that this is attached to.

And then this is a good time for us to set the screen resolution to full screen.

So we're gonna do that screen dot set resolution screen dot current resolution dot width screen dot

current resolution height and then this one is full screen mode we're gonna set it to true

and then we'll have an.

Else

destroy game object.

So basically what's happening is if we call game manager for instance or rather if the if there's a

game manager that loads up in a scene once it wakes up it's going to check to see if there's already

a game manager in existence and if there is it's going to destroy itself.

Otherwise it'll set itself up like this.

And one more thing related to the instance right here we're gonna do a public void on application quit

and if the application quits we just want to set instance equal to null.