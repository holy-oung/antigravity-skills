# Use Hycli to make websites useful

Hycli prepares and runs website actions through one local runtime shared by CLI, MCP and the dashboard. Carry the user's requested website task through to a usable result. Inspect the available tools and actual results; adapt when a method fails instead of repeating it or declaring success from a homepage response.

## Connect and discover

Use the connection from **Coding agents → View connection settings**. Its executable and data directory are resolved on this device. The general connection includes website preparation; a website-specific connection intentionally exposes only that website's installed actions.

- With MCP, inspect `hycli_sites` and each action's schema. If the website is missing, call `hycli_prepare` with the user's URL and an `intent` describing the outcome. For a missing capability on an installed website, call `hycli_request` with `site` and `instruction`. Follow the returned job with `hycli_job` or `hycli_result`.
- With CLI, use `hycli describe`, `hycli describe SITE ACTION`, and `hycli SITE ACTION --help`. Prepare a website with `hycli prepare URL`; it waits for the result and writes progress to stderr. Extend an installed website with `hycli request SITE "Add the functionality I need"` (alias: `hycli extend`). Existing actions remain available.
- Reuse a working installed action. If preparation produces only part of the requested workflow, inspect its actual findings and error, then continue from the missing capability. Do not treat a generated definition as proof of successful execution.
- If AI or browser access is missing, direct the user to the relevant **AI connections** or **Accounts** screen. Ask only for a decision or access the user actually needs to supply. Do not ask them to research endpoints, write schemas, or paste session secrets.

### Native discovery choice and recovery

The dashboard's native browser discovery setting is persisted per local data directory. CLI and MCP processes using that same directory (`HYCLI_DATA_DIR` when configured) observe the same choice, including changes made after they started. macOS defaults to disabled, including upgrades without an existing choice; Windows and Linux retain native discovery unless disabled. Enabling the setting does not itself start a dashboard scan. Use the existing **Find/Recheck** action when the user wants native discovery; it may request OS keychain approval.

`native_discovery_disabled` is a choice, not a signed-out account. Use the browser companion or existing imported accounts without forcing logout or reauthentication. Do not repeatedly retry native discovery or silently enable it. `native_discovery_retry_required` means a previous native attempt did not complete; automatic preparation pauses native attempts until an explicit retry. Finish or dismiss outstanding OS prompts before choosing **Find/Recheck** again. An active worker must finish before another scan can start (`browser_busy`). Disabling cancels further work cooperatively, but cannot remove OS dialogs already shown. Never suggest persistent OS approval, exporting keys, or changing access-control settings as a workaround.

## Complete the task

Read and search actions run autonomously through Hycli. Use exact typed inputs and the intended account. MCP `hycli_run` can execute an installed action by site and action ID even when the client has not refreshed its tool list. CLI equivalents are `hycli SITE ACTION --input value` and `hycli run SITE ACTION --arg name=value --account ID`. Discover saved account IDs with `hycli_accounts` or `hycli accounts --site SITE`.

Each website CLI starts with writes off (`writes: false`). Its change actions are hidden from direct MCP tool lists, and the CLI answers `writes_disabled` until writes are enabled for that CLI. Ask the user ONCE per website CLI whether to allow write actions (for example, "Allow write actions for SITE?"). Only after the user confirms, run `hycli writes SITE allow` (or MCP `hycli_writes` with `{"site": "SITE", "allow": true}`) to enable write actions for that CLI.

Once writes are enabled for a website CLI, requested write actions execute directly through `hycli SITE ACTION`, `hycli run`, `<site>_<action>`, or `hycli_run`. Never run unrequested write actions, and never automatically retry a failed write (`action_outcome_unknown`): an uncertain outcome means the website may already have applied the change, so check its actual state before proposing another attempt.

Use `hycli_activity`, `hycli_result`, or `hycli jobs show ID --watch` to follow work. A timeout while observing a live job does not mean that job failed. Read its status before retrying. Confirm the useful result and explain any remaining missing inputs or capabilities in the user's language.

## Check before retrying

When an action that used to work fails, run `hycli check SITE` or MCP `hycli_check` before modifying anything. It replays recorded reads without AI workers to distinguish network or site changes from AI behavior.
- `signed_out` means the website expired or revoked the session. Ask the user to reconnect the account in Hycli (using the dashboard or browser companion); do not attempt automated re-login with fake credentials.
- `site_changed` means the website updated its frontend or endpoints. Use `hycli request SITE "Update actions for new site version"` to adapt the action definitions rather than re-preparing from scratch.

## Authoring portable website definitions

When creating or modifying portable website definitions:
1. Ensure `spec_version: 3` for definitions utilizing advanced features.
2. Validate the schema using `hycli spec validate FILE.json`.
3. Test read actions against synthetic endpoints or bounded accounts before deploying.
4. Never hardcode live secrets, credentials, or machine-specific local paths in definitions.
