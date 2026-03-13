# 003 DHT22 Sensor Programming Part II en

---

All right, so first, we need to update the HTML document for the DHT twenty two censored data.

So let's create a section for it right here.

Let's create a divide.

And call it DHT, 22 cents of.

Now, let's create an age two and say DHT 22 sensor readings.

Now close that.

Then we need a label for.

Temperature reading.

And right temperature.

Colin and close the label.

Next to the divide for temperature reading.

And then close the div.

Then now we can create a label for humidity reading.

And then let's right humidity, Colin, and then close the label.

Then now let's create the divide for humidity reading.

And then close the diff.

Now we can close the DHT 22 sensor diff.

And then let's put a horizontal rule right here.

Next, let's grab the temperature reading and go to the stylesheet.

And he will give it the same styling as some of the other elements, so let's create the styling for

it right here.

And we want to display in line, so let's grab this one and pasted here.

And we also want to give it the same color.

So let's paste that there.

So now let's copy this.

And then paste it here.

And now we want the humidity reading.

So now just include it there.

All right, that's fine, so now we can go to James.

And now let's go down to the bottom of the file.

So now let's create a function.

That gets the DHT 22 sensor temperature.

And humidity values.

For display on the Web page.

And will say function, get DHT sense of values.

He will use to get Jason Method, so say, dollar sign.

Don't get Jason parentheses.

Single quotes.

Forward slash DHT center that Jason.

And then function parentheses data.

And then open curly braces.

And say dollar sign.

In quotations, pound temperature underscore reading.

And then say dot text in parentheses, data brackets in quotes, say temp.

Now, let's just copy this.

And then paste it and then just change this to humidity reading.

And now this one to humidity.

Now, just close it with the semicolon.

All right, so next, let's create another function that sets the interval.

For getting the updated.

DHT 22 sensor values.

And right function start DHT sensor interval.

And then here will use set interval.

And pass to get DHT sensor values, function name and we'll call it every five seconds.

Now, let's copy this function.

And let's go up to the document ready function and paste it right there.

OK, cool.

So next, let's go over to the FTP server, see?

And first here, we want to include the DHT 22 to date each file.

Now we could go down to register that you are right, handler.

Invite, you will say register DHT Censored.

Jason Handler.

And now I'll go to Etta James just to make sure I have the right name.

OK, good.

So let's go back.

And create the handler.

For the DHT center, Jason.

And here the you are right, is forward slash DHT center, Jason.

In the method is HTP Get.

And the handler.

We can call HTP Server, get DHT sensor readings.

Jason Handler.

And user CTCs is no.

Then now let's register the handler.

In past the HTTP server handle and a reference to the DHT center JSON struct.

All right, so now let's go and define this handler.

So copy it.

And you will say.

DHT sensor readings.

Jason Handler responds with DHT 22 sensor data.

And for the parameter and the return, let's just copy from up here.

And then just paste it.

OK, then let's just grab the name again.

And now we can say static diaspora type, know a handler name, and it takes the HTTP request type.

Point to barbecue.

Next week at ESP Log Info.

That DHT center that Jason requested.

And then we need a care DHT center, Jason Buffer.

Of 100 bytes.

That should be enough, and then we can now sprint off into the DHT center adjacent buffer.

Then we can do the escape sequence here for the Jason to just follow what I do now.

So first for the temp.

To one decimal place.

And next to the humidity.

And that is also to one decimal place.

And now we can close it and call get temperature.

And also get humidity.

Then let's set the response type.

For the request and its application, Jason.

Then send the response.

For the request.

And DHT censor Jason.

And still of the DHT censor, Jason.

Then return ESP, OK.

OK, it looks good.

Now let's build.

OK, now where's here?

So then let's flesh.

And don't worry about this, there's a problem recognizing ESP luck, and there's a fix for this that

I'll provide to you.

OK, so let's just proceed.

OK, we're flesh, so now let's open the monitor.

And now connect to the ESP.

Let's now use Google Chrome and then navigate to the ISP's IP.

And give the JavaScript functions a moment to be invoked.

And there you have it.

We have DHT.

Twenty two cents of data displayed in the web page.

Excellent.

And the data is updated on the page at the interval that we specified in J.S..

All right, so we could see our handler requested and the DHT sensor readings perfect.

But now let's comment out these print deaths, because we no longer need them now that the web page

shows the data there.

So let's get rid of that.

And in the next section, we'll talk about connecting and disconnecting Wi-Fi.

All right, so see you there.