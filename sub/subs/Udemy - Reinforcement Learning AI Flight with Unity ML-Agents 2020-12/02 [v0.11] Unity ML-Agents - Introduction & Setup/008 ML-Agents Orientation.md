# ML-Agents Orientation

So I've downloaded and unzipped the MLA agent's directory into a convenient directory on my desktop

and you can you know you can put it on your desktop if you want.

Or just somewhere else.

I just recommend you keep all of these files that we end up using together while you're going through

the course it'll make things easier so you can ignore this aircraft MLA folder for now.

I'm actually recording this course out of order so that's why that's here.

We'll be creating that later the assets directory is just the downloadable assets for the course and

then this MLA agent's directory is the MLA agent's directory as downloaded from this beta 11:00 release.

Now what we're gonna do sorry lose in losing my place here.

What we're gonna do is take a look inside here.

So this actually should look very familiar.

If you were looking at this page I'm gonna try and pull this up again.

This is the exact same folder of code.

So it's got the config folder the demos folder the docs folder it's got everything that was on this

page now downloaded to your desktop and I want to point out a few things.

One is the documentation page.

I tend to read this on the web because it's a little bit easier.

Like I just go into DOCS and then if you scroll past the files at the top you can see the read me for

that page and then you can see all the documentation which is really great.

In particular we're going to be interested in the example environments.

So I'm going to open that now and we're we would like to learn a little bit about how these how this

project works.

So we're going to open one of these example environments and take a look at how to use the neural networks

that are in there and how to train as well.

Now there's a few other things inside here that I want to point out.

This is in the MLA agents directory.

There is an MLA agents and an MLA agent stash in V's folder inside here.

This is a lot of Python code that's designed to train the neural networks so we won't need to modify

this at all but just know that that's where the code is.

That is training your agents.

They kind of lives inside of inside of these two directories.

And if you're wondering where an error message is coming from while you're training you probably want

to look in these folders and then there's the unity SDK folder.

There's obviously a ton of other folders here.

We'll get to those as we need certain ones of some of them we'll never touch unity SDK is actually a

Unity project and inside here this assets is your assets directory inside of a Unity project and they

have this MLA agent's folder.

Now a lot of people I think based on some of the YouTube comments I've seen on the videos I've done

on MLA agents seem to open up MLA agents from this directory and I'm going to recommend against that.

I've found that it makes more sense to create a new project and then move this make a copy of it and

put it into that project and that way you're not messing with this directory at all.

We can keep it nice and clean and then we can start a bunch of new projects and you know if you mess

one up or you decide to go in a different direction you can just create a fresh project and you don't

need to read download this folder.