---
title: "Pull Request Guidelines"
---

### Adding commits

Once a PR has been reviewed, do not add more commits other than to resolve the comments. This makes it harder for reviewers and lengthens the time to get a PR through review.

### Single purpose

A PR should ideally accomplish one thing. Good examples are:

- Decompiling a single larger function
- Decompiling multiple smaller functions
- Renaming a symbol
- Changing something about the build system
- Rearranging code

A PR that does all of those things is much harder to review.

This does not prohibit combining certain things that make logical sense. For example:

- Decompiling a function and renaming it can be in a single PR. However, if the renaming touches a lot of files it probably makes more sense to split it.

### Follow the naming and style guidelines

See [https://github.com/Xeeynamo/sotn-decomp/blob/master/docs/NAMING.md](https://github.com/Xeeynamo/sotn-decomp/blob/master/docs/NAMING.md) and [https://github.com/Xeeynamo/sotn-decomp/blob/master/docs/STYLE.md](https://github.com/Xeeynamo/sotn-decomp/blob/master/docs/STYLE.md)

### Continuous Integration Checks

All CI checks should be passing. This means a matching build for all versions and correct code formatting. See the build page for more information on checking this locally. [https://github.com/Xeeynamo/sotn-decomp/wiki/Build](https://github.com/Xeeynamo/sotn-decomp/wiki/Build)

### DECOMP\_ME\_WIP Usage

DECOMP\_ME\_WIP is part of the function\_finder script that we use to tag decomp.me scratches for inclusion in the output. There are pros and cons to tagging a function:

Pros:

- If a function is renamed, the scratch will still be associated with it. Otherwise it would be lost.
- It can avoid function collisions with other projects or overlays since the matching is done by the function name.
- If the top scraped scratch is a questionable match, it can be overridden.

Cons:

- If there is a better scratch than the one in the source code, it won't be listed in the function\_finder output.

The policy right now is that if someone goes to the trouble of submitting a PR requesting this, we will merge it. However it's not really necessary since the scraper should work in 99% of cases.

### Entities

For entities, avoid using `.ext.generic` and `.ext.stub`. Make make separate structs for every entity.

### New Overlays

At this time, we want to figure out more about how the game is structured. For example, there is a large problem with duplicated functions in each overlay that we do not yet have a good solution for. For the time being, we are not accepting PRs for new overlays. We are not setting an exact criteria for when this will be opened up. We are hoping as DRA and the current stage overlays progress, it will become more clear when to add new overlays. If you have work on a new overlay done, open up a PR as a draft so we can track it.