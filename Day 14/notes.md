`ALT`

1. Placeholder
2. Visually impaired (Inclusive development)
3. SEO( Search Engine Optimisation)
   - Rank
     1. Page visits
     2. Bounce (how long users stay in the site)
     3. Unique content

### SEO FIGHT

- SEO expert will want you to write something that will make your page rank higher and not the description of the image.
- Home Loan at 8% interest instead of family looking at Home
- Lighthouse tool for SEO on Google Chrome

## Gradient

- use mycolorspace

## Official docs

- https://developer.mozilla.org/en-US/docs/Web/CSS/background

### No emojis

- use icons because some emojis are not available in some operating systems

## Color patterns

- https://coolors.co/ff7477-e69597-f1ffe7-4e937a-1a1b41

## icons

- they are in SVG
- there is no pixelation when you zoom in
- you can color them easily
- svg is in kbs so it doesn't take much size (space-efficient)
- svg can't do gradients

## CSS Styles

1. Internal- ❌
   - some things can load on screen immediately
   - reduces the round-trip to server
   - can't be used if the file is very long/heavy
   - must be small in size so that it speeds up the render tree| performance
2. In-line
3. External (95%✅)
   - Re-use ⬆️ - Add CSS to multiple HTML
   - Separation of concern - HTML & CSS

`if external css is heavy- it will take long to display on the screen`

## Inline elements

- don't respect height or width
- side by side( if there is enough space or else stacked)

## Block elements

- respect height and width
- always stacked

## Flex

- always side by side
- apply it on parent element and not child (so the main div)
- tries to keep height constant so the more the content the more space it will take up
- width is just a suggestion for Flex, it doesn't obey the width, as it focuses on keeping height constant
- flex-shrink(number) - how fast it shrinks
- is master at moving space around(horizontally)/ distributing space
- space even has even space for every gap
- space around has even space on the inside and on the outside the space is even on either side but it is half of the inside
- align vertically(align-items)
- improve flex game - flexbox froggy- https://flexboxfroggy.com/
