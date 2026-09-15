// Deployment script (Node.js): upload to S3, invalidate CloudFront, Slack notify, rollback
// Run: node deploy.js --env production

const fs = require('fs')
const path = require('path')
const { execSync } = require('child_process')

// --- Configuration ---
const BUILD_DIR = path.join(__dirname, 'dist/spa')
const S3_BUCKET = 'my-app-bucket'
const CLOUDFRONT_DIST_ID = 'E123ABCDEF456'
const MAX_VERSIONS = 3
const SLACK_WEBHOOK = process.env.SLACK_WEBHOOK_URL

// --- Simulated AWS operations (replace with real AWS SDK calls in production) ---

function uploadToS3(buildDir, version) {
  console.log(`[Deploy] Uploading build to S3 (version: ${version})...`)
  // Real implementation:
  // const AWS = require('aws-sdk')
  // const s3 = new AWS.S3()
  // Read all files in buildDir and upload each to s3://bucket/version-N/
  const files = listFiles(buildDir)
  files.forEach(file => {
    const key = `versions/${version}/${file}`
    console.log(`  ↑ Uploading: ${key}`)
    // s3.putObject({ Bucket: S3_BUCKET, Key: key, Body: fs.readFileSync(...) })
  })
  console.log(`[Deploy] Uploaded ${files.length} files to S3.`)
  return files.length
}

function invalidateCloudFront() {
  console.log('[Deploy] Invalidating CloudFront cache...')
  // Real implementation:
  // const cloudfront = new AWS.CloudFront()
  // cloudfront.createInvalidation({ DistributionId, InvalidationBatch: { Paths: { Quantity: 1, Items: ['/*'] } } })
  console.log('[Deploy] CloudFront invalidation complete.')
}

function sendSlackNotification(message, isError = false) {
  if (!SLACK_WEBHOOK) {
    console.log(`[Slack] (no webhook) ${message}`)
    return
  }
  // Real implementation:
  // fetch(SLACK_WEBHOOK, { method: 'POST', body: JSON.stringify({ text: message }) })
  console.log(`[Slack] ${isError ? 'ALERT: ' : ''}${message}`)
}

function listFiles(dir, base = '') {
  let files = []
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const fullPath = path.join(dir, entry.name)
    const relativePath = base ? `${base}/${entry.name}` : entry.name
    if (entry.isDirectory()) {
      files = files.concat(listFiles(fullPath, relativePath))
    } else {
      files.push(relativePath)
    }
  }
  return files
}

// --- Version management for rollback ---
function getVersions() {
  // Real implementation: list S3 prefixes under versions/
  return ['v1.0.0', 'v1.0.1', 'v1.0.2']  // Simulated
}

function cleanupOldVersions() {
  const versions = getVersions()
  if (versions.length <= MAX_VERSIONS) return
  const toRemove = versions.slice(0, versions.length - MAX_VERSIONS)
  toRemove.forEach(v => {
    console.log(`[Deploy] Removing old version: ${v}`)
    // Real implementation: s3.deleteObjects for each version prefix
  })
}

function rollback(targetVersion) {
  console.log(`[Rollback] Rolling back to version ${targetVersion}...`)
  // Real implementation:
  // 1. Update CloudFront to point to versions/${targetVersion}/
  // 2. Invalidate CloudFront cache
  // 3. Notify Slack
  invalidateCloudFront()
  sendSlackNotification(`Rolled back to ${targetVersion}`)
  console.log(`[Rollback] Complete. Now serving version ${targetVersion}.`)
}

// --- Main deployment process ---
async function deploy() {
  const version = `v${new Date().toISOString().replace(/[:.]/g, '-')}`
  console.log(`\n=== Starting deployment ${version} ===\n`)

  // 1. Verify build exists
  if (!fs.existsSync(BUILD_DIR)) {
    sendSlackNotification('Build directory not found! Run `quasar build` first.', true)
    process.exit(1)
  }

  // 2. Upload to S3
  const fileCount = uploadToS3(BUILD_DIR, version)

  // 3. Invalidate CloudFront
  invalidateCloudFront()

  // 4. Cleanup old versions (keep last 3)
  cleanupOldVersions()

  // 5. Notify Slack
  sendSlackNotification(`Deployment ${version} complete. ${fileCount} files uploaded.`)

  console.log(`\n=== Deployment ${version} successful ===`)
  console.log(`To rollback: node deploy.js --rollback ${version}\n`)
}

// Parse command line args
const args = process.argv.slice(2)
if (args[0] === '--rollback' && args[1]) {
  rollback(args[1])
} else {
  deploy()
}

/*
=== Full Deployment Process ===

1. Build: quasar build -m spa → dist/spa/
2. Upload: All files in dist/spa/ uploaded to S3 under versions/<version>/
3. Invalidate: CloudFront cache invalidated so new content is served
4. Cleanup: Old versions beyond last 3 are deleted from S3
5. Notify: Slack notification sent with deployment status

Rollback:
- Each deployment creates a new versioned folder in S3
- Rollback updates CloudFront to point to a previous version
- Last 3 versions are always kept for quick rollback
- Command: node deploy.js --rollback <version>
*/
