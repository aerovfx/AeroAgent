# Training Results

Well, the training has now been running for about twenty five minutes and it has been on step four

or lesson four for at least five.

Looks like more than five minutes, almost ten minutes.

So that's probably a good sign that these agents are successfully navigating the entire course.

And indeed, if we go over here, I'm going to change the time scale down to one so that we can see

a little better.

We can see.

Look at those airplanes.

They are just perfectly flying through this course.

And that's so cool.

So you'll see that them disappear sometimes because they are being reset.

And they're not.

They're kind of staggered on their resets because the you know, they crashed at different times.

But I also want to point out that they're boosting intelligently, like they don't boost one hundred

percent of the time.

They don't always have it on, but they will hold it on for as long as it makes sense for them to.

And it's actually like almost seems unfair when you're playing against them.

But so so these are working great.

So I'm actually going to press play and what that'll do is stop the training.

And it saves the training.

So, as it says here, it converts the tensor flow graph to aircraft learning N.N..

And that's an aircraft underscore 02.

And we can go into our project and let's create a folder, and you can either call it T.F. Models or

I like to call it and models, just because they're N.N. files, it makes more sense to me.

And then we can find that model under the model's directory in aircraft 02 and then drop in aircraft

learning and.

And then what we can do is let's save this scene.

I don't know what I did to change the scene, I didn't.

I don't think I changed anything, but whatever.

And then we can go back to our scenes.

We can go to our desert scene.

And we can select our main airplane.

Go to the inspector.

And find the model field and we can click on this little circle and find that aircraft learning neural

network.

So we have this aircraft learning neural network now imported.

And the desert area.

It's in training mode right now.

And I don't really want to mess with that at the prefab level.

So what I'm going to do is change it in this in this level.

So this won't affect the prefab.

It'll just affect the one that's in this scene.

And then we've got these four here.

So it should work.

The only thing is this camera is currently following the airplane player.

So let me put it I'll just put it behind, like, the blue one here.

And let's see what happens when we press play.

OK.

So if you have this selected, you have to just kind of click away.

And now we're watching.

Flying behind all of these agents that are flying trained neural networks.

So I'm not controlling this at all.

This is all coming from the neural networks.