# 5 -Authentication and API Keys translated

---

Some quick tips that you should never forget if you develop MCB servers or if you generally speaking do just something with APIs.

The first thing, never ever expose your API keys. I hope that I don't have to tell you this.

If you create API keys, store them in a safe place.

If you include API keys, hard code it for example in your MCB server and you publish it,

like that's on you, please don't do this. Always store your API keys in a safe place.

Delete your API keys before you publish something and always make sure to rotate your API keys from time to time.

Also, if you develop a server and everything works on your server and you use your API keys,

rotate them from time to time just to be safe. So stay safe with your API keys, store them safely

and rotate them from time to time. And if you develop a server, please also make sure to use a

authentication. You also know it. If you create something inside of an event for example and you

want to publish it or maybe you are in a hosted version just like me and you have this thing

addictive, make sure that you come into your MCB server and don't do it like me. This authentication

don't use none, use a bearer off or a header off and just include a password and then you are safe.

And if you don't need your application any longer because this is just a stupid example, throw this

so that people can not access it. And if you develop a server for yourself, invite me,

type script or whatever, also use identifications whenever possible. If you just work via STDIO on your

local machine, everything is fine. But as soon as you use Streamable HTTP and as soon as you consider

to publish your server, always make sure to use authentication and then you are safe. Just a quick

reminder, safe API keys, use authentication, rotate your stuff from time to time. See you in the

next one.