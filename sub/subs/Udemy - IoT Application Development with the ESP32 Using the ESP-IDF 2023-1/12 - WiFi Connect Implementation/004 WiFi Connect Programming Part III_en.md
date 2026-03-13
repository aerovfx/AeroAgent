# 004 WiFi Connect Programming Part III en

---

All right, so let's continue and let's grab this message, and then let's head over to wi fi up that

scene.

And then here under the connecting from HTTP server case, let's make a comment here and say attempt

to connection.

And then right, we Fayette Connect.

Stay.

And this function will define that later.

All right, now, let's say, set current number of retirees to zero.

And the global reach by no.

Just set it to zero.

OK, next, let's let the FTP server know.

About the connection attempt.

And then call FTP Server Monitor Send Message.

With ADHD, http message, wi fi connect and it.

And then next, let's define the Connect function.

Now that's coming to you connects the ESB 30 to.

To an external access point using the updated station configuration.

And it's a static void.

WI fi app Connect Stay and it's void.

OK, now let's check.

ESP Wi-Fi config.

And passed the ESP interface, wi fi stay.

And for the config, we can call wi fi app, get wi fi config.

Next, let's SPRO, check the Spotify Connect.

And that's all.

All right, so now let's go to the event handler.

And under the stay disconnected case.

We're going to print some some disconnect error codes.

So come here and let's use wi fi event state disconnected type.

And that's a pointer Wi-Fi event, stay disconnected.

And now let's typecast Wi-Fi event, stay disconnected.

And now memory allocate the size of Wi-Fi event, stay disconnected.

OK, and then let's set the value that this points to.

All right, and then just follow me here.

It's a value and we're typecasting.

Right.

And we want the we want the event data.

All right, and now let's just print the information.

Stay disconnected.

Reason code.

Goes here.

And it's from Wi-Fi event, stay disconnected, and let's access the reason.

Like so?

OK.

And then, right, if global reach by no.

Is less than Max Connection retrace?

Then let's call ESP wi fi connect again.

OK.

And just increment the global retry number here.

Else, we're going to send a disconnect message.

So do we fight send message?

Why fi app message stay disconnected?

So let's copy this message, because it's not a message.

And let's include it to our message genome.

All right, that's it, so now let's go back.

Now, let's go on to the gut IP case.

Now here we can send our gut IP message.

So we fire up, send message.

WI fi app Message Stay Connected, got IP.

OK, now let's go down to the gut IP case.

And here we need to send a message to the FTP server monitor.

So we'll say HTP Server Monitor.

Send message.

HTP message, wi fi connect success.

OK, good.

So now let's copy this case.

Let's paste just below.

Let's define the stay disconnected case.

So that's just log this message.

Let's remove the LED function call.

And then now that's in the fail message.

So now let's briefly review.

What's going on here in the handler?

OK, so if there's a disconnect we'll retry from maximum retrace and once we reach the maximum, we

seen the disconnect message.

Then we let the webserver know about the connection failure.

And in the Web server when that happens.

The global status variable is updated, and it's also updated for the successor case and an APT charges.

Our statuses reflect what happens in the Web server side, back to the user with the messages here.

So let's continue.

So now go to HGTV server.

Let's go down to the other eye handlers.

And let's get the Connect status, Jason Handler.

So we can define it.

And first, let's comment that.

WI fi connect status handloom.

Updates to connection status for the Web page.

And it's a static ESP type.

Connects that his handler, which takes the pointer to the request.

And first, let's fix this comment.

Now, just copy this one.

And leave it here.

Let's log.

That wi fi connect status requested.

And we need to care.

That is, Jason, of 100 Bytes.

And then sprint deaf to it.

Our escape sequence.

For Wi-Fi Connect status.

And here, just give it the global Wi-Fi Connect status variable.

Now said the response type.

For the request and its application, Jason.

Now, let's send the response.

For the request.

From the status, Jason.

For Stalin of status, Jason.

And then let's return.

ESP, OK.

And that's it.

And as for a wife, iconic status and the index HTML, that is just right down here.

And also, we have the credentials errors.

So let's just test it out and build.

Right now, we can flesh.

OK, now let's open up a monitor.

Can now connect the ESP.

Now, let's go to the Web page.

Right now, if we hit Connect.

We get our error messages for both the suicide and the password.

And if we type something in the password field.

Only the suicide warning shows.

OK, and then just the suicide and the password warning appears great.

And next, I'll try connecting to an access point.

Nail into a fake password here.

And I'll show it.

And then I'll try to connect.

Now it shows connecting.

And now it's tempting for each retry.

And some reason codes are now printed here.

Which you can feel free to look up.

And after the Max Retrials, the Web page is updated with a failure message as expected.

Nice.

OK, so now try to connect with the real password.

And I'll try to connect.

And.

Very nice.

We have the connection success message, awesome.

And the terminal messages confirm what we expect to see.

So that's it for this one.

I'll see you in the next.