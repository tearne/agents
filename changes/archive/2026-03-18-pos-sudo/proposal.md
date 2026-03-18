# Proposal: POS Sudo Guidance
**Status: Approved**

## Intent
POS scripts sometimes require elevated privileges for specific commands. The current guidance does not address this. Scripts should request the sudo password once upfront — before the work begins — rather than requiring the entire script to be run as sudo or prompting mid-execution.

## Specification Deltas

### ADDED

- **Sudo pattern** — Scripts that will need elevated privileges should call an `init_password()`-style function early in `main()`, after argument parsing but before the work begins. The function should:
  1. Return immediately if already running as root (`os.geteuid() == 0`) — e.g. inside a container
  2. Return immediately if passwordless sudo is available (`sudo -n true`)
  3. Otherwise prompt once via `getpass.getpass()`, validate immediately with `sudo -S true`, and cache the password for the session

  All subsequent privileged `subprocess` calls pass the cached password via `sudo -S`. This ensures the user is never interrupted mid-execution, and is never prompted at all if privileges turn out not to be needed or are already available.

  The pattern should be documented inline in `POS.md` with a concise code example. The following improvements over the naive implementation should be incorporated:
  - Use a dedicated sentinel (e.g. `_PASSWORDLESS = object()`) rather than `None` to distinguish "passwordless sudo available" from "not yet initialised"
  - Offer up to 3 attempts on wrong password, matching standard `sudo` behaviour
  - Encapsulate stdin handling inside the sudo helper so callers don't need to manage it
