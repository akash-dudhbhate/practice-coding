/**
 * LESSON 20 — Quasar Deployment
 * HARD P02 — Node.js Deployment Script
 * ============================================
 * CONCEPT: A deploy script automates: verify build exists → upload files
 * to S3 under a versioned prefix → invalidate CloudFront → prune old
 * versions (keep last N) → Slack notify → and support --rollback <ver>.
 * Stub the AWS calls but keep the flow and logging real.
 *
 * PROBLEM: Write deploy.js: config constants (BUILD_DIR, bucket, dist id,
 * MAX_VERSIONS=3, webhook from env); listFiles() walking dist/spa;
 * uploadToS3 / invalidateCloudFront / sendSlackNotification (simulated ok);
 * cleanupOldVersions and rollback(target); a deploy() main + argv parsing
 * for --rollback; comment the full process.
 *
 * TRY THIS: const version = `v${new Date().toISOString().replace(/[:.]/g,'-')}`
 * if (args[0] === '--rollback') rollback(args[1]) else deploy()
 *
 * EXPECTED OUTPUT: `node deploy.js` uploads + invalidates + notifies;
 * `--rollback v1.2.3` restores a previous version.
 *
 * CHECK: python3 check.py hard/p02
 */
// TODO: write your deployment script here
