# 10 -Hosting Flowise on Render Step‑by‑Step and a quick HTML lesson translated

---

Let's just say you want to host this application.

Maybe this thing right here or also the tool agent that we have already built it out.

Maybe you want to create a rec application or something with an MCB server

that clients from you can use, that you can use in your companies, that your employees can use.

Of course, then it's not possible that you work on this local host 3000.

You need to host this application.

And in order to host it, we have a lot of different options.

I do like the hosting from Render relatively good for low-wise.

Because on Render it's easy and relatively cheap.

Hosting here hasn't unfortunately no option to host low-wise until yet.

So that's why I want to roll with Render.

So this means after this video you can make your applications public.

You can embed them into webpages.

You can bring them in your Python application, JavaScript application.

You can curl them from wherever you want,

or you can simply share your chatbots with these links.

So let's just talk about hosting.

Of course, if you want to do it really, really easy,

you can also simply come to low-wise and you can come to the pricing.

Until you can simply start with the free plan.

But this will be most likely a little bit too small if you want to do a bit more.

You can also use the starter plan, but the starter plan you know it costs you 35 bucks a month.

And that's why I want to show you how you can host this on Render.

I think this is the most powerful way if you want to sell your chatbot.

If you want to provide this chatbot to clients or also if you want to host this chatbot

and you use it from other computers.

If you want to build something that everybody can use and that you can also use from other PCs

and so on, this is the way to go.

First of all, you need to go to get up.

And if you scroll down, you see that you have a lot of options that you can use in order to host this chatbot.

And you can see here the other options I think the best option is to deploying it to Render.

And if you press on it, you get also the whole documentation.

So you can follow this click-by-click also from the documentation.

But of course, I want to show you this in a video.

You go back. The first thing that you need to do is to press fork.

Of course, I have already forked this, but if you have not forked it, simply press on this button.

So you need to simply press one time on this fork button.

Like I said, I already have forked this, but you simply need to give permission.

You press OK one time and I view my existing fork.

As soon as you have accepted this, you are in this fork right here.

So your name will be here because you already have a GitHub account at least, that's what I hope.

And then you have forked this instance.

And by the way, while we are here, if you want to host this in the cloud,

you can update your flow wise instance really, really easy.

You see it also here.

This branch is 27 commits behind.

So I can reforch this so I can synchronize my fork in order to update my instance.

This is just a few days ago that I have updated these.

So flow wise makes a lot of updates.

In order to synchronize your fork, you simply press on synchronize fork.

And then you press update branch.

And this will be done in no time whatsoever.

Bam, there it is.

This branch is up to date.

Right now my branch is up to date and I hope that you have forked your flow wise instance

in your GitHub profile.

As soon as you have forked this, you need to go on render.

You can simply Google render and press on the first link.

Here you need to make an account.

You can start totally for free, but later you need a small plan

if you want to host this permanently.

So I simply press start for free.

You need to log in yourself with Google or you need to make an account.

Of course, I already have an account.

And there we are.

And here you see I have two failed deployments and the rest is here updating

because I have updated my branch.

So you see the rest of this is deploying,

but I want to create something new right now.

And if you want to start here from scratch, you simply press new

and we want to have a new web service to build and deploy

from a Git repository.

So we press next.

If this is your first time on this web page,

you need to connect your GitHub.

This will be somewhere right here.

If you already have connected your GitHub account,

you will find something like this and we press connect.

So this is my flow wise instance on GitHub.

So we press connect.

Now you need to give this a name.

Let's just say flow wise 33 because I already have a flow wise instance.

Then you need to give your region.

So where are you living?

I use here the Frankfurt EU Central.

Then the branch will leave this at main.

And now we go down to runtime.

I would simply leave this at the Docker.

And now it gets important because right now if you just want to follow

with this tutorial, you can use the Vray plan.

But if you want to host this completely forever in the cloud,

you need this starter plan for the sake of this tutorial.

I will use this Vray plan.

And here you see what the downsides are.

For instances, spin down after periods of inactivity.

They do not support SSH access scaling one of chops or persistent disk.

Select any bait instance type to enable these features.

Long story short, all your stuff will get deleted if you use this Vray plan over time.

But for a sake of a tutorial, this is completely fine.

If you want to host this forever in the cloud,

you need the starter plan and the starter plan is more than enough.

But like I said for this tutorial and also if you just want to test it out,

just use the Vray plan.

But don't be surprised if your chat flows will get deleted.

Then the next thing is the environment variables.

And we need a view of these variables.

If we go in the flow wise documentation,

here we find of course under configurations,

the environment variables.

And here we can see every single thing that we need.

So we go back to the render dashboard.

And here we simply type in flow wise username.

So you see flow wise username.

If I press on this, this is automatically because I have done this a lot of time.

So flow wise username.

You can also go right here and copy this.

Flow wise username and then insert it here.

And now you need to give a value.

For example, Arnie, one.

And then we use new variables because we need a password.

So we press on it.

Flow wise underscore password.

This is also nice.

And of course you can copy also the flow wise password from here.

And now you need to give a password.

Just use something that is somehow safe.

I use one, two, three, four for this tutorial.

But you should use something that is a little bit better.

Then we press once again,

add environment variables.

And now we need the note version.

If I press on this, this is automatically also by me.

The note version.

And of course you can copy this.

And the version of note should be 18.18.1.

This is the version that works right now.

Also higher versions will work.

Most of the time just start with this.

You can also go back on flow wise where is it?

It is down here.

And you can scroll down and see for yourself.

18.15.0 could eventually also work.

It just needs to be higher than this.

So 18.18.1 is higher than 18.15.0.

It needs to be higher than this.

And if you want to start with your free instance,

you can press create web service.

If on the other hand, you want to host experimentally.

You go back up, you press on starter.

And now we have a few more options that we can choose.

So we press on advanced.

If you want to have a persistent disk,

you need to do this.

So like I said, the free plan you were ready to rock.

You simply can create this service.

If you use the starter plan and you want to host this

permanently, you need to follow up this way.

So we need to add a disk.

And now we need to type in some information.

And now it gets important.

The mount path.

You need to start this right here.

So slash OPT slash render slash dot flow wise.

This is important because you need to copy these

of you time.

Then the size one gigabyte is more than enough for flow wise.

Now we scroll up once again because we need more variables

because we use our mount path.

We press add environment variables once again.

We need to have the database path.

And you can simply type it in database path.

You can also find this things right here.

So this is the thing that you need database path.

You can simply copy these.

You go back to render.

You can eventually just insert it here.

The next thing that you need is the API key.

So you go here.

You need the API key path.

So this right here.

We copy it and one more time at you environment.

We need the log path.

And you find the log path also here.

So you simply copy it and you insert it.

And now this is important.

Now you can copy this thing right here.

And you can insert it at every single variable right here.

But on the last one you need to also type in slash locks.

And the last thing that you need,

you can also insert the secret key path.

So this thing down here.

We insert it back down here.

And of course this is also this thing right here.

And now we are done.

This is everything the thing that we need.

And now you would simply press create web service.

And like I told you,

this only works if you use the starter plan.

If you go in the free plan,

you can not use your persistent disk.

So you see on the advanced settings,

your persistent disk is offline.

And we could eventually also delete

all these other paths down here.

So for the sake of this tutorial,

I will delete this path.

The only path,

the only that three paths that I need

are this free paths right here.

And now we press create web service

because like this is in the free plan right now.

Then we are here in the building phase.

No logs to show because this will take a little bit of time.

I think in two to five minutes,

it depends a little bit.

This will be done.

So see you as soon as this is created.

And by the way,

you also see this right here.

Your free instance will spin down with an activity,

which can delay requests by 50 seconds or more.

So if you are not active,

this thing will get spin down.

And if you are not active for a few days,

you all your flows will be deleted

because we have no persistent disk.

So you absolutely need this paid plan,

the seven bucks a month.

If you want to host it permanently in the web.

But if you make this project for a client,

you can charge of course way, way more.

You can sell such chatbots for 1000 or even $2000.

It depends on the project.

And you can also charge them a fee

for making this up to date all the time.

So if you create this for a client,

it's really worth this money.

And if you just want to try this out,

just use the free instance just like I did.

And you can delete all these other variables

that we just need for our persistent disk.

And of course, I will see you as soon as this is deployed.

I think this will take another two or three minutes.

And right now we are done.

As soon as you see this right here,

life, you can simply press on this link

and you will be in flow wise.

And of course, you need to have your username

and your password.

And I think my user name was Arnie one.

Arnie one and the password was one, two, three, four.

I hope I don't mess this up.

So I want to log in.

And yes, there we are.

And of course, I am now in flow wise.

I can make this in the dark mode.

Of course, right now I have no chat flows

because this is a completely new instance.

And all of this will get also deleted.

So if I make here for example new chat flows

and if I integrate here for example, some agents

so out to GPT or whatever and I save this

and I call this Arnie and I go back.

This agents will be here in this chat flows of course.

So here is right now my chat flow.

So this is now hosted in the cloud.

And I can open this up even if I am on another PC.

I can open this up wherever I want.

And of course, I can also host my chat pots

in the cloud right now.

But my instances they will get spent down over time.

This is the downside.

And sometimes requests can take a long time.

So for a tutorial, this is completely fine.

But like I said, if you are not active,

your instances they will get spent down.

They will get deleted.

Your chat flows, they will be gone.

So you really need this paid subscription

if you want to host them forever.

And like I said, if you just want to test this out,

this is completely fine.

Right now the next thing that you could eventually do

is the following.

If you have built it out something, for example,

on your local host, you can simply press here on settings.

You can export your agent.

In your downloads, you will have your JSON file

and then you can come on your host and instance of render

and you can import it.

Right now I am in flow wise once again,

but this time on the host and instance of render.

And then if you press right here, load the agents,

you can simply import your workflow

and then your workflow is also imported

inside of your hosted instance.

And right now of course you can save this up.

Give it a name.

That's just called client.

Maybe this is a project for a client.

The next step would be of course to connect the API keys

that are not connected.

This is the only downside that you have to do once again.

So of course you need to connect your credentials once again.

Then everything should work.

And as soon as you have connected your credentials,

you can come on this embed chat.

And here you see that I am on the host and instance

of render right now.

And of course right now you can either share your chatbot

with other people via this link.

You can curl this into any other application

that allows to curl this in.

You can embed it into JavaScript, into Biden

or also as a embed chat.

I just want to make the quickest example possible

with our integrated chatbot.

Let's just assume that this is your web page.

I have simply coded this web page up with chat GPT.

So let's assume this is your web page

and you want to integrate this chatbot inside your web page

or inside of the web page of some of your clients.

Of course you can simply come into the HTML code.

I have simply this local viral right here

and I can open this up by pressing on it,

open with, we can open it with cursor or VS code

or whatever, I just simply use VS code.

And then we can see the source code of this web page.

And now we can scroll down until we find the body.

And after the body we can take a new line.

Of course we need to copy this once again.

And here you can simply include this.

And as soon as this is included, you can simply save it.

And as soon as this is saved,

you can come back to your web page and you reload it.

And then this thing will pop up.

So you'll see it's here, disclaimer,

by using this chatbot you agree to the terms and condition

and then you can press start chatting.

And here you can edit every single thing that you want.

So you can type in stuff,

this thing is powered by a low wise answer one.

And if you want to change this things up,

of course you can simply come into this configurations.

And here you can change like everything that you want.

If you want to have for example another welcome message

you can simply type in just hey, then you save it.

And if you reload this page,

you see down here that we only have hey.

Of course you can give custom branding and a lot more.

But this is not really the point of this tutorial.

Generally speaking we talk about MCPs.

This was just a small little X course.

You can absolutely integrate this in your web page

in the web page of your clients.

You can sell these applications.

You can make custom branding and do a lot more.

If you have problems with this cold snap,

but you can simply give it to chat.

APT you can give custom icons.

You can do a lot of cool stuff and you can integrate

these applications into every single web page

with custom branding with everything that you need.

And of course in the background,

flow wise will work and also your MCP servers

that can also connect to any then and to everything that you want.

So in this video you have learned how we can host flow wise

on render in the cloud.

You can work completely for free if you just want to test this out.

But your chat flows they will disappear over time.

If you want to host these things forever for other clients

and if you want to have access all the time to your chat flows

in the cloud, of course you need to have the small plan,

the starter plan with 7 bucks a month

and you need to insert all these variables.

Then you are completely safe and you can use this forever.

This is really really important.

But the 7 bucks a month they are really really cheap

because if you do this for other people

you can charge them good prices.