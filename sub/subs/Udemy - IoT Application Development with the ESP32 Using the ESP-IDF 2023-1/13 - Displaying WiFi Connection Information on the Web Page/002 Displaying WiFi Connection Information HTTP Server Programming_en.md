# 002 Displaying WiFi Connection Information HTTP Server Programming en

---

So let's continue the display and connect info section by further developing the Web server to send

the connection information.

So let's now head over to HTP server does seem.

And first, we need to include ESP wife died because we need functions there to get the app and IP info.

So here let's include.

DSP wi fi Duddridge.

All right, and now let's head down to the you are right handlers.

And let's copy this one.

So we can use it below.

You know, update the name to Wi-Fi Connect info.

And the structure name as well.

And let's update that you are right to Wi-Fi Connect info.

Jason.

And the method is to get.

And the handler will call FTP server life.I get connect info.

And then take the name of the structure and let's pass it down to the euro handler.

And now let's go up and define the handler.

So first, let's take this comment.

And pasted down here.

And change this to wi fi connect info Dot, Jason.

And it updates the Web page with connection information.

Now, let's go back and grab the function name.

And now back to the definition.

And stay static.

Espera type.

Our handler name and it's the request type pointer.

Our HQ.

Now, let's first ESP log info.

WI fi connect info that JSON requested.

And next, we need a care IP and Phil Jason.

Of 200 bytes.

And that should be more than enough.

And then let's set.

IP info, Jason.

Two zero.

For the size of.

IP info, Jason.

And now we need a buffer to hold the IP address, so say care IP.

And the size is IP for address star Len Max.

And this definition will give us the maximum length for an IPv4 address.

So now let's copy that.

And pasted twice.

Now, let's do the netmask.

And the Gateway.

Then let's say if global Wi-Fi Connect status.

Is HTP Wi-Fi status connect success?

Then we need wi fi, AP record type.

And call it Wi-Fi data.

And now let's espero check.

ISP, Wi-Fi.

To get a info and then pass a reference to Wi-Fi data.

OK.

Next, we need a care pointer as a side equals.

Care pointer type cast.

To the Wi-Fi data, Typekit as a side.

And if we follow that, we can view the entire description for the wi fi app record.

So now use the ESP net if IP info typedef.

And call it IP info.

Then do.

Espérer, check.

ESPN net if get IP info.

And then pass or ISP net if state object.

And then a reference to IP info.

And if you recall, this is our station object.

OK, so next, let's convert this IP info to human readable form using ISP.

IPv4 address.

Network to ask you.

And pass a reference to the IP info that IP.

And the IP buffer.

And the length, which is IPv4 address.

Starlin Max.

So copy this line.

Then let's paste it twice.

And then first to the IP in Phil Netmask.

In the netmask buffer.

And then do then do IP Info, Dot Gateway and then pass the gateway buffer.

Next, Sprint Deaf and to IP and Phil Jason.

The escape sequence.

First for the AP.

Then for the netmask.

And then also for the Gateway.

And lastly, for the AP.

And then close it.

And then let's provide variables for the IP netmask.

Gateway and suicide.

And then use the HPD response, said type.

For the request as application JSON.

And then use a speedy response, send.

For the request from AP and Phil Jason for this story, Lin of AP and Phil Jason.

And then I'll return ESP, OK.

All right, so that's it for the handler.

However, I would like to rename it, and let's just do just this white flight part.

So right click here.

You've got to refactor factor, rename and change it to get Wi-Fi.

Connect info and then hit Enter.

OK.

That's it.

Now to recap, this handler checks the global Wi-Fi Connect status, and if it's connect success, meaning

that there is a connection, then we get the connection information and update the IP info JSON with

the connection info and then we send it.

Otherwise, the IP info JSON is sent blank, in which case nothing is displayed on the web page.

OK, so now let's build.

OK, now, flesh.

Now open a monitor.

And then connect to the ESP.

And then go to the Web page with Chrome.

And now let's connect the ESP.

No connect.

And.

There you go, the access point that the ESP is connected to is displayed as well as our assigned IP

information.

All right, well done.

Now, if you refresh the page, the connection success should go away.

So let's try that.

Refresh the page.

And yes, that looks good.

Great.

The connection success message went away.

All right.

So I'll see you in the next lesson and we'll implement the disconnect button here.