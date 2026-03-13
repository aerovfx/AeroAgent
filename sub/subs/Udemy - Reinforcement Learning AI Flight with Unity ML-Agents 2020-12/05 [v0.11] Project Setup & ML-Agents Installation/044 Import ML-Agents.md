# Import ML-Agents

Once it's open you're going to see this sort of construction scene.

And if we're in the scene view sometimes it'll be this sort of blue cyan color while it's auto generating

lighting.

And here it's still kind of.

So just know that it might take a little bit of time.

Now there's a lot of stuff in here we're not gonna use any of these assets.

The only exception is there's some settings in here for the universal render pipeline that we're gonna

keep.

But everything else we're going to delete before we do that let's create a new folder and this folder

is going to be called aircraft and then open that up and create a new folder called scenes.

So we're gonna keep all of our assets and scenes and scripts and everything separate from the rest of

the code by doing it inside of here.

So we're gonna create a new scene and we will call this desert.

This is going to be the level that we're making for our airplanes so open this up.

And the reason we're opening this up is so that when we delete all of those other assets then that scene

that had all the construction stuff in it is not there.

So now make sure you do not select your aircraft folder but you can hold down control and you can select

the rest of these.

With the exception of the settings directory as well and then you can just hit delete and it will remove

all of these

and now those are gone.

And we want to import our MLA agents directory from the assets.

So we want to go into the MLA agents folder and then go under a unity SDK assets MLA agents and then

we do just loops.

We want to click and drag just this folder down in we don't need the DOT met a file.

Unity will create a new dot metaphor file to keep track of this on its own.

Now we're importing all of these assets.

We'll have all the examples in here.

We don't actually need most of the example content but there are some scripts and things in there that

we will want to use.

So we're not going to delete them if you need to clean up your project just do some experimentation

because there are some things that our project will use from the examples directory and then I wanted

to show you there is kind of one problem with this importing this.

I've realised that if you open up one of these scenes the materials get messed up which is why we when

we were looking at the examples we didn't do universal render pipeline if you for some reason do want

to look at this scene for reference you can go in and find the materials that are attached to these

things like here the basic agent the cube has this pink texture on it you can replace it for some reason

at least on my machine it's choosing this Autodesk interactive shader I'm pretty sure if I were to switch

it back to the let's see the universal render pipeline lit then the material will show up correctly

but now the colors off anyway we're not going to go through that we're not going to worry about it we

if you want to look at the examples just open it without the universal render pipeline let's go back

into our aircraft scene here and we can start working on our project I also want to point out I get

some error messages when I try to import the that project you might get some warnings and error messages.

These are probably fine these are just the example files coming in and none of this you know we don't

have any code in this yet.

So if you get some error messages don't don't panic until something actually doesn't work and you can

always clear this and then make it look nice.