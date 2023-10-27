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
  - image: "https://m.media-amazon.com/images/I/61XUtQ7NTgL._SY466_.jpg"
    link: "https://www.amazon.com/48-Laws-Power-Robert-Greene/dp/0140280197/ref=zg_bsms_g_books_sccl_30/141-8862560-3103627?psc=1&_encoding=UTF8&tag=geoffreyvanwy-20&linkCode=ur2&linkId=d24229f0b8203e53408eb20861d725ae&camp=1789&creative=9325"
    title: "The 48 Laws of Power"
  - image: "https://m.media-amazon.com/images/I/51D8IgtBaQL._SX342_SY445_.jpg"
    link: "https://www.amazon.com/Total-Money-Makeover-Classic-Financial/dp/1595555277/ref=zg_bsms_g_books_sccl_37/141-8862560-3103627?psc=1&_encoding=UTF8&tag=geoffreyvanwy-20&linkCode=ur2&linkId=27f2ad50ecec699a02ed02ca3abeeb2e&camp=1789&creative=9325"
    title: "The Total Money Makeover"
  - image: "https://m.media-amazon.com/images/I/51Hfv2MfNGL._SY445_SX342_.jpg"
    link: "https://www.amazon.com/Rich-Dad-Poor-Teach-Middle/dp/1612681131/ref=zg_bsar_g_books_sccl_28/141-8862560-3103627?psc=1&_encoding=UTF8&tag=geoffreyvanwy-20&linkCode=ur2&linkId=7a71501cc27b9dad5bd92240bde89a96&camp=1789&creative=9325"
    title: "Rich Dad Poor Dad"
  - image: "https://m.media-amazon.com/images/I/71UypkUjStL._SY466_.jpg"
    link: "https://www.amazon.com/Think-Grow-Rich-Landmark-Bestseller/dp/1585424331/ref=zg_bsar_g_books_sccl_7/141-8862560-3103627?psc=1&_encoding=UTF8&tag=geoffreyvanwy-20&linkCode=ur2&linkId=6e3273c65a2e8d7b7f5596aa0bc0199a&camp=1789&creative=9325"
    title: "Think and Grow Rich"
---

A list of my current and past projects, which I own or have contributed to significantly.

[TOC]

## Learning Sandbox Online

A website with sandbox instances of all the supported Moodle versions. The purpose of the sandboxes is to provide Moodle users with instant access to fresh, default Moodle instances for learning or quickly testing out a feature. The sandboxes are supposed to automatically reset to fresh states every hour, but I must still implement this feature.

The website and Moodle instances are created via Ansible using my custom roles for Moodle and PHP.

[learningsandbox.online](https://learningsandbox.online)
{: .icon-before .icon-solid .icon-link .icon-space-md .prose-p:text-red-600 style="margin-bottom: 0"}

[geoffreyvanwyk/learningsandbox.online](https://github.com/geoffreyvanwyk/learningsandbox.online)
{: .icon-before .icon-brands .icon-github .icon-space-md style="margin-top: 0"}

## Ansible Role for Moodle

Deploys, installs, and upgrades Moodle on Ubuntu servers. Because the role I created for my previous employer was not open source, I created this role from scratch.

[Ansible Galaxy](https://galaxy.ansible.com/ui/standalone/roles/geoffreyvanwyk/moodle/)
{: .icon-before .icon-solid .icon-link .icon-space-md .prose-p:text-red-600 style="margin-bottom: 0"}

[geoffreyvanwyk/ansible-role-moodle](https://github.com/geoffreyvanwyk/ansible-role-moodle)
{: .icon-before .icon-brands .icon-github .icon-space-md style="margin-top: 0"}

## Ansible Role for PHP

Using Ansible, installs, configures and extends the PHP programming language on Ubuntu servers. Multiple versions of PHP can be installed simultaneously on the same server.

Originally, I was using a third-party Ansible role for installing PHP that only allows a single PHP version at a time. For occasions on which multiple websites requiring different PHP versions must be installed on the same server, that third-party role was not appropriate.  That is why I had to create my own role.

I also limited the role to Ubuntu, because that is the Linux distribution I focus on

[Ansible Galaxy](https://galaxy.ansible.com/ui/standalone/roles/geoffreyvanwyk/php/)
{: .icon-before .icon-solid .icon-link .icon-space-md .prose-p:text-red-600 style="margin-bottom: 0"}

[geoffreyvanwyk/ansible-role-php](https://github.com/geoffreyvanwyk/ansible-role-php)
{: .icon-before .icon-brands .icon-github .icon-space-md style="margin-top: 0"}

## Timepiece

Timepiece is an alarm clock that runs on your desktop and includes a stopwatch and a countdown timer. All three timepieces can run simultaneously.

You can choose your own sound file to start playing at the set alarm time. The sound for the countdown timer is also customizable. The alarm clock has a snooze feature.

Timepiece has more than 5000 downloads on Sourceforge.

[SourceForge](https://sourceforge.net/projects/timepiece/)
{: .icon-before .icon-solid .icon-link .icon-space-md .prose-p:text-red-600 style="margin-bottom: 0"}
