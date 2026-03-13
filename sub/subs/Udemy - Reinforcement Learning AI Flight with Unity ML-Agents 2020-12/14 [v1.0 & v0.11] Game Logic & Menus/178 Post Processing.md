# Post Processing

Earlier in the course I mention adding some motion blur for the propeller.

So we're going to try and do that now so we'll right click in the hierarchy and we need to create a

volume global volume.

Now this volume is something that's going to apply post-processing effects to any cameras that are in

the entire scene.

That's what global means.

So I'm going to just position this at 0 0 0 and then it wants a profile and it turns out we actually

already have a profile in our project because we never deleted the one that came with the template for

a universal render pipeline.

So assuming you still have this you could just write or you could just click and drag this in to your

profile field here but nothing actually happens.

So what we'll do is go into main camera and then you have to actually tell it.

Yeah render this post-processing processing so we'll check this box and something shows up it doesn't

look very good because that scene profile wasn't really designed for this scene but you can tell that

it's at least on.

So that's a good place to start.

Now we're not going to use this one.

We're gonna create our own so we're going to right click and create a volume profile and we'll call

this aircraft loops.

Well maybe we'll call this dessert.

I'm on the fence.

I'm going to call it aircraft volume for now and it might be the case that other scenes need different

settings.

And so we might have to rename this to desert if we in the future ever add any more scenes to this game.

But just just know that.

So I'm going to add a couple overrides to this volume that I've now got selected and I like to add Blum

and let's right now come in here and update this profile to use this so if we select this then we can

kind of mess with the bloom settings.

So I'm going to turn on the threshold and intensity and what you can do is kind of play with this to

see if you can find a spot where you like it.

Obviously you can go way too strong on this and then it just looks like you're inside of a light bulb

or something or you can go a little more subtle you know maybe somewhere around point five for this

and then you'll get something that looks a little more glowing like I can turn it off turn it back on

it just kind of brightens up the scene makes it reflect the light a little bit more so I'm gonna keep

it like that you can also mess with you know these different settings the scatter tent whatever this

works pretty well for this scene seems And then there's another one under post-processing called motion

blur now this one unfortunately I was a little disappointed wasn't quite working the way I hoped but

I will show you kind of what it looks like.

So if we could play we need to do this so that we'll actually see it.

Spinning course it's a little difficult to watch it while it's flying.

So what we can do fortunately is pause the game and we can still see all these propellers spinning and

if you turn on quality and intensity you probably don't want to do low quality unless you're targeting

a lower end device.

I'm just gonna put mine on high and see if I can get some decent results and then kind of increase this.

You'll notice even if you put it all the way up like the propeller I'm not sure.

Hopefully the video is capturing this.

The propeller doesn't seem to look much more blurry to me than it did before.

And the downside is if we resume suddenly the game looks a lot worse because it's trying to process

some blur on this while they're turning and stuff.

And in general I'm just disappointed in how it looks so I'm going to turn it way down and resume the

game and then it at least looks okay now.

And then if I turn this off honestly can't tell the difference.

So you know you might have better results than I do with yours.

But just wanted to show you that that's how you could add motion blur to this if you wanted to experiment

with that.

I'm not sure if maybe it has something to do with how fast this is spinning it's just too fast for it

to properly detect.

I've never had to work with really fast moving objects like this before.

To be honest with you but that should kind of wrap up post-processing.

One last thing that you can experiment with.

Let me just pause this really quick.

These edges right here.

So that's called aliasing where you can kind of see the pixels the pixilated edges.

There is something you can do about that.

The being camera has something on it.

This anti aliasing and you can turn this on and watch those pixels.

It kind of smooth zoom out a little bit more.

So that's something that you may want to have on depending on your quality settings and you know it

looks a little bit smoother.

So I think my frame might frame rate might be dropping a bit.

Let me turn on stats so my frame rate is still eighty eight eighty six frames per second so that's not

too bad.

I don't think that I need to worry too much about that.

If I were to dip below 60 then I'm not sure that that would be worth it.

But let me experiment.

If I turn this off it does.

It does go up a little bit briefly but it doesn't seem to stay really much higher.

So I don't I don't know that I'm necessarily

saving any frames by turning that off.

So just a little trick that you can do to increase the sort of cool factor of your game just add those

post-processing effects and the anti aliasing.