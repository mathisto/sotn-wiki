# Deduplication

SOTN has a huge number of duplicates. We want to get these factored out to make the codebase more usable.

## Functions Without Data

This PR is a good example of the process when data is not involved: https://github.com/Xeeynamo/sotn-decomp/pull/1200/files

**Steps:**

1. Add the function (e.g., `CheckColliderOffsets`) to the `symbols.txt` for each stage you want to dedupe. The address will be different for each overlay.
2. Factor out the function into a header file.
3. `#include` the header in each source file.

## Functions With Data

This is similar to the previous case but all data needs to be given names and added to `symbols.txt` as well.

**Example PR:** https://github.com/Xeeynamo/sotn-decomp/pull/459/files

**Note:** Some stages may require data symbols to be renamed (e.g., `PfnEntityUpdates`) to avoid conflicts.
