# Play Testing

Now that we have all of these UI setup let's try and actually play it.

Now this won't work.

I'm just gonna say that ahead of time.

These are all just line ending errors.

I'm just going to clear these for now.

When we hit play it's going to fail because there's no game manager in the scene.

But I just wanted to show you that just in case you end up in this situation.

So the race is going and all the UI show up but we're getting tons of error messages and the UI doesn't

go away.

So that is because there's several places where there's problems so pause menu controller line eleven

is trying to access the game manager the race manager is trying to access a game manager let's add a

game manager that should solve things so let's do create empty game manager and we'll do 0 0 0 we'll

add a component game manager and then if things are right then we can hit play and it should work

three two one go and now we're resuming I'm in fourth place I've got my lab techs showing there let's

see if I can get in front of either these guys crashing up now I'm in second oh fourth see if I can

get into second place again oh boy I must've missed all right why is it taking second place let's just

try and do this really quick so that's got to be in race manager there's a function that says get Agent

place so I'm saying it should be second I'm saying if places less than or equal to eleven and less than

an equal to thirteen I want greater than or equal to eleven and less than or equal to thirteen let's

try that again

now this time I'm gonna boost right away so that I get the same advantage that these other guys so I'm

holding down the spacebar.

Okay so I'm in second third fourth third first.

Okay so things seem to be working out.

UPS I just missed it but you can also see watch this as I point toward the check points.

Now it's showing me where the next checkpoint is so it updates it's either on screen or it's kind of

off screen and then it shows the arrow until I get to it.

It is pretty cool took me a little bit of messing around to find a way to make the UI look nice especially

with this like sort of oval around the outside.

Believe it or not I actually copied that mechanic from Star Wars Battlefront 2.

They have a really awesome flight UI sort of as part of their star fighter assault part.

So yeah.

Now are our races seems to be working and I'm doing a horrible job racing but the the general game seems

to be completely functional.

And I just went through so now I'm on lap 2 that updated and you can see that the time is counting down.

If I run out of time like I'll just do that right now it should reset me to that last place that I was

at.

I'm just going to boost off try not to crash because if I crash it will reset me as well.

OK so I'm running out of time and it's back to where I was.

So that's good.

It's a little bit jarring because the camera kind of flies over there but that's not something I'm going

to worry too much about right now.

And then I'm gonna I'm gonna go all the way to the end so that you can see what the end screen looks

like

probably should have been playing this with the X Box controller.

It'd be a little bit easier for me but arrow keys are all right.

Okay so this should be game over right here.

Yep and now it says I came in fourth place and I can go back to the main menu and here I am back at

the main menu.

I should be able to start and it starts again.

Now let's test out the pause menu so I'm gonna hit escape and the pause menu showed but something isn't

working so it's it's saying that it's been destroyed but you're still trying to access it so that's

something that is gonna be a bug we're gonna have to fix.