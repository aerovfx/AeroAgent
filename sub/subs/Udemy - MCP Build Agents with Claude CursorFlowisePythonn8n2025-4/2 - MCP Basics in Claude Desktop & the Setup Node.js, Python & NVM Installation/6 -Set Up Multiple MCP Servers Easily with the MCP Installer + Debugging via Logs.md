# 6 -Set Up Multiple MCP Servers Easily with the MCP Installer + Debugging via Logs translated

---

And this would be a one to show you a nice little trick how you can install every single server a lot faster, a lot easier.

If we come back to this documentation once again, you see that the next steps after you have tested this out is, of course, exploring other servers.

And every server is relatively easy to set up.

You can use Postgres SQL. You can use SQLite. You can use Google Drive.

If you use Google Drive, you also need to go into Google Cloud Console later on this, we will dive into this in detail.

If you are a developer, you can include Git, Git, Top Git, Lab, Sentry and so on.

If you want to include web browsing tools, you can use the Brave Search, you can use Fetch, you can use Bupadeer.

We will take at this a look in later videos because I do think this is cool.

You can also include Slack, Google Maps, Memory.

This is also a cool feature because this is graph-based, related to a persistent memory system with knowledge graphs,

similar to a vector database and it works locally.

You can basically include a lot of different servers and every server is a little bit different to set up.

And if you come on these servers, a nice documentation will guide you through it.

On some servers you need to install a bit. On other servers, you just need to plug in an API key and so on.

All of this should be relatively easy, relatively self-explanatory.

Over the course, we will integrate some different servers that are a little bit different to implement,

so don't worry if you do not understand every server just yet.

But if you scroll down, you also see that you have the official GitHub repo for all the servers.

If you open this up, you are basically, let's just see, on this GitHub repo,

model context protocol slash servers, and here you see there is a lot that you can install.

And every server is a little bit different to install, the config file needs to look a little bit different.

You need to include maybe an API key or two or something like this.

And we also have a second GitHub repo, also MCB servers.

And here are even more awesome MCB servers.

Most of the servers focus specifically on tools, because I do also think this is the greatest point of leverage.

If you want to include different tools for gaming, for knowledge and memory,

for whatever you want, you will find a server for it, like 99% of the time you will find a server for it.

But every server is a little bit of a pain to set up, at least sometimes.

And that's why I want to show you this server.

It's called the MCB installer, and it already has over a thousand stars on GitHub.

And it's also really, really easy and nice to use.

If you scroll down, you see how to install it.

You just need to put this into your cloud desktop config file, and then you are basically ready to rock.

I just want to show you how this works.

You copy this.

This time you see we have MCB servers.

It is the MCB installer.

The command is this time once again, npx and not uv.

And the arguments is simply the GitHub repo.

So you can simply copy this.

And attention, we do not start with a currently bracket.

So we come into cloud.

You can come back once again here, on file, settings, developer, edit config file.

We open up our old config file and we throw it right here.

This right here is right now our old one.

It also works with npx, so also not with uv.

And what you should do right now is to delete all of this.

Just for the sake of this tutorial.

Now you do not have to delete this file every time,

but I will do it in this course so that we can work clearly

so that you can see it every time step by step.

And now I include the server.

And maybe you already guessed what's wrong.

Of course, we do have a syntax.

This stuff is also right right now.

We always need to start with a currently bracket.

So what you can do is of course, to throw this into a currently bracket.

So what you can do is do the lead this once again.

Then you throw in your currently bracket and in your currently bracket,

you include your code.

For better clarity, you can also take a new rundown here and boom.

Then you have everything included without syntax errors.

You see it, nothing is right anymore.

And now you press safe.

You can also press it on file, safe.

And then you are ready to rock.

So we close this down.

We also close down the plot completely so quick.

We can also close this down.

Then we will open up the plot once again.

And now we have this mcp installer installed.

And this thing helps us install more awesome servers

from GitHub from wherever you want.

If you press on it, you will find just a second.

It will pop up relatively fast down here.

You see it mcp installer, you can press on it.

Install repo mcp servers or install local mcp servers.

So this thing helps you install mcp servers.

And everything just in cloth.

This is really cool.

Let's just come back once again into the settings,

into developer and once again into this config file.

This config file right now looks something like this.

But cloth has now access to this config file and can edit it.

And I want to show you how this works.

Let's just say you want to install another server.

You can do it right now in cloth directly.

Let's just come to also mcp servers.

And I want to find something for, let's just say YouTube.

Here come on, a YouTube transcript.

I can simply press on this servers.

And let's just say I want to have transcripts from YouTube.

I can scroll down and then you see how you can install this.

So here you have some commands and so on.

Then you have your configurations for the config file.

And sometimes especially if you are completely new to development,

this can be like a little bit hard for you.

Not for everybody but for some people.

If you open up your config file,

you already have some stuff included.

And maybe it's like hard for you to grasp how you can include this file.

If you already have included this file.

And right now this thing will simply do this for us.

So what you can do is to just copy this line.

So just the line that gives us the arguments.

And then we can simply ask cloth.

So just copy this line.

Then you can come back into cloth and you tell something like this.

Please install this mcp server for me.

You don't have to tell please and you also don't have to make typos.

I hope you get it.

But right now our mcp server should be activated.

You see I just want to allow always.

And then it will go into my cloth desktop config file and it will edit it.

It's already done basically.

Let's just see.

Boom. There we are.

And here you can see that without a syntax error,

we have our second server included.

So the first mcp server is of course the mcp installer.

It's mcp servers, mcp installer, the command is npx.

The argument is this right here and then we are done.

And then we start with the next mcp server.

mcp server YouTube transcripts.

The command is npx.

The argument is this thing down here and then we are done.

And no syntax errors.

You can close this.

Then you can restart cloth once again.

So quit.

Open it up once again.

Let's just see.

Now we press right here and we wait.

There we have it.

mcp server YouTube transcript.

You can press on it and you see.

You can get the transcript.

So let's just test it out.

I am right now on my English YouTube channel.

Yes, I have a little bit of a bigger one in German.

In English, I just have one video excuse me for this.

But I just want to get this transcript from this video.

It's a long video.

To the telegram we can do is to simply copy this URL.

For example, then we can come back into cloth and I ask something like this.

Make a summary of this YouTube video.

And I send it out.

Then our new mcp server will get most likely triggered.

I just want to allow this always.

The language is English.

You can also come to my German YouTube channel by the way and make a quick summary.

And right now we will get the perfect overview.

So building AI agents with NADN video summary.

Yes, I am building AI agents with NADN in this video.

The core setup, the platform is NADN.

Then the main interface, the AI models that we use,

the architecture, the telegram,

bot integration, core functionalities for g-mails, labeling,

and so on calendar, web research, contact management, social media,

and so on.

So basically this is all the stuff that I go through in my YouTube video.

You can also close this down and rate for yourself here just a tiny bit if you want.

So in no time whatsoever you can make your summary for YouTube.

Video this can also be really, really practical if you just want to include this in cloth.

But the most important thing is that you can install every single mcp server in no time whatsoever.

Let's just include a third one so that you can see that you can install

how many servers as you want.

But a little bit cautious here.

If you include like 20 or 30 servers,

you rather than will at some point not be smart enough to decide the right server to use,

you should always keep this in mind.

Let's just come to the servers and include one more thing.

Let's just scroll down and I think I want to include the time.

Because cloth does not know what time it is.

Because it has mostly no internet access.

And even then like it always has to search the web.

So let's just see time mcp available tools get current time, time zone and so on.

You can install it via uv.

So instead of pip install or uv install let's just come to this configuration of the cloth app

using uvx.

Um um um let's just try this thing here.

And I need to make something clear.

The command is here right now uvx.

This means we work with uv.

Uv is a package manager of python.

You need to have python installed and you also need to have uv installed.

If you do not have this installed don't worry, you will be covered in the next video.

But for the sake of this tutorial I will go on right now and I assume that you have

python and uv installed and if not like don't worry, you will run most likely into an error.

But the error will be fixed at latest in the next video.

So just keep watching but remember uvx if you want to try this right now you need to have

python and uv installed.

The arguments we simply copied is arguments and we tell.

Please install this mcp server.

I hope you have a quick time and you will see it in lifetime.

It will be relatively fast.

I'll at least I think so.

Let me install it for you.

Boom and there it's added so it was really really fast.

So we have the mcp server time command is uvx.

The arguments mcp server time.

Before we can run this.

So let's just see.

I just want to close this down.

I am not entirely sure if we need to run in the terminal our uvx command or not.

But let's just test it.

I save this.

I close it.

Then I also close down cloud desktop.

Let's just reopen cloud once again.

And see if we get our mcp server or not.

And there we are.

We do have some troubleshooting.

So we can open up mcp settings.

This thing has some errors.

So let's just open the lock folders.

Server and time.

This thing is the stuff that has errors.

You can simply copy all of this and ask what's the error.

Let's just test it out.

What is the error here?

It is really that easy if you always have an alarm.

We need to set the proper time zone environment variable before running the server.

And you can also see here what's the exact problem.

This is a Windows specific issue where the system time zone name contains

a space or a special character that aren't properly handled by patents.

So name for model.

The error occurs because the mcp time server is trying to get your local time zone.

Windows reports it as middle-oil-oil-base is on the other side.

So this is of course in German and our mcp server or

Python doesn't understand this.

Python's zoning for expects standard IANA time zone.

Like for example Europe or Berlin or Europe Vienna.

And that's why we need to set this of course,

either in our terminal or we can also try this to edit it in the config file.

It should work and maybe we are also lucky and our mcp server can do this for us.

We can either set it in the terminal directly or I just want to test this out.

Let's just see.

I just want to ask the mcp installer if it can change my config file.

Please change my config file so that the server will run.

Use the mcp and there you see as the arguments we use Berlin right now as time zone.

So I do think we got an upgrade.

Let's just see file settings developer.

Let's just see edit config file.

We do have the local time zone as Europe and Berlin.

It is saved.

Let's just restart cloud and see if it works right now or not.

Quit re-open cloud.

Until now no errors.

Let's just press on it.

mcp server time.

Get current time.

Convert time.

What time and date is today?

We ask our mcp server always allow.

It should use Europe or Berlin as the time zone.

So this was a Windows specific problem just for me because I live in Europe.

And you see it's Monday, June 2nd, and 3 15 pm.

And this is exactly the time and date where I am living in.

This is perfectly fine for me right now.

So it can be really that easy.

In this video you have learned basically I do think a lot.

You can install mcp installer.

The mcp installer will help you install all of your mcp servers that you want.

You can start with a simple server just like the YouTube transcript.

Then I just wanted to include this time zone.

And this time zone had some problems because I live in Europe.

And my Windows is in German like it was MS.

It was mid-low-irubation side zone and our server did not understand this.

So I simply opened up the logs.

I throw the logs into the slot.

The slot found out exactly what's another right for our server.

And then I told the slot, please just edit my config file.

The mcp server can edit my config file.

Can include that I use the Berlin time zone.

And then I have my config file working once again.

You can do this with every single server under the sun.

If you have API keys and you do not know how to include this API keys

just throw the logs in, add Cloud how to fix it,

and then ask this server to fix your config file.

It's really a game changer.

I do think this video can help you save a lot of trouble shooting.

Just install this mcp installer.

Throw in the arguments of the thing that you want to install.

And if you have problems in the logs, throw the logs in and ask

Cloud if it can fix it and write a new config file for you.

This is a game changer.

I'll see you in the next video.