# Google Access – OAuth Bridge

## Status
- Calendar: ✅ Working
- Gmail (readonly): ✅ Working
- Drive: ⚠️ Partial (needs re-auth with full `drive` scope instead of `drive.file`)

## Auth Method
OAuth user credentials (ADC fallback). Service account with domain-wide delegation is the future target.

## Credential Path
`~/.config/gcloud/application_default_credentials.json` (chmod 600)
- Account: praneet@moongate.one
- Quota project: moongate-422713 (MoonGate GCP project)
- Token: refresh_token based (auto-refreshes via gcloud)

## Current Scopes
- `https://www.googleapis.com/auth/gmail.readonly`
- `https://www.googleapis.com/auth/drive.file` (limited; needs upgrade to `drive`)
- `https://www.googleapis.com/auth/calendar`

## Helper Scripts
| Script | Purpose |
|--------|---------|
| `scripts/google-calendar-today.js` | List today's calendar events (IST) |
| `scripts/gmail-unread.js` | List up to 10 unread inbox messages |
| `scripts/google-drive-recent.js` | List 10 most recently modified Drive files |

## Usage
```bash
node scripts/google-calendar-today.js
node scripts/gmail-unread.js
node scripts/google-drive-recent.js
```

## Known Issues
The Node scripts must pass `X-Goog-User-Project: moongate-422713` in all API headers to avoid 403 quota errors.

## Fix Drive Access
Run:
```bash
source ~/google-cloud-sdk/path.bash.inc && gcloud auth application-default login \
  --scopes=https://www.googleapis.com/auth/cloud-platform,\
https://www.googleapis.com/auth/gmail.readonly,\
https://www.googleapis.com/auth/drive,\
https://www.googleapis.com/auth/calendar
```
Then:
```bash
gcloud auth application-default set-quota-project moongate-422713
```

## Upgrade Path: Service Account
1. Create GCP project `rocky-google-bridge`
2. Enable Gmail, Drive, Calendar APIs
3. Create service account + JSON key → store at `~/.config/rocky/google-service-account.json` (chmod 600)
4. Set `GOOGLE_APPLICATION_CREDENTIALS=~/.config/rocky/google-service-account.json`
5. In Google Workspace Admin Console (super admin required):
   - Security → API Controls → Domain-wide Delegation
   - Add service account client ID with scopes:
     `gmail.readonly, drive, calendar`
6. Use impersonation: `subject=praneet@moongate.one`
7. Delete OAuth ADC creds once verified
