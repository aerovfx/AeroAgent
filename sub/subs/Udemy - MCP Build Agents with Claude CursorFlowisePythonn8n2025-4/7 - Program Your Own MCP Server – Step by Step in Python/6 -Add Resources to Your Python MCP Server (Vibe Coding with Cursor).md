# 6 -Add Resources to Your Python MCP Server (Vibe Coding with Cursor) translated

---

In this video, we will integrate resources into our Python MCB server.

So if you can actually on the documentation, you see that you also can add resources you already know it.

And in this overview, you see that you can add, for example, file contents, database records,

API responses, live stream data, and so on, so you can add a lot.

The resource URL should be structured something like this.

And here you see some examples. If you have a PDF, for example, on your local machine, you can give the file path.

If you have something in postgres, you can give it like this.

And if you have something on your screen, you can give it like this.

The resource types could be of course source code, configuration files, log files, XML data, or plain text.

And you can include images, PDFs, audio files, video files, and a lot more.

And here you see the direct resources that you can include like something like this.

With JSON format, here you see that you can also include resource templates, with dynamic resources, with a code something like this.

Reading resources, if you just want to read your resource, you can also make resource updates.

And here you see some example implementation for typescript, but we work in Python right now.

It should actually look something like this.

And here you see the best practices, security considerations, and that's basically it.

What we want to do is we work of course with the Python SDK, but let's just assume that you in your server wants to give a resource how to use the typescript SDK.

What we are doing is we open up the typescript SDK and we come to the readme.com.

And actually I just want to copy all of these readme.

So copy raw file. And actually I just want to throw it on my local machine.

So I make a new let's just say text file. I call it die script SDK MCP.

And it should be not dot TXT. It should be dot md because we want to have it in markdown.

Then I open this thing up and I include all the file from from previous so boom.

So boom right now we have everything included. We have the whole typescript SDK included how to use all of it.

This seems to work perfect. I want to save this. I close this down.

And what we want to do right now is I just copy this file.

So copy as path. Then I open up cursor and I tell cursor something like this.

I want to include a resource in my MCP server.

Please follow the at docs MCP full and implement this MD file from my desktop as read source.

Here is the link to the file and I include it.

And right now I send it out and let's just see if cloud can pull this off or not.

Right now my connection failed. Why does my connection fail?

I have some problems. I also do think that maybe this link is not perfect.

So let's just do it in the terminal.

So I come back to this content right here and I copy this.

Then I open up terminal and in this terminal I write something like this.

See the desktop. Let's just call it new item.

Name. Let's just call it type SDK.md.

Then item type should be a file and I send it out.

Then I type in notepad type SDK.md and we send it out.

This thing gets opened up right now in my editor.

I want to include the whole SDK.

Should be included right now. Let's just save it.

So I have my file and everything is saved.

File is also here. It's called right now type SDK.md and it should be also opened up in this terminal here.

We come back to cursor and I tell cursor I want to include a resource in my MCP server.

Please follow the MCP LLM full and implement a file from my desktop.

The file is called type SDK.md on my desktop and I send it out.

First it was reading the type SDK.

Then it included everything in our server and it tells me that it works.

The URL is file type SDK and also on the file path.

If I'll path see user Arnold desktop type SDK.md seems to work.

Key features and so on. Let's just see what we have implemented.

The git ignore should be the same Python version the same.

This is the same. Also this is the same.

Read me. The read me we could eventually update.

The read me because we have right now.

Also this included but let's just come to the server.py.

In the server.py we need some new library race.

We need to include OS and we need to include import path.

Except then define the path to resource file.

The resource file path is this right here.

This seems to be fine. Then we use this time of course not the tool.

But we use at MCP resource. This is important.

So we don't use MCP tool but we use MCP resource right now.

And the file is this typed SDK from my desktop.

And the path is this right here.

We use the ASIC Dev provide access to the Dabbed Script SDK MCP documentation.

This resource contains information about the Dabbed Script SDK for MCP.

Seems to be fine. Then we use OS and if it's existing we use the desktop file path.

Open with desktop file path.

We have seems to be fine. I do think this works.

Yes. So accept. This seems to be just fine.

So I do think we have this included.

What we need to do next is we need to come to the MCP inspector.

We restart our server. So this is right now connected.

Right now we come to resources and we press list resources.

Boom. Get typescript resources.

And here you can see that we have our resource included.

So here is everything.

And right now let's just see if also in cloud we have these resource included.

In order to see the resource we need to restart cloud because yeah.

Always the same thing with cloud quit. Open up cloud.

We press on it. The calculator is still included but where do we have our resources?

I will show you. You need to press on plus.

Add from calculator server.

Get typescript resource. Boom. And there we have it.

So you can press on it and see we have the whole typescript SDK included as a resource in cloud desktop.

And then you can tell cloud desktop something like this.

Please build a simple typescript MCP.

Use the docs include a tool that can use the tool.

That can use the weather API.

Then of course you would give the weather API and so on.

I just sent this out just as an example and right now cloud can work for us and it can build of course really really nice MCP servers.

And right now you see we get our code back.

But the main point for me is that you can include every single resource that you want.

Just an example. You can come to the documentation and see for yourself what you want to include.

But it always works completely the same.

You can include images, PDFs, audio files, video files or other non text formats.

You simply give the path and then it should work. Have fun including resources and in the next video we need to include prompts.