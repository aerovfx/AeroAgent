# Rotate.cs for Checkpoints & Propeller

Now we'd like these checkpoints to rotate so let's add a new script to do that.

So we'll go into scripts we'll create a new C sharp script and we'll call it rotate.

Now this rotate script.

That's a pretty common name and there's a high probability that rotate might be used somewhere else

in your project.

So that's where the beauty of using a namespace comes in.

So if we say namespace aircraft and we put this inside of there then in the event that there is a conflict

as long as there's nothing else called rotate in this in this namespace then we don't have to worry

about any conflict.

So since we're here and since we didn't do it already for I think it was the agent class or the Academy

let's just add that now namespace aircraft.

So adding that to the aircraft agent code and if you if you place this down here it should automatically

tab in and if you're wondering where these dots came from.

These are actually visible whitespace.

So I believe it's under edit advanced maybe view whitespace there's a basically just something that

makes it so that tabs will show up as arrows and then just spaces show up as these blue dots.

I find it helpful for organizing my tabs and making sure that things are indented the right amount of

space so I'll save this and then also need to do this for the Academy.

So open up the academy and then I'll do namespace aircraft

OK.

So now rotate is gonna be a very simple script so you can keep the update function but delete the rest

and we're just going to create a public vector 3 and we'll call it rotate speed and then we're going

to in the update method say transform dot rotate new.

Sorry we don't need to do that rotate speed and then cell space itself.

OK.

So what this just says is I have an extra parentheses what this says is rotate by this amount in the

local space.

Every update so and actually we probably won't rotate speed times time dot delta time because otherwise

if the frame rate changes then the speeds gonna be different so let's apply this script to our checkpoint.

So if we go into the prefabs we find our checkpoint we can double click it to open it and we can add

the rotate script and we need to figure out what speed to set this to.

I don't really have a good idea of what speed to set it to so we're gonna just pick a speed and see

how it goes.

So we're gonna try doing a speed of one and we want it to rotate around the z axis that blue axis.

So that's why I chose Z.

And then let's click play and see what that looks like okay.

So you can see that they are moving but like super slow.

So I think what I can say we're in play mode so any changes we make to these this probably won't make

any difference.

So we can experiment with this so let's try 10 OK.

That's that's pretty good.

Maybe 30 actually think that's a little too fast or maybe 20.

All right.

I'm going to go with 20 for this.

So we'll keep well we'll unplug it hurt click play again and then we'll go back into the check point

prefab and then we'll set this to 20 and then we also need to do this to the finish line so we can open

this up at a rotate component and then we'll also do 20.

Now we can actually reuse this rotate script.

We can go into our airplane and we can do the same thing with the propeller and added rotate and this

one we're probably gonna want it to move quite a bit faster.

So let's try to one hundred and just see how fast that looks.

We do want to make sure that we're focused in on this airplane and that we can see it but I think we'll

be able to see it because we're for our cameras right behind the airplane already.

So we'll just hit play and see how that looks.

All right.

So two hundred does not seem to be fast enough.

Let's experiment with it.

So if we open up this and let's just multiply this by 10 OK that looks pretty good.

We might be missing out on some frames but I think that probably two thousand is going to work for us.

I'll try one thousand just to see what that looks like.

Yeah that's not fast enough.

And five thousand.

I'm curious I've never gone this high with it before but yes you then at some point it just starts chopping

out you start missing frames so

2000 probably is good enough.

All right.

So now I just need to go into this airplane and we need to find the propeller and just set this to two

thousand and we'll probably want to put some sort of motion blur on this at some point probably not

until the very end of the course but that will make it so that this looks a little more natural because

right now it's just showing every frame and it's not showing any real blur to it OK.

So that'll do it for our rotate script.