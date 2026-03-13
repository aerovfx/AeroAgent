# Creating a Snow Scene

So we've got this cool menu.

We've got a desert scene.

Unfortunately that's all we have.

We don't have another scene to test out this drop down menu and if you get bored of playing with the

desert then you've got nothing else to play with.

So let's create a new scene.

And what I'm gonna do is reuse the terrain and the rocks will create a completely different race path

and we'll place the rocks differently.

But we can create a completely different feel of a level without even creating any new assets in blender

so let's take a look inside our desert scene.

There are a couple things or there's like two more things that I think we want to make into prefabs

before we do this.

So let's go into our prefabs directory.

We will take this global volume and we'll drag this down so that this can be a prefab so we can just

drop that right into another scene and then this camera combo the virtual camera and the main camera

let's create a new empty.

And we'll call this camera manager.

Technically there's nothing really being managed but I can't think of a better name right now.

So then we'll drag this virtual camera underneath it and then the main camera underneath it and then

we can take this down and make a prefab out of that too.

So the only thing that's not a prefab right now is the directional light and then we can save our scene.

And just for good measure you might want to play it and then make sure that the camera's still working

properly.

If this isn't like if you didn't do this properly I'm not sure if it'll you know if the camera will

get moved over properly but this seems to be working so I think we're good now let's create a new scene.

So we'll go into our scenes folder and you can ignore this desert photography one I was using that to

take some screenshots for the course.

You can right click Create scene and we'll call this one snow.

We're going to make a snowy terrain so you can open this up and let's get basically let's duplicate

the desert right now and then we can make sure that everything we need is there.

So we'll go to prefabs.

We of course we will first of all let's delete the main camera.

We don't need that anymore.

We just need the directional light.

We need the desert area.

We need a game manager we can do the global volume we need the aircraft Academy we need the race manager

basically all of these things and the camera manager doesn't really matter what order these things go.

And then I think we just need to build lighting so we'll generate lighting and then you can test out

your scene and save it as well and then we'll just click play just to make sure that everything is functioning

fully so that we can start modifying this.

OK so there is one thing that seems to be off.

We have a new player that has entered the game so now there's five of them which you know is kind of

cool but maybe isn't exactly what we're looking for.

So I will disable that one last time.

One last player.

So in desert area I'll turn off this one in the inspector I'll just uncheck that.

So now.

Now we have only four of these that should start up when we click play and we can begin modifying this

scene.

So let's just double check.

All right.

That seems to be better we only had for that time.