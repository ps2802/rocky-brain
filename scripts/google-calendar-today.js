#!/usr/bin/env node
import { execSync } from 'node:child_process';

const QUOTA_PROJECT = 'moongate-422713';

function getAccessToken() {
  return execSync("source ~/google-cloud-sdk/path.bash.inc && gcloud auth application-default print-access-token",
    { encoding: 'utf8', shell: '/bin/bash' }).trim();
}

function getIstRange() {
  const offsetMs = 330 * 60 * 1000;
  const now = Date.now();
  const istNow = new Date(now + offsetMs);
  const year = istNow.getUTCFullYear();
  const month = istNow.getUTCMonth();
  const day = istNow.getUTCDate();
  const startUtcMs = Date.UTC(year, month, day) - offsetMs;
  return {
    timeMin: new Date(startUtcMs).toISOString(),
    timeMax: new Date(startUtcMs + 86400000).toISOString()
  };
}

async function main() {
  const token = getAccessToken();
  const { timeMin, timeMax } = getIstRange();
  const params = new URLSearchParams({ timeMin, timeMax, singleEvents: 'true', orderBy: 'startTime', maxResults: '20' });
  const res = await fetch(`https://www.googleapis.com/calendar/v3/calendars/primary/events?${params}`, {
    headers: { Authorization: `Bearer ${token}`, 'X-Goog-User-Project': QUOTA_PROJECT }
  });
  if (!res.ok) { console.error(await res.text()); process.exit(1); }
  const data = await res.json();
  const events = (data.items || []).map(e => ({
    summary: e.summary || '(no title)',
    start: e.start.dateTime || e.start.date,
    end: e.end?.dateTime || e.end?.date,
    location: e.location || null,
    hangoutLink: e.hangoutLink || null
  }));
  console.log(JSON.stringify({ events, timeMin, timeMax }, null, 2));
}
main().catch(e => { console.error(e); process.exit(1); });
