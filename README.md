# HouseOfHer
*A story-driven, survival horror game built in Unreal Engine 5.*  
You are Rowan. Trapped. Hunted. Alone.  
Your goal: Escape — one item, one decision at a time.

---

## 🎮 Core Gameplay: Survival Loop

**Rowan is trapped in a haunted house. To escape, he must:**

- 🔍 Identify which of the 3 exits is active (random every run)
- 🔑 Find and carry, one at a time:
  - The correct Key  
  - Crowbar  
  - Door Handle  
  - Fuse(s)
- 🔦 Manage total darkness every 3 minutes
- 🧠 Remember where he dropped items (no inventory)
- 🚷 Avoid "Her", who roams and hunts based on noise

> Only one item can be held at a time — no inventory, only instinct.

---

## 🔁 Item System: No Inventory, Only Hands

- Rowan can **only hold one item** at a time (besides his flashlight)
- Picking up a new item **automatically drops** the current one at your feet
- Dropped items stay where you left them
- Flashlight is always in hand

**This creates:**
- Realistic item juggling  
- Memory-based gameplay  
- High tension, especially in the dark

---

## 🔌 Fuse & Power System

- Game starts with power ON and **Fuse A** in the box  
- Every **3 minutes**, lights go OFF — player must:
  1. Drop held item  
  2. Find new fuse  
  3. Insert it to restore power  
- After each fuse:
  - Light intensity **dims** slightly  
  - A new fuse spawns at a new location

---

## 🚪 Exit Logic

Only **one of three exits** is active in each game.  
To unlock it, Rowan must bring:
- The correct Key  
- Crowbar (to remove wooden blocks)  
- Door Handle (to install)  
- Power must be ON

---

## 👣 What This Adds

| Effect | Description |
|--------|-------------|
| 🧠 Strategic Movement | Plan what to carry and when |
| ⏱️ Time Pressure | Fuse resets every 3 minutes — no time to waste |
| 👣 Memory Challenge | Must recall item locations |
| 😨 Realism + Horror | Rowan is fragile, human |
| 🧼 Minimal UI | No inventory, no menus — just survival |

---

## 🔧 Unreal Engine Blueprint Notes

| System | Notes |
|--------|-------|
| Item Pickup | `HeldItem` variable in Player BP |
| Drop Logic | On pickup: drop current item to world |
| Fuse Timer | Global 3-min timer triggers `PowerOff()` |
| Light Dimming | Lower intensity in `PowerOn()` |
| Object Tags | Use tags: `"Key"`, `"Fuse"`, `"Handle"` etc. |

---

## 🔤 Opening Monologue

> *“I always thought I was alone…*  
> *No family, no home — just silence.”*

> *“I asked myself why my life is this way…*  
> *I had no answers.*  
> *Only hopelessness.”*

> *“Until one day, I found out…*  
> *I have a relative.*  
> *Far away. Distant. Forgotten.”*

> *“Today, I’ll pay her a visit.”*

---

*The screen slowly fades in.*  
A **gloomy house** sits under a colorless sky.  
**Wind howls** through leafless trees.  
The camera pulls back… revealing **Rowan**, still, standing at the gate.

A moment of silence.

Suddenly —  
**Control is given to the player.**

→ You walk into *Her* home.

---


## ✅ Example Player Scenario

1. Rowan finds the Exit Key → picks it up  
2. Lights go out → drops key  
3. Finds fuse → inserts into fuse box → lights ON  
4. Remembers where he dropped the key → retrieves it  
5. Drops key again to get crowbar  
6. Same for door handle  
7. Avoids "Her" the entire time, who reacts to noise and movement

---

## 🎮 Status: Early Development

Currently working on:
- Physics-based item pickup/drop
- Light control & dimming system
- Initial AI movement prototype
- First map grayboxing

---

## ✍️ Notes

This is not just horror.  
This is **emotional weight**, **fragility**, **claustrophobia**, and **choice**.

Every action has a cost.

---

