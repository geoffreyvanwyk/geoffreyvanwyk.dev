---
title: Portfolio
image:
  src: images/labrador-puppies-in-wheelbarrow.jpg
  alt: Labrador puppies in wheelbarrow
  creator:
    name: Andrew Lancaster
    link: https://unsplash.com/@andrewlancaster?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash
  publisher:
    name: Unsplash
    link: https://unsplash.com
sidebar_links:
  - image: "https://m.media-amazon.com/images/I/51M+z-t6QFL._SY445_SX342_.jpg"
    link: "https://www.amazon.com/Elon-Musk-Walter-Isaacson/dp/1982181281/ref=zg_bsar_g_books_sccl_11/141-8862560-3103627?psc=1&_encoding=UTF8&tag=geoffreyvanwy-20&linkCode=ur2&linkId=6317b7e049d3e734fe6160ed7abb4a66&camp=1789&creative=9325"
    title: "Elon Musk"
  - image: "https://m.media-amazon.com/images/I/51rBwNT0gEL._SY445_SX342_.jpg"
    link: "https://www.amazon.com/American-Prometheus-Triumph-Tragedy-Oppenheimer/dp/0375726268/ref=zg_bsar_g_books_sccl_10/141-8862560-3103627?psc=1&_encoding=UTF8&tag=geoffreyvanwy-20&linkCode=ur2&linkId=149450a0fc697683816502223dbe35d6&camp=1789&creative=9325"
    title: "American Prometheus"
  - image: "https://m.media-amazon.com/images/I/61XUtQ7NTgL._SY466_.jpg"
    link: "https://www.amazon.com/48-Laws-Power-Robert-Greene/dp/0140280197/ref=zg_bsms_g_books_sccl_30/141-8862560-3103627?psc=1&_encoding=UTF8&tag=geoffreyvanwy-20&linkCode=ur2&linkId=d24229f0b8203e53408eb20861d725ae&camp=1789&creative=9325"
    title: "The 48 Laws of Power"
  - image: "https://m.media-amazon.com/images/I/71UypkUjStL._SY466_.jpg"
    link: "https://www.amazon.com/Think-Grow-Rich-Landmark-Bestseller/dp/1585424331/ref=zg_bsar_g_books_sccl_7/141-8862560-3103627?psc=1&_encoding=UTF8&tag=geoffreyvanwy-20&linkCode=ur2&linkId=6e3273c65a2e8d7b7f5596aa0bc0199a&camp=1789&creative=9325"
    title: "Think and Grow Rich"
  - image: "https://m.media-amazon.com/images/I/71vK0WVQ4rL._SY466_.jpg"
    link: "https://www.amazon.com/How-Win-Friends-Influence-People/dp/0671027034/ref=zg_bsar_g_books_sccl_14/141-8862560-3103627?psc=1&_encoding=UTF8&tag=geoffreyvanwy-20&linkCode=ur2&linkId=988a311df045f903ea1d0c04873476af&camp=1789&creative=9325"
    title: "How to Win Friends & Influence People"
  - image: "https://m.media-amazon.com/images/I/51D8IgtBaQL._SX342_SY445_.jpg"
    link: "https://www.amazon.com/Total-Money-Makeover-Classic-Financial/dp/1595555277/ref=zg_bsms_g_books_sccl_37/141-8862560-3103627?psc=1&_encoding=UTF8&tag=geoffreyvanwy-20&linkCode=ur2&linkId=27f2ad50ecec699a02ed02ca3abeeb2e&camp=1789&creative=9325"
    title: "The Total Money Makeover"
  - image: "https://m.media-amazon.com/images/I/51Hfv2MfNGL._SY445_SX342_.jpg"
    link: "https://www.amazon.com/Rich-Dad-Poor-Teach-Middle/dp/1612681131/ref=zg_bsar_g_books_sccl_28/141-8862560-3103627?psc=1&_encoding=UTF8&tag=geoffreyvanwy-20&linkCode=ur2&linkId=7a71501cc27b9dad5bd92240bde89a96&camp=1789&creative=9325"
    title: "Rich Dad Poor Dad"
---

A list of my current and past projects.

[TOC]

---

## Learning Sandbox Online

> Sandbox instances of Moodle

The _Learning Sandbox Online_ is a website with default, out-of-the-box (for the
most part) installations of all the officially supported versions of
[Moodle][m]{: target="_blank"}. The installations serve as playgrounds or sandboxes giving instant,
hassle-free access to:

* potential new users who want to see what Moodle looks like and what it offers;
* new users who are learning it and need an instance for that, for example while taking a course;
* existing users of customized versions who want to see how a certain feature normally works;
* existing users who want to compare features between versions;
* existing users who want to see what is available in the newest version;
* etc.

The sandboxes are supposed to automatically reset to fresh states every hour,
but I must still [implement this feature][itf]{: target="_blank"}.

The website and Moodle instances are _automatically_ installed and updated with
[Ansible][a]{: target="_blank"} using my custom roles for Moodle and PHP.

There is already an official Moodle demo website, but I had a number of reasons
for building this website:

* I wanted to see how I would implement it myself.
* I wanted to use my custom Ansible role for Moodle in a real-world project.
* It fulfills my goal of building and maintaining a useful website with many
  users, which I formed when first seeing StackOverflow and reading about its
  history.
* Because it is open source, it can be used by e-learning service providers to
  create their own branded demo website to showcase to their clients.

[learningsandbox.online](https://learningsandbox.online)
{: .icon-before .icon-solid .icon-link .icon-space-md .prose-p:text-red-600 style="margin-bottom: 0" }

[geoffreyvanwyk/learningsandbox.online](https://github.com/geoffreyvanwyk/learningsandbox.online)
{: .icon-before .icon-brands .icon-github .icon-space-md style="margin-top: 0" }

---

## Ansible Role for Moodle

> Deploys, installs, and upgrades Moodle on Ubuntu servers

At a former employer, one of my tasks was to set up new Moodle instances for
clients. I set out to document the steps for doing so. Because many of those
steps were Bash shell commands, I realized I should create a script to
automatically do the installations. While setting out to write the script, which
would end up in many scripts that would need to be combined, I thought I should
rather use a framework that came with a prebaked, proven method of organizing the
scripts. The Bash framework that I chose did not work well at all and was a
complete disaster.

I had heard many times of things like Puppet, Chef and Ansible, but when I
visited their websites I would always be stumped by the generalized language on
their home pages that left me stumped as to whether they were relevant to my
plan, or as to even how to start. Luckily I found an
[introduction video][iv]{: target="_blank"} on YouTube that got me started
quickly with Ansible with which I created a role for Moodle.

Because the role I created for my former employer was not open source, I had
to recreate this role completely from scratch. The advantage sometimes of
redoing something is doing it better.

[Ansible Galaxy](https://galaxy.ansible.com/ui/standalone/roles/geoffreyvanwyk/moodle/)
{: .icon-before .icon-solid .icon-link .icon-space-md .prose-p:text-red-600 style="margin-bottom: 0" }

[geoffreyvanwyk/ansible-role-moodle](https://github.com/geoffreyvanwyk/ansible-role-moodle)
{: .icon-before .icon-brands .icon-github .icon-space-md style="margin-top: 0" }

---

## Ansible Role for PHP

> Installs, configures, and extends PHP on Ubuntu

This Ansible role installs, configures and extends the [PHP][php] programming language
on [Ubuntu][u] servers. Multiple versions of PHP can be installed simultaneously on
the same server.

Originally, I was using another third-party Ansible role for installing PHP that
only allows a single PHP version at a time. For occasions on which multiple
websites requiring different PHP versions must be installed on the same server
(for example _Learning Sandbox Online_ where PHP 7.4, 8.0, and 8.1 are required
simultaneously), that role was not appropriate.  That is why I had to create my
own role.

I also limited the role to Ubuntu, because that is the Linux distribution I
focus on.

[Ansible Galaxy](https://galaxy.ansible.com/ui/standalone/roles/geoffreyvanwyk/php/)
{: .icon-before .icon-solid .icon-link .icon-space-md .prose-p:text-red-600 style="margin-bottom: 0" }

[geoffreyvanwyk/ansible-role-php](https://github.com/geoffreyvanwyk/ansible-role-php)
{: .icon-before .icon-brands .icon-github .icon-space-md style="margin-top: 0" }

---

## Timepiece

> Alarm clock for your desktop

Timepiece is an alarm clock that runs on your desktop and includes a stopwatch
and a countdown timer. All three timepieces can run simultaneously.

You can choose your own sound file to start playing at the set alarm time. The
sound for the countdown timer is also customizable. The alarm clock has a snooze
feature.

Timepiece has more than 5000 downloads on Sourceforge. I once saw that somebody
created a video review of it. I cannot find it anymore, but it made me extremely
proud.

[SourceForge](https://sourceforge.net/projects/timepiece/)
{: .icon-before .icon-solid .icon-link .icon-space-md .prose-p:text-red-600 style="margin-bottom: 0" }

[a]: https://docs.ansible.com/ansible/
[itf]: https://github.com/geoffreyvanwyk/learningsandbox.online/issues/7
[iv]: https://www.youtube.com/watch?v=uR1_hlHxvhc
[m]: https://moodle.org/
[php]: https://php.net
[u]: https://ubuntu.com
