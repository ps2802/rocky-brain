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

All helper scripts add `X-Goog-User-Project: moongate-422713` to every API request. Without that header, Google falls back to the default SDK project and throws 403 quota errors.

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
