# POS Command Echo

## Intent

When a POS script runs a shell command, the user has no visibility into what is being executed — they see only the output, or silence. Printing each command to stdout in a highlighted colour before it runs gives the user a clear trace of what the script is doing, aids learning, and makes it easier to identify where something went wrong.

## Approach

A `_run()` utility function wraps `subprocess.run()`: it prints the command string to stdout in a distinct colour using `rich` before executing it. This becomes the standard replacement for direct `subprocess.run()` calls throughout POS scripts. The `sudo()` helper is updated to print similarly before executing its privileged command.

`rich` is already pre-approved in POS, so no new dependency is introduced. The print colour should be visually distinct from normal output — `bold cyan` is used to signal a command rather than a result.

`_run()` is added to the utilities section (bottom of file) and referenced in the subprocess guidance. The existing examples in the standard are updated to use `_run()`.

Both `AGENT/ADDITIONAL/POS.md` and a new `SPLIT/BUILDER/ADDITIONAL/POS.md` are updated identically — the SPLIT builder carries its own copy for isolation. `SPLIT/BUILDER/README.md` is updated to import it.

## Plan

- [x] UPDATE `AGENT/ADDITIONAL/POS.md` — add `_run()` helper, update subprocess guidance and examples, update `sudo()` to echo before executing
- [x] ADD `SPLIT/BUILDER/ADDITIONAL/POS.md` — identical content
- [x] UPDATE `SPLIT/BUILDER/README.md` — add `@ADDITIONAL/POS.md` import

## Conclusion

Completed as planned. During review, the initial approach of making `_run()` mandatory was revised to a recommendation for commands where user visibility is of value. The standalone Utilities section was also dropped in favour of presenting `_run()` inline within the subprocess guidance.
