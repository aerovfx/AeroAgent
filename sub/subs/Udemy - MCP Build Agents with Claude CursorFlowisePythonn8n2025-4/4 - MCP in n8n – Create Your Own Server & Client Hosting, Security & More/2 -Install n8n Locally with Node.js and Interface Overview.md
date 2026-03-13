# 2 -Install n8n Locally with Node.js and Interface Overview translated

---

In this section we will work with a tool that is called anadenn.

Anadenn is really great for automations.

The interface, as soon as you build something out, will look something like this.

And in this video I want to show you how you can install it locally.

And I will also show you in this video that you can also start

without installing this locally of course with the plan from anadenn.

Anadenn is especially cool because here we can create our own MCP servers.

So anadenn can function as an MCP server and you can connect whatever you want.

For example, the Google Calendar, but also Gmail,

Accelculator, Google Sheets, or for example, Vector databases.

But of course you can do even more because you not only have the MCP server,

you also have an MCP client.

So anadenn can be a client and a server.

This is really great.

You can create basically SSEN points.

So you see we always use the server sentiment.

And you can create servers and clients in anadenn.

And you can also access stuff like for example,

this thing's here that will trigger other workflows.

These other workflows can for example also trigger HDDB requests

in order to generate pictures and do a lot of cool stuff.

Besides that we also have a community node

where we can also connect to GitHub servers just like for example Airbnb.

Here we need to include a few variables,

but I promise this will be relatively easy.

So long story short, you can create servers

and you can connect these servers to every client that you want.

You can also use anadenn as a client

and connect servers from anadenn or also other servers.

And if you want to connect servers from GitHub,

you need to use the community node.

So basically you can do every single thing

that MCP allows us to do inside of anadenn.

This will be a really great section.

If you want to use the plan from anadenn,

you can simply press get started for free on this webpage.

And then you will be in an interface that looks something like this.

You can simply give here your credentials

and then you can basically log yourself in and you are done.

It's really really easy.

And you can test this out completely for free for 14 days.

But after this of course your instance will spin down.

They don't need any credit card at least not yet,

but later they want to have a credit card if you want to use this for longer.

And actually if you come to pricing,

you can see how much this thing is costing.

It costs at least right now 20 euros.

I would guess like also 20 dollars a month.

In this standard plan, and if you use this standard plan,

you can do also everything that you want.

If you come back once again,

if you only want to follow this tutorial

as over the next few videos and you do not want to install it locally,

just use this free version for two weeks and you are completely set.

But for everybody that wants to install

is to locally of course you are covered in this video.

Because NADN is also open source.

And you can find the GitHub repo.

And on this GitHub repo you see that NADN has a lot of stars.

A lot of people love this tool.

And if you scroll down you see that you can basically install

this via a view of different things.

You can install it with npx.

And of course for npx you need note.js.

If you like to work with Docker, of course you can also install it

in a Docker container.

And if you scroll down once again,

you can also see the license and so on.

We will talk at this in more detail like the end of this course right now.

It's not that important.

And if you come to the documentation

and come to self-host NADN,

you also see that you have a lot of possibilities

to self-host your NADN instance.

You can use digital ocean,

Heroku, the Hetzner cloud,

AWS Azure, the Google Cloud platform.

Also here Docker Compose.

You can also use render and hosting error.

So you have a lot of options.

But more on self-hosting later,

because we talk about self-hosting as soon as it's needed.

So if you simply want to follow this tutorial,

just press get started for free.

And you can use this completely for free for two weeks.

And if you want to install it on your local machine,

you need to install note.js.

I hope that you have already done this.

And I will also recommend you once again to use NVM

if you have problems with this version.

Normally if you work in the version 22.16.0

so the default version, everything should work great.

Now as soon as these two things are installed,

or at least as soon as notice installed,

you will have this on your search bar.

You can press on it.

You can search for the note.js command prompt.

And with this thing, you can install NADN.

Here you simply have to type in NPM, install,

NADN, dash G.

And then you send this thing out.

This will be done like in two minutes or so.

And you do this only once.

And as soon as your packages are installed,

it will look something like this.

You can either clear your window or you can reopen it.

And then you simply type in N8N.

And send this out.

And then your local note installation will open up.

After one or two minutes, it should look something like this.

You will get the Z URL.

And you can simply copy the Z URL,

throw it in your browser and send it out.

Then you will see something like this.

Just simply type in your mail, your first name, your last name,

and of course a bus word.

Then you fill out this information.

After this is done, you will be in an instance

that looks something like this.

But you will not have any workflows.

So you see I have already some workflows here installed.

But your canvas will most likely be completely empty.

It will look something like this.

I want to give you a quick overview.

So the first thing is workflows.

Most likely your things are here empty.

You can search for workflows as soon as you have created a lot of them.

You can filter through these workflows.

And you can search by last update,

or whatever you like by name, or what you want.

Then you can press on credentials.

You can also include some credentials.

You see I have already included a lot of different credentials here.

But most likely you will not have included them

because we will do this step by step later.

Then you can also press on executions and tier.

Here you see what executions were triggered

in the last few sessions, for example.

If you go back on workflows,

you see that you can also create new workflows

by pressing on this button.

And if you press here,

you can also create credentials.

If you press create workflow,

you will be in a canva that looks something like this.

But don't worry,

first we go back right here and we see what's here on the left side.

On the left side you have here this plus sign.

And here you have once again workflow credentials.

And you can also go on the enterprise plan.

The enterprise plan has some special offers

that you do not need right now.

Then you have here templates.

And if you press on templates,

you are in a marketplace.

And here you can search through templates.

There are three templates.

There are also paid templates.

You can search through templates later

as soon as you understand the basics.

If you press on finance, for example,

you will find some examples for finance templates

that you can use.

You can either buy them.

Here you see something for 25 bucks.

Here is something for $49.

Or you can also search for stuff that is completely for free.

But like I said,

first you need to understand these workflows before you use them.

So if you go down,

here you find variables.

And if you press on them,

you can also create variables for later workflows.

But of course, step by step.

Then you have your help guide.

If you press on these,

you have a quick starter with some videos.

You have the whole documentation.

The documentation is really great.

You should take a look of these and we will also use it over

and over in this course.

You have a forum.

You also have a small course.

You can report the back

and you can also press on about

and then here you get some information.

And down here is your name.

And if you press on this,

you can simply go to settings or sign out.

If you go to settings,

you simply see how many workflows you can make.

For example, in this local instance,

I can make unlimited workflows.

If you press on personal,

you can simply type in your information.

If you go on user,

you see from who this is owned.

In my case, this is from my normal email address.

You can also press on the N8N API.

And you can programmatically use N8N

if you simply create an API key

so you can include this in other workflows.

And then you have some stuff

that is only a vibrant enterprise plan.

You have external servers,

more on that later.

And environments that you can create,

SSO, LDP,

and of course also lock streaming.

And lastly, you have to community notes.

In the left corner,

you also see what version is active.

In the next video, I want to show you

how we can update this version.

Because right now there's an update available.

If you go back on settings once again,

and if you press on overview and create workflow,

we are once again in this canvas

and here the magic happens.

Here in this canvas, we can create our workflows.

You have always to start with a trigger node

so you simply press plus

and you can use these nodes.

But of course, more on these nodes later,

because we will need to do this step-by-step.

So I hope this local installation works for you.

And if not, you are covered in the next video.

Because it is most likely

the node version that won't work for you.

So in the next video, I will show you once again

how you can manage your node versions over NVM.

And I will show you exactly the version

that I have used for these tutorials.