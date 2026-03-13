# AircraftAgent.cs_ Add Script, Rigidbody, TrailRenderer to Prefab

Now we're going to add our first function.

So this one's going to be a public override.

And let's pick initialize agent and I'm going to skip over adding a comment to this because it's basically

we're just initializing the agent.

So the first thing we'll do is say area equals get component in parent and we want to get the let's

see which area of the aircraft area

so this no matter what the agent should be a child of an area.

So it should be able to find the area component in its parent that we need to set the rigid body equal

to get component rigid body and then we're gonna set the trail render so trail equals get component

trail renderer

and since we just added those here let's go make sure that they're attached to our object in the game

so that we don't forget these so we'll switch back in here and we'll open up our airplane prefab and

then on here.

Let's go ahead and add our airplane our aircraft agent script to it and we need to also add the rigid

body don't do the 2D one make sure you do the regular one we're gonna set the mast to 500 and the drag

two 5 and the angular drag to 25 turn off use gravity because we're gonna cheat we're not going to make

these things fall automatically and then we're we're gonna do under constraints if you expand this do

X Y and Z for the freeze rotation line and then let's add a trail render

and for the trail renderer we do need to add a material for this to look good.

So let's go to materials and we'll create a new material and this is going to be the trail and we're

going to make it transparent and we'll also set let's set the visibility here.

Let's set this all the way down to Alpha at zero and we'll set it to black.

We'll put the smoothness all the way down and then we'll use a mission for a white trail here.

But let's see if we can do what we need to do our alpha.

Probably like here and we might as well just put it on white.

OK.

So if you didn't follow Sorry that was about halfway on the alpha then it's white in color and then

we put some emission on it as well.

So hopefully this will update we can always tweak it if we need to.

But let's go back to our airplane prefab here and then under trail render we need to drag this in and

put the trail material on their so these will automatically be pulled in.

And when we added that aircraft's agent there was some an additional thing that kind of popped up and

we'll get to talking about that shortly.