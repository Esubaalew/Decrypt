---
title: "Introduction to bot programming(COPIED )"
datePublished: Wed Nov 23 2022 06:47:21 GMT+0000 (Coordinated Universal Time)
cuid: cm1l6ylor000108lhb2fray3c
slug: introduction-to-bot-programming-copied-96f529bf8427

---

Many users are interested in programming their own Telegram bot. Sadly there’s not much information out there on how to start out creating one. This article should help you get started.

1.  ***How can I create my own Bot?***  
    To begin with, there is this big question: Are you able to code? To create a “real” Telegram bot you need to write a little program to interact with the Telegram servers. If you can’t, there are alternative ways like “Manybot” which requires no coding. These will not be covered in detail in this article.
2.  ***1) Using Botmakers such as “Manybot” (etc.)  
    ***These kind of services offer to create a bot on their servers. They provide a skeleton bot, to which you can add minor stuff such as dialogs. Important: You can only do what they (e.g. Manybot) let you do. You are very limited in your actions! If they don’t offer a feature you need, you can’t use their service. But of course you don’t need to care about programming and hosting the bot.
3.  ***2) Coding it yourself***  
    When you do all the coding yourself, you’re not as limited: You can do everything that’s possible via the Telegram bot API. For example: You could create a bot that’s connected to your home automation system, so that you can switch on/off lights in your house via a simple Telegram message. BUT: when coding it yourself you need to think about where you’ll host the code (more on that later). If you can’t code and aren’t going to learn programming any time soon, you should stop reading here and go with a botmaker service (e.g. Manybot) or pay a programmer for creating a bot for you.

Okay: since you’re still reading, I assume you are able to code or at least want to try it. Let’s dive into detail.

***2\. How do I start?***

Quick reminder: From here on out, you must know a programming language.

***2.1) Hosting***

First things first. To avoid frustration later on, you should NOW think about where to host your bot. A bot is a piece of code which interacts with the (Telegram) servers via an API. In order to have a 24/7 online bot, it needs to run on any type of computer for 24/7 (obviously). Telegram does not host your code. You have several ways to go:

Micro-Controller/Raspberry Pi  
Having your PC running 24/7  
Pay for a VPS from a hosting provider  
The advantages and disadvantages are clear: RasPi consumes only a tiny amount of energy compared to a PC and costs ~30$. When paying for a VPS, you have a lot more computing power and don’t need to care about power/internet connection outages, but it costs on a monthly basis. Also check out this link on where to host your bot.

Now that you have decided where to host your bot, let’s decide for a programming language.

***2.2) Programming Language***  
If you already know a programming language, you can go ahead and use it. If you don’t know any language or want to use another/a better suited one, check the list of languages I can suggest for bot programming.

Python  
Go  
C#  
Java  
PHP   
Node.js (JavaScript)  
I mostly code my bots in Python since there are quite a few nice libraries and frameworks (more on that later) for it and it’s a very easy language: Easy to learn and easy to code. Languages such as C#, Go, and Java are (also) very powerful and offer a wide variety of features. PHP and Node.js are widely used in the web development branch. They are not bad in general, but I personally am not a big fan of them. Check them out if you’re curious and go with the one you like the most. There is no right or wrong.

***2.3) Getting ready to code***  
You’re now only a few steps away from coding your first own bot. Go ahead and download any IDE for your language (or a simple text editor such as Atom or Notepad++ for coding). For Python I can suggest PyCharm (the developer of PyCharm also offers a whole lot of other IDEs for other languages) or VS Code. More lightweight tools would be Sublime Text or Lite XL. Also you might want to start checking out the basics of the language you chose.

In this post I cannot help you learn a programming language or programming in general. Go ask Google for nice tutorials, there are thousands of them.

Now that you have set up your IDE and familiarised yourself with the programming language, we can begin. You need to contact [@BotFather](http://twitter.com/BotFather "Twitter profile for @BotFather") on Telegram. BotFather is an official Telegram bot for creating new bot accounts. Use the command /newbot and follow its instructions to create a new bot.

After following BotFather’s procedure, you’ll get a bot token, which allows you to interact with the Telegram servers. You can try it yourself. Insert your bot token into the following link [https://api.telegram.org/bot](https://api.telegram.org/bot)<your\_token\_here>/getMe, open it in your browser and and it will display information about your bot. Read the Telegram bot api documentation thoroughly and play with the available methods. Try sending and receiving some messages.

3\. Library, Framework or None of these?  
Telegram uses an HTTP based API. You call the URL via HTTP and pass it parameters via the URL, as multipart/form-data or as the body of a POST request. It then sends back a JSON encoded answer that your code needs to interpret. You could do all of this on your own. You would need a JSON parser and some code to do the HTTP requests. That would be kind of annoying since there are many issues you can run into. So why not just use a library or a framework?

First, you need to know the difference between both terms. A library is a package of code used for one task or a group of tasks. For example, libraries for image editing probably contain functions like ‘resize’ or ‘rotate’, which you can then call from your own code. You don’t need to reinvent the wheel. A framework however is a piece of software which is kind of a skeleton. It runs autonomously and does stuff when it needs to be done. You only provide the code for some special stuff — your business logic. For Telegram that would be the code for the single commands.

When comparing both for usage with Telegram, we’ll find that frameworks are pretty awesome, since they take care of receiving and sending messages, partly even of rate limits and message queues. You just provide the code to be executed when someone sends a command to your bot. With a library you would still need to periodically check for updates and handle the conversations yourself. A framework does that for you. Both frameworks and libraries provide you with methods such as ‘send\_message()’ to send messages to your users. You don’t need to know how they work. They just do.

I highly recommend using a framework. Here are some libraries/frameworks and bot samples. For NodeJS you might want to check this framework.

***4\. Let’s code***  
I will not teach you how to code. I just want to give you a short introduction into how to get started.

Now that you have decided about hosting, chosen a language, set up a new bot with BotFather and picked up a nice framework/library, we can start. I’ll use the Python programming language and the python-telegram-bot framework (which is really great).  
PS: I assume you installed the framework according to the framework’s installation guide.

***4.1) Hello World/Echo bot***  
Create a new project and create a new python file called main.py. All the coding goes into that file for the beginning. You need to import some of the framework’s classes, create an instance of “Updater” and create a function to be executed when the user writes something. That can look like this GitHub Gist. This code is taken from the official python-telegram-bot repository. When you successfully started out with the above code, try something more complicated.

***4.2) How to go on?***  
Now you have your first own bot up and running, you can start out extending it. Add new commands and command handlers. Definitely check out these examples to learn more about how to code within this framework. More important is to read the documentation of your framework and the Telegram Bot API documentation! Knowing the commands and the parameters will help you a lot in the future.

***4.3) Going professional***  
When you finally made your bot work the way you desired, you might not want your bot to ask the Telegram servers for updates every X seconds (also known as “long polling”). This is why Telegram offers “webhooks”. The Telegram servers will actively start an HTTPS connection to your server when new messages arrive (also known as “push technology”). But this is nothing for beginners. Apart from your VPS you need some kind of webserver which takes care of the requests — and more importantly, you need a TLS certificate. Since the whole process isn’t easy, a kind guy named Marvin created a comprehensive guide on how to setup webhooks with Telegram bots.

**4.4) Further questions?**  
If you still have questions not covered by this guide, come to the Telegram Bot Talk group ([@BotTalk](http://twitter.com/BotTalk "Twitter profile for @BotTalk")) and ask your questions. It’s a group made up of hundreds of bot enthusiasts and developers. In most cases there will be someone able to help you. Feel free to ask any bot-related questions in there.

PPS: If you read all of this article and got a serious question you are about to ask in Bot Talk, please append ‘I like bananas’ to your question. That will help us separate the spammy kind of questions from the actual, serious ones.

4.5) Sample modular bots  
Python:

[https://github.com/leonjza/hogar](https://github.com/leonjza/hogar)  
[https://github.com/datamachine/telex](https://github.com/datamachine/telex)  
Lua:

[https://github.com/wrxck/mattata](https://github.com/wrxck/mattata)  
PHP:

[https://github.com/php-telegram-bot/core](https://github.com/php-telegram-bot/core)  
C#:

[https://github.com/GreyWolfDev/CSChatBot-Core](https://github.com/GreyWolfDev/CSChatBot-Core)  
4.6) Various resources, video courses, etc.  
This section is dedicated for further resources, video courses, blog posts, articles, tutorials, etc. So if you are a content creator and would like to add your resource to this article, feel free to contact me.

4.6.1) Video courses  
[https://www.linkedin.com/learning/building-a-telegram-bot-for-business](https://www.linkedin.com/learning/building-a-telegram-bot-for-business) (Paid course)  
4.6.2) Other articles  
[https://telegra.ph/Very-first-manual-bot-steps-03-25](https://telegra.ph/Very-first-manual-bot-steps-03-25) (another article with detailed instructions for your very first bot)  
[https://grammy.dev/guide/introduction.html#how-to-write-a-bot](https://grammy.dev/guide/introduction.html#how-to-write-a-bot) (guide for the javascript famework “grammY” — also a great read on how to start creating bots)