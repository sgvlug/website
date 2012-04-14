---
layout: page
title: "I don't want my e-mail messages archived!"
description: ""
group: "info"
---
{% include JB/setup %}
	 	 
Written by Tom Emerson

Tuesday, 20 September 2005

Hey, I see you archive all e-mails and make them available on the web -- I don't want this, what can I do?

First, some history:

Around June of 2005, we switched mailing list managers from "majordomo" to "mailman".  In the process, we enabled an "archive" feature for the first time in the history of our group.  This is generally regarded as "a good thing" as most of our discussions are technical in nature (i.e. answers to questions on how to do something using Linux or computers in general)  However, some folks are concerned about the fact that the e-mails are available to the general public, particularly due to the likelihood that spammers will "crawl" our site and pick up e-mail addresses (a legitimate concern)  Others are afraid that their posts might come back to haunt them in the future (this is a rather suspect concern -- if you're worried about what you might say, then don't say it in public -- even if we didn't specifically archive messages, nothing stops a list member from keeping every message on their own)

Now, the answer you were looking for:

Our mailing list software honors the "X-No-Archive" flag.  This is a special e-mail header you can add to any message you send to the list, and your message will NOT be kept in the archive.  If you have an e-mail client that doesn't allow you to add custom headers, you can place this on the FIRST line of your message and it will be recognized as well.


One of our members posted the following method for setting this "special header" in Mozilla's thunderbird:

Using Mozilla/mozilla-spinoff email, put this in your user.js:

    pref("mail.identity.id1.headers", "header1,header2");
    pref("mail.identity.id1.header.header1", "X-No-Archive: Yes");
    pref("mail.identity.id1.header.header2", "X-Archive: No");
    pref("mail.identity.id2.headers", "header1,header2");
    pref("mail.identity.id2.header.header1", "X-No-Archive: Yes");
    pref("mail.identity.id2.header.header2", "X-Archive: No");
    pref("mail.identity.id3.headers", "header1,header2");
    pref("mail.identity.id3.header.header1", "X-No-Archive: Yes");
    pref("mail.identity.id3.header.header2", "X-Archive: No");
