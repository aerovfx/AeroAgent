# New Project, Install ML-Agents, & Import Examples

In this video, we're going to create a new unity project, install M.L. agents and then import the

example Amelle agents projects from the MLA Agents GitHub repository.

So the first thing you should do is open unity hub and then make sure you've got your twenty nineteen

three version of unity or newer and create a new project.

We're gonna do the 3D template for now because that's what the Unity MLS agents example's uses.

And then let's give this project a name and I'm going to call it MLA for short examples.

It doesn't really matter what you call it and make sure you put it somewhere that's easy for you to

find and then click create.

And this will take a moment to create.

So while this is happening, we want to go and download the example project's.

So if you go to the unity M.L. agents get Hub page, which I'll provide a link in the course.

But if you want to know, it's get hub dot com slash unity dash technologies, slash N.L. dash agents.

And if you're not super familiar with get hub, it's basically just a place to store code.

And this is essentially a folder that has lots of other folders in code and other assets and things

in it.

This is the official unity GitHub page.

And we want to get the example projects that are contained inside, but I'll warn you right away, you

don't want to just click, clone and download because this is the master branch.

And by the time you see this tutorial, they'll have made changes that could mess with things and change

things and cause problems.

So instead of that, I'm going to suggest that you scroll down past this picture and find the section

that says releases and documentation.

And as they say here, the table below lists all our releases, including our master branch, which

is under active development and may be unstable.

So that's just saying, in other words, why we're not using the master branch.

Right now, the newest for me is May 20th, 2020.

So that's the version I'm going to suggest that you work with through the rest of this course.

Just so that you don't have any compatibility issues, they so far have made small changes that end

up having kind of big impacts, at least in terms of making a course and following along.

So it's probably best that you stick with the version that I'm using.

And then after you've gone through the course, then the updates to the latest versions should be very

minimal.

So find released two and then click on download.

And then save this file.

I've already saved it, so I'm not going to download it again, but save it and unzip it somewhere that

is convenient to work with.

I suggest moving it out of your downloads folder just for better organization so you don't accidentally

delete it later.

But it doesn't really matter where it is because we'll just be pulling files out of it for now.

So once unity is up and running and it seems like everything's all set.

We've got this empty scene.

We need to install Unity MLA agents.

So for that, you're going to want to go up to the window menu and find the package manager.

And you should have this pop up.

It is the package manager and it's already got a long list of different things on the side here.

You need to make sure that you have under this advanced menu.

Show preview packages needs to be enabled.

And then you're going to see all of these different options with preview next to them.

Then you can find the MLA agents package, which they're in alphabetical order, so should be about

halfway down the list.

And then right now, the default one for me is version one point zero, point two.

By the time you take this, that could have changed, so you can click on this, see all versions and

then make sure you just select the one point zero point two version to install.

Then go ahead and install that.

While this is installing, I want to draw your attention to the Emmel agents release to folder.

So this is the unzipped version of what I just told you to download.

And inside here, this is just all of the same files that are in that GitHub repository.

So what we're gonna need from in here is inside of this project folder.

There's a lot else going on in here.

I don't want to go into everything that's in here.

There's actually really helpful documentation that's in here or that you can view.

On the page, so you can see everything that's going on in here.

But there's a few things that I'll just point out.

There's this calm.

Unity M.L. Agents folder.

That's actually what gets updated in the package manager.

They submit this folder to the unity package manager on the back end so that when you're downloading

it, this the files that get installed from here are actually what goes into the packages.

So I'll show you that really quick.

So I think it's it's installed now.

Up to date.

So I can close the package manager and I can look down in packages.

And then this e-mail agent's folder has ed plug ins, runtime tests, all of these.

If you go in here, you're going to see these same folders, ed, plug ins, runtime tests and some

other stuff that's in here, too.

But that's essentially what lives inside of the packages folder here.

It's this thing.

But you don't need to do any of that manually because we're using the package manager.

There's also these two MLA agents and MLA agents, Envy's Folder's.

These are the Python libraries.

And we'll be installing them via Anaconda later, but that's where those live.

And then the one that we want to use right now is in this project folder.

Project just contains a unity project.

And this is a unique unity project with examples in it.

And we want to import those examples to our new project.

So go to your assets folder.

And find the assets folder in the project directory.

And then you can just click and drag this email agent's folder, the whole thing down into your assets

directory.

Now it's it's working.

So it might ding at me.

They try and hide this, so I'm just gonna be patient.

I guess.

And now that this is imported, looks like all the progress bars are done.

I can open up this folder and look inside the examples thing.

So inside of the examples folder, you'll see lots of different examples.

And these are really great for learning what M.L. agents can do and some ideas for how you can do it.

So we'll be going through this in the next video.

But if you want to get familiar with what the different examples are, you can go to the M.L. Agents

page.

You can scroll down to the released to docs, click on that.

And then there's a section here under getting started, for example, environments.

And you can see all of them here.

These are all of the example environments that are contained in this project.

So we'll be looking at one of those in the next video.