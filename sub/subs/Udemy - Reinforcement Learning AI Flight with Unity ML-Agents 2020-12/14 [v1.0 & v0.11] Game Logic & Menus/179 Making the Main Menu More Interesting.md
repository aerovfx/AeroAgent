# Making the Main Menu More Interesting

I mean the main menu scene right now and it's pretty boring.

If we look at the game tab it's just this horizon with blue sky.

It'd be pretty cool if we could show an airplane flying in the background.

Well it turns out it's actually super easy to do that the way that we've designed this.

So if we go into our aircraft folder and we go to our prefabs folder we can actually drag a desert area

into the scene and we can drag in an aircraft Academy and now actually let's go to the lighting settings

and remember that's under window rendering lighting.

Then we can just click generate lighting so that this is for sure updated

and it's taking a moment but then all we need to do once that's completed is make sure that our area

doesn't have any player agents in it.

So we want to make sure we turn off airplane player so I'll go to the inspector and uncheck this but

there's no race manager in the scene there's no UI so it shouldn't compete with this UI.

And if we save the scene as long as believe we need to have a virtual camera in this scene too.

So let's add that too.

So we've got to send a machine create virtual camera and we probably want a copy.

Well we we can see what this looks like.

So we just need to set the follow to follow and look at transforms here so I'm going to pick the red

airplane for this one so I'm going to drop this in here and here and then.

Now this game is going to follow this red airplane so we can we can mess with this however we want we

could actually have this in front of the airplane if we like we could have it really high up in the

air you know something like that maybe to just make it a little different.

So let's let's hit play and we'll click away from the virtual camera.

Otherwise you're going to see this red outline around it.

And then when we click play it should actually just play.

And these four agents will just fly around in the background while you're deciding on your options.

So this is you know it doesn't look amazing right now.

There's a couple things we could do we could add a global effects volume that would add some Bloom to

the scene.

So that would be probably worth doing.

I'm going to experiment a little bit with this and maybe put this more in front and back up even more.

You know you can really play with this however much you want.

You can have it be right in front.

I actually like the way that looks a little better and then probably I just want to fix the yard damping

a bit so that it looks a little smoother

so that's pretty cool.

So now you know you're not just sitting here looking at a boring horizon you're looking at airplanes

flying so let me just fix that really quick.

I think I set this to two and then this was set to 1 and then can save.

Let's add that affects volume to the scene so we're gonna create a let's see volume global volume and

then we just need to pick that aircraft volume again and then that should turn on the bloom.

And I think I had motion blur off because I was taking some screenshots.

You know leave it on or off depending on your preference

and then.

Now we have this more interesting menu that we can have for our players which I like quite a bit

it looks like I'm closer to the to the plane so I might fix that but other than that I'm looking pretty

good.