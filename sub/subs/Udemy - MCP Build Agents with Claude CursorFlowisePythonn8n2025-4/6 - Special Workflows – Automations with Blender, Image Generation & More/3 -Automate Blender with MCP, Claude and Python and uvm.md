# 3 -Automate Blender with MCP, Claude and Python and uvm translated

---

Let's create a monkey.

And boom, we have a monkey.

Now we need to add some bananas.

There we have the bananas.

Now I actually want to make a house.

Let's automate Blender.

For everybody that already works with Blender, this is great.

And for everybody that don't know how to work with Blender,

this is also great because you don't have to know a lot

to simply start out and exploring your ideas.

The first thing that we do is, of course,

that we come to this GitHub repo.

The GitHub repo is about the Blender MCP server.

So it's always about the model context protocol

and we can scroll down just a tiny bit.

Blender MCP connects Blender to call out AI

through the model context protocol,

allowing call to directly interact and control Blender.

This integration enables prompt assisted 3D modeling,

scene creation and manipulation.

You will also find the tutorial, but we will do it click by click.

Here you can basically see what's added

and what you can do, but I will show you.

We have two main components.

First, the Blender add-on with addon.py

and we will find it in the source code in the GitHub repo.

And of course, the MCP server.

Before you install this, we need to have three different things.

You need to have Blender installed.

You need to have Python, 3.10 or higher.

And you need to have the UV back catch manager.

So the first thing is, of course,

to simply Google Blender and to download it.

You can simply press on this button.

Blender is completely open source and for free.

So you would simply press download here.

You can also donate to Blender if you want,

but you do not have to do this.

It's important that this is completely for free.

So just download it and install it.

These are just two clicks.

Then of course, we need to have Python 3.10 installed or higher.

We already have Python installed, but let's just check it.

If we open up PowerShell or TermNell or whatever you want,

you simply type in Python and you send it out.

I have 3.12.10 installed.

This is of course higher than 3.10.

So this is completely fine.

And next, you need to have the UV back catch manager.

If you are on Mac, this is, of course,

the thing how you can install it.

And if you are on Windows, you can install it with this command.

Basically, we have also installed the UV back catch manager

in one of these previous videos.

But if you did not do this, of course,

just copy this command and throw it into your PowerShell.

So just include it and send it out.

I have already done this.

You need to have UV installed.

And the same thing is true for Mac.

So just install the UV back catch manager.

You already know how this is working.

It's really important that you have UV installed.

If it's not installed, this will not work.

So you cannot work with pip here.

Then we have, of course, our desktop integration.

We also have a cursor integration and some other settings.

But before we do this, we need to do something

really, really important.

You need to come to this code

and you need to download the zip file.

So you need to have this zip file downloaded.

And in this zip file, you find the Blender MCP main.

And you can simply throw it on your desktop.

And you see that I have already done this.

So just throw this file on your desktop

and then you are set.

Because in this file, you will find the stuff that you need.

We need this add-on.py later.

Just like the GitHub repo tells us.

We need the add-on.py.

Then the next thing, as soon as you have thrown this

on your desktop and as soon as Blender is installed,

I have already installed Blender.

We need to open up Blender, so just press on it.

As soon as you are in Blender, you need to come to edit.

Here you need to come to preferences.

Then you need to come to add-ons.

I can also make this right now a little bit bigger

because this is a bit too small.

So you come to add-ons.

Then you press on this button

and you need to press install from disk.

Then you would come, of course, to your desktop.

You search for the Blender MCP main.

And here you need to press on the add-on.py

and you need to press install from disk.

I have already done this.

So just press on install from disk

and then you can close this thing down.

And then on your add-ons, you will find actually

the Blender MCP.

You can see it right here.

I have already included this thing.

As soon as this thing is installed,

you can actually close it down.

And now you need to press end on your keyboard.

So if you press end, this thing should open up.

Decide bar will pop up.

And here you can see that you have the Blender MCP included.

And the Blender MCP runs on this board.

So board 9876.

And in order that this thing is working,

you need to press connect to MCP server.

So you need to press this thing right here

and only then it's running on this board.

If you forget to do this, this thing will not work.

You can also include these two things right here.

So use assets from Bolly Heaven if you want to include this.

But you don't have to.

And use Hyper3D-Roting, 3D model generation.

If you actually know Blender, you can work with this

and you can throw in your API key.

I just want to make this basic.

So we just connect with this basic MCP server right now.

So this thing is running on this board.

And now we need to go on with the next step.

The next step is as always, as you know,

you need to configure your desktop config file.

And it always depends on what model you want to work with.

You can work with Cloud Desktop.

You can work with Cursor.

You can work with whatever you want.

You just have to copy this command line.

Then you come, for example, into Cloud Desktop.

You come once again, of course, in file,

set things, developer, edit config file.

On this config file, you will open this up.

And here you need to include, let me just throw this aside,

you need to include, of course,

this thing right here and make sure

to don't make any syntax errors.

So the curly bracket is already included.

You see that we use the MCP server.

It's called Blender.

The command is UVX.

It's important UVX.

This is why you need to have the UV Backage Manager installed.

Then the arguments are simply the Blender MCP.

And then we will connect via Python

and this extension in our Blender.

So you can simply save this.

We close it down.

Then we actually need to restart, as you know,

Cloud Desktop.

I hope they fixed this soon.

Then we can open up Cloud Desktop once again.

Now we press right here and we wait until the MCP gets integrated.

Boom.

And there we have it.

Brand the MCP.

And you see that we can do 17 different actions

with just one single connection.

This is powerful.

We can get seen info.

We can get object info.

We can get viewpoints screenshot.

We can execute Blender code.

Get polyhaving categories.

Search polyhaving assets.

Download polyhaving assets.

Set texture.

Get polyhaving status.

Get type of Redis status.

Get sketchfab status.

Search, sketchfab models.

Download these models.

Generate type of Redis models.

Pull rowding job status and import generated assets.

So you see you can control Blender here

right now with Cloud Desktop.

And one of the coolest things that I like to do

is to simply make this a little bit smaller.

And row with our side.

Then we can open up a Blender, for example.

Also Blender, let's just make it a tiny bit smaller.

So what I like to do is something like this.

Boom.

And now you can work on your projects.

This is really cool.

Now actually let's just test this out.

What is in Blender right now?

I send it out.

This thing will ask me if I want to allow this.

I have only to allow these ones.

And then I can ask all the time.

Or actually I think I already give an access.

So we have in Blender right now a cube

with the position 0, 0, 0.

We have our light with this position.

And we have our camera with this position.

And if you come in Blender, you see that we have the cube

that is in the center.

We have the light in this position.

And we have the camera.

You can also see it here on this side.

And you can press on it actually.

And if you don't know how to do like a specific thing,

you can always talk to Claude.

And Claude will give you really, really nailed

to down the information because this thing

can control everything from here.

And see what you are doing.

Let's just try it a little bit.

Create a 3D model from a monkey.

And I send it out.

We need to look at what's inside of Blender right now.

And now our Ramsy piece, Erber, actually

tries to use Hyper 3D.

And you see Hyper 3D is right now excluded.

So of course, we need to connect to it.

And we also need to give an API key if we want.

But if you do not like to do this,

then you can also work with like not the Hyper 3D model.

So for example, you can do something like this.

Create a simple monkey like shape using basic modeling techniques.

And of course, if you want to work more professionally,

you can totally do this by simply enabling this

and connecting this API key.

For right now, you see that we have deleted some stuff

we are starting to create new stuff actually.

And we will model a monkey.

If the monkey does not look great, of course,

we have the possibility to use the Hyper 3D model

because I do think this monkey looks like a little bit special.

Let's just wait until we get it.

Right now we do have a monkey,

but I don't think that the monkey looks great.

Actually, we can't even know if this is really a monkey or not.

You can also work with different stuff here.

With the Blender built in monkey, for example,

we can also search for monkey models and a lot more.

If you are not satisfied, you can also take a new chat

and ask ones again, for example.

Sometimes it can happen that Blender creates better stuff.

I have to tell you I am also not an expert in Blender.

Right now you see like that we get a monkey that looks a lot better.

This is the head of the monkey.

I do think that we also get the body of the monkey.

And this time we get the scene info,

then we execute the Blender code.

This time we did it all with Python, I do think.

We created the existing mash and so on.

So you basically see that we integrate everything that we need.

And if you want to connect to Hyper3DAI,

of course you can totally do this.

You can just come to the API.

You can scroll down until you see that you can

like integrate really, really great stuff from this API.

Everything that you have to do is of course,

to create an API key.

If you press on this API,

then you can create a new API key.

But I have to tell you that this API is not for free.

But if you work with Blender like most likely,

you are already connected with this API.

So Cloud Desktop can absolutely also control this API

over Blender with the model context protocol.

This is enormously great.

Our monkey head is basically done.

And now Cloud asks me what I can do, rotate the view and so on.

What would I want to do is also add a body

to the monkey.

Then of course, Cloud needs to check once again,

where the monkey is set at.

And then it will try to add a body to this monkey.

Let's just see if Cloud can actually pull this off boom.

And there we have a body.

And Cloud also made our look a little bit smoother.

What I can do right now is, for example,

add four bananas around the head of the monkey.

Cloud actually made some mess.

Of course, this is most likely because of my prompting.

I told Cloud the digits basically just clean up the mess

and create four new bananas.

Let's just see what we get.

I do think right now this is fine for me.

We have four things that look at least like somehow,

like a banana.

And they are around the head of this monkey.

Of course, you can make this more professionally.

You can make this better.

What I want to do last is, for example,

the bananas should circle around the head.

I can send this out.

And then we will get most likely bananas

that are circling around, that are floating around.

Of course, you can not only make stupid monkeys.

You can also try to create like entire houses

and do whatever you want.

If you already understand blender,

you know how powerful this tool is.

And you know that I am a new pin blender.

But still, with Cloud, at least I can make something out of this.

Cloud tells me that we have some frames animated.

And this bananas should have a smoother rotation.

And all pivots rotate three-six degrees around this axis.

And if you do not know how to watch this,

you can ask Cloud,

or you can also just press on this button.

Then you see that these bananas are floating around.

So everything seems to work completely perfect right now.

And lastly, like delete,

everthing I send it out.

And everything is gone.

Create a simple 3D model of a house.

Of course, once again, we use the right libraries.

We have this basic health right now.

But Cloud still goes on.

It tries to create also at least somehow

everything that we need to have on a house like doors.

Interesting roof.

The thing where Santa Claus can come.

Now the roof got an update.

Of course, it depends on how you look at this house.

Cloud tries to clean up its mess automatically.

I have not prompted Cloud.

Cloud is still on work right now.

So this gets a,

so this will be her special house.

And Cloud tells me that it's done.

Of course, you can fine tune this house.

And of course, this things will only get better from here.

These are the dumbest AI models that you will ever use.

But still, they can create stuff that looks somehow nice,

somehow okay.

This can be a house.

It depends on how you look at it.

Remember, these are the worst models that you ever use.

And if you know what you are doing in Blender,

you get great starting points.

And if you don't know what you are doing in Blender,

you can create stuff that are otherwise not possible

to create.

Blender is a relatively complex tool.

If you have never used it,

it's nearly impossible to create something that makes sense.

I have worked in Blender like a few years back,

so I also don't know a lot about it anymore.

Create a garden around the house.

We will include some trees with a random seat,

a front garden bed.

And right now we do have like a relatively interesting garden

around this house.

Of course, you can also tell Cloud,

make it all green.

So just a little bit of grass around this house,

you can do whatever you want.

You can delete stuff, you can add stuff,

you can work with this stuff however you want.

But I do think this is really, really nice.

And I wouldn't be surprised if this will be the new thing

that everybody will use in the future.

As soon as I let them get a tiny bit smarter,

maybe you can also thank you,

to your NaClout model,

you can give a detailed system prompt with some examples.

Maybe you can connect it with a vector database,

where you give examples of stuff that you want to create,

and then you are able to create stuff

like really really fast.

Long story short, I do think this is a special workflow.

You have to install Blender, you have to install Python,

you have to install the UVBaccadge manager,

you need to download the code,

then you need to have the addon.py

and you need to connect it with Blender.

As soon as everything is connected,

just open up your board and press connect.

And then you can simply manage your config file,

just edit into a whatever host you want to use,

and then you can control Blender.

And a Zee, of course, in the next video.

I do really think this is somehow the future,

how we can control software.

Just think about it how powerful all of this is.

As soon as these LLMs get a lot smarter,

maybe with some fine tuning,

also on specific datasets,

you can simply talk to your phone

and create standing stuff inside of Blender.

This is powerful.