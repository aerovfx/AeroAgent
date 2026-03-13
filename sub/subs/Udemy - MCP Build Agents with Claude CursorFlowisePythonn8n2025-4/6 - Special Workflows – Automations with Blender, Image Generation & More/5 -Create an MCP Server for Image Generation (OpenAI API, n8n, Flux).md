# 5 -Create an MCP Server for Image Generation (OpenAI API, n8n, Flux) translated

---

In this video I want to show you some kind of a special workflow, because some hosts can

absolutely not generate pictures for you.

And of course you can integrate every single picture API that you want.

You can include Flux, you can include Flux context, you can include the OpenAI Image model,

you can include every single API that can generate pictures, and in this video I want to give

you a basic setup.

We will create an MCB server, the MCB server will be a little bit different, a little bit

special, and then you can connect the server like to every single host that you want.

The first thing that we do is of course to create a workflow, then we press plus and

we want to have an MCB server trigger.

On this MCB server trigger we need to do something special, because we need to include the tool,

and the tool will be called an A-DAN workflow tool.

Why this tool?

This tool is a little bit special, or more likely the workflow is a little bit special.

We need to call another workflow.

This other workflow will generate the whole picture because we need maybe to move like

base64 to some different kinds of settings.

So what I want to call this is for example MCB, pick generation, and I want to save this.

Right now once again we can come eventually in a new workflow or we can also do it right

here in it.

It does not really matter.

For the sake of this tutorial I just come to a completely new workflow, but you can also

do it right in this workflow.

So you press create workflow, then we press plus once again, and here we need to use when

executed by another workflow.

So we simply include this, and down here we use right now for this minute except all

data.

Later we maybe need to fix this like to a chase input, but first let's just work with

except all data.

And the next thing that we need to do is to use a HTTP request node.

Because we always need to send out a HTTP request to include the image model that we want.

And now you can decide for yourself.

Some image models that I really love are for example the Vlax context models.

And here you can include whatever you want.

Replicate gives you a lot of really really cool examples.

Face to many context so you can upload for example a picture review and make it like

into different settings.

You can do like a lot of cool stuff with it.

You can also use just normal multi-image list things.

You can basically call everything LAPI that you want.

And if you need to do this you can simply come on run with an API.

Then you come of course on HTTP.

And you can just copy this call.

Then you would come on this HTTP request node and here you simply include your call.

You import it.

And then you need to fill out your bearer API key.

So here you need to include the API key that you will find on replicate if you come to

your API keys.

Because this is a little bit too easy for us.

We will do it in the harder way the way that is right now a little bit harder to set up.

But you can also work with flux.

What I want to do is to use our HTTP request once again and we want to use the image model

from OpenAI.

The OpenAI image model is really really great.

It's also a little bit slower to run.

It's harder to set up.

I just show it because it's harder to set up.

Because here we get basic 64 back and we need some steps that you do not need if you use

just this flux models.

So if you want to create images with this API, of course, we need to set it up first.

We need to come to the image API.

And here we get the examples that we can use.

And you see that we only have this Python example.

But don't worry, we can set it up really, really easy.

Here you see the stuff that is required.

You always need to have a prompt.

And you need to make your API calls exactly on this API and you need to have a post request.

So of course, just copy this thing right here.

Then we come back.

We come to our HTTP request.

This time, of course, it's post and we post on this API.

Then we need to have our authentication.

Then I use preferred credential type.

And here I simply use OpenAI because I have OpenAI already included with my account that

I have connected with an add-in.

Then we need to send some stuff right here.

And if we come back to our API, you see what we need to send out.

We need to send out the model.

The model is this right here.

We need to send out a prompt.

The prompt will be dynamic.

We need to send out a size.

The size can be this right here.

But you can also use different sizes.

Different sizes come with different prices.

You can look at the prices in more detail for yourself.

Generally speaking, these are the sizes and the bigger the size, the more expensive this

API gets.

Of course, you can also edit images if you call this API, but we just want to create an

image right now.

You are really, really flexible with this API.

So we need to send out the value model.

So just copy this.

We come back into an add-in.

We have our credentials connected.

And we need to send out the body.

The body is in chase and we need to define our fields below.

The name is model.

And then we come back to the API.

And we use this GPT image model one because this makes great pictures.

And we simply include it.

We want to have more parameters.

So press on add parameters.

Then you come back to this API.

And we want to have a prompt.

So we copy this prompt.

For example, we come back once again.

The name is prompt.

On the prompt we have value.

And the value should be an expression.

And here if you already send it some data through, you can simply map it from here.

You need to have a query.

Because we do not have any mapping data yet.

We just want to use like a variable.

So we open up our curly brackets and we open up two brackets for our chase and stuff.

Then we type in dollar sign.

Chasing.

Open up a curly bracket.

Inside of this curly bracket, we open up quotient marks and inside of this quotient marks

we type in query.

So this will be our dynamic query.

And then one last parameter.

Let's just add it.

I do think it was size.

Let's just see.

Yes, it was size.

So you can also always copy this.

Then we type in size.

And the size let's just run with 124 by 124 because I do think this is big enough.

And we include the size.

So this thing is set up and now I want to show you something special.

If you come here once again on this API, you see that the image byte comes back as base

64.

This is basically our encoded chasen.

And that's why this thing is a little bit harder to set up.

Everything that we need to include is we press plus once again.

Then we need to have a common word note.

So convert to file.

Move base 64 string to file.

We need to include this.

Then the files should come right here through as soon as we throw something in this workflow.

But I do think that I know this like from my head.

So we come on expressions, for example, but you can also leave it at fixed.

I do think this is data 0.b64 for base 64 underscores chasen.

I do think this should be fine.

If we get an error, we will simply fix it later.

But I do think this should work because also in the documentation, you can see it right

here.

We need to get the 0.b64 underscores chasen.

So right now we will make a HTTP request to generate our picture and then we will convert

our file.

You can already test this workflow.

But I do think that we should upload this workflow somewhere.

We could upload it for example into Google Drive.

So plus let's just use Google Drive, but you can use whatever you want.

So Google Drive.

We need to have upload file.

Google Drive account file upload data, then the file name.

The file name of course later you can also use a variable.

I just want to call this big.

So for pictures, then we need to use a folder.

If you don't have a folder, we will simply create one.

So new folder, mcp, big generation, create.

We come back into an add-in and we search for it.

We go, so I do think this is fine.

Let's just save it.

Now as soon as everything is connected, of course we should give this a name so that we can

find it.

Let's just call it big generator for mcp.

And I do think this is fine.

Let's just save it.

Then you can also copy this so you can absolutely throw it in this other workflow, but to make

it easier, let's just leave it right here.

Then we come on personal once again.

We come to our mcp server that we have created.

So the mcp big generation.

So this is our server.

We come on call and add-in workflow.

And on this call and add-in workflow, we need to give a description.

So for example, call this tool to generate pictures, then the source is database and we

need to choose from list.

This was of course big generator for mcp, so we would simply connect this.

And then you see this up workflow is set up to receive all input data.

Without specific inputs, the agent will not be able to pass data to this tool.

You can define specific inputs in this up workflow.

So you see we need to define our input, it should be query.

But first let's just leave it how it is and then we press save.

We can make this public, of course, so got it.

And then you can work as always with this production URL.

So make sure to save all of this up.

As soon as everything is saved, we should create our client.

Of course you can work with Cloud, you can work with everything that you want.

But I just want to make this easy and simple, so we include an AI agent node for example.

On this AI agent node, we simply want to connect the chat trigger.

So let's just start with the chat trigger moment.

Chat trigger.

We connect this chat trigger with our agent.

We connect also an AI model, of course.

I simply use the open AI models to make it fast with GPD4 or MiniDOS is fine.

And right now we need to connect a tool and the tool should be of course the production

URL of this server.

Make sure to make it public.

So plus then we need the MCB client tool.

We include this client and we give the client the SSE endpoint.

And right now we can simply trigger this.

Then we will get most likely an error and then we will fix this error.

So what we are doing right now is open chat and I simply type in create a pick of a dog.

And I send it out and then we will get the error.

We will trigger most likely the client.

I do think that this will try this like two or three times.

We can simply post as soon as we get our errors.

If it works, it's great.

If it doesn't work, we need to configure our chase format.

And boom, it works.

OK, I do think that then it has fixed this back because previously we had a bug, but let's

just see if everything worked or not.

If I come back on personal, of course we saved this right now.

And on personal we come to our picture narrator for MCB.

We close this down.

We come on executions.

Then we can basically see that we got an execution that come through.

So this means that we should have our file right here of a dog.

Boom.

And we have this dog.

It should be of course in our Google Drive.

So let's just come to my Google Drive.

Inside my Google Drive, we have of course our MCB picture generation.

And this means we have this dog inside my Google Drive.

I want to address this problem still because I do think that then I then can make some problems

here from time to time.

If you do get errors, you can come back to personal once again.

You come to your MCB picture generation.

And then you open up your executions here.

On these executions, you can simply come to your workflow.

And here you basically see that this thing, a query that's named a cute dog, came through.

So you can basically just press on chasing and you can copy this query.

And if you copy this, then you would come back to personal once again and then to your

second workflow to the picture generation.

And here on this first note, instant of acceptable data you would use, defined using

chasing below.

And in this chasing, you would delete this thing down here and include.

That one.

And you need to make sure that you don't have any syntax error.

So just delete this.

And also that one.

And then we have query, for example, a cute dog.

And then everything will get included like the right way.

So right now you can also call this workflow and you will communicate every time with chasing.

If accept all data will make errors for you.

I do think that normally this should work.

This was previously a bug, but right now it seems that then it has fixed this bug.

So make sure to choose one of these two options, either the chase below and then you can include

something like this or you use accept all data, accept all data is of course a lot easier

with less steps.

If we save this and come back once again to our MCP server that can create pictures, we

open a chat and I ask for example, make a pick of a cat right now.

This time it's a cat so that you can see that we can generate whatever we want.

And then we will connect of course to the MCP server to other hosts to see if it's still

working or not.

But we are generating a open up cloud.

And inside of cloud desktop we come of course to files, settings, the developer, we edit

our config file.

I have blender included.

I also want to show you that I have saved here.

I need an config file as a simple text file.

So you can simply copy these.

Don't worry I have already linked all of this for you.

Then you come in this list, Jason convict file in this Jason convict file we include.

This thing right here we need to call MCP server.

It's an end the command design px the argument that why super get away with the ssn point.

And here yeah this is in German you will get it in English.

Here we need to insert the trigger from our MCP server.

So we come back here our picked also got generated but first let's just copy this production

where I'll insert it in this file and save it so that we can call this and we restart

cloud.

So quit cloud right now I come to Google Drive to see if I get a picture of a cat boom.

There we have our cat so you see everything is working really really fine.

Also here you can come on personal once again you can come to this big generator for MCP

and on executions right now you can see once again of course what came through.

If you press on the first thing you see this is our chase an example but our query that

came through was a cute cat sitting on a sunny windowsill with green plants in the background.

So the AI also generated a better prompt for us it was not on their cat.

Then the next thing is of course our API call it's the query that came through then we get

our base 64 back if we come to the next file the base 64 gets converted into binary data

file it's a PNG you can also view it here and at the last note we simply upload this to our

Google Drive.

So you see everything is working you can decide for yourself make it easy start with accept

all data if you get an error use define chase below and include such an example right now

we need to restart cloud inside of cloud we should get our NADN MCP as soon as this thing

is reloaded and boom there it is and you see that we can call a NADN workflow tool and

also here you can say create a pick of a class with wine it does not really matter what

prompts you are using if we send it out I do think that this thing can make problems because

it does not know to create a tool but it did so allow always so surprise surprise everything

worked zero shot without telling that we need our MCP even if this MCP is just called call

NADN workflow it's not called big generation but still it works I've created an image of an

elegant wine glass filled with red wine for you and so on and you immediately get the link back

so you can press on it I will open this link and boom there we have our wine glass so you see how

easy this is cloud is right now able to generate picture of course cursor can do this wind surf can

do this love of the can do this every single host that you want can generate pictures for you

and remember you are not limited to the open AI API to generate pictures you can include

the flux models so flux context this is really great I do think that this is a really genius model and

you can do whatever you want with these you can also allow uploading of pictures you can allow

making for example like messy pictures into linkedin profile pictures you can create entire apps

with your MCP server you can also make requests on like other models that can generate videos you

could for example also make API calls to way of three also way of three is integrated into replicate

so you can absolutely also call a video API and also here you can simply import the curl but I

have to tell you that this thing is really expensive if you come on video free from Google you see

that this thing costs 75 cents per video generation this equals like roughly six bucks per video because

one video is roughly eight seconds long here you get an example how these videos look these videos

are great they can also generate audio we interrupt this program to bring you some breaking news

v03 is now live on replicate let's go we are MCP server you can at least in fee or a trigger

whatever you want with a workflow like this you can simply call another workflow include the

request maybe you need to move your file like into another format and then you can upload it to

google drive you can also upload it immediately to social media you can make like extremely powerful

automations maybe you just want to include for example here YouTube shorts or something like this

you can simply connect youtube and upload for example a video directly to youtube and create it

from every host that you want this is a powerful powerful concept and you can integrate whatever you

want everything that you have to do is to create a server in an event you use call another workflow

inside of call another workflow you make a HTTP request to a picture model to a audio model to a

video model to every single model that you want and you already know how you can integrate the API

cars it's really easy you simply import a curl or you type in the stuff that you need we have used

the open AI model because it's the hardest to work with because it sends us base 64 and we

need to move base 64 to an normal file if you work with another API like with flux or something else

you wouldn't even need this node so you can simply call iBI and then immediately upload it to google

drive or upload it to social media upload it to wherever you want and you can basically come to

clothe and tell clothe create a video with way of three and publish it on youtube the possibilities

are completely endless with this please please please make sure to play a little bit with these

of course i cannot make a video on every single use case you need to be creative yourself

and if you need more help for more ideas or for whatever or how to set up a specific node send

me a mail or something but i am relatively sure that you know how you can integrate everything

you know how you can call APIs you know how you can make servers you know how you can make workflows

you know how you can include the model context protocol congratulations you can automate every single

special workflow that you want let's just do it