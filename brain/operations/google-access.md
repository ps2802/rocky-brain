# Google Access – OAuth Bridge

## Status
- Calendar: ✅ Working
- Gmail (readonly): ✅ Working
- Drive: ✅ Working (full `drive` scope)

## Auth Method
OAuth user credentials (ADC fallback). Service account with domain-wide delegation remains the long-term target.

## Credential Path
`~/.config/gcloud/application_default_credentials.json` (chmod 600)
- Account: praneet@moongate.one
- Quota project: moongate-422713 (MoonGate GCP project)
- Token: refresh_token based (auto-refreshes via gcloud)

## Current Scopes
- `https://www.googleapis.com/auth/gmail.readonly`
- `https://www.googleapis.com/auth/drive`
- `https://www.googleapis.com/auth/calendar`

These scopes cover the live requirements: reading Gmail, accessing/updating existing Drive files, and creating/editing Google Docs/Sheets.

## Helper Scripts
| Script | Purpose |
|--------|---------|
| `scripts/google-calendar-today.js` | List today's calendar events (IST) |
| `scripts/gmail-unread.js` | List up to 10 unread inbox messages |
| `scripts/google-drive-recent.js` | List 10 most recently modified Drive files |

## Operational Notes
- **Quota header:** Every script sends `X-Goog-User-Project: moongate-422713`. Without it, Google bills the default SDK project (764….) and returns 403s.
- **Credential storage:** ADC JSON lives at `~/.config/gcloud/application_default_credentials.json` (chmod 600). Reference links live in `SECRETS.md`; no values are stored in markdown.
- **Account routing:** All OAuth tokens are for `praneet@moongate.one`. If personal-account access is needed, run the same `gcloud auth application-default login` flow with the personal profile and store the JSON at `~/.config/gcloud/adc-personal-praneet.json`.
- **Scope rationale:** `gmail.readonly` covers inbox monitoring, `drive` is required for opening/editing existing files and creating Docs/Sheets, and `calendar` powers scheduling. No `gmail.send` scope is requested until we have an actual sending requirement.
- **Upgrade path:** When Workspace super-admin access is available, follow the service-account section below to remove the OAuth user dependency entirely.

## Usage
```bash
node scripts/google-calendar-today.js
node scripts/gmail-unread.js
node scripts/google-drive-recent.js
```

## Upgrade Path: Service Account
1. Create GCP project `rocky-google-bridge`
2. Enable Gmail, Drive, Calendar APIs
3. Create service account + JSON key → store at `~/.config/rocky/google-service-account.json` (chmod 600)
4. Set `GOOGLE_APPLICATION_CREDENTIALS=~/.config/rocky/google-service-account.json`
5. Workspace Admin Console (super admin): grant domain-wide delegation for scopes `gmail.readonly, drive, calendar`
6. Use impersonation (`subject=praneet@moongate.one`)
7. Retire OAuth ADC creds once verified
