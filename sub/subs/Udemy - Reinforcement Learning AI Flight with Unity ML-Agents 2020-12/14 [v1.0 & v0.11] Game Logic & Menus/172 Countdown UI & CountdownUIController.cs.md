# Countdown UI & CountdownUIController.cs

Now we're going to add our countdown UI.

So let's right click on race manager to UI and we need a text mesh pro text option this one.

We'll name count down UI and we only have one text object in here but I'll still name it count down.

Text and this is kind of hiding behind the resume thing.

So let me just hide this temporarily and I'll hide the HUD temporarily too so we can at least see what's

going on.

So this text we're going to want it to be centered and centered like that and we're going to want it

to be pretty huge.

So let's try a font size of 200 which of course doesn't look very good.

So let's see what it's actually going to show.

This is where it's going to show three two one go.

So three two one go Oh.

So that doesn't work.

So we do want to make sure that we update the with this that this fits on the screen.

So I'm just going to keep going.

OK.

So like I'm just gonna make this 500 and we'll make this five hundred two for good measure.

So if we go to the scene view it's it's gigantic.

Maybe it doesn't need to be 500 by 500 but it's going to be centered at the middle.

And now we have enough room for everything that's going to go in here.

So I'm gonna just delete that text because it doesn't need to be there for now.

And then we need to create our countdown UI script.

So let's go into our scripts directory and find our countdown UI controller

and we can pretty much remove these two and we're gonna say public text mesh pro you g you I and then

we can do control periods so that we're adding using team pro countdown text.

So this is the text that we just created.

We're gonna pass that in here and we're gonna say this one instead of being internal object it's going

to be public eye and numerator and numerator that one.

Start countdown.

OK so this is where we're going to start controlling that text so that it shows three two one go like

that so and let's make it caps just like we showed.

All right.

So the first thing we'll do is count down text.

Text equals three loops and we want to set it to the string three not the number three.

Then we'll say yield return new Wait four seconds one f so we're gonna wait one second then we're going

to say count down loops count on text dot text equals string dot empty yield return new wait for seconds.

Point five.

So we're going to show three for one second and then for half a second we're gonna show nothing.

Okay so let's copy all of this and we're gonna do the same thing for two and then the same thing for

one and then the last one we're gonna do we can just oops too many lines there we can set it to go and

then we don't need to wait for seconds at the end of this one for the half a second because it's just

going to be empty from then on forward.

So now this start countdown is ready so it's gonna show three two one go let's just hook up that countdown

UI script so we go in here and we can add a countdown UI controller and we can hook up our countdown

text right there and then let's just go back in and we will reactivate the heads up display and the

pause menu.