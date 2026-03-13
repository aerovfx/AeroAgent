# MainMenuController.cs_ Hook Up UI, Build Manager, & Game Manager

So let's go back into unity and let's hook up these UI items to those functions in the script so we

will need to add our our script to this canvas.

So let's go into our scripts directory and then let me select this again and we'll do we'll drag this

over on here and I'm going to rename this to main menu canvas

and then we just need to tell it what levels there are.

So we'll say dessert as if to say how many there are first then hit enter and then we can put in dessert.

If we had more let's say we had three then we could add more.

But right now we only have one level so we're just going to say one that we need to give it the level

dropdown and the difficulty dropdown.

So let's drag this here and here OK so it knows about these it's going to be able to populate them.

So let's just see what that looks like.

We hit start

now it's showing up as dessert which is cool and normal or we can choose hard.

And then if we click Start or quit they don't do anything because we haven't hook them up yet.

So let's do that first let's let's look at the level dropdown and if we scroll down we can see it has

the three options here which we of course replace and then it has this on value changed area.

If we click the plus button we can choose something to call functions on.

So click on this main menu canvas and drag it down into this little box here that's gonna give us give

us access to the script that's attached to it.

That main menu controller and we want to call Main Menu controller set level for this first one and

then you can just leave that zero they're going to do the same thing here.

So we're gonna do this.

We're gonna drag the main menu canvas here.

We're gonna call Main Menu controller Dot.

I guess it's suggesting it for us up here but let's do set difficulty.

Well let's pick this one.

I don't know what that dynamic in one means but this should set it.

So now we need to do the buttons and we'll add an on click event here so we'll go to plus and then we

need to do this main menu canvas again and we will call Main Menu controller start button clicked and

then for this one the equipment.

We're gonna do the same idea.

Take this down and then we'll do the quick button clicked.

All right.

So if we save this now we can play again.

We have this setup.

If we go start then it's gonna try and load something it's going to say no reference exception.

The reason for this is because the I believe it's because we don't actually have this added to our build

settings yet.

So let me show you how to do that.

But we can also we can hit quit and well that's not hooked up either so I'm not sure why that's not

working but I definitely know why this scene isn't showing or we're not able to load the new scene.

So let's let's fix that.

You go to file build settings we need to add this open season so we're adding the main menu to this.

Then close this down.

We want to switch over to our dessert scene and we need to add this to the build settings as well.

So build settings add open scenes and then we can go back to our main menu and we should be able to

start that level now

still getting a no reference exception.

Let's see if I can figure this out on the fly.

So we're calling start button clicked and we're getting a null reference exception.

So this is on line 55.

So we're saying game manager instance state game difficulty.

OK here's the issue.

So we need to add a game manager or else it's not going to be able to use the game manager which makes

a fair amount of sense.

So let's create an empty.

We'll call it game manager we'll set it to 0 0 0 and we will add a component game manager and now I

think it'll work

click start and it says desert is loading and there we go.

Now we're in the desert.

So that's pretty cool.

We now have a menu scene that will take us into a level that we pick from a dropdown.

And of course that you know the difficulty doesn't it's not hooked up to anything and there's no way

to get back to the menu but pretty cool that now we have this main menu working.