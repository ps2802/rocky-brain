#!/usr/bin/env node
import { execSync } from 'node:child_process';

const QUOTA_PROJECT = 'moongate-422713';

function getAccessToken() {
  return execSync("source ~/google-cloud-sdk/path.bash.inc && gcloud auth application-default print-access-token",
    { encoding: 'utf8', shell: '/bin/bash' }).trim();
}

async function fetchJson(url, token) {
  const res = await fetch(url, {
    headers: { Authorization: `Bearer ${token}`, 'X-Goog-User-Project': QUOTA_PROJECT }
  });
  if (!res.ok) throw new Error(`${res.status}: ${await res.text()}`);
  return res.json();
}

async function main() {
  const token = getAccessToken();
  const list = await fetchJson('https://gmail.googleapis.com/gmail/v1/users/me/messages?maxResults=10&labelIds=INBOX&q=is:unread', token);
  const ids = (list.messages || []).map(m => m.id);
  const messages = [];
  for (const id of ids) {
    const msg = await fetchJson(
      `https://gmail.googleapis.com/gmail/v1/users/me/messages/${id}?format=metadata&metadataHeaders=Subject&metadataHeaders=From&metadataHeaders=Date`, token);
    const headers = {};
    (msg.payload?.headers || []).forEach(h => { headers[h.name.toLowerCase()] = h.value; });
    messages.push({
      id,
      subject: headers.subject || '(no subject)',
      from: headers.from || '(unknown)',
      date: headers.date || ''
    });
  }
  console.log(JSON.stringify({ unread: messages.length, messages }, null, 2));
}
main().catch(e => { console.error(e.message); process.exit(1); });
