<!--
LESSON 02 — Quasar Layout System
HARD P03 — Two Layouts + Routes
============================================
CONCEPT: Different sections of an app need different shells — e.g. a
login page has no drawer/header. In Quasar, routes pick which layout
component wraps their pages, and router-view renders the child page.

PROBLEM: Write MainLayout — q-layout with q-header (menu toggle +
title), a q-drawer with nav links using to="/" and to="/dashboard",
and a q-page-container holding <router-view />. In a comment, also
show the BlankLayout template (q-layout + q-page-container +
router-view only) and the routes config that maps /login to
BlankLayout and /dashboard to MainLayout.

TRY THIS: the drawer nav items should navigate via the `to` prop so
router-view swaps the page inside the same shell.

EXPECTED OUTPUT: MainLayout renders header + drawer + routed page;
the commented BlankLayout shows a bare q-page-container shell.

CHECK: python3 check.py hard/p03
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
