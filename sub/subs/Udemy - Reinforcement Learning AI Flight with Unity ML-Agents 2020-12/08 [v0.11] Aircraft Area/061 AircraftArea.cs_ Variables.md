# AircraftArea.cs_ Variables

So all this time I've been alluding to these scripts that we're gonna write that are gonna place the

checkpoints.

Well let's write some of that code so we'll go up into our aircraft directory and create a new folder

and we'll call it scripts

inside of scripts.

We're gonna create a new C sharp script and we'll call this aircraft area and you can double click that

to open it up with Visual Studio.

So first of all if you haven't used this very much there's basically two ways to fight or three ways

to find files in this project.

So one is you can find it inside of here you can double click it to open it.

The other is it shows up in the solution explorer.

But there's a bunch of other stuff in here like the the files are in here but it's kind of more of a

mess.

There's also the Unity project explorer.

That's a clean way to see all of your scripts.

So just wanted to point that out.

So this aircraft area script the first thing we're gonna do is place it in a namespace namespace aircraft.

And what this will do is it'll just sort of separate our code from other code and make sure that if

we write any code that conflicts or otherwise would conflict with some sort of name somewhere else in

a simple asset or something like that that there's just no conflict so now inside of here we're going

to start adding some public variables that we can see in the inspector.

So we're gonna create a public cinema machine smooth path and you won't have this yet.

It's actually going to give us this red squiggly line.

And if you hover over it it just says it doesn't exist.

So there's show potential fixes so you can.

What I usually do is this control period shortcut.

So control period and then it's going to suggest that we add this using Cydia machine.

So I'm going to hit enter and then it's going to add that up here.

So now it's happy and this will be our race path.

So we're going to tell it what our race path is so that it knows where to place the check points let's

add a tooltip to this and we'll say the path the race will take so this tool tip will show up if you

hover over it in the inspector view in unity.

Now we'll add another one public game object checkpoint prefab

and this one will add a tooltip the prefab to use for checkpoints

and then we've got another one public game object finish checkpoint prefab

will add a tooltip for this as well and it'll say the prefab to use for the start slash and checkpoint

and then we're gonna have one more public variable public.

Well I should say we should.

We'll have one more public variable that'll show up in the inspector.

That's something that the user can modify.

Public bool training mode.

Now we are gonna use this boolean to basically track whether we're training our agents or not.

And it's gonna behave differently depending on that so we're add a tooltip for this that says if true

enable training mode.

Now let's add three more really quick we're gonna have a public list of something called aircraft agent

which doesn't yet exist.

So don't worry it's gonna complain but we're gonna we're gonna fix that and we'll call this aircraft

agents and we'll use the shortcut syntax for this.

Get private set so we can get this externally but we can only set it inside of this class.

And we're gonna do a public list game object we'll call it checkpoints

and this will also have a get a private set and then we're gonna do a public aircraft Academy.

So this is another script that we don't yet have but we will be creating momentarily and we'll call

it aircraft Academy and this will also be a get a private set ordinarily I would add comments for these

but they're pretty self-explanatory especially the way that we use them in code.

So I'm not going to bother adding the comments for these.