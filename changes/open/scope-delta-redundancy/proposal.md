# Proposal: Scope/Delta Redundancy
**Status: Note**

## Intent
The Scope and Delta/ADDED sections of a proposal inevitably overlap when a change is predominantly additive — both end up listing the same new things. The Scope section is meant to draw the boundary (what is and isn't being touched), while the Delta captures precise spec changes, but for all-new additions this distinction collapses.

Two possible improvements:
- Move the Delta section above the Scope section, so the precise changes are stated first. The Scope section can then focus almost entirely on the out-of-scope boundary, since what is in scope is already implicit from the Delta.
- Reframe the Scope section as primarily an out-of-scope boundary, with the in-scope list either omitted or kept very brief.
