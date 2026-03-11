#!/usr/bin/env node
import { execSync } from 'node:child_process';

const QUOTA_PROJECT = 'moongate-422713';

function getAccessToken() {
  return execSync("source ~/google-cloud-sdk/path.bash.inc && gcloud auth application-default print-access-token",
    { encoding: 'utf8', shell: '/bin/bash' }).trim();
}

async function main() {
  const token = getAccessToken();
  const params = new URLSearchParams({
    pageSize: '10',
    orderBy: 'modifiedTime desc',
    fields: 'files(id,name,mimeType,modifiedTime,webViewLink)'
  });
  const res = await fetch(`https://www.googleapis.com/drive/v3/files?${params}`, {
    headers: { Authorization: `Bearer ${token}`, 'X-Goog-User-Project': QUOTA_PROJECT }
  });
  if (!res.ok) { console.error(await res.text()); process.exit(1); }
  const data = await res.json();
  console.log(JSON.stringify({ files: data.files || [] }, null, 2));
}
main().catch(e => { console.error(e); process.exit(1); });
