---
title: "Alucard"
---

# Alucard

Alucard is the player character for SOTN.

## Afterimage Effect

Alucard, Richter and a select few entities in the game have an "afterimage" that draws duplicate graphics of the character behind them as they run or perform specific moves, creating an interesting visual effect that has become one of the game's most iconic elements.

The effect works by drawing 6 separate images that are duplicates of the player character's graphics. The images are split up into three separate entity groups, so each group has two afterimage graphics.

As the effect starts, a duplicate image is created that is based off of the player character's current frame of animation and is positioned behind the player. On the next frame of gameplay, a second image is generated and because the player's animation frame has changed, the second duplicate image will feature a different still image. The first image that was drawn previously continues to keeps the old frame. The effect continues to do this until it reaches the maximum number of after-images, which is 6. If there's already 6 images generated, then the oldest one is cleared as the effect creates the newest duplicate image.

A RAM value is used as an index to animate the blue color and opacity fade out effects that are mixed in with the 6 images. A timer is used to increment the index, which steps through three different tables that contain the values for the duration and amount of transparency for the effect. Once an index value of 10 is reached, the effect stops completely until the player stops pressing the D-pad and starts moving again. Some player actions like attacking or landing after a hard fall also stop the effect instantly. Interestingly, the effect's three different animation tables all share the same length of 16, which is more than the max index value of 10. Because of this, it's likely that the effect was originally longer in duration.

#### Flicker effect

During each frame of gameplay, only three of the six total afterimages are visible, while the other three are hidden from view. Once an afterimage graphic is actually drawn on-screen, the effect skips drawing the next image it generated and draws image number #3 instead. It does this all the time, which means that one frame will show images 1, 3, 5 and the next frame afterwards displays images 2, 4, 6. Essentially, when the screen refreshes on the next frame, the visibility of the images flip-flops, so that the 3 previously hidden graphics are now in view. This creates a nice 60 fps "flicker" effect that makes the trailing graphics much more interesting to look at.