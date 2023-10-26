---
Title: Portfolio
---

A list of my current and past projects, which I own or have contributed to significantly.

[TOC]

## Learning Sandbox Online

A website with sandbox instances of all the supported Moodle versions. The purpose of the sandboxes is to provide Moodle users with instant access to fresh, default Moodle instances for learning or quickly testing out a feature. The sandboxes are supposed to automatically reset to fresh states every hour, but I must still implement this feature.

The website and Moodle instances are created via Ansible using my custom roles for Moodle and PHP.

## Ansible Role for Moodle

Deploys, installs, and upgrades Moodle on Ubuntu servers. Because the role I created for my previous employer was not open source, I created this role from scratch.

## Ansible Role for PHP

Using Ansible, installs, configures and extends the PHP programming language on Ubuntu servers. Multiple versions of PHP can be installed simultaneously on the same server.

Originally, I was using a third-party Ansible role for installing PHP that only allows a single PHP version at a time. For occasions on which multiple websites requiring different PHP versions must be installed on the same server, that third-party role was not appropriate.  That is why I had to create my own role.

I also limited the role to Ubuntu, because that is the Linux distribution I focus on

## Timepiece

Timepiece is an alarm clock that runs on your desktop and includes a stopwatch and a countdown timer. All three timepieces can run simultaneously.

You can choose your own sound file to start playing at the set alarm time. The sound for the countdown timer is also customizable. The alarm clock has a snooze feature.

Timepiece has more than 5000 downloads on Sourceforge.
