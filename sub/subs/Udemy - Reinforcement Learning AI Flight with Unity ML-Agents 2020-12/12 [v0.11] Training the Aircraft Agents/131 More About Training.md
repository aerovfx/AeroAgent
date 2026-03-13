# More About Training

So let's take a closer look and I'm going to go into the scene view here and you can see here that there

are clearly something happening.

So the wheels are turning and we've got these black fans that are kind of just scooting around randomly.

So these black fans are actually the recasts the reason that you can see them.

Now ordinarily you can't see Ray casts.

But in the code for the ray perception 3D class which I I opened up ahead of time in that Ray cast perceive

or the ray perception perceived function.

They actually do a debug dot draw Ray so they're drawing these rays each ups each update.

And that's why we can see them so these agents are taking essentially random actions and there's 16

of them running simultaneously at a 50 times speed and if you're ever curious about how what speed you're

running at you can check your project settings which I have a tab open right here if you don't have

that tab go to edit project settings and you can see the timescale under the time option here.

You can actually modify this if you want to see what's you know what's happening in real time.

I'm not going to do it right now because I want them to keep training at full speed but you can modify

this and change it down to one and then you'll be able to see them flying around in real time.

And remember this time scale comes from what you set in the aircraft Academy.

We go to the inspector this time scale right here will match.

So whatever you set this to for training configuration is what will be running their.