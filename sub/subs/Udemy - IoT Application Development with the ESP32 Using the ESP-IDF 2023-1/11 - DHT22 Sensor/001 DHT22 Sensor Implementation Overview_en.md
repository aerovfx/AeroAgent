# 001 DHT22 Sensor Implementation Overview en

---

Hey, welcome back.

In this section will implement the DHT twenty two censored portion of the project.

So let's take a look at the overview.

And this course, we are using the AM to three zero two DHT 22 temperature and humidity sensor module.

This is a very popular, easy to find module, and if you do an online search for the sensor, you should

be able to find an online store that can ship it to your home country.

This module outputs a single digital signal and contains a calibrated temperature and humidity combined

sensor.

It only requires three connections, so you'll just connect the data line to the GPIO that we'll define

in the firmware and also connect the VXI and ground lines on the ESP 32 to VXI and the ground lines

on the DHT 22 sensor.

Also, a couple of more notes about the sensor.

It provides higher accuracy than the HD 11 variant, and the temperature ranges from negative 40 to

80 degrees Celsius, and the humidity range is from 20 to 90 percent.

And here is how I've connected the DHT 22 to my Rover Dev kit.

The blue wire three point three volts on the Dev Kit is connected to VXI on the DHT 22, and the gray

wire ground on the dev kit is connected to ground on the DHT 22 and the Purple Wire is GPIO 25 on the

delicate and connected to data on the DHT 22.

All right, so that's the three connections that we need.

All right, so let's take a look at how will accomplish getting the sensor data, the sensor data readings

will be handled by an existing library for the DHT 22 sensor.

I've attached the DHT 22 Dot C and Dot H files to.

The resources for this section will include these files directly under the main folder will create a

free autos task to read the DHT 22 data at a specified interval, and we'll test it.

Next, we'll update the web page files the Index HTML app to Access and APKs files in order to display

the updated data, and the web server will then need to be updated to respond to the get requests with

temperature and humidity data from the DHT 22 sensor.

And that's it, so now let's get the programming.