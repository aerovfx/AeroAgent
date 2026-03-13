# Desert Terrain & Rock Prefabs

Let's start using these assets a little bit.

So the first thing I want you to do is right click in here and we're going to create empty and this

is going to be called our desert area and we can set the position to 0 0 0.

We are going to now bring this desert terrain into this desert area.

So drag it right on top.

And now it's a child of this desert area so you can see this is now in the scene which is great but

we want to add a material to it or else it's not going to look very good.

So let's hop back up to our aircraft directory.

We're going to create a new folder

called it materials inside of here we're going to create a material and this is going to be called sand

and then move the smoothness down to zero so that it's rough.

And we will change the color of this to something kind of in the yellow ish range color that I found

that I liked was 255 to thirty one one sixty five so that's the specific color that I thought looked

pretty good.

So we're going to accept that and then we need to drag this material onto our sand.

So now this desert terrain is looking OK if your lighting doesn't look quite right.

I think I may have actually done this already but you can go into your lighting tab and if you don't

have the lighting tab go to window rendering lighting settings and then you can hit generate lighting

and then it will generate lighting for your scene and then it should update update the way this looks.

I've recorded this video more than once.

So that's why my lighting was already built in this case.

So now let's add a few more things to the scene.

So we're going to go into our meshes again and let's import a rock.

So we'll choose the let's go with the rock em underscore 0 1 and we will put this into our desert area

as well.

So right now this rock doesn't have any collision on it so it's probably a good idea for us to do that

right away.

So we're gonna go into the inspector tab.

We're going to add a component and this will be a mesh collider and by default what will happen is it

will use this mesh for its mesh collider.

Unfortunately that's a little bit more complicated than we want.

So what we want to do instead is pull in our respective rock em underscore 0 1 collider and while we

can't drag that directly we have to expand this.

And then we can choose this this mesh and either drag that in there or you can choose it from here.

So like this is what it's by default.

Move it to this and then it's going to be quite a bit simpler and we can also change it to convex and

that will simplify it even further.

So now we have this rock that doesn't have a material on it but it at least has a collider on it so

let's go into our materials directory and create a new material for it.

And I want to point out for some reason sometimes these these aren't updating immediately for me like

it was still showing Gray there for a moment.

It does seem to at some point update we're gonna create a new material and we'll call this rock

and we'll move this move this all the way down and we'll set the color.

We want something sort of in the orange range over here.

But the one the color that I have that I like is to twenty six one fifty three and 1 0 8.

So it's kind of like a reddish mud color and then I'm going to apply this to the rock.

So now you can see in this scene kind of expand this a little bit.

How the rock looks next to the sand and I think that the the contrast with the blue sky and the yellow

sand and the sort of reddish brown rock looks quite nice.

So you're welcome to of course experiment with this as much as you like but these are the the the look

that I like so this rock.

We've changed a few things about it and we're gonna want to use this rock.

A ton of times in this environment.

So rather than have to do that manually every time let's create a prefab for it and we'll create a new

prefab folder inside of our aircraft directory.

So create a new folder prefabs and then let's rename this to have capital letters in it.

And that will be one way that we can tell the difference between what is just an imported mesh and what's

a prefab.

So we're gonna take this drag it down into our prefabs directory and then we can say original prefab

and then it'll save those save that mesh collider on there with convex and everything so that when we

want to add one to our scene we can just go like this.

And then we have a rock that's matching those exact settings.

Now we have two of these and if they're both inside of desert area it's fine when there's two but if

we were to start getting more than two then this is going to get overwhelming.

So we will make sure that this is organized a little better.

But let's first go in and we can do the rest of our rocks the exact same way.

So I'm going to just delete this for now and let's go back to our meshes we'll create one for the flat

rock.

So let's put this here and you can see that it places it kind of in the same spot.

That's fine.

Not a big deal.

We will just hide this one for now.

Actually we can just delete it.

We don't need it so same thing.

Let's add a mesh collider and let's select the rock f collider we'll set it to convex and then we'll

apply that material that we had to it the rock material we'll rename this to have capital letters and

then we'll go into our prefabs and drag it down and create an original prefab and then I'll delete this

and then we'll do our last rock that we have here in meshes we have this rock t so drag the sand and

then we will add a mesh collider to it will choose the correct collider.

Set it to convex and then rename it to capitalise loops.

Make sure I get that right and then we'll apply our material open up our prefabs and then we'll create

an original prefab and we can delete this and for good measure we'll save our scene.

So now we have our three rock prefabs ready for use.