# 001 WiFi Connect Implementation Overview en

---

Hey, welcome back.

In this section, I'll give a brief overview of how we're going to connect the ESP thirty two to an

access point via the web page.

So let's jump right into discussing our implementation.

We'll create text fields in the Web page where we can enter the credentials of the access point that

we want to connect to and to connect button to trigger the action to connect on the server side.

The web server will handle receiving the credentials we've entered, updating the Wi-Fi configuration

and then attempt the connection, and the application will let the user know the connection status by

displaying the connection result on the web page, whether it was successful or not.

Additionally, will display the connection details on the web page the access point name that the ECP

32 is connected to and the IP information assigned to the ECP 32.

Furthermore, will implement the disconnect button that the user can use to disconnect Wi-Fi via the

web page.

And lastly, we'll use our GB led to indicate the connection status when the ESP 32 is connected to

another access point.

All right, so let's take a look at some of the impressive IDF APIs we'll use in this section.

OK, so what's the Connect button is pressed in the web page side.

Our uteri handler for receiving credentials would be triggered and the HPD requests get header value.

Length function will be invoked.

This function returns the length if the field is found in the request URL or zero if the field is not

found or it's an invalid request.

Next, the PD requests get header values.

String function is used, which gets values from the text fields.

After that, we'll need to update the wife by configuration, and we'll update the data in the Wi-Fi

config structure.

In this case, we need to update the station details because this pertains to the ESP acting as a station

connected to another API.

In our case, we need to update the SSA, ID and password of the access point that we're connecting

to.

Then we will set the configuration using the ISP, Wi-Fi set configuration function.

And again, in this case, the ISP is acting as a station because it's connecting to another access

point.

So we'll specify the ISP interface Wi-Fi station.

When doing this, then we'll need to call the ESB Wi-Fi Connect to attempt the connection, which connects

the ESP 32 station to an access point using the SSA, ID and password.

We've set the configuration for and later we'll implement the Disconnect button, and this case will

use the ISP Wi-Fi Disconnect function.

This function will disconnect the ESP from an access point that it's connected to.

In upcoming programming sections, we'll get the inside for display on the Web page.

We'll take the Wi-Fi Access Point record structure, which holds the description of the wi fi app and

pass it to the ISP Wi-Fi station, get access point information function to get the Society of the Connected

app.

We'll also get the IP connection information by using an instance of the ISP network interface, IP

infrastructure and passing it to the ISP network interface.

Get IP info function, the IP Gateway and netmask.

Information obtained from this function will be in numeric form and will need to be converted to dotted

decimal ASCII.

And we will do that by using the ISP IPv4 address into our function, which again converts the IP address

into dotted decimal ASCII.

And at this point, we'll have the strings that we need after using Sprint F, and we'll send the response

to the web page using a ftpd response and as we have been doing in our you array handlers.

So just to refresh, the ESB 32 will be an access point station mode, an access point in that other

devices can connect to it and a station, and that it will be connected to another access point.

So that's all for the background info.

Let's get started.